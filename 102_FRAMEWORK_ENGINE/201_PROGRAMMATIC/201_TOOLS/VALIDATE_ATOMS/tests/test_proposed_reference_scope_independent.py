"""Independent controls for explicitly bounded reference admission, not Project validity."""

from pathlib import Path
import unittest
from unittest.mock import patch

import test_proposed_carrier_admission_regressions as fixtures
from authoritative_status_models import capture_status_models
from project_selection import bind_selection
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier as admission
from VALIDATE_ATOMS.validate_atoms_workers import proposed_references as references
from golden_authority import write_frozen_authority


PRMEDO = ("Plan", "Requirement", "Method", "Evaluation", "Delivery", "Operations")
BODY = "# Summary\n\nCheck action\n\n## Scope\n\nSelected action.\n\n## Claim\n\nVerify action.\n\n## Details\n\nExact check.\n"
PATH = Path("06_evaluation/CA-E-701--check.md")
BROKEN = b"---\natom_id: [unterminated\n---\n# Legacy\n"


class ExplicitReferenceScopeIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ProposedCarrierAdmissionRegressions()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.selection = self.fixture.project()
        self.control = self.selection.control_relative
        base = self.root / self.control / (
            "101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/"
            "frozen-authority/CA-R-1947.md"
        )
        base.write_bytes((Path(__file__).parent / "fixtures/current_graph_authority/CA-R-1947.md").read_bytes())
        write_frozen_authority(
            self.root, self.control,
            tuple(dict.fromkeys((*admission._FRONTIER_IDS, *admission._GRAPH_IDS, "CA-D-378"))),
            graph_only_identifiers=frozenset(admission._GRAPH_IDS),
        )
        self.target = self.fixture.put(self.control / "09_operations/action.md", (
            b"---\natom_id: CA-O-702\ncontent_role: Operations\ntype: Action\n"
            b"current_scope_unit: amber\nstatus: Active\nversion: 1\n---\n# Summary\n\nAction\n"
        ))
        self.metadata = self.fixture.metadata(
            atom_id="CA-E-701", content_role="Evaluation", type="QA Case",
            relations={"evaluation_for": ["CA-O-702"]},
        )
        with bind_selection(self.selection):
            self.context = admission.source_context_from_project(self.root)
            self.status_index = capture_status_models(self.root, self.context._reader)

    def validate(self, *, scope=PRMEDO, metadata=None, allow=False):
        return admission.validate_proposed_carrier(
            self.metadata if metadata is None else metadata, BODY, self.context, PATH,
            reference_roles=scope, allow_existing_relations=allow,
            _status_index=self.status_index,
        )

    def test_scoped_success_does_not_read_malformed_excluded_roles_or_write(self):
        for folder in ("01_concern", "02_analysis"):
            self.fixture.put(self.control / folder / "legacy.md", BROKEN)
        before = fixtures.snapshot(self.root)
        result = self.validate()
        self.assertEqual((result["findings"], result["gaps"]), ([], []))
        self.assertEqual(result["reference_scope"], {
            "extent": "finite-proposed-carrier", "project": "amber", "roles": list(PRMEDO),
            "role_folders": dict(zip(PRMEDO, ("03_plan", "04_requirement", "05_method", "06_evaluation", "07_delivery", "09_operations"))),
            "authority_paths": [self.control.as_posix(),
                                (self.control / "101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES").as_posix()],
            "direct_targets": ["CA-O-702"], "plan_parent_closure": [],
        })
        self.assertEqual(fixtures.snapshot(self.root), before)

    def test_default_still_refuses_malformed_legacy_in_admitted_role(self):
        self.fixture.put(self.control / "01_concern/legacy.md", BROKEN)
        with self.assertRaises(admission.ProposedCarrierError):
            self.validate(scope=None)

    def test_malformed_included_role_still_refuses(self):
        self.fixture.put(self.control / "05_method/broken.md", BROKEN)
        with self.assertRaises(admission.ProposedCarrierError):
            self.validate()

    def test_scope_cannot_skip_existing_relation_resolution(self):
        self.target.unlink()
        for allow in (False, True):
            with self.subTest(allow_existing_relations=allow):
                with self.assertRaises(admission.ProposedCarrierError):
                    self.validate(allow=allow)

    def test_excluded_target_cannot_leak_from_graph_authority_sources(self):
        # CA-R-1018 is genuinely present among the verified graph-rule sources.
        self.assertIn("CA-R-1018", admission._GRAPH_IDS)
        metadata = dict(self.metadata, relations={"evaluation_for": ["CA-R-1018"]})
        for allow in (False, True):
            with self.subTest(allow_existing_relations=allow):
                with self.assertRaises(admission.ProposedCarrierError):
                    self.validate(scope=("Evaluation", "Operations"), metadata=metadata, allow=allow)

    def test_explicit_concern_reference_is_not_dropped_by_prmedo_scope(self):
        self.fixture.put(self.control / "01_concern/concern.md", (
            b"---\natom_id: CA-C-702\ncontent_role: Concern\ntype: Problem\n"
            b"current_scope_unit: amber\nstatus: active\nversion: 1\n---\n# Summary\n\nConcern\n"
        ))
        metadata = dict(self.metadata, relations={
            "evaluation_for": ["CA-O-702"], "depends_on": ["CA-C-702"],
        })
        result = self.validate(scope=("Concern", *PRMEDO), metadata=metadata)
        self.assertEqual((result["findings"], result["gaps"]), ([], []))
        for allow in (False, True):
            with self.subTest(allow_existing_relations=allow):
                with self.assertRaises(admission.ProposedCarrierError):
                    self.validate(metadata=metadata, allow=allow)

    def test_allowed_role_cannot_disguise_an_excluded_bound_authority_target(self):
        self.target.write_bytes(self.target.read_bytes().replace(b"CA-O-702", b"CA-R-1018"))
        metadata = dict(self.metadata, relations={"evaluation_for": ["CA-R-1018"]})
        with self.assertRaisesRegex(admission.ProposedCarrierError, "authority target is outside"):
            self.validate(scope=("Evaluation", "Operations"), metadata=metadata, allow=True)

    def test_scoped_plan_receipt_identifies_exact_authenticated_parent_closure(self):
        parent = self.control / "03_plan/parent.md"
        self.fixture.put(parent, (
            b"---\natom_id: CA-P-702\ncontent_role: Plan\ntype: Plan\n"
            b"current_scope_unit: amber\nstatus: Active\nversion: 1\n---\n# Summary\n\nParent\n"
        ))
        metadata = self.fixture.metadata(relations={"is_decomposition_of": ["CA-P-702"]})
        result = admission.validate_proposed_carrier(
            metadata, fixtures.PLAN_BODY, self.context, Path("03_plan/parent/child.md"),
            reference_roles=("Plan",), allow_existing_relations=True,
            _status_index=self.status_index,
        )
        self.assertEqual(result["reference_scope"]["direct_targets"], ["CA-P-702"])
        self.assertEqual(result["reference_scope"]["plan_parent_closure"], ["CA-P-702"])
        self.assertEqual(result["reference_scope"]["roles"], ["Plan"])

    def test_default_success_has_no_scoped_receipt_and_scope_order_is_canonical(self):
        self.assertNotIn("reference_scope", self.validate(scope=None))
        result = self.validate(scope=tuple(reversed(PRMEDO)), allow=True)
        self.assertEqual(result["reference_scope"]["roles"], list(PRMEDO))

    def test_invalid_scope_and_excluded_candidate_refuse(self):
        for scope in ((), ("Evaluation", "Evaluation"), ("evaluation",),
                      ("Evaluation", "Unknown"), ("Operations",), ["Evaluation"], "Evaluation"):
            with self.subTest(scope=scope), self.assertRaises(admission.ProposedCarrierError):
                self.validate(scope=scope)
        with self.assertRaises(admission.ProposedCarrierError):
            self.validate(metadata=dict(self.metadata, type="Action"))

    def test_stale_role_authority_cannot_be_hidden_by_explicit_scope(self):
        entry = admission._entry("CA-D-324")
        path = self.root / self.control.joinpath(*Path(entry["source_path"]).parts[1:])
        path.write_bytes(path.read_bytes() + b"\nChanged after context capture.\n")
        with self.assertRaises(admission.ProposedCarrierError):
            self.validate()

    def test_admitted_frontier_change_during_inventory_refuses(self):
        original = references._frontier
        calls = 0

        def changing_frontier(*args, **kwargs):
            nonlocal calls
            result = original(*args, **kwargs)
            calls += 1
            if calls == 1:
                self.fixture.put(self.control / "03_plan/new.md", BROKEN)
            return result

        with patch.object(references, "_frontier", changing_frontier):
            with self.assertRaises(admission.ProposedCarrierError):
                self.validate()
        self.assertGreaterEqual(calls, 1)


if __name__ == "__main__":
    unittest.main()
