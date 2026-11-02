"""Synthetic regressions for normative parent ownership, not Subject equality."""

from __future__ import annotations

import copy
from pathlib import Path
import sys
import unittest

TOOL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL))

from golden_authority import frozen_sources  # noqa: E402
from validate_atoms_workers.authority import AuthorityContext, Obligation  # noqa: E402
from validate_atoms_workers.check_graph_extended import relations_resolution  # noqa: E402
from validate_atoms_workers.check_support import Check  # noqa: E402


def unit(name: str, parent: str, depth: int) -> dict:
    return dict(
        scope_unit_name=name, parent=parent, structural_level=depth,
        scope_unit_type="Unordered", scope_unit_label="Layer",
        navigational_order_number=1, authority_path=f".caprmedio_demo/{name}",
        delivery_path=f"src/{name}",
    )


def atom(identity: str, owner: str, tier: int, **changes) -> dict:
    return dict(
        atom_id=identity, version=1, content_role="Requirement", status="Active",
        current_scope_unit=owner, global_tier=tier, **changes,
    )


class AncestorParentAdmissionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sources = frozen_sources()

    def setUp(self) -> None:
        self.child = atom("X-R-1", "CORE", 9, subjects={"governs": "Entity/Continuant"})
        self.parent = atom(
            "X-R-2", "SOURCES", 8, type="Goal", claim_target_scope_unit="CORE",
            subjects={"governs": "CORE/Goal"},
        )
        self.structure = dict(schema_version=1, scope_units=[
            unit("METHODOLOGY", "PROJECT", 1),
            unit("SOURCES", "METHODOLOGY", 2),
            unit("CORE", "SOURCES", 3),
            unit("CONFIG", "SOURCES", 3),
            unit("ENGINE", "PROJECT", 1),
        ])

    def check(self, *, structure=True, complete=True) -> Check:
        child = {**self.child, "relations": {"child_of": [self.parent["atom_id"]]}}
        context = AuthorityContext([], 0, 0, 0, [], (), {}, False)
        check = Check(Obligation("relations.resolution", [], True, "fixture"), context)
        check.inputs = {
            "sources": self.sources,
            "references": [{"path": Path("/inventory/parent.md"), "metadata": self.parent}],
            "reference_complete": complete,
            "path": Path("/inventory/child.md"),
            "_project_identity": {"project": {"name": "demo"}},
        }
        if structure:
            check.inputs["structure"] = self.structure
        before = copy.deepcopy((child, self.parent, self.structure))
        relations_resolution(child, "", check)
        self.assertEqual((child, self.parent, self.structure), before)
        return check

    def test_ancestor_goal_with_different_subject_and_owner_is_accepted(self) -> None:
        result = self.check()
        self.assertFalse(result.findings + result.gaps)

    def test_distant_ancestor_and_nonadjacent_tier_are_accepted(self) -> None:
        self.parent.update(current_scope_unit="METHODOLOGY", global_tier=5)
        result = self.check()
        self.assertFalse(result.findings + result.gaps)

    def test_equal_tier_ancestor_is_accepted_under_e117(self) -> None:
        self.parent["global_tier"] = self.child["global_tier"]
        result = self.check()
        self.assertFalse(result.findings + result.gaps)

    def test_project_parent_resolves_from_explicit_identity(self) -> None:
        self.parent.update(current_scope_unit="demo", global_tier=1)
        result = self.check()
        self.assertFalse(result.findings + result.gaps)

    def test_same_owner_needs_no_new_structure_input(self) -> None:
        self.parent.update(current_scope_unit="CORE", global_tier=9)
        self.child["global_tier"] = 11
        result = self.check(structure=False)
        self.assertFalse(result.findings + result.gaps)

    def test_sibling_or_unrelated_owner_is_not_replaced_by_claim_target(self) -> None:
        for owner in ("CONFIG", "ENGINE"):
            with self.subTest(owner=owner):
                self.parent.update(current_scope_unit=owner, claim_target_scope_unit="CORE")
                result = self.check()
                self.assertTrue(any("same or an ancestor" in x["reason"] for x in result.findings))
                self.assertFalse(result.gaps)

    def test_descendant_cannot_be_parent_even_with_lower_carried_tier(self) -> None:
        self.child["current_scope_unit"] = "SOURCES"
        self.parent["current_scope_unit"] = "CORE"
        self.assertTrue(self.check().findings)

    def test_same_owner_requires_strictly_lower_parent_tier(self) -> None:
        self.parent["current_scope_unit"] = self.child["current_scope_unit"]
        for tier in (9, 10):
            with self.subTest(tier=tier):
                self.parent["global_tier"] = tier
                result = self.check()
                self.assertTrue(result.findings)

    def test_greater_tier_ancestor_is_rejected(self) -> None:
        self.parent["global_tier"] = self.child["global_tier"] + 1
        result = self.check()
        self.assertTrue(any("greater Global Tier" in x["reason"] for x in result.findings))

    def test_missing_or_noninteger_tier_remains_unresolved(self) -> None:
        for value in (None, True, "8"):
            with self.subTest(value=value):
                self.parent["global_tier"] = value
                result = self.check()
                self.assertTrue(result.gaps)
                self.assertFalse(result.findings)

    def test_missing_structure_cannot_prove_ancestry(self) -> None:
        self.assertTrue(self.check(structure=False).gaps)

    def test_unknown_owner_is_not_inferred_from_target(self) -> None:
        for owner in ("UNKNOWN", "PROJECT"):
            with self.subTest(owner=owner):
                self.parent["current_scope_unit"] = owner
                self.assertTrue(self.check().gaps)

    def test_invalid_parentage_is_not_accepted(self) -> None:
        for defect in ("cycle", "duplicate", "unknown", "depth"):
            with self.subTest(defect=defect):
                self.setUp()
                rows = self.structure["scope_units"]
                if defect == "cycle":
                    rows[1]["parent"] = "CORE"
                elif defect == "duplicate":
                    rows.append(copy.deepcopy(rows[2]))
                elif defect == "unknown":
                    rows[1]["parent"] = "UNKNOWN"
                else:
                    rows[2]["structural_level"] = 9
                self.assertTrue(self.check().gaps)

    def test_ancestor_permission_does_not_bypass_active_parent_requirement(self) -> None:
        self.parent["status"] = "Archived"
        result = self.check()
        self.assertTrue(any("Active" in x["reason"] for x in result.findings))

    def test_ancestor_permission_does_not_bypass_reference_resolution(self) -> None:
        self.assertTrue(self.check(complete=False).gaps)


if __name__ == "__main__":
    unittest.main()
