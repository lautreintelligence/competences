# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml==6.0.3"]
# ///
"""Valide chaque SKILL.md du repo contre le spec et la convention aien.

Usage: uv run scripts/validate-skills.py
"""
import re
import sys
from pathlib import Path

import yaml

SPEC_ALLOWED = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
AIEN_REQUIRED = {"name", "description", "license", "metadata"}
NAME_RE = re.compile(r"^[a-z0-9-]+$")
MAX_TAGS = 3


def check(skill_md: Path) -> list[str]:
    """Retourne la liste des erreurs pour un SKILL.md. Liste vide = conforme."""
    errs = []
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---[ \t]*(?:\n|$)", text, re.DOTALL)
    if not m:
        return ["frontmatter YAML absent ou mal forme"]
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return [f"YAML invalide : {e}"]
    if not isinstance(fm, dict):
        return ["le frontmatter doit etre un dictionnaire YAML"]

    extra = set(fm) - SPEC_ALLOWED
    if extra:
        errs.append(f"cles hors spec : {', '.join(sorted(map(str, extra)))}")
    missing = AIEN_REQUIRED - set(fm)
    if missing:
        errs.append(f"cles requises absentes : {', '.join(sorted(missing))}")

    name = fm.get("name")
    if isinstance(name, str):
        if not NAME_RE.match(name) or name.startswith("-") or name.endswith("-") or "--" in name:
            errs.append(f"name '{name}' n'est pas en kebab-case strict")
        if len(name) > 64:
            errs.append(f"name trop long ({len(name)} > 64)")
        if name != skill_md.parent.name:
            errs.append(f"name '{name}' different du dossier '{skill_md.parent.name}'")
    else:
        errs.append("name doit etre une chaine non vide")

    desc = fm.get("description")
    if isinstance(desc, str):
        if "<" in desc or ">" in desc:
            errs.append("description : chevrons < ou > interdits")
        if not desc.strip():
            errs.append("description doit etre non vide")
        if len(desc) > 1024:
            errs.append(f"description trop longue ({len(desc)} > 1024)")
    else:
        errs.append("description doit etre une chaine non vide")

    license_value = fm.get("license")
    if not isinstance(license_value, str) or not license_value.strip():
        errs.append("license doit etre une chaine non vide")

    compat = fm.get("compatibility")
    if "compatibility" in fm:
        if not isinstance(compat, str) or not compat.strip():
            errs.append("compatibility doit etre une chaine non vide")
        elif len(compat) > 500:
            errs.append(f"compatibility trop longue ({len(compat)} > 500)")

    allowed_tools = fm.get("allowed-tools")
    if "allowed-tools" in fm and (
        not isinstance(allowed_tools, str) or not allowed_tools.strip()
    ):
        errs.append("allowed-tools doit etre une chaine non vide")

    meta = fm.get("metadata")
    if not isinstance(meta, dict):
        errs.append("metadata doit etre un objet de chaines")
    else:
        for key, value in meta.items():
            if not isinstance(key, str) or not isinstance(value, str):
                errs.append("metadata : chaque cle et chaque valeur doivent etre des chaines")
        for key in ("version", "author", "tags"):
            value = meta.get(key)
            if not isinstance(value, str) or not value.strip():
                errs.append(f"metadata.{key} doit etre une chaine non vide")
        tags = meta.get("tags")
        if isinstance(tags, str):
            values = [tag.strip() for tag in tags.split(",")]
            if len(values) > MAX_TAGS:
                errs.append(f"metadata.tags : {len(values)} valeurs, maximum {MAX_TAGS}")
            if not all(values):
                errs.append("metadata.tags : chaque tag doit etre non vide")

    nested = [p for p in skill_md.parent.rglob("SKILL.md") if p != skill_md]
    if nested:
        rel = ", ".join(str(p.relative_to(skill_md.parent)) for p in nested)
        errs.append(f"SKILL.md imbrique rejete a l'envoi : {rel}")
    return errs


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    skills = sorted(root.glob("plugins/*/skills/*/SKILL.md"))
    if not skills:
        print("aucun SKILL.md trouve sous plugins/*/skills/")
        return 1
    skills += sorted(root.glob("templates/**/SKILL.md"))
    failed = 0
    for s in skills:
        rel = s.relative_to(root)
        errs = check(s)
        if errs:
            failed += 1
            print(f"FAIL {rel}")
            for e in errs:
                print(f"       - {e}")
        else:
            print(f"OK   {rel}")
    print(f"\n{len(skills) - failed}/{len(skills)} conformes")
    return 1 if failed else 0


def demo() -> None:
    """Auto-controle : la logique de check doit attraper ses propres cas."""
    import tempfile

    ok = "---\nname: a\ndescription: d\nlicense: MIT\nmetadata:\n  version: '1'\n  author: AIEN\n  tags: x\n---\n"
    cases = {
        ok: 0,
        "---\nname: a\ndescription: d\n---\n": 1,                                        # license + metadata absents
        "---\nname: a\ndescription: d\nlicense: MIT\nmetadata: {}\n---\n": 1,            # version/author/tags absents
        ok.replace("tags: x", "tags: a, b, c, d"): 1,                                    # 4 tags
        ok.replace("tags: x", "tags: [x]"): 1,                                          # liste non portable
        ok.replace("author: AIEN", "author: 12"): 1,                                       # author non chaine
        ok.replace("description: d", "description: 'a <b>'"): 1,                           # chevrons
        ok.replace("name: a", "name: A_b"): 1,                                             # kebab-case
        ok.replace("license: MIT", "license: MIT\nversion: '1'"): 1,                       # cle hors spec
    }
    with tempfile.TemporaryDirectory() as td:
        for i, (body, expect_fail) in enumerate(cases.items()):
            d = Path(td) / "a"
            d.mkdir(exist_ok=True)
            f = d / "SKILL.md"
            f.write_text(body, encoding="utf-8")
            errs = check(f)
            assert bool(errs) == bool(expect_fail), f"cas {i} : {errs}"
    print("demo OK")


if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo()
    else:
        sys.exit(main())
