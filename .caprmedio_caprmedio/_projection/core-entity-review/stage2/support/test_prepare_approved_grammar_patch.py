"""Focused checks for the CA-P-2059 create-only grammar-adoption preview."""
from __future__ import annotations

from copy import deepcopy
import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).with_name("prepare_approved_grammar_patch.py")
SPEC = importlib.util.spec_from_file_location("prepare_approved_grammar_patch", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

TIMESTAMP = "2026-10-11 03:45:00 +0400"


class PrepareApprovedGrammarPatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.preview = MODULE.assemble_preview(MODULE.ROOT, TIMESTAMP)

    def copied_preview(self) -> dict:
        return deepcopy(self.preview)

    def test_exact_five_coverage_and_revision_sequence(self) -> None:
        MODULE.validate_preview(self.preview)
        effects = self.preview["planned_effects"]
        self.assertEqual([effect["atom_id"] for effect in effects], ["CA-R-1204", "CA-R-1321", "CA-R-1324", "CA-M-228", "CA-E-383"])
        self.assertEqual(effects[0]["successor"]["atom_id"], "CA-R-1931")
        self.assertEqual(effects[0]["successor"]["version"], 1)
        self.assertEqual([(effect["active"]["old_version"], effect["active"]["new_version"]) for effect in effects[1:]], [(12, 13), (10, 11), (14, 15), (13, 14)])
        self.assertIn("version: 1\n", effects[0]["successor"]["content_utf8"])
        self.assertIn("version: 13\n", effects[1]["active"]["new_content_utf8"])

    def test_rejects_successor_collision(self) -> None:
        with self.assertRaisesRegex(ValueError, "successor ID collision"):
            MODULE.ensure_successor_id_unoccupied({"CA-R-1204", "CA-R-1931"})

    def test_rejects_stale_approved_source_pin(self) -> None:
        preview = self.copied_preview()
        preview["source_pins"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "preview differs from pinned effect set: source_pins"):
            MODULE.validate_preview(preview)

    def test_rejects_missing_or_extra_change(self) -> None:
        missing = self.copied_preview()
        missing["planned_effects"].pop()
        with self.assertRaisesRegex(ValueError, "preview differs from pinned effect set: planned_effects"):
            MODULE.validate_preview(missing)
        extra = self.copied_preview()
        extra["planned_effects"].append(deepcopy(extra["planned_effects"][1]))
        with self.assertRaisesRegex(ValueError, "preview differs from pinned effect set: planned_effects"):
            MODULE.validate_preview(extra)

    def test_rejects_unapproved_other_bytes(self) -> None:
        preview = self.copied_preview()
        content = preview["planned_effects"][1]["active"]["new_content_utf8"]
        preview["planned_effects"][1]["active"]["new_content_utf8"] = content.replace('status: "Active"', 'status: "Disabled"')
        with self.assertRaisesRegex(ValueError, "preview differs from pinned effect set: planned_effects"):
            MODULE.validate_preview(preview)

    def test_preserves_prior_bytes_and_limits(self) -> None:
        replacement = self.preview["planned_effects"][0]
        self.assertEqual(replacement["approved_predecessor"]["content_utf8"], replacement["history"]["content_utf8"])
        for effect in self.preview["planned_effects"][1:]:
            self.assertEqual(effect["active"]["old_content_utf8"], effect["history"]["content_utf8"])
        self.assertTrue(any("No Journal entry" in limit for limit in self.preview["limits"]))
        self.assertIn("relations.evaluation_for CA-R-1204 -> CA-R-1931", self.preview["planned_effects"][-1]["allowed_changes"])
        self.assertIn("Details", self.preview["planned_effects"][-1]["allowed_changes"])

    def test_e383_uses_only_the_approved_mixed_component_case(self) -> None:
        content = self.preview["planned_effects"][-1]["active"]["new_content_utf8"]
        self.assertIn("`Artifact/Atom.Status: Active` **must** pass", content)
        self.assertIn("legacy five-component fixture", content)
        self.assertNotIn("`Atom.Content Role: Requirement.Type: Demand`", content)


if __name__ == "__main__":
    unittest.main()
