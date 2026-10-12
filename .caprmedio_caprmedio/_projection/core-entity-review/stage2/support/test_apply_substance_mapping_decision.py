"""Focused structural checks for the one-off CA-P-2048 supplement builder."""
from __future__ import annotations

from copy import deepcopy
import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).with_name("apply_substance_mapping_decision.py")
SPEC = importlib.util.spec_from_file_location("apply_substance_mapping_decision", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ApplySubstanceMappingDecisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.document = MODULE.build_supplement()

    def copied_document(self) -> dict:
        return deepcopy(self.document)

    def test_exact_coverage_and_target(self) -> None:
        MODULE.validate_supplement(self.document)
        rows = self.document["occurrences"]
        self.assertEqual(len(rows), 143)
        self.assertEqual(len({row["source_path"] for row in rows}), 142)
        self.assertEqual(sum(row["baseline_proposed_value"] != MODULE.TARGET_VALUE for row in rows), 137)
        self.assertEqual(sum(row["baseline_proposed_value"] == MODULE.TARGET_VALUE for row in rows), 6)
        self.assertTrue(all(row["old_value"] == "Atom/Claim" for row in rows))
        self.assertTrue(all(row["proposed_value"] == "Atom.Substance" for row in rows))
        self.assertTrue(all(row["executable"] is False for row in rows))

    def test_rejects_stale_input_pin(self) -> None:
        document = self.copied_document()
        document["evidence_pins"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "stale or incomplete input pins"):
            MODULE.validate_supplement(document)

    def test_rejects_stale_current_source(self) -> None:
        stale = deepcopy(self.document["occurrences"][0])
        stale["source_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "stale current source"):
            MODULE.current_body_evidence(MODULE.ROOT, stale)

    def test_rejects_missing_or_extra_occurrence(self) -> None:
        missing = self.copied_document()
        missing["occurrences"].pop()
        with self.assertRaisesRegex(ValueError, "exact supplement occurrence coverage"):
            MODULE.validate_supplement(missing)
        extra = self.copied_document()
        extra["occurrences"].append(deepcopy(extra["occurrences"][0]))
        with self.assertRaisesRegex(ValueError, "exact supplement occurrence coverage"):
            MODULE.validate_supplement(extra)

    def test_rejects_wrong_or_compound_mapping(self) -> None:
        wrong_target = self.copied_document()
        wrong_target["occurrences"][0]["proposed_value"] = "Atom.Claim"
        with self.assertRaisesRegex(ValueError, "exact Atom.Substance proposal"):
            MODULE.validate_supplement(wrong_target)
        compound = self.copied_document()
        compound["occurrences"][0]["old_value"] = "Atom/Claim/Content Role"
        with self.assertRaisesRegex(ValueError, "baseline origin changed: old_value"):
            MODULE.validate_supplement(compound)

    def test_preserves_baseline_quarantine_and_candidate_only_boundary(self) -> None:
        document = self.copied_document()
        document["occurrences"][0]["quarantined"] = True
        with self.assertRaisesRegex(ValueError, "baseline origin changed: quarantined"):
            MODULE.validate_supplement(document)
        self.assertTrue(all(row["question"] is None for row in self.document["occurrences"]))
        self.assertTrue(all(row["executable"] is False for row in self.document["occurrences"]))


if __name__ == "__main__":
    unittest.main()
