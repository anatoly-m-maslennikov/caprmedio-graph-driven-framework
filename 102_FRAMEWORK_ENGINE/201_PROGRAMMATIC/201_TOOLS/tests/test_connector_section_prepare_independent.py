"""Literal section preparation controls with real selected admission and schema."""

from __future__ import annotations

import copy
import hashlib
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "VALIDATE_ATOMS/tests"))

import test_connector_bindings as binding_fixtures
import test_proposed_carrier_admission_regressions as project_fixtures
import connector_section_prepare as prepare_module
from connector_bindings import ConnectorBindingError, ConnectorBindings, SelectedOperationAdmission, capture_source
from connector_section_parse import SectionError
from project_selection import bind_selection
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier
from VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier import _entry, source_context_from_project, validate_proposed_carrier
from workflow_run_support import _canonical_digest


NOTES = b"### Notes\n\nKeep notes.\n\n#### Nested\n\nKeep nested bytes.\n\n"
LINKS = b"### References\n\nKeep reference.\n"
BODY = b"# Summary\n\nIndependent Plan\n\n## Objective\n\nCheck admission.\n\n## Details\n\n### Definition of Done\n\nExact controls pass.\n\n" + NOTES + LINKS
IDENTITY = {"level": 3, "title": "Notes"}
REFERENCES = {"level": 3, "title": "References"}


