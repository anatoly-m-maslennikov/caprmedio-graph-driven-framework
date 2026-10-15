"""Author controls for explicit private reference-role scope, not rule skips."""

import hashlib
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1])]

import test_proposed_carrier_admission_regressions as fixtures
from project_selection import bind_selection
from VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier import (
    ProposedCarrierError, _entry, _FRONTIER_IDS, _GRAPH_IDS,
    source_context_from_project, validate_proposed_carrier,
)


PRMEDO = ("Plan", "Requirement", "Method", "Evaluation", "Delivery", "Operations")
TARGET = (
    b"---\natom_id: CA-O-901\ncontent_role: Operations\ntype: Action\n"
    b"current_scope_unit: amber\nstatus: Active\nversion: 1\n---\n# Summary\n\nTarget.\n"
)
BODY = "# Summary\n\nEvaluate action.\n\n## Scope\n\nSelected action.\n\n## Claim\n\nVerify the action.\n\n## Details\n\nIndependent check.\n"


class ProposedReferenceScopeTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ProposedCarrierAdmissionRegressions(
            "test_unrelated_partial_and_identityless_legacy_do_not_block_exact_target"
        )
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.selection = self.fixture.project()
        self.root = self.selection.root
        self.control = self.selection.control_relative
        for identifier in dict.fromkeys((*_FRONTIER_IDS, *_GRAPH_IDS)):
            entry = _entry(identifier, graph=identifier in _GRAPH_IDS)
            raw = (fixtures.REPOSITORY / entry["source_path"]).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), entry["sha256"])
            self.fixture.put(self.control.joinpath(*Path(entry["source_path"]).parts[1:]), raw)
        self.target = self.fixture.put(self.control / "09_operations/action.md", TARGET)
        with bind_selection(self.selection):
            self.context = source_context_from_project(self.root)
        self.metadata = self.fixture.metadata(
            atom_id="CA-E-701", content_role="Evaluation", type="QA Case",
            relations={"evaluation_for": ["CA-O-901"]},
        )

    def validate(self, *, metadata=None, **options):
        return validate_proposed_carrier(
            self.metadata if metadata is None else metadata, BODY,
            self.context, Path("06_evaluation/CA-E-701--independent-evaluation.md"), **options,
        )

    def test_scoped_receipt_is_explicit_and_default_stays_unscoped(self):
        default = self.validate()
        self.assertNotIn("reference_scope", default)
        scoped = self.validate(reference_roles=tuple(reversed(PRMEDO)))
        self.assertEqual(scoped["reference_scope"], {
            "extent": "finite-proposed-carrier", "project": "amber", "roles": list(PRMEDO),
            "role_folders": dict(zip(PRMEDO, (
                "03_plan", "04_requirement", "05_method", "06_evaluation", "07_delivery", "09_operations",
            ))),
            "authority_paths": sorted([
                self.control.as_posix(),
                (self.control / "101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES").as_posix(),
            ]),
            "direct_targets": ["CA-O-901"], "plan_parent_closure": [],
        })
        self.assertFalse(scoped["findings"] or scoped["gaps"])

    def test_deferred_malformed_carriers_are_outside_only_the_explicit_scope(self):
        for folder in ("01_concern", "02_analysis"):
            self.fixture.put(self.control / folder / "legacy.md", b"---\natom_id: [unterminated\n---\n")
        before = fixtures.snapshot(self.root)
        with self.assertRaises(ProposedCarrierError):
            self.validate()
        # Default existing-relation preservation remains unchanged.
        self.assertNotIn("reference_scope", self.validate(allow_existing_relations=True))
        scoped = self.validate(reference_roles=PRMEDO, allow_existing_relations=True)
        self.assertEqual(scoped["reference_scope"]["direct_targets"], ["CA-O-901"])
        self.assertEqual(fixtures.snapshot(self.root), before)

    def test_scope_requires_canonical_unique_roles_and_includes_candidate(self):
        for roles in ((), ("Plan", "Plan"), ("plan",), ("Unknown",), (True,), ["Plan"], "Plan", ("Operations",)):
            with self.subTest(roles=roles), self.assertRaises(ProposedCarrierError):
                self.validate(reference_roles=roles)

    def test_offscope_target_and_authority_cannot_be_grandfathered(self):
        self.fixture.put(
            self.control / "01_concern/concern.md",
            TARGET.replace(b"CA-O-901", b"CA-C-901").replace(b"Operations", b"Concern").replace(b"Action", b"Problem").replace(b"Active", b"active"),
        )
        for target, roles in (("CA-C-901", PRMEDO), ("CA-R-1018", ("Evaluation", "Operations"))):
            metadata = dict(self.metadata, relations={"depends_on": [target]})
            with self.subTest(target=target), self.assertRaises(ProposedCarrierError):
                self.validate(metadata=metadata, reference_roles=roles, allow_existing_relations=True)

    def test_duplicate_or_malformed_inside_selected_scope_still_refuses(self):
        for raw in (TARGET, b"---\natom_id: [unterminated\n---\n"):
            with self.subTest(raw=raw):
                extra = self.fixture.put(self.control / "09_operations/extra.md", raw)
                try:
                    with self.assertRaises(ProposedCarrierError):
                        self.validate(reference_roles=PRMEDO)
                finally:
                    extra.unlink()

    def test_scoped_admission_preserves_authority_and_type_checks(self):
        metadata = dict(self.metadata, type="Task")
        with self.assertRaises(ProposedCarrierError):
            self.validate(metadata=metadata, reference_roles=PRMEDO)
        for identifier, graph in (("CA-D-324", False), ("CA-R-1018", True)):
            entry = _entry(identifier, graph=graph)
            path = self.selection.control_root.joinpath(*Path(entry["source_path"]).parts[1:])
            original = path.read_bytes()
            path.write_bytes(original + b"\n# stale source\n")
            try:
                with self.subTest(identifier=identifier), self.assertRaises(ProposedCarrierError):
                    self.validate(reference_roles=PRMEDO)
            finally:
                path.write_bytes(original)


if __name__ == "__main__":
    unittest.main()
