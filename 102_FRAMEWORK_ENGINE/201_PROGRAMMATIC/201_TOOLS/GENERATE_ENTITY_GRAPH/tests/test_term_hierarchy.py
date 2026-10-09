"""Focused unit tests for the pure Terms-Graph hierarchy module."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "term_hierarchy.py"
SPEC = importlib.util.spec_from_file_location("term_hierarchy", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
hierarchy = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = hierarchy
SPEC.loader.exec_module(hierarchy)


def carrier(atom_id: str = "CA-D-258", revision: int = 11) -> dict[str, object]:
    return {
        "atom_id": atom_id,
        "atom_revision": revision,
        "carrier_path": f"selected/{atom_id}.md",
        "carrier_sha256": "a" * 64,
    }


def contribution(claim: str, *, section: str = "Claim") -> dict[str, object]:
    return {"primary_section": section, "primary_claim": claim}


class AssessHierarchyClaimTests(unittest.TestCase):
    def test_recognizes_each_confirmed_current_classification_claim(self) -> None:
        cases = (
            ("CA-D-258", 11, "File Carrier", "Carrier", "the Term File Carrier NARROWER_THAN Carrier."),
            ("CA-D-259", 11, "Directory Carrier", "Carrier", "the Term Directory Carrier NARROWER_THAN Carrier."),
            ("CA-D-414", 14, "Carrier", "Primary Entity", "the Term Carrier **must** be **NARROWER_THAN** Primary Entity."),
            (
                "CA-D-416", 11, "Markdown Atom Carrier", "File Carrier",
                "the Term Markdown Atom Carrier **must** be **NARROWER_THAN** File Carrier.",
            ),
        )
        for atom_id, revision, child, parent, claim in cases:
            with self.subTest(atom_id=atom_id):
                result = hierarchy.assess_hierarchy_claim(
                    carrier(atom_id, revision),
                    {"governs": [child], "depends_on": [parent]},
                    contribution(claim),
                )

                self.assertEqual("recognized", result["state"])
                self.assertEqual(child, result["facts"][0]["child"])
                self.assertEqual(parent, result["facts"][0]["parent"])

    def test_recognizes_exact_current_plain_claim_with_source_evidence(self) -> None:
        result = hierarchy.assess_hierarchy_claim(
            carrier(),
            {"governs": "File Carrier", "depends_on": ["Carrier"]},
            contribution("the Term File Carrier NARROWER_THAN Carrier."),
        )

        self.assertEqual("recognized", result["state"])
        self.assertEqual(1, len(result["facts"]))
        fact = result["facts"][0]
        self.assertEqual("terms/NARROWER_THAN", fact["kind"])
        self.assertEqual("terms/NARROWER_THAN", fact["relation"])
        self.assertEqual("File Carrier", fact["child"])
        self.assertEqual("Carrier", fact["parent"])
        self.assertEqual("child_to_parent", fact["direction"])
        evidence = fact["source_evidence"]
        self.assertEqual("Claim", evidence["primary_section"])
        self.assertEqual("a" * 64, evidence["carrier_sha256"])
        self.assertIn("primary_section_sha256", evidence)
        self.assertIn("claim_sha256", evidence)
        self.assertIn("native-admission-unassessed", {row["code"] for row in result["diagnostics"]})

    def test_recognizes_exact_current_obligation_claim(self) -> None:
        result = hierarchy.assess_hierarchy_claim(
            carrier("CA-D-414", 14),
            {"governs": ["Carrier"], "depends_on": ["Primary Entity"]},
            contribution("the Term Carrier **must** be **NARROWER_THAN** Primary Entity."),
        )

        self.assertEqual("recognized", result["state"])
        self.assertEqual("Primary Entity", result["facts"][0]["parent"])

    def test_legacy_subkind_is_not_aliased(self) -> None:
        result = hierarchy.assess_hierarchy_claim(
            carrier(),
            {"governs": ["File Carrier"], "depends_on": ["Carrier"]},
            contribution("File Carrier SUBKIND_OF Carrier."),
        )

        self.assertEqual("not_relation", result["state"])
        self.assertEqual([], result["facts"])

    def test_details_and_fences_are_not_claim_input(self) -> None:
        result = hierarchy.assess_hierarchy_claim(
            carrier(),
            {"governs": ["File Carrier"], "depends_on": ["Carrier"]},
            contribution("the Term File Carrier NARROWER_THAN Carrier.", section="Details"),
        )

        self.assertEqual("not_relation", result["state"])
        self.assertEqual([], result["facts"])

    def test_candidate_must_match_governs_and_depends_on_exactly(self) -> None:
        result = hierarchy.assess_hierarchy_claim(
            carrier(),
            {"governs": ["Other Carrier"], "depends_on": ["Different Parent"]},
            contribution("the Term File Carrier NARROWER_THAN Carrier."),
        )

        self.assertEqual("target_mismatch", result["state"])
        self.assertEqual([], result["facts"])
        self.assertIn("hierarchy-claim-subject-mismatch", {row["code"] for row in result["diagnostics"]})

    def test_relation_like_noncurrent_claim_is_unsupported(self) -> None:
        result = hierarchy.assess_hierarchy_claim(
            carrier(),
            {"governs": ["File Carrier"], "depends_on": ["Carrier"]},
            contribution("the Term File Carrier must be NARROWER_THAN Carrier."),
        )

        self.assertEqual("unsupported_candidate", result["state"])

    def test_prohibition_never_emits_a_hierarchy_fact(self) -> None:
        result = hierarchy.assess_hierarchy_claim(
            carrier("CA-R-1264"),
            {"governs": ["File Carrier"], "depends_on": ["Carrier"]},
            contribution("the Term File Carrier **must not** be **NARROWER_THAN** Carrier."),
        )

        self.assertEqual("unsupported_candidate", result["state"])
        self.assertEqual([], result["facts"])


class AnalyzeHierarchyTests(unittest.TestCase):
    @staticmethod
    def fact(child: str, parent: str, *, relation: str = "terms/NARROWER_THAN") -> dict[str, object]:
        return {
            "relation": relation,
            "child": child,
            "parent": parent,
            "direction": "child_to_parent",
            "source_evidence": {"carrier_path": f"selected/{child}.md"},
        }

    def test_multiple_parents_and_ancestors_are_supported(self) -> None:
        result = hierarchy.analyze_hierarchy(
            ["Child", "Parent A", "Parent B", "Grandparent"],
            [
                self.fact("Child", "Parent A"),
                self.fact("Child", "Parent B"),
                self.fact("Parent A", "Grandparent"),
            ],
        )

        self.assertEqual(["Parent A", "Parent B"], result["parents_by_term"]["Child"])
        self.assertEqual(["Grandparent", "Parent A", "Parent B"], result["ancestors_by_term"]["Child"])
        self.assertEqual(["Grandparent", "Parent B"], result["roots"])
        self.assertEqual([], result["cycles"])

    def test_narrower_than_cycles_only_are_reported(self) -> None:
        result = hierarchy.analyze_hierarchy(
            ["A", "B"], [self.fact("A", "B"), self.fact("B", "A")],
        )

        self.assertEqual([["A", "B"]], result["cycles"])
        self.assertIn("terms-narrower-than-cycle", {row["code"] for row in result["diagnostics"]})

    def test_external_parent_neither_becomes_native_nor_false_isolated_root(self) -> None:
        result = hierarchy.analyze_hierarchy(
            ["Child", "Independent"], [self.fact("Child", "External Parent")],
        )

        self.assertEqual({"Child": [], "Independent": []}, result["parents_by_term"])
        self.assertEqual(["Independent"], result["roots"])
        self.assertEqual(["External Parent"], [row["parent"] for row in result["external_references"]])
        self.assertIn("root-coverage-unresolved", {row["code"] for row in result["diagnostics"]})

    def test_unknown_relation_kind_is_rejected_without_edge_inference(self) -> None:
        result = hierarchy.analyze_hierarchy(
            ["Child", "Parent"],
            [{**self.fact("Child", "Parent"), "kind": "legacy/SUBKIND_OF", "relation": "legacy/SUBKIND_OF"}],
        )

        self.assertEqual([], result["edges"])
        self.assertEqual(["Child", "Parent"], result["roots"])
        self.assertIn("hierarchy-kind-unsupported", {row["code"] for row in result["diagnostics"]})