class IndependentSectionPreparationTests(unittest.TestCase):
    def setUp(self):
        self.binding_fixture = binding_fixtures.ConnectorBindingTests()
        self.binding_fixture.setUp()
        self.addCleanup(self.binding_fixture.doCleanups)
        self.root = self.binding_fixture.root
        self.selection = project_fixtures.ProposedCarrierAdmissionRegressions.project(self)
        for identifier in ("CA-R-1933", "CA-M-373", "CA-D-623"):
            entry = _entry(identifier)
            raw = (project_fixtures.REPOSITORY / entry["source_path"]).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), entry["sha256"])
            destination = self.selection.control_root.joinpath(*Path(entry["source_path"]).parts[1:])
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(raw)
        self.path = self.selection.control_root / "03_plan/CA-P-701--independent-plan.md"
        self.identity = "CA-P-701"
        self.path.parent.mkdir()
        self.raw = (
            b'---\natom_id: CA-P-701\ncontent_role: Plan\ntype: Plan\nlabel: Task\n'
            b'current_scope_unit: amber\nclaim_target_scope_unit: amber\nlocal_tier: Standard\nglobal_tier: 2\n'
            b'status: Active\nauthor: Fixture Operator\nversion: 1\nupdated_at: "2026-10-13 15:00:00 +0400"\n'
            b'subjects: {governs: Tool, depends_on: [Plan]}\nrelations: {}\n---\n'
        ) + BODY
        self.path.write_bytes(self.raw)
        with bind_selection(self.selection):
            self.context = source_context_from_project(self.root)

    def bound(self, delta, **overrides):
        request = copy.deepcopy(self.binding_fixture.request)
        request.update(operation="modify", target={"kind": "Atom", "identity": self.identity},
                       delta=delta, expected_state={"version": 1})
        request.update(overrides)
        outer = self.binding_fixture.outer(request)
        original = copy.deepcopy(outer)
        for field in ("proposal_receipt", "proposal_receipt_digest", "operator_authorization", "assigned_action_id"):
            outer.pop(field)
        outer.update(mode="preview", request_id=outer["request_id"] + "-section-independent",
                     target_frontier=[self.path.relative_to(self.root).as_posix()])
        outer["target_frontier_digest"] = _canonical_digest(outer["target_frontier"])
        preview = self.binding_fixture.tracker.run_selected_operation(outer)
        outer.update(mode="execute", assigned_action_id=original["assigned_action_id"],
                     proposal_receipt=preview["proposal_receipt"], proposal_receipt_digest=preview["proposal_receipt_digest"])
        outer["operator_authorization"] = {
            "authorization_ref": "permission.md",
            "authorization_freshness": {"state": "current", "digest": self.binding_fixture.digest("permission.md")},
            **{key: copy.deepcopy(outer[key]) for key in (
                "request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness")},
        }
        admission = SelectedOperationAdmission(self.binding_fixture.tracker, outer, map_request=self.binding_fixture.map_request)
        binding = ConnectorBindings(
            admission, supported_operations=("modify",), supported_kinds=("Atom",),
            validate_payload=lambda _request: None,
            resolve_sources=lambda _request: (capture_source(self.root, self.path.relative_to(self.root)),),
            authority_sources=self.binding_fixture.authorities,
        )
        return binding.bind(request)

    def prepare(self, delta, **overrides):
        return prepare_module.prepare_section(self.bound(delta, **overrides), self.context)

    def snapshot(self):
        return project_fixtures.snapshot(self.root)

    def test_each_operation_preserves_literal_unrelated_bytes_without_write(self):
        cases = (
            ({"operation": "add", "section": {"level": 3, "title": "Extra"}, "content": "\nNew value.\n\n", "position": {"before": REFERENCES}}, self.raw.replace(LINKS, b"### Extra\n\nNew value.\n\n" + LINKS)),
            ({"operation": "replace", "section": IDENTITY, "content": "\nReplacement.\n\n"}, self.raw.replace(NOTES, b"### Notes\n\nReplacement.\n\n")),
            ({"operation": "remove", "section": IDENTITY}, self.raw.replace(NOTES, b"")),
            ({"operation": "title", "section": IDENTITY, "title": "Evidence"}, self.raw.replace(b"### Notes\n", b"### Evidence\n")),
            ({"operation": "position", "section": IDENTITY, "position": {"after": REFERENCES}}, self.raw.replace(NOTES + LINKS, LINKS + NOTES)),
        )
        for delta, expected in cases:
            with self.subTest(operation=delta["operation"]):
                bound = self.bound(delta)
                before = self.snapshot()
                self.assertEqual(prepare_module.prepare_section(bound, self.context), expected)
                self.assertEqual(self.snapshot(), before)

    def test_verified_noops_keep_revision_time_history_and_all_bytes(self):
        for delta in (
            {"operation": "replace", "section": IDENTITY, "content": NOTES.split(b"\n", 1)[1].decode()},
            {"operation": "title", "section": IDENTITY, "title": "Notes"},
            {"operation": "position", "section": IDENTITY, "position": {"before": REFERENCES}},
        ):
            with self.subTest(operation=delta["operation"]):
                bound = self.bound(delta)
                before = self.snapshot()
                self.assertEqual(prepare_module.prepare_section(bound, self.context), self.raw)
                self.assertEqual(self.snapshot(), before)

    def test_complete_schema_summary_and_type_restrictions_refuse_without_write(self):
        for delta in (
            {"operation": "remove", "section": {"level": 2, "title": "Objective"}},
            {"operation": "replace", "section": {"level": 1, "title": "Summary"}, "content": "\nDifferent identity.\n\n"},
            {"operation": "replace", "section": IDENTITY, "content": "\nNew.\n\n", "type": "Other"},
        ):
            with self.subTest(delta=delta):
                bound = self.bound(delta)
                before = self.snapshot()
                with self.assertRaises((SectionError, ConnectorBindingError)):
                    prepare_module.prepare_section(bound, self.context)
                self.assertEqual(self.snapshot(), before)

    def test_invalid_complete_source_cannot_be_accepted_as_noop(self):
        self.path.write_bytes(self.raw.replace(b"## Objective\n\nCheck admission.\n\n", b""))
        bound = self.bound({"operation": "title", "section": IDENTITY, "title": "Notes"})
        before = self.snapshot()
        with self.assertRaises((SectionError, ConnectorBindingError)):
            prepare_module.prepare_section(bound, self.context)
        self.assertEqual(self.snapshot(), before)

    def test_ordinary_requirement_method_delivery_need_no_placeholder_type(self):
        header = self.raw[:self.raw.index(b"# Summary")]
        body = b"# Summary\n\nOrdinary carrier\n\n## Scope\n\nOne tool.\n\n## Claim\n\nPreserve its contract.\n\n## Details\n\n" + NOTES + LINKS
        for role, code, folder, status_source in (
            ("Requirement", "R", "04_requirement", "CA-R-1309"),
            ("Method", "M", "05_method", "CA-R-1397"),
            ("Delivery", "D", "07_delivery", "CA-R-1399"),
        ):
            with self.subTest(role=role):
                entry = _entry(status_source)
                raw = (project_fixtures.REPOSITORY / entry["source_path"]).read_bytes()
                self.assertEqual(hashlib.sha256(raw).hexdigest(), entry["sha256"])
                destination = self.selection.control_root.joinpath(*Path(entry["source_path"]).parts[1:])
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(raw)
                self.identity = f"CA-{code}-701"
                self.path = self.selection.control_root / folder / f"{self.identity}--ordinary.md"
                self.path.parent.mkdir(exist_ok=True)
                self.raw = header.replace(b"CA-P-701", self.identity.encode()).replace(
                    b"content_role: Plan", f"content_role: {role}".encode()).replace(b"type: Plan\n", b"") + body
                self.path.write_bytes(self.raw)
                parsed = parse_carrier(self.raw, self.path)
                result = validate_proposed_carrier(parsed.metadata, parsed.body, self.context,
                                                   self.path.relative_to(self.selection.control_root))
                self.assertFalse(result["findings"] + result["gaps"])
                bound = self.bound({"operation": "title", "section": IDENTITY, "title": "Evidence"})
                before = self.snapshot()
                self.assertEqual(prepare_module.prepare_section(bound, self.context),
                                 self.raw.replace(b"### Notes\n", b"### Evidence\n"))
                self.assertEqual(self.snapshot(), before)

    def test_actual_identity_and_expected_state_are_checked(self):
        delta = {"operation": "title", "section": IDENTITY, "title": "Notes"}
        for overrides in (
            {"target": {"kind": "Atom", "identity": "CA-P-999"}},
            {"expected_state": {"version": 2}},
        ):
            with self.subTest(overrides=overrides):
                with self.assertRaises((SectionError, ConnectorBindingError)):
                    self.prepare(delta, **overrides)

    def test_atom_id_kind_must_match_its_actual_content_role(self):
        self.identity = "CA-R-701"
        self.path = self.selection.control_root / "03_plan/CA-R-701--wrong-role.md"
        self.path.write_bytes(self.raw.replace(b"CA-P-701", b"CA-R-701"))
        bound = self.bound({"operation": "title", "section": IDENTITY, "title": "Evidence"})
        before = self.snapshot()

        with self.assertRaises(SectionError):
            prepare_module.prepare_section(bound, self.context)

        self.assertEqual(self.snapshot(), before)

    def test_source_permission_and_context_drift_refuse(self):
        delta = {"operation": "title", "section": IDENTITY, "title": "Notes"}
        for path in (self.path, self.root / "permission.md", self.selection.structure_path):
            with self.subTest(path=path.name):
                bound = self.bound(delta)
                original = path.read_bytes()
                path.write_bytes(original + b"\n# external drift\n")
                try:
                    with self.assertRaises((SectionError, ConnectorBindingError)):
                        prepare_module.prepare_section(bound, self.context)
                finally:
                    path.write_bytes(original)

    def test_missing_or_changed_type_authority_refuses_even_noop(self):
        entry = _entry("CA-R-1700")
        path = self.selection.control_root.joinpath(*Path(entry["source_path"]).parts[1:])
        original = path.read_bytes()
        for missing in (False, True):
            with self.subTest(missing=missing):
                bound = self.bound({"operation": "title", "section": IDENTITY, "title": "Notes"})
                if missing:
                    path.unlink()
                else:
                    path.write_bytes(original + b"\n# changed authority\n")
                try:
                    with self.assertRaises(SectionError):
                        prepare_module.prepare_section(bound, self.context)
                finally:
                    path.write_bytes(original)

    def test_source_changed_during_real_validation_is_rechecked(self):
        bound = self.bound({"operation": "title", "section": IDENTITY, "title": "Evidence"})
        original = prepare_module.validate_proposed_carrier
        changed = False

        def validate_and_drift(*args, **kwargs):
            nonlocal changed
            result = original(*args, **kwargs)
            if not changed:
                changed = True
                self.path.write_bytes(self.raw + b"External change.\n")
            return result

        with patch.object(prepare_module, "validate_proposed_carrier", validate_and_drift):
            with self.assertRaises((SectionError, ConnectorBindingError)):
                prepare_module.prepare_section(bound, self.context)
        self.assertTrue(changed)
        self.assertEqual(self.path.read_bytes(), self.raw + b"External change.\n")


if __name__ == "__main__":
    unittest.main()
