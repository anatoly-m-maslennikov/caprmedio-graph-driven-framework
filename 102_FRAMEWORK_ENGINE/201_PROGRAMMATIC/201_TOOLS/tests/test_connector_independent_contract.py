"""Independent bounded regressions for D625/D527, R864 and R1938.

Producer fixtures construct inputs only; expected refusals, source bytes and
effect-free state follow the governing contracts, not producer test results.
"""

from __future__ import annotations

import copy
import dataclasses
import hashlib
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import test_connector_atom_read as atom_inputs
import test_connector_bindings as binding_inputs
import test_connector_scope_parsing as scope_inputs
from connector_atom_read import AtomReadError, read_atom
from connector_bindings import ConnectorBindingError, ConnectorBindings, SelectedOperationAdmission, capture_source
from connector_scope_parsing import validate_scope_request
from connector_scope_reading import execute_scope_request
from workflow_run_support import RunTracker, SelectedRunError


class IndependentConnectorContractTests(unittest.TestCase):
    def fixture(self, fixture_type):
        value = fixture_type()
        value.setUp()
        self.addCleanup(value.doCleanups)
        return value

    def assert_refusal(self, exception_type, code, action):
        with self.assertRaises(exception_type) as caught:
            action()
        self.assertEqual(caught.exception.code, code)

    @staticmethod
    def snapshot(root):
        return {path.relative_to(root).as_posix(): path.read_bytes()
                for path in root.rglob("*") if path.is_file()}

    def scope_fixture(self, validator=validate_scope_request):
        fixture = self.fixture(binding_inputs.ConnectorBindingTests)
        control = fixture.root / ".caprmedio_demo"
        control.mkdir()
        settings = control / "caprmedio_project_settings.toml"
        structure = control / "project_structure.toml"
        settings.write_text(scope_inputs.SETTINGS, encoding="utf-8")
        structure.write_text(scope_inputs.serialize_project_structure(scope_inputs.rows()), encoding="utf-8")
        request = {**copy.deepcopy(fixture.request), "target": {"kind": "Scope Unit", "identity": "ALPHA"}}
        admission = SelectedOperationAdmission(fixture.tracker, fixture.outer(request),
                                                map_request=fixture.map_request)
        sources = tuple(capture_source(fixture.root, path.relative_to(fixture.root))
                        for path in (settings, structure))
        bindings = ConnectorBindings(admission, supported_operations={"read"}, supported_kinds={"Scope Unit"},
            validate_payload=validator, resolve_sources=lambda _: sources, authority_sources=fixture.authorities)
        return fixture, request, bindings, settings, structure

    def test_inner_and_context_seals_preserve_json_types(self):
        fixture = self.fixture(binding_inputs.ConnectorBindingTests)
        for original, substituted in ((1, True), (True, 1), (1, 1.0), (1.0, 1)):
            with self.subTest(original=original, substituted=substituted):
                admitted = {**fixture.request, "expected_state": {"revision": original}}
                changed = {**fixture.request, "expected_state": {"revision": substituted}}
                self.assert_refusal(ConnectorBindingError, "permission_denied",
                                    lambda: fixture.bindings(request=admitted).bind(changed))
                request = {**fixture.request, "context": {"revision": substituted}}
                outer = fixture.outer(request, context_reference={"revision": original})
                admission = SelectedOperationAdmission(fixture.tracker, outer, map_request=lambda value: (
                    value["parameters"]["connector_request"], value["parameters"]["context_reference"]))
                self.assert_refusal(ConnectorBindingError, "input_invalid", lambda: admission.check(request))

    def test_reused_request_id_cannot_reseal_different_canonical_bytes(self):
        fixture = self.fixture(binding_inputs.ConnectorBindingTests)
        outer = fixture.outer()
        outer["initiative"]["instruction_summary"] = "another canonical instruction under the same ID"
        preview_only = {key: value for key, value in outer.items() if key not in {
            "proposal_receipt", "proposal_receipt_digest", "assigned_action_id", "operator_authorization", "requested_runs"}}
        preview_only["mode"] = "preview"
        other_tracker = RunTracker(fixture.root, source_observer=fixture.observe, executor=fixture.never_execute)
        preview = other_tracker.run_selected_operation(preview_only)
        outer["proposal_receipt"] = preview["proposal_receipt"]
        outer["proposal_receipt_digest"] = preview["proposal_receipt_digest"]
        outer["operator_authorization"]["proposal_receipt_digest"] = preview["proposal_receipt_digest"]
        before = self.snapshot(fixture.root)
        self.assert_refusal(SelectedRunError, "request-id-conflict", lambda: fixture.tracker.run_selected_operation(outer))
        admission = SelectedOperationAdmission(fixture.tracker, outer, map_request=fixture.map_request)
        self.assert_refusal(ConnectorBindingError, "permission_denied", lambda: admission.check(fixture.request))
        self.assertEqual(self.snapshot(fixture.root), before)

    def test_callbacks_cannot_replace_the_already_admitted_request_snapshot(self):
        for callback in ("validator", "resolver"):
            with self.subTest(callback=callback):
                fixture = self.fixture(binding_inputs.ConnectorBindingTests)
                def mutate_alias(_request):
                    fixture.request["target"]["identity"] = "CA-R-999"
                    if callback == "resolver":
                        return (capture_source(fixture.root, "source.txt"),)
                bound = fixture.bindings(**{callback: mutate_alias}).bind(fixture.request)
                self.assertEqual(bound.request["target"], {"kind": "Atom", "identity": "CA-R-863"})
                self.assertEqual(fixture.request["target"]["identity"], "CA-R-999")
                bound.revalidate_before_effect()

    def test_history_token_alone_selects_exact_revision_and_missing_token_refuses(self):
        fixture = self.fixture(atom_inputs.AtomConnectorTests)
        first = fixture.write("CA-R-1", "Earlier", [], placement="archive", status="Archived", version=1)
        fixture.write("CA-R-1", "Later", [], placement="archive", status="Archived", version=2)
        history = dataclasses.replace(fixture.view, source_view="history", lifecycles=("archived",))
        raw = first.read_bytes()
        token = hashlib.sha256(raw).hexdigest()
        before = self.snapshot(fixture.root)
        result = read_atom("CA-R-1", history, {"source_token": token})
        self.assertEqual(result["data"]["source"], raw.decode("utf-8"))
        self.assertEqual(result["current_state"]["version"], 1)
        self.assertEqual(result["current_state"]["source_token"], token)
        self.assertEqual(result["effects"], [])
        self.assert_refusal(AtomReadError, "target_ambiguous", lambda: read_atom("CA-R-1", history))
        self.assert_refusal(AtomReadError, "stale_state", lambda: read_atom("CA-R-1", history, {"source_token": "0" * 64}))
        self.assertEqual(self.snapshot(fixture.root), before)

    def test_historical_pin_cannot_change_the_receiving_current_view(self):
        fixture = self.fixture(atom_inputs.AtomConnectorTests)
        previous = fixture.write("CA-R-1", "Previous", [], placement="archive", status="Archived", version=3)
        pin = {"source_token": hashlib.sha256(previous.read_bytes()).hexdigest()}
        self.assert_refusal(AtomReadError, "stale_state", lambda: read_atom("CA-R-1", fixture.view, pin))

    def test_scope_read_observes_complete_declaration_and_exact_state_without_effects(self):
        fixture, request, bindings, settings, structure = self.scope_fixture()
        before = self.snapshot(fixture.root)
        result = execute_scope_request(request, bindings=bindings, project_name="demo", source_view="current")
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["effects"], [])
        self.assertEqual(result["data"], {"identity": "ALPHA", "declaration": {
            "scope_unit_name": "ALPHA", "parent": "PROJECT", "scope_unit_type": "Unordered",
            "scope_unit_label": "FEATURE", "structural_level": 1, "navigational_order_number": 1,
            "authority_path": "unmaterialized/ALPHA/", "delivery_path": "implementation/ALPHA", "authority_mode": "casual"}})
        self.assertEqual(result["current_state"], {"project": "demo", "source_view": "current", "source_evidence": {
            "project_settings": {"sha256": hashlib.sha256(settings.read_bytes()).hexdigest()},
            "project_structure": {"sha256": hashlib.sha256(structure.read_bytes()).hexdigest()}}})
        self.assertEqual(self.snapshot(fixture.root), before)

    def test_scope_read_refuses_source_drift_before_completion_without_connector_writes(self):
        calls = []
        def validator(request):
            validate_scope_request(request)
            calls.append(None)
            if len(calls) == 2:
                structure.write_bytes(original + b"\n# independent external drift\n")
        fixture, request, bindings, _, structure = self.scope_fixture(validator)
        original = structure.read_bytes()
        before = self.snapshot(fixture.root)
        result = execute_scope_request(request, bindings=bindings, project_name="demo", source_view="current")
        self.assertEqual(result["errors"][0]["code"], "stale_state")
        self.assertIsNone(result["data"])
        self.assertEqual(result["effects"], [])
        before[structure.relative_to(fixture.root).as_posix()] = original + b"\n# independent external drift\n"
        self.assertEqual(self.snapshot(fixture.root), before)


if __name__ == "__main__":
    unittest.main()
