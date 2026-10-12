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
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TESTS = Path(__file__).resolve().parent
TOOLS = TESTS.parents[1]
GRAPH_TOOLS = TOOLS / "GENERATE_ENTITY_GRAPH"
TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)

for path in (TOOLS, GRAPH_TOOLS, TESTS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import atom_operations as operations  # noqa: E402
import generate_entity_graph as graph  # noqa: E402
import test_subject_tools_acceptance as fixtures  # noqa: E402


APPROVED_GRAMMAR_PINS = [
    (
        "CA-R-1931",
        1,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
        "METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/"
        "CA-R-1931-CORE_META_MODEL--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md",
        "f11bc913a0f7b31abc746a86599eaeaa76db8be412568ef4c34f68c7d01525c8",
    ),
    (
        "CA-R-1321",
        14,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
        "METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/"
        "CA-R-1321-CORE_META_MODEL-CORE--define-subject-expression.md",
        "d883f1bd53ac3ea83aeff2d3d1fdfb5498641a0e5f2db5e8e79d8dfd5c5a84df",
    ),
    (
        "CA-R-1324",
        12,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
        "METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/"
        "CA-R-1324-CORE_META_MODEL-REQUIREMENT--reserve-subject-expression-separators.md",
        "33cbfee9844ba4dd895ae6745121fd5db5793a20aab27eb8b8d7b4591e7fb9a3",
    ),
    (
        "CA-M-228",
        16,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
        "METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/"
        "CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification.md",
        "0f398721d7d15aaf8e0b0f69a20b1b541e8d306839073c98eea4b80f9580b40d",
    ),
    (
        "CA-E-383",
        15,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
        "METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/"
        "CA-E-383-CORE_META_MODEL-EVALUATION_APPROACH--reject-invalid-subject-expressions.md",
        "6baca162365f248e08fc8d8a29b27e350149ff478290553b3cd6ee0441b4a6a6",
    ),
]


def graph_carrier(atom_id: str, governs: str, depends_on: tuple[str, ...]) -> str:
    dependency_lines = "\n".join(f"    - {value!r}" for value in depends_on)
    dependency_block = "  depends_on: []" if not dependency_lines else f"  depends_on:\n{dependency_lines}"
    return "\n".join((
        "---",
        f"atom_id: {atom_id}",
        "version: 1",
        "content_role: Definition",
        "type: Definition",
        "status: Active",
        "current_scope_unit: CORE_META_MODEL",
        "claim_target_scope_unit: CORE_META_MODEL",
        "subjects:",
        f"  governs: {governs!r}",
        dependency_block,
        "---",
        "# Summary",
        "",
        "Test-only carrier.",
        "",
        "## Claim",
        "",
        "Approved notation has no native slash edge admission.",
    ))


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

        self.graph_temporary = tempfile.TemporaryDirectory(
            dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True
        )
        self.addCleanup(self.graph_temporary.cleanup)
        self.graph_repository = Path(self.graph_temporary.name)
        self.graph_sources = self.graph_repository / "sources"
        self.graph_sources.mkdir()

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
        self.assertEqual(
            APPROVED_GRAMMAR_PINS,
            [(pin["atom_id"], pin["version"], pin["path"], pin["sha256"]) for pin in pins if isinstance(pin, dict)],
        )
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

    def test_approved_graph_has_only_literal_dot_and_colon_native_edges(self) -> None:
        source = self.graph_sources / "CA-R-4001.md"
        source.write_text(
            graph_carrier(
                "CA-R-4001",
                "RMEDO/Capability.Substance: Scope Unit",
                ("RMEDO/Run.Operator: AI Agent",),
            ),
            encoding="utf-8",
        )
        projection = graph.generate_projection(
            self.graph_repository, self.graph_sources, subject_profile="approved"
        )
        edges = [
            (row["relation"], row["source_subject"], row["source_term"], row["target_subject"], row["target_term"])
            for row in projection["term_system"]["edges"]
        ]
        expected_edges = [
                ("IS_ALLOWED_VALUE_OF", "RMEDO/Capability.Substance: Scope Unit", "Scope Unit",
                 "RMEDO/Capability.Substance", "Substance"),
                ("IS_ALLOWED_VALUE_OF", "RMEDO/Run.Operator: AI Agent", "AI Agent",
                 "RMEDO/Run.Operator", "Operator"),
                ("IS_BORNE_BY", "RMEDO/Capability.Substance", "Substance", "RMEDO/Capability", "Capability"),
                ("IS_BORNE_BY", "RMEDO/Run.Operator", "Operator", "RMEDO/Run", "Run"),
        ]
        self.assertEqual(expected_edges, edges)
        corrupted = copy.deepcopy(edges)
        corrupted[0] = ("NARROWER_THAN", *corrupted[0][1:])
        with self.assertRaises(AssertionError):
            self.assertEqual(expected_edges, corrupted)
        self.assertFalse(any(row[0] == "NARROWER_THAN" for row in edges))
        self.assertFalse(any(row[1] in {"RMEDO/Capability", "RMEDO/Run"} for row in edges))


if __name__ == "__main__":
    unittest.main()
