"""Tests du contrat de validation des skills, via son interface publique."""
import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

SPEC = importlib.util.spec_from_file_location(
    "validate_skills", Path(__file__).with_name("validate-skills.py")
)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class SkillValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.skill = Path(self.temp.name) / "example"
        self.skill.mkdir()
        self.path = self.skill / "SKILL.md"
        self.frontmatter = {
            "name": "example",
            "description": "Explique un exemple concret.",
            "license": "Apache-2.0",
            "metadata": {"version": "0.1.0", "author": "Example", "tags": "a, b, c"},
        }

    def validate(self):
        self.path.write_text(
            "---\n" + yaml.safe_dump(self.frontmatter) + "---\n\nInstructions.\n",
            encoding="utf-8",
        )
        return validator.check(self.path)

    def test_portable_metadata(self):
        self.frontmatter["metadata"]["homepage"] = "https://example.org"
        self.assertEqual(self.validate(), [])

    def test_required_values_reject_null_empty_and_wrong_types(self):
        for field in ("name", "description", "license", "metadata"):
            original = self.frontmatter[field]
            for value in (None, "", "  ", [], 12, False):
                with self.subTest(field=field, value=value):
                    self.frontmatter[field] = value
                    self.assertTrue(self.validate())
            self.frontmatter[field] = original

    def test_optional_strings_are_validated_when_present(self):
        for field in ("compatibility", "allowed-tools"):
            for value in (None, "", "  ", [], 12):
                with self.subTest(field=field, value=value):
                    self.frontmatter[field] = value
                    self.assertTrue(self.validate())
            self.frontmatter[field] = "Read"
        self.assertEqual(self.validate(), [])

    def test_all_metadata_keys_and_values_must_be_strings(self):
        for key, value in (("tags", ["a"]), ("custom", True), ("custom", {}), (1, "a")):
            with self.subTest(key=key, value=value):
                self.frontmatter["metadata"] = {
                    "version": "0.1.0", "author": "Example", "tags": "a", key: value
                }
                self.assertTrue(self.validate())

    def test_required_metadata_values_must_be_nonempty(self):
        for field in ("version", "author", "tags"):
            for value in (None, "", "  "):
                with self.subTest(field=field, value=value):
                    self.frontmatter["metadata"] = {
                        "version": "0.1.0", "author": "Example", "tags": "a", field: value
                    }
                    self.assertTrue(self.validate())

    def test_tags_count_and_empty_items(self):
        for value in ("a,b,c,d", "a,", ",a", "a, ,b"):
            with self.subTest(value=value):
                self.frontmatter["metadata"]["tags"] = value
                self.assertTrue(self.validate())

    def test_name_and_lengths(self):
        for field, value in (
            ("name", "different"), ("name", "-example"), ("name", "ex--ample"),
            ("name", "Example"), ("name", "a" * 65),
            ("description", "d" * 1025), ("description", "a <b>"),
            ("compatibility", "a" * 501),
        ):
            with self.subTest(field=field, value=value):
                old = self.frontmatter.get(field)
                self.frontmatter[field] = value
                self.assertTrue(self.validate())
                if old is None:
                    self.frontmatter.pop(field)
                else:
                    self.frontmatter[field] = old
        self.frontmatter["description"] = "d" * 1024
        self.frontmatter["compatibility"] = "a" * 500
        self.assertEqual(self.validate(), [])

    def test_unknown_fields_report_errors_without_crashing(self):
        self.frontmatter["version"] = "1.0.0"
        self.frontmatter[42] = "unexpected"
        self.assertTrue(self.validate())

    def test_missing_required_fields(self):
        for field in ("name", "description", "license", "metadata"):
            with self.subTest(field=field):
                old = self.frontmatter.pop(field)
                self.assertTrue(self.validate())
                self.frontmatter[field] = old

    def test_nested_skill_is_rejected(self):
        nested = self.skill / "references"
        nested.mkdir()
        (nested / "SKILL.md").write_text("Nested skill.")
        self.assertTrue(self.validate())

    def test_invalid_yaml_and_delimiters(self):
        self.assertEqual(self.validate(), [])
        valid = self.path.read_text()
        for content in ("Instructions.", "---\nname: [\n---\n", "---\n[]\n---\n",
                        valid.replace("\n---\n", "\n---not-a-delimiter\n")):
            with self.subTest(content=content):
                self.path.write_text(content)
                self.assertTrue(validator.check(self.path))

    def test_cli_includes_templates(self):
        root = Path(self.temp.name) / "repo"
        script = root / "scripts" / "validate-skills.py"
        script.parent.mkdir(parents=True)
        shutil.copyfile(Path(__file__).with_name("validate-skills.py"), script)
        published = root / "plugins" / "example" / "skills" / "example" / "SKILL.md"
        template = root / "templates" / "example" / "SKILL.md"
        self.assertEqual(self.validate(), [])
        for target in (published, template):
            target.parent.mkdir(parents=True)
            shutil.copyfile(self.path, target)
        result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("2/2 conformes", result.stdout)
        template.write_text(template.read_text().replace("tags: a, b, c", "tags: [a, b, c]"))
        result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("FAIL templates/example/SKILL.md", result.stdout)


if __name__ == "__main__":
    unittest.main()
