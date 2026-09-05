"""Tests des versions distribuees et des mises a jour de plugins."""
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "validate_releases", Path(__file__).with_name("validate-releases.py")
)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class ReleaseValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.plugin = self.root / "plugins" / "example"
        self.write_release("1.0.0")
        self.git("init", "-q")
        self.git("config", "user.name", "Example")
        self.git("config", "user.email", "example@example.org")
        self.git("add", ".")
        self.git("-c", "commit.gpgsign=false", "commit", "-qm", "Initial fixture")
        self.base = self.git("rev-parse", "HEAD").strip()

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, text=True)

    def write_release(self, version):
        for harness in (".claude-plugin", ".codex-plugin"):
            path = self.plugin / harness / "plugin.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps({"name": "example", "version": version}))
        (self.plugin / "CHANGELOG.md").write_text(f"# Changelog\n\n## {version}\n")

    def test_unchanged_plugin(self):
        self.assertEqual(validator.check(self.root, self.base), [])

    def test_changed_plugin_requires_version_increment(self):
        (self.plugin / "CHANGELOG.md").write_text("# Changelog\n\n## 1.0.0\n\nChanged.\n")
        self.assertTrue(validator.check(self.root, self.base))

    def test_new_version_passes_before_and_after_commit(self):
        self.write_release("1.0.1")
        self.assertEqual(validator.check(self.root, self.base), [])
        self.git("add", ".")
        self.git("-c", "commit.gpgsign=false", "commit", "-qm", "Release fixture")
        self.assertEqual(validator.check(self.root, self.base), [])

    def test_version_cannot_decrease(self):
        self.write_release("0.9.0")
        self.assertTrue(validator.check(self.root, self.base))

    def test_manifests_must_agree(self):
        (self.plugin / ".codex-plugin/plugin.json").write_text(
            json.dumps({"name": "example", "version": "1.0.1"})
        )
        self.assertTrue(validator.check(self.root))

    def test_name_must_match_directory(self):
        (self.plugin / ".codex-plugin/plugin.json").write_text(
            json.dumps({"name": "other", "version": "1.0.0"})
        )
        self.assertTrue(validator.check(self.root))

    def test_missing_version_note(self):
        (self.plugin / "CHANGELOG.md").write_text("# Changelog\n\n## 1.0.01\n")
        self.assertTrue(validator.check(self.root))

    def test_malformed_and_missing_manifests(self):
        path = self.plugin / ".codex-plugin/plugin.json"
        for content in ("{", "null", "[]", '{"version": null}', '{"version": "01.0.0"}'):
            with self.subTest(content=content):
                path.write_text(content)
                self.assertTrue(validator.check(self.root))
        path.unlink()
        self.assertTrue(validator.check(self.root))

    def test_new_plugin_has_no_previous_version(self):
        self.plugin = self.root / "plugins" / "new"
        self.write_release("1.0.0")
        for path in self.plugin.glob(".*-plugin/plugin.json"):
            path.write_text(json.dumps({"name": "new", "version": "1.0.0"}))
        self.git("add", ".")
        self.assertEqual(validator.check(self.root, self.base), [])


if __name__ == "__main__":
    unittest.main()
