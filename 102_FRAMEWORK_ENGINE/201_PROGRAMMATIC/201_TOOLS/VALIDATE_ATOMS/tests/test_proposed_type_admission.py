"""Current source-bound Type checks at the shared proposed-carrier boundary."""

from pathlib import Path
import sys
import unittest
from unittest.mock import patch

TOOL = Path(__file__).resolve().parents[1]
TOOLS = TOOL.parent
PROJECT = TOOLS.parents[2]
sys.path[:0] = [str(TOOLS), str(TOOL)]

from validate_atoms_workers import proposed_carrier
from validate_atoms_workers.authority import Obligation
from validate_atoms_workers.check_schema_extended import ADAPTERS
from validate_atoms_workers.check_support import Check
import test_proposed_carrier_admission_regressions as fixtures  # noqa: E402


class ProposedTypeAdmissionTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ProposedCarrierAdmissionRegressions()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.selection = self.fixture.project()
        self.root = self.selection.root
        self.context = proposed_carrier.source_context_from_project(self.root)

    def check_type(self, role, kind):
        check = Check(Obligation("model.domains", [], True, "verified sources"),
                      self.context.authority, self.context.inputs)
        metadata = {"content_role": role}
        if kind is not None:
            metadata["type"] = kind
        ADAPTERS["model.domains"](metadata, "", check)
        return check

    def test_supported_role_types_and_ordinary_absence(self):
        admitted = {
            "Concern": ("Question", "Conflict", "Problem"),
            "Analysis": ("Analysis Report", "Rationale"),
            "Plan": ("Plan", "Action Policy"),
            "Requirement": (None, "Boundary", "Constraint", "Goal", "Demand"),
            "Method": (None, "Implementation Method", "Implementation Decision",
                       "External Implementation Method", "Method Binding"),
            "Evaluation": ("QA Case", "Evaluation Control", "Evaluation Approach"),
            "Delivery": (None, "Release Definition", "Environment Definition"),
            "Operations": ("Action", "Workflow", "Step", "Actor"),
        }
        for role, kinds in admitted.items():
            for kind in kinds:
                with self.subTest(role=role, kind=kind):
                    check = self.check_type(role, kind)
                    self.assertEqual((check.findings, check.gaps), ([], []))
        for role, kind in (("Plan", "Action"), ("Concern", "Plan"),
                           ("Analysis", "Action"), ("Requirement", "QA Case"),
                           ("Method", "Plan"), ("Delivery", "Action"),
                           ("Operations", "Plan"), ("Evaluation", "Evaluation"),
                           ("Evaluation", "Test")):
            with self.subTest(role=role, kind=kind):
                self.assertTrue(self.check_type(role, kind).findings)
        self.assertTrue(self.check_type("Implementation", "Code").gaps)

    def test_shared_boundary_rejects_plan_action(self):
        metadata = dict(
            atom_id="CA-P-999999", content_role="Plan", type="Plan",
            current_scope_unit="amber", claim_target_scope_unit="amber",
            local_tier="Standard", global_tier=2, status="Active", version=1,
            author="Fixture Operator", updated_at="2026-10-13 12:00:00 +0400",
            subjects={"governs": "Tool", "depends_on": []}, relations={},
        )
        body = ("# Summary\n\nType admission\n\n## Objective\n\nCheck a Plan.\n\n"
                "## Details\n\n### Definition of Done\n\nThe check passes.\n")
        path = Path("03_plan/CA-P-999999--type-admission.md")
        proposed_carrier.validate_proposed_carrier(metadata, body, self.context, path)
        with self.assertRaises(proposed_carrier.ProposedCarrierError):
            proposed_carrier.validate_proposed_carrier(
                dict(metadata, type="Action"), body, self.context, path)

    def test_missing_or_changed_type_pin_refuses_context(self):
        original = proposed_carrier._entry
        for changed in (False, True):
            def entry(identifier, **kwargs):
                result = original(identifier, **kwargs)
                if identifier == "CA-R-1666":
                    return dict(result, sha256="0" * 64) if changed else {}
                return result
            with self.subTest(changed=changed), patch.object(proposed_carrier, "_entry", entry):
                with self.assertRaises(proposed_carrier.ProposedCarrierError):
                    proposed_carrier.source_context_from_project(self.root)


if __name__ == "__main__":
    unittest.main()
