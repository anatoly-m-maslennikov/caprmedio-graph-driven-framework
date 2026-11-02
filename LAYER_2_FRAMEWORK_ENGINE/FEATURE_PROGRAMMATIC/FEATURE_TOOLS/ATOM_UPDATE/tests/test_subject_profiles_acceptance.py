"""CA-P-1975 independent acceptance checks for approved Subject notation.

Expected occurrence rows and graph edges below are literal test-owned values.
They deliberately do not ask a graph producer to decide what the expected
lookup result or native edge direction should be.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


TESTS = Path(__file__).resolve().parent
TOOLS = TESTS.parents[1]

for path in (TOOLS, TESTS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import atom_operations as operations  # noqa: E402
import test_subject_tools_acceptance as fixtures  # noqa: E402
from subject_notation import get_profile  # noqa: E402


class SubjectProfilesAcceptanceTests(unittest.TestCase):
    """A literal acceptance ledger over a disposable complete Project fixture."""

    def setUp(self) -> None:
        # Reuse only the established complete-carrier Project scaffolding.  The
        # selected Atom subjects, expected occurrence ledger, and edge ledger
        # remain authored locally in this test.
        self.fixture = fixtures.SubjectToolsAcceptanceTest()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        self.paths: dict[str, Path] = {}
        self._write_approved_atoms()

    def _write_approved_atoms(self) -> None:
        self.paths["requirement"] = self.fixture._write_atom(
            self.fixture.requirements / "CA-R-3001-FRAMEWORK_METHODOLOGY-REQUIREMENT--approved-rmedo.md",
            "CA-R-3001", "Requirement", "FRAMEWORK_METHODOLOGY",
            "RMEDO/Capability.Substance: Scope Unit",
            ("RMEDO/Run.Operator: AI Agent",),
        )
        self.paths["operations"] = self.fixture._write_atom(
            self.fixture.methodology_operations / "CA-O-3002-FRAMEWORK_METHODOLOGY-OPERATIONS--approved-rmedo.md",
            "CA-O-3002", "Operations", "FRAMEWORK_METHODOLOGY",
            "RMEDO/Run.Operator: AI Agent",
            ("RMEDO/Capability.Substance: Scope Unit",),
        )
        self.paths["method"] = self.fixture._write_atom(
            self.fixture.methods / "CA-M-3006-FRAMEWORK_METHODOLOGY-METHOD--approved-rmedo.md",
            "CA-M-3006", "Method", "FRAMEWORK_METHODOLOGY",
            "RMEDO/Capability.Substance: Scope Unit", (),
        )
        self.paths["evaluation"] = self.fixture._write_atom(
            self.fixture.evaluations / "CA-E-3007-FRAMEWORK_METHODOLOGY-EVALUATION--approved-rmedo.md",
            "CA-E-3007", "Evaluation", "FRAMEWORK_METHODOLOGY",
            "RMEDO/Capability.Substance: Scope Unit", (),
        )
        self.paths["delivery"] = self.fixture._write_atom(
            self.fixture.deliveries / "CA-D-3008-FRAMEWORK_METHODOLOGY-DELIVERY--approved-rmedo.md",
            "CA-D-3008", "Delivery", "FRAMEWORK_METHODOLOGY",
            "RMEDO/Capability.Substance: Scope Unit", (),
        )
        self.paths["concern"] = self.fixture._write_atom(
            self.fixture.concerns / "CA-C-3003-FRAMEWORK_METHODOLOGY-CONCERN--excluded-rmedo.md",
            "CA-C-3003", "Concern", "FRAMEWORK_METHODOLOGY",
            "RMEDO/Capability.Substance: Scope Unit", (),
        )
        self.paths["analysis"] = self.fixture._write_atom(
            self.fixture.analysis / "CA-A-3004-FRAMEWORK_METHODOLOGY-ANALYSIS--excluded-rmedo.md",
            "CA-A-3004", "Analysis", "FRAMEWORK_METHODOLOGY",
            "RMEDO/Capability.Substance: Scope Unit", (),
        )
        self.paths["plan"] = self.fixture._write_atom(
            self.fixture.plans / "CA-P-3005-FRAMEWORK_METHODOLOGY-PLAN--excluded-rmedo.md",
            "CA-P-3005", "Plan", "FRAMEWORK_METHODOLOGY",
            "RMEDO/Capability.Substance: Scope Unit", (),
        )

    def _search(self, subject: str, *, content_role: list[str] | None = None) -> dict[str, object]:
        args = argparse.Namespace(
            subject=subject,
            subject_field="both",
            subject_match="prefix",
            content_role=content_role,
            scope_unit=None,
            under=None,
            lifecycle=None,
            atom=None,
            query=None,
            limit=None,
            view="metadata",
            subject_profile="approved",
        )
        return operations.run_search(self.root, args)

    @staticmethod
    def _occurrence_ledger(result: dict[str, object]) -> list[tuple[object, ...]]:
        occurrences = result["occurrences"]
        assert isinstance(occurrences, list)
        return [
            (row["atom_id"], row["field"], row["index"], row["value"])
            for row in occurrences
            if isinstance(row, dict)
        ]

    @staticmethod
    def _verify_preview_seal(preview: dict[str, object]) -> None:
        """Independent canonical-byte verifier, intentionally not a producer call."""

        unsigned = copy.deepcopy(preview)
        supplied = unsigned.pop("preview_sha256")
        expected = hashlib.sha256(
            json.dumps(unsigned, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
        ).hexdigest()
        if supplied != expected:
            raise AssertionError("preview seal does not cover the complete preview")

    def test_approved_lookup_has_literal_rmedo_ledger_and_cap_exclusion(self) -> None:
        selected = self._search(
            "RMEDO/Capability",
            content_role=["Requirement", "Method", "Evaluation", "Delivery", "Operations"],
        )
        self.assertEqual("approved", selected["subject_profile"])
        self.assertEqual(
            [
                ("CA-R-3001", "governs", None, "RMEDO/Capability.Substance: Scope Unit"),
                ("CA-M-3006", "governs", None, "RMEDO/Capability.Substance: Scope Unit"),
                ("CA-E-3007", "governs", None, "RMEDO/Capability.Substance: Scope Unit"),
                ("CA-D-3008", "governs", None, "RMEDO/Capability.Substance: Scope Unit"),
                ("CA-O-3002", "depends_on", 0, "RMEDO/Capability.Substance: Scope Unit"),
            ],
            self._occurrence_ledger(selected),
        )
        self.assertEqual(5, selected["count"])

        operations_only = self._search("RMEDO/Run", content_role=["Operations"])
        self.assertEqual(
            [("CA-O-3002", "governs", None, "RMEDO/Run.Operator: AI Agent")],
            self._occurrence_ledger(operations_only),
        )
        excluded = self._search("RMEDO/Capability", content_role=["Concern", "Analysis", "Plan"])
        self.assertEqual(
            {
                ("CA-C-3003", "governs", None, "RMEDO/Capability.Substance: Scope Unit"),
                ("CA-A-3004", "governs", None, "RMEDO/Capability.Substance: Scope Unit"),
                ("CA-P-3005", "governs", None, "RMEDO/Capability.Substance: Scope Unit"),
            },
            set(self._occurrence_ledger(excluded)),
        )
        self.assertFalse(
            {row[0] for row in self._occurrence_ledger(selected)}
            & {"CA-C-3003", "CA-A-3004", "CA-P-3005"}
        )

    def test_approved_preview_seals_evidence_and_tampering_is_rejected(self) -> None:
        source = self.paths["requirement"]
        before = source.read_bytes()
        selector = source.relative_to(self.root).as_posix()
        payload = {
            "subject_profile": "approved",
            "atoms": [{
                "selector": selector,
                "expected": {
                    "atom_id": "CA-R-3001",
                    "version": 1,
                    "sha256": hashlib.sha256(before).hexdigest(),
                },
                "subject_patches": [{
                    "field": "governs",
                    "old": "RMEDO/Capability.Substance: Scope Unit",
                    "new": "RMEDO/Capability.Substance: Bounded Scope Unit",
                }],
            }],
        }
        with patch.object(operations, "_load_payload", return_value=payload), patch.object(
            operations, "_validate_complete_carrier"
        ) as validate:
            preview = operations.run_update(self.root, argparse.Namespace(input="-", apply=False))
        self.assertEqual(2, validate.call_count)
        self.assertEqual(before, source.read_bytes())
        self.assertEqual("approved", preview["subject_profile"])
        evidence = preview["subject_profile_evidence"]
        self.assertIsInstance(evidence, dict)
        self.assertEqual("not_performed", evidence["native_admission"])
        pins = evidence["grammar_pins"]
        self.assertIsInstance(pins, list)
        for pin, selected in zip(pins, get_profile("approved").grammar_pins, strict=True):
            raw = (self.root / selected.path).read_bytes()
            metadata = operations.parse_carrier(raw, self.root / selected.path).metadata
            self.assertEqual((selected.atom_id, metadata["version"], selected.path, hashlib.sha256(raw).hexdigest()),
                             (pin["atom_id"], pin["version"], pin["path"], pin["sha256"]))
        self.assertEqual(1, preview["count"])
        change = preview["atoms"][0]
        self.assertIsInstance(change, dict)
        self.assertEqual(2, change["after_version"])
        patches = change["patches"]
        self.assertIsInstance(patches, list)
        self.assertEqual(1, len(patches))
        record = patches[0]
        self.assertIsInstance(record, dict)
        self.assertEqual(
            {"field": "governs", "index": None, "old": "RMEDO/Capability.Substance: Scope Unit",
             "new": "RMEDO/Capability.Substance: Bounded Scope Unit", "changed": True},
            {key: record[key] for key in ("field", "index", "old", "new", "changed")},
        )
        self.assertIsInstance(record["span"], dict)
        self.assertTrue(all(isinstance(record["span"][key], int) for key in ("start", "end")))
        self._verify_preview_seal(preview)
        corrupted = copy.deepcopy(preview)
        corrupted["atoms"][0]["patches"][0]["new"] = "caller-corrupted-value"
        with self.assertRaises(AssertionError):
            self._verify_preview_seal(corrupted)

        with patch.object(operations, "_load_payload", return_value=payload):
            with self.assertRaises(operations.ToolError) as refused:
                operations.run_update(self.root, argparse.Namespace(input="-", apply=True))
        self.assertEqual("subject-apply-not-admitted", refused.exception.code)
        self.assertEqual(before, source.read_bytes())

if __name__ == "__main__":
    unittest.main()
