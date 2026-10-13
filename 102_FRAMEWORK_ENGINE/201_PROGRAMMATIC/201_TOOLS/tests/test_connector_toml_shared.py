"""Actual selected-admission and file effects on isolated configuration fixtures."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from connector_bindings import ConnectorBindings, SelectedOperationAdmission, capture_source
from connector_toml_shared import execute
from connector_toml_write import replace_source
import test_selected_run_support as fixture_support
from work_journal import canonical_json_digest
from workflow_run_support import RunTracker


class SharedConnectorTests(unittest.TestCase):
    def setUp(self):
        temporary_root = Path(__file__).resolve().parents[4] / ".caprmedio_tmp"
        self.directory = tempfile.TemporaryDirectory(prefix="toml-admission-", dir=temporary_root)
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / ".git").mkdir()
        self.source = self.root / "source.toml"
        self.payload = b'# exact comment\nschema_version = 1\nname = "before"\nmembers = ["a", "b"]\n[extra]\nkeep = true\n'
        self.source.write_bytes(self.payload)
        (self.root / "schema.json").write_text(json.dumps({"schema_version": 1, "name_type": "string"}))
        self.keys = {"name": ("name",), "members": ("members",)}

    def request(self, operation="read", identity="Project Structure", value="after"):
        state = {"identity": identity, "project": "fixture", "source_view": "current",
                 "sha256": hashlib.sha256(self.source.read_bytes()).hexdigest()}
        return {"operation": operation, "target": {"kind": "Configuration", "identity": identity},
                "query": None, "delta": None if operation == "read" else {"edits": [
                    {"action": "replace", "mode": "value", "field": "name", "value": value}]},
                "expected_state": None if operation == "read" else state,
                "authorization": "authorizations/fixture.json", "context": "contexts/fixture.json"}

    @staticmethod
    def validate(document):
        if (type(document.get("schema_version")) is not int or document.get("schema_version") != 1 or type(document.get("name")) is not str
                or type(document.get("members")) is not list or document.get("extra") != {"keep": True}):
            raise ValueError("Complete fixture schema fails")

    def bindings(self, request, *, mode="execute", sources=None):
        schema = capture_source(self.root, "schema.json")
        source = capture_source(self.root, "source.toml")
        outer = fixture_support.SelectedRunSupportTest()._request()
        parameters = {"logical_request": copy.deepcopy(request), "context_reference": request["context"]}
        outer.update({"operation_route": "configuration.fixture", "parameters": parameters,
                      "parameters_digest": canonical_json_digest(parameters), "target_frontier": ["source.toml"],
                      "target_frontier_digest": canonical_json_digest(["source.toml"]),
                      "effects": [] if request["operation"] == "read" else [{"type": "modify", "target": "source.toml"}],
                      "definition_manifest": {"manifest_ref": "schema.json", "manifest_digest": schema.sha256},
                      "source_freshness": {"selected_source_registry_ref": "schema.json", "selected_source_registry_version": 1,
                                           "selected_source_registry_digest": schema.sha256,
                                           "selected_binding_ref": "source.toml", "selected_binding_digest": source.sha256}})
        outer["effects_digest"] = canonical_json_digest(outer["effects"])
        def observer(admitted):
            schema.revalidate()
            source.revalidate()
            return {"selected": admitted["operation_route"] == "configuration.fixture", "current": True,
                    "observed": {**admitted["source_freshness"], "definition_manifest": admitted["definition_manifest"]}}
        tracker = RunTracker(self.root, source_observer=observer, executor=lambda *_: self.fail("No outer execution in binding checks"))
        preview = tracker.run_selected_operation(outer)
        authorization = {"authorization_ref": request["authorization"], "authorization_freshness": {"state": "current", "digest": schema.sha256},
                         **{key: outer[key] for key in ("request_id", "operation_route", "parameters_digest", "target_frontier_digest",
                                                       "effects_digest", "definition_manifest", "source_freshness")},
                         "proposal_receipt_digest": preview["proposal_receipt_digest"]}
        outer.update({"mode": mode, "proposal_receipt": preview["proposal_receipt"],
                      "proposal_receipt_digest": preview["proposal_receipt_digest"], "assigned_action_id": "fixture-action",
                      "operator_authorization": authorization})
        if mode == "preview":
            for key in ("proposal_receipt", "proposal_receipt_digest", "assigned_action_id", "operator_authorization"):
                outer.pop(key)
        admission = SelectedOperationAdmission(tracker, outer, map_request=lambda admitted: (
            admitted["parameters"]["logical_request"], admitted["parameters"]["context_reference"]))
        bindings = ConnectorBindings(admission, supported_operations={"read", "modify"}, supported_kinds={"Configuration"},
                                     validate_payload=lambda _: None, resolve_sources=lambda _: sources or [source], authority_sources=[schema])
        return bindings

    def run_request(self, request, bindings=None, **changes):
        arguments = {"bindings": bindings or self.bindings(request), "project": "fixture", "source_view": "current",
                     "validate_document": self.validate, "keys": self.keys}
        arguments.update(changes)
        return execute(request, **arguments)

    def test_independent_read_and_modify_both_configuration_identities(self):
        for identity in ("Project Structure", "Project Settings"):
            self.source.write_bytes(self.payload)
            read = self.run_request(self.request(identity=identity))
            self.assertEqual(read["errors"], [])
            self.assertEqual(read["effects"], [])
            self.assertEqual(read["data"]["source_text"].encode(), self.payload)
            request = self.request("modify", identity)
            result = self.run_request(request)
            self.assertEqual(result["errors"], [])
            self.assertEqual(result["data"]["document"]["name"], "after")
            self.assertEqual(result["data"]["document"]["extra"], {"keep": True})
            self.assertEqual(result["current_state"]["sha256"], hashlib.sha256(self.source.read_bytes()).hexdigest())
            self.assertEqual(result["effects"][0]["state"], "known")

    def test_noop_retains_exact_bytes_and_skips_writer(self):
        with mock.patch("connector_toml_write.replace_source") as writer:
            result = self.run_request(self.request("modify", value="before"))
        writer.assert_not_called()
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["effects"], [])
        self.assertEqual(result["data"]["effective_diff"], [])
        self.assertEqual(self.source.read_bytes(), self.payload)

    def test_read_seal_is_not_modify_permission_and_preview_cannot_write(self):
        read = self.request()
        bindings = self.bindings(read)
        denied = self.run_request(self.request("modify"), bindings)
        self.assertEqual(denied["errors"][0]["code"], "permission_denied")
        request = self.request("modify")
        preview = self.run_request(request, self.bindings(request, mode="preview"))
        self.assertEqual(preview["errors"][0]["code"], "permission_denied")
        self.assertEqual(self.source.read_bytes(), self.payload)

    def test_stale_read_evidence_and_schema_refusal_prevent_write(self):
        request = self.request("modify")
        self.source.write_bytes(self.payload.replace(b'before', b'changed'))
        current = self.source.read_bytes()
        result = self.run_request(request)
        self.assertEqual(result["errors"][0]["code"], "stale_state")
        request = self.request("modify", value=3)
        result = self.run_request(request)
        self.assertEqual(result["errors"][0]["code"], "schema_invalid")
        self.assertEqual(self.source.read_bytes(), current)

    def test_backend_failure_before_and_after_effect_and_unknown_effect(self):
        request = self.request("modify")
        with mock.patch("connector_toml_write.replace_source", side_effect=OSError("before effect")):
            result = self.run_request(request)
        self.assertEqual(result["errors"][0]["code"], "backend_failure")
        self.assertEqual(result["effects"], [])
        self.assertEqual(self.source.read_bytes(), self.payload)
        def write_then_fail(path, payload):
            replace_source(path, payload)
            raise OSError("after effect")
        with mock.patch("connector_toml_write.replace_source", side_effect=write_then_fail):
            result = self.run_request(request)
        self.assertEqual(result["errors"][0]["code"], "backend_failure")
        self.assertEqual(result["effects"][0]["state"], "known")
        self.assertEqual(result["data"]["document"]["name"], "after")
        self.source.write_bytes(self.payload)
        def unexpected(path, payload):
            replace_source(path, payload.replace(b'after', b'other'))
        with mock.patch("connector_toml_write.replace_source", side_effect=unexpected):
            result = self.run_request(request)
        self.assertEqual(result["errors"][0]["code"], "effect_uncertain")
        self.assertEqual(result["effects"][0]["state"], "unknown")

    def test_closed_request_identity_and_protected_fields(self):
        for request, code in (({**self.request(), "path": "source.toml"}, "input_invalid"),
                              (self.request(identity="source.toml"), "input_invalid")):
            result = self.run_request(request)
            self.assertEqual(result["errors"][0]["code"], code)
        request = self.request("modify")
        request["delta"]["edits"][0]["field"] = "generated"
        self.assertEqual(self.run_request(request)["errors"][0]["code"], "schema_invalid")
        self.assertEqual(self.source.read_bytes(), self.payload)

    def test_source_and_schema_changes_during_validation_refuse_read(self):
        for change in ("source", "schema"):
            self.source.write_bytes(self.payload)
            schema = self.root / "schema.json"
            schema.write_text(json.dumps({"schema_version": 1, "name_type": "string"}))
            request = self.request()
            bindings = self.bindings(request)
            def validate_then_change(document):
                self.validate(document)
                if change == "source":
                    self.source.write_bytes(self.payload.replace(b'before', b'changed'))
                else:
                    schema.write_text('{"changed":true}')
            result = self.run_request(request, bindings, validate_document=validate_then_change)
            self.assertIsNone(result["data"])
            self.assertEqual(result["errors"][0]["code"], "stale_state")

    def test_invalid_native_json_representation_refuses_full_read(self):
        self.source.write_bytes(self.payload + b'typed_date = 2026-10-13\n')
        result = self.run_request(self.request(), validate_document=lambda _: None)
        self.assertIsNone(result["data"])
        self.assertEqual(result["errors"][0]["code"], "schema_invalid")

    def test_actual_writer_allocates_scratch_only_in_project_temporary_state(self):
        with mock.patch("connector_toml_write.os.replace", wraps=os.replace) as replace:
            result = self.run_request(self.request("modify"))
        self.assertEqual(result["errors"], [])
        staged, target = replace.call_args.args
        self.assertTrue(Path(staged).is_relative_to(self.root / ".caprmedio_tmp"))
        self.assertEqual(Path(target), self.source)
        self.assertEqual(list((self.root / ".caprmedio_tmp" / "connector-toml" / "atomic").iterdir()), [])


if __name__ == "__main__":
    unittest.main()
