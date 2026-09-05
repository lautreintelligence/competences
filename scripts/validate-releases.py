"""Controle les versions stables des plugins et leur progression depuis une revision Git.

Usage: python scripts/validate-releases.py [--base-ref REVISION]
"""
import argparse
import json
import re
import subprocess
from pathlib import Path


def check(root: Path, base_ref: str | None = None) -> list[str]:
    errors = []
    plugins = sorted(path for path in (root / "plugins").iterdir() if path.is_dir())
    if not plugins:
        return ["aucun plugin trouve"]
    base = None
    if base_ref:
        # Resolve once; subsequent Git arguments use the verified object ID.
        base = subprocess.check_output(
            ["git", "rev-parse", "--verify", "--end-of-options", f"{base_ref}^{{commit}}"],
            cwd=root, text=True,
        ).strip()
    for plugin in plugins:
        try:
            manifests = [json.loads((plugin / harness / "plugin.json").read_text())
                         for harness in (".claude-plugin", ".codex-plugin")]
            if not all(isinstance(manifest, dict) for manifest in manifests):
                errors.append(f"{plugin.name} : les manifestes doivent etre des objets")
                continue
            versions = [manifest.get("version") for manifest in manifests]
            if not all(isinstance(version, str) and re.fullmatch(
                r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", version
            ) for version in versions):
                errors.append(f"{plugin.name} : version stable x.y.z requise dans les deux manifestes")
                continue
            if versions[0] != versions[1]:
                errors.append(f"{plugin.name} : versions Claude et Codex differentes")
            if any(manifest.get("name") != plugin.name for manifest in manifests):
                errors.append(f"{plugin.name} : nom de manifeste different du dossier")
            changelog = (plugin / "CHANGELOG.md").read_text()
            if not re.search(rf"^## {re.escape(versions[0])}(?:\s|$)", changelog, re.M):
                errors.append(f"{plugin.name} : version absente du CHANGELOG.md")
            if base is None:
                continue
            relative = plugin.relative_to(root).as_posix()
            changed = subprocess.check_output(
                ["git", "diff", "--name-only", base, "--", relative], cwd=root, text=True,
            ).strip()
            if not changed:
                continue
            previous_path = f"{base}:{relative}/.claude-plugin/plugin.json"
            exists = subprocess.run(
                ["git", "cat-file", "-e", previous_path], cwd=root, capture_output=True,
            )
            if exists.returncode:
                continue  # A newly added plugin has no previous release.
            previous = json.loads(subprocess.check_output(
                ["git", "show", previous_path], cwd=root, text=True,
            ))["version"]
            if tuple(map(int, versions[0].split("."))) <= tuple(map(int, previous.split("."))):
                errors.append(f"{plugin.name} : contenu modifie sans increment de version ({previous})")
        except (OSError, ValueError, KeyError, TypeError) as error:
            errors.append(f"{plugin.name} : {error}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-ref", help="revision Git de reference avant les modifications")
    args = parser.parse_args()
    try:
        errors = check(Path(__file__).resolve().parent.parent, args.base_ref)
    except (OSError, subprocess.CalledProcessError) as error:
        print(f"FAIL validation des versions : {error}")
        return 1
    for error in errors:
        print(f"FAIL {error}")
    if not errors:
        print("Versions des plugins conformes")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
