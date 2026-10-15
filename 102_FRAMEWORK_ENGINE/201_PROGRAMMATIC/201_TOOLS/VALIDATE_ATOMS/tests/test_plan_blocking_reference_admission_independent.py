"""Real finite-carrier Plan blocking admission, not readiness or publication."""

from copy import deepcopy
from pathlib import Path
import unittest

import test_proposed_reference_scope_independent as scoped


class PlanBlockingReferenceAdmissionIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = scoped.ExplicitReferenceScopeIndependentTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.metadata = self.fixture.fixture.metadata(relations={"blocks": ["CA-P-710"]})

    def target(self, status="Backlog", *, identifier="CA-P-710", version=1, filename="target.md", relations="{}"):
        folder = {"Active": "", "Backlog": "001_backlog", "Done": "done", "Canceled": "canceled", "Archived": "archived"}[status]
        return self.fixture.fixture.put(self.fixture.control / "03_plan" / folder / filename, (
            f"---\natom_id: {identifier}\ncontent_role: Plan\ntype: Plan\n"
            f"current_scope_unit: amber\nstatus: {status}\nversion: {version}\nrelations: {relations}\n"
            "---\n# Summary\n\nBlocking endpoint\n"
        ).encode())

    def validate(self, metadata=None, scope=scoped.PRMEDO):
        return scoped.admission.validate_proposed_carrier(
            self.metadata if metadata is None else metadata, scoped.fixtures.PLAN_BODY,
            self.fixture.context, Path("03_plan/proposed.md"), reference_roles=scope,
        )

    def test_backlog_plan_target_passes_complete_source_bound_admission(self):
        self.target()
        original = deepcopy(self.metadata)
        before = scoped.fixtures.snapshot(self.fixture.root)
        for scope in (None, scoped.PRMEDO):
            with self.subTest(scope=scope):
                result = self.validate(scope=scope)
                self.assertEqual((result["findings"], result["gaps"]), ([], []))
                self.assertEqual(self.metadata, original)
        self.assertEqual(scoped.fixtures.snapshot(self.fixture.root), before)

    def test_blocks_cannot_target_operations_or_mix_plan_and_operation_endpoints(self):
        self.target("Active")
        for targets in (["CA-O-702"], ["CA-P-710", "CA-O-702"]):
            with self.subTest(targets=targets):
                with self.assertRaises(scoped.admission.ProposedCarrierError):
                    self.validate(dict(self.metadata, relations={"blocks": targets}))

    def test_blocking_wrong_role_without_status_authority_refuses_cleanly(self):
        self.fixture.fixture.put(self.fixture.control / "08_implementation/implementation.md", (
            b"---\natom_id: CA-I-720\ncontent_role: Implementation\n"
            b"current_scope_unit: amber\nstatus: Active\nversion: 1\n---\n# Summary\n\nImplementation\n"
        ))
        with self.assertRaises(scoped.admission.ProposedCarrierError):
            self.validate(dict(self.metadata, relations={"blocks": ["CA-I-720"]}), scope=None)

    def test_independent_scope_root_does_not_inherit_unrelated_role_bundle_semantics(self):
        selected = self.fixture.selection
        selected.structure_path.write_text(selected.structure_path.read_text() + (
            '\n[[scope_units]]\nscope_unit_name = "NESTED"\nparent = "PROJECT"\n'
            'scope_unit_type = "Unordered"\nscope_unit_label = "FEATURE"\n'
            'structural_level = 1\nnavigational_order_number = 1\n'
            f'authority_path = "{self.fixture.control}/08_implementation/bundle"\n'
            'delivery_path = "native/nested"\n'
        ))
        self.fixture.fixture.put(self.fixture.control / "08_implementation/bundle.md", (
            b"---\natom_id: CA-I-721\ncontent_role: Implementation\n"
            b"current_scope_unit: amber\nstatus: Active\nversion: 1\n---\n# Summary\n\nUnrelated\n"
        ))
        self.fixture.fixture.put(self.fixture.control / "08_implementation/bundle/03_plan/001_backlog/target.md", (
            b"---\natom_id: CA-P-710\ncontent_role: Plan\ntype: Plan\n"
            b"current_scope_unit: NESTED\nstatus: Backlog\nversion: 1\n---\n# Summary\n\nTarget\n"
        ))
        selection = scoped.fixtures.resolve_project(self.fixture.root, self.fixture.control)
        with scoped.bind_selection(selection):
            self.fixture.context = scoped.admission.source_context_from_project(self.fixture.root)
        result = self.validate(scope=None)
        self.assertEqual((result["findings"], result["gaps"]), ([], []))

    def test_ordinary_inactive_operation_reference_stays_refused(self):
        self.fixture.target.unlink()
        self.fixture.fixture.put(self.fixture.control / "09_operations/draft/action.md", (
            b"---\natom_id: CA-O-702\ncontent_role: Operations\ntype: Action\n"
            b"current_scope_unit: amber\nstatus: Draft\nversion: 1\n---\n# Summary\n\nAction\n"
        ))
        with self.assertRaises(scoped.admission.ProposedCarrierError):
            self.fixture.validate()

    def test_normal_requirement_method_evaluation_delivery_status_guards_remain(self):
        for kind, role, folder in (("R", "Requirement", "04_requirement"), ("M", "Method", "05_method"),
                                   ("E", "Evaluation", "06_evaluation"), ("D", "Delivery", "07_delivery")):
            with self.subTest(role=role):
                identifier = f"CA-{kind}-720"
                metadata = dict(self.fixture.metadata, relations={"evaluation_for": ["CA-O-702"], "depends_on": [identifier]})
                raw = (f"---\natom_id: {identifier}\ncontent_role: {role}\n"
                       + ("type: QA Case\n" if role == "Evaluation" else "")
                       + "current_scope_unit: amber\nstatus: Active\nversion: 1\n---\n# Summary\n\nTarget\n").encode()
                path = self.fixture.fixture.put(self.fixture.control / folder / "ordinary.md", raw)
                result = self.fixture.validate(metadata=metadata)
                self.assertEqual((result["findings"], result["gaps"]), ([], []))
                path.unlink()
                draft = self.fixture.fixture.put(self.fixture.control / folder / "draft/ordinary.md",
                                                raw.replace(b"status: Active", b"status: Draft"))
                with self.assertRaises(scoped.admission.ProposedCarrierError):
                    self.fixture.validate(metadata=metadata)
                draft.unlink()

    def test_all_five_admitted_plan_statuses_pass_without_rewriting_target(self):
        for status in ("Active", "Backlog", "Done", "Canceled", "Archived"):
            with self.subTest(status=status):
                path = self.target(status, filename="target@1.md" if status == "Archived" else "target.md")
                before = scoped.fixtures.snapshot(self.fixture.root)
                result = self.validate()
                self.assertEqual((result["findings"], result["gaps"]), ([], []))
                self.assertEqual(result["reference_scope"]["direct_targets"], ["CA-P-710"])
                self.assertEqual(scoped.fixtures.snapshot(self.fixture.root), before)
                path.unlink()

    def test_blocking_relaxation_does_not_extend_to_other_relation_kinds(self):
        path = self.target("Backlog")
        for relations in ({"depends_on": ["CA-P-710"]},
                          {"blocks": ["CA-P-710"], "depends_on": ["CA-P-710"]},
                          {"blocks": ["CA-P-710"], "is_decomposition_of": ["CA-P-710"]}):
            with self.subTest(relations=relations):
                with self.assertRaises(scoped.admission.ProposedCarrierError):
                    self.validate(dict(self.metadata, relations=relations))
        self.assertTrue(path.is_file())

    def test_current_plan_coexists_with_exact_older_active_header_history(self):
        current = self.target("Backlog", version=2)
        old = self.target("Active", version=1, filename="old.md")
        historical = old.parent / "archived/target@1.md"
        historical.parent.mkdir(exist_ok=True)
        old.rename(historical)
        before = scoped.fixtures.snapshot(self.fixture.root)
        result = self.validate()
        self.assertEqual((result["findings"], result["gaps"]), ([], []))
        self.assertEqual(scoped.fixtures.snapshot(self.fixture.root), before)
        current.unlink()
        with self.assertRaises(scoped.admission.ProposedCarrierError):
            self.validate()

    def test_ambiguous_or_conflicting_plan_revision_evidence_refuses(self):
        current = self.target("Backlog", version=2)
        for status, version, filename in (("Backlog", 2, "duplicate.md"),
                                          ("Done", 3, "other-current.md"),
                                          ("Archived", 3, "later@3.md"),
                                          ("Archived", 1, "bad-suffix@2.md")):
            with self.subTest(status=status, version=version, filename=filename):
                competing = self.target(status, version=version, filename=filename)
                with self.assertRaises(scoped.admission.ProposedCarrierError):
                    self.validate()
                competing.unlink()
        self.assertTrue(current.is_file())

    def test_pending_target_cannot_hide_wrong_type_owner_or_status_placement(self):
        path = self.target()
        raw = path.read_bytes()
        for before, after in ((b"type: Plan", b"type: Action"),
                              (b"current_scope_unit: amber", b"current_scope_unit: OTHER"),
                              (b"status: Backlog", b"status: Planned"),
                              (b"status: Backlog", b"status: Done")):
            with self.subTest(after=after):
                path.write_bytes(raw.replace(before, after))
                with self.assertRaises(scoped.admission.ProposedCarrierError):
                    self.validate()
        path.write_bytes(raw)

    def test_malformed_pending_target_status_is_a_controlled_refusal(self):
        path = self.target()
        path.write_bytes(path.read_bytes().replace(b"status: Backlog", b"status: [Backlog]"))
        with self.assertRaises(scoped.admission.ProposedCarrierError):
            self.validate()

    def test_unrelated_partial_non_scalar_identity_does_not_break_exact_target_lookup(self):
        self.target()
        self.fixture.fixture.put(self.fixture.control / "03_plan/unrelated.md", (
            b"---\natom_id: [unrelated]\nversion: 1\n---\n# Summary\n\nUnrelated\n"
        ))
        result = self.validate()
        self.assertEqual((result["findings"], result["gaps"]), ([], []))

    def test_old_parent_bundle_cannot_supply_a_current_blocking_endpoint(self):
        self.target("Active", identifier="CA-P-730", version=2, filename="parent.md")
        self.target("Archived", identifier="CA-P-730", version=1, filename="parent@1.md")
        self.target("Active", version=1, filename="archived/parent@1/child.md",
                    relations='{"is_decomposition_of": ["CA-P-730"]}')
        current = self.target("Backlog", version=2)
        result = self.validate()
        self.assertEqual((result["findings"], result["gaps"]), ([], []))
        current.unlink()
        with self.assertRaises(scoped.admission.ProposedCarrierError):
            self.validate()

    def test_blocking_duplicates_cycles_and_unknown_targets_refuse(self):
        target = self.target("Active")
        for targets in (["CA-P-710", "CA-P-710"], ["CA-P-999999"], [self.metadata["atom_id"]]):
            with self.subTest(targets=targets):
                with self.assertRaises(scoped.admission.ProposedCarrierError):
                    self.validate(dict(self.metadata, relations={"blocks": targets}))
        target.write_bytes(target.read_bytes().replace(b"relations: {}", (
            'relations: {"blocks": ["' + self.metadata["atom_id"] + '"]}'
        ).encode()))
        with self.assertRaises(scoped.admission.ProposedCarrierError):
            self.validate()

    def test_stale_blocking_storage_and_status_authority_refuse(self):
        self.target("Backlog")
        for identifier in ("CA-R-1580", "CA-D-471", "CA-R-1539"):
            with self.subTest(identifier=identifier):
                entry = scoped.admission._entry(identifier, graph=identifier in scoped.admission._GRAPH_IDS)
                path = self.fixture.root / self.fixture.control.joinpath(*Path(entry["source_path"]).parts[1:])
                raw = path.read_bytes()
                path.write_bytes(raw + b"\n# changed authority\n")
                with self.assertRaises(scoped.admission.ProposedCarrierError):
                    self.validate()
                path.write_bytes(raw)


if __name__ == "__main__":
    unittest.main()
