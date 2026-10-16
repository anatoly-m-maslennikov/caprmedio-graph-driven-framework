"""Complete source-bound preparation, with real selected-operation admission."""

from __future__ import annotations

import copy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

import yaml

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "VALIDATE_ATOMS/tests"))
import test_connector_bindings as bindings_fixture
import test_proposed_carrier_admission_regressions as carrier_fixture
from golden_authority import frozen_entry, write_frozen_authority
from connector_bindings import ConnectorBindings, SelectedOperationAdmission, capture_source
from connector_section_parse import SectionError
from connector_section_prepare import SECTION_AUTHORITY_IDS, prepare_section
from project_selection import bind_selection
from VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier import source_context_from_project  # noqa: E402
from workflow_run_support import _canonical_digest


class SectionPreparationTests(unittest.TestCase):
    def setUp(self):
        # Reuse exact canonical-source fixture setup, not its validator or any
        # permission mock. The production validator and RunTracker both run.
        self.io = bindings_fixture.ConnectorBindingTests()
        self.io.setUp()
        self.addCleanup(self.io.doCleanups)
        self.carriers = carrier_fixture.ProposedCarrierAdmissionRegressions()
        self.carriers.setUp()
        self.addCleanup(self.carriers.doCleanups)
        self.root = self.io.root
        self.selection = self.carriers.project(root=self.root)
        write_frozen_authority(self.root, self.selection.control_relative, SECTION_AUTHORITY_IDS)
        self.path = self.selection.control_root / "03_plan/CA-P-701--independent-plan.md"
        self.path.parent.mkdir(parents=True)
        self.raw = ("---\n" + yaml.safe_dump(self.carriers.metadata(), sort_keys=False) + "---\n"
                    + carrier_fixture.PLAN_BODY + "\n## Notes\n\nKeep this.\n\n## Evidence\n\nKeep that.\n").encode()
        self.path.write_bytes(self.raw)
        with bind_selection(self.selection):
            self.context = source_context_from_project(self.root)

    def bound(self, delta=None, **changes):
        request = {**self.io.request, "operation": "modify",
                   "target": {"kind": "Atom", "identity": "CA-P-701"},
                   "expected_state": {"version": 1},
                   "delta": delta or {"operation": "replace", "section": {"level": 2, "title": "Notes"},
                                      "content": "\nRevised.\n\n"}, **changes}
        # Seal the actual complete source path in the admitted frontier.
        original_outer = self.io.outer(request)
        outer = {key: copy.deepcopy(value) for key, value in original_outer.items()
                 if key not in {"proposal_receipt", "proposal_receipt_digest", "operator_authorization", "assigned_action_id"}}
        outer["mode"] = "preview"
        outer["request_id"] += "-section"
        outer["target_frontier"] = [self.path.relative_to(self.root).as_posix()]
        outer["target_frontier_digest"] = _canonical_digest(outer["target_frontier"])
        receipt = self.io.tracker.run_selected_operation(outer)
        outer.update(mode="execute", assigned_action_id=original_outer["assigned_action_id"], proposal_receipt=receipt["proposal_receipt"],
                     proposal_receipt_digest=receipt["proposal_receipt_digest"])
        outer["operator_authorization"] = {
            "authorization_ref": "permission.md",
            "authorization_freshness": {"state": "current", "digest": self.io.digest("permission.md")},
            **{key: copy.deepcopy(outer[key]) for key in (
                "request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness")},
        }
        admission = SelectedOperationAdmission(self.io.tracker, outer, map_request=self.io.map_request)
        bindings = ConnectorBindings(
            admission, supported_operations=("modify",), supported_kinds=("Atom",),
            validate_payload=lambda _: None,
            resolve_sources=lambda _: (capture_source(self.root, self.path.relative_to(self.root)),),
            authority_sources=self.io.authorities,
        )
        return bindings.bind(request)

    def test_all_five_edits_validate_complete_candidate_without_effect(self):
        notes, evidence = {"level": 2, "title": "Notes"}, {"level": 2, "title": "Evidence"}
        deltas = [
            {"operation": "replace", "section": notes, "content": "\nRevised.\n\n"},
            {"operation": "add", "section": {"level": 2, "title": "Extra"}, "content": "\nExtra.\n\n",
             "position": {"before": evidence}},
            {"operation": "remove", "section": notes},
            {"operation": "title", "section": notes, "title": "Other notes"},
            {"operation": "position", "section": evidence, "position": {"before": notes}},
        ]
        for delta in deltas:
            with self.subTest(operation=delta["operation"]):
                before = carrier_fixture.snapshot(self.root)
                candidate = prepare_section(self.bound(delta), self.context)
                self.assertNotEqual(candidate, self.raw)
                self.assertEqual(candidate.split(b"---\n", 2)[1], self.raw.split(b"---\n", 2)[1])
                self.assertIn(b"# Summary\n\nIndependent Plan\n\n", candidate)
                self.assertEqual(carrier_fixture.snapshot(self.root), before)

    def test_noop_preserves_every_byte(self):
        delta = {"operation": "replace", "section": {"level": 2, "title": "Notes"}, "content": "\nKeep this.\n\n"}
        self.assertEqual(prepare_section(self.bound(delta), self.context), self.raw)

    def test_complete_validator_rejects_required_section_removal(self):
        delta = {"operation": "remove", "section": {"level": 2, "title": "Objective"}}
        with self.assertRaisesRegex(SectionError, "Complete Atom validation"):
            prepare_section(self.bound(delta), self.context)
        self.assertEqual(self.path.read_bytes(), self.raw)

    def test_protected_summary_and_invalid_source_refuse(self):
        delta = {"operation": "replace", "section": {"level": 1, "title": "Summary"}, "content": "\nDifferent.\n\n"}
        with self.assertRaises(SectionError):
            prepare_section(self.bound(delta), self.context)
        self.raw = self.raw.replace(b"version: 1", b"version: 0")
        self.path.write_bytes(self.raw)
        with self.assertRaises(SectionError):
            prepare_section(self.bound(), self.context)

    def test_wrong_identity_and_expected_version_refuse(self):
        for changes, code in (({"target": {"kind": "Atom", "identity": "CA-P-702"}}, "target_not_found"),
                              ({"expected_state": {"version": 2}}, "stale_state")):
            with self.subTest(changes=changes), self.assertRaises(SectionError) as caught:
                prepare_section(self.bound(**changes), self.context)
            self.assertEqual(caught.exception.code, code)

    def test_existing_plan_with_action_type_must_refuse(self):
        self.raw = self.raw.replace(b"type: Plan", b"type: Action")
        self.path.write_bytes(self.raw)
        with self.assertRaises(SectionError):
            prepare_section(self.bound(), self.context)

    def test_missing_section_authority_refuses(self):
        entry = frozen_entry(SECTION_AUTHORITY_IDS[0])
        self.selection.control_root.joinpath(*Path(entry["source_path"]).parts[1:]).unlink()
        with self.assertRaisesRegex(SectionError, "source authority"):
            prepare_section(self.bound(), self.context)

    def test_ordinary_rmd_without_type_allow_edit_and_exact_noop(self):
        for role, letter, folder, status_id in (
            ("Requirement", "R", "04_requirement", "CA-R-1309"),
            ("Method", "M", "05_method", "CA-R-1397"),
            ("Delivery", "D", "07_delivery", "CA-R-1399"),
        ):
            with self.subTest(role=role):
                write_frozen_authority(self.root, self.selection.control_relative, (status_id,))
                identity = f"CA-{letter}-701"
                metadata = self.carriers.metadata(atom_id=identity, content_role=role)
                metadata.pop("type")
                metadata.pop("label")
                self.path = self.selection.control_root / folder / f"{identity}--ordinary.md"
                self.path.parent.mkdir(parents=True, exist_ok=True)
                self.raw = ("---\n" + yaml.safe_dump(metadata, sort_keys=False) + "---\n"
                            "# Summary\n\nOrdinary source\n\n## Scope\n\nSelected Project\n\n"
                            "## Claim\n\nPreserve the source.\n\n## Details\n\nKeep this.\n").encode()
                self.path.write_bytes(self.raw)
                target = {"kind": "Atom", "identity": identity}
                delta = {"operation": "replace", "section": {"level": 2, "title": "Details"},
                         "content": "\nRevised.\n"}
                candidate = prepare_section(self.bound(delta, target=target), self.context)
                self.assertEqual(candidate, self.raw.replace(b"Keep this.", b"Revised."))
                delta["content"] = "\nKeep this.\n"
                self.assertEqual(prepare_section(self.bound(delta, target=target), self.context), self.raw)
                self.assertEqual(self.path.read_bytes(), self.raw)

    def test_header_byte_changes_refuse_even_when_parsed_properties_are_equal(self):
        # The carrier parser normalizes line endings, but a section edit must
        # retain raw frontmatter too, not just equivalent parsed Properties.
        frontmatter, body = self.raw.rsplit(b"---\n", 1)
        changed = frontmatter.replace(b"\n", b"\r\n") + b"---\r\n" + body
        with patch("connector_section_prepare.edit_section", return_value=changed):
            with self.assertRaisesRegex(SectionError, "cannot change Atom Properties"):
                prepare_section(self.bound(), self.context)


if __name__ == "__main__":
    unittest.main()
