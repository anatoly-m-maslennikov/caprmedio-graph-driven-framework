"""Independent actual-admission fixture checks; not live Workflow admission."""

from __future__ import annotations

import builtins
import hashlib
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import test_connector_toml_shared as fixtures
from connector_bindings import ConnectorBindingError
from connector_toml_write import replace_source


class IndependentMaterializationIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.SharedConnectorTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.before = (b'# independent carrier\r\nschema_version = 0x1\r\n'
            b'name = "before" # selected\r\nmembers = ["a", "b"]\r\n'
            b'\r\n[extra]\r\nkeep = true # untouched\r\n')
        self.after = (b'# independent carrier\r\nschema_version = 0x1\r\n'
            b'name = "after" # selected\r\nmembers = ["a", "b"]\r\n'
            b'\r\n[extra]\r\nkeep = true # untouched\r\n')
        self.fixture.source.write_bytes(self.before)

    def run_modify(self, **arguments):
        request = self.fixture.request("modify")
        return self.fixture.run_request(request, **arguments)

    def assert_known_effect(self, result, expected):
        self.assertEqual(len(result["effects"]), 1)
        effect = result["effects"][0]
        self.assertEqual(effect["state"], "known")
        self.assertEqual(effect["evidence"]["before_sha256"], hashlib.sha256(self.before).hexdigest())
        self.assertEqual(effect["evidence"]["after_sha256"], hashlib.sha256(expected).hexdigest())
        self.assertEqual(effect["evidence"]["proposed_sha256"], hashlib.sha256(expected).hexdigest())
        self.assertEqual(self.fixture.source.read_bytes(), expected)

    def test_real_modify_writes_only_literal_proposed_bytes_and_returns_them(self):
        result = self.run_modify()
        self.assertEqual(result["errors"], [])
        self.assert_known_effect(result, self.after)
        self.assertEqual(result["data"]["source_text"].encode(), self.after)
        self.assertEqual(result["data"]["document"], {"schema_version": 1, "name": "after",
            "members": ["a", "b"], "extra": {"keep": True}})
        self.assertEqual(result["data"]["effective_diff"], [{"field": "name", "action": "replace",
            "mode": "value", "before_present": True, "after_present": True,
            "before": "before", "after": "after"}])

    def test_noop_never_loads_dependency_or_calls_writer(self):
        request = self.fixture.request("modify", value="before")
        bindings = self.fixture.bindings(request)
        real_import = builtins.__import__
        def no_library(name, *args, **kwargs):
            if name == "tomlkit" or name.startswith("tomlkit."):
                raise AssertionError("No-op loaded changed-materialization dependency")
            return real_import(name, *args, **kwargs)
        with patch("builtins.__import__", side_effect=no_library), patch("connector_toml_write.replace_source") as writer:
            result = self.fixture.run_request(request, bindings)
        writer.assert_not_called()
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["effects"], [])
        self.assertEqual(result["data"]["effective_diff"], [])
        self.assertEqual(result["data"]["source_text"].encode(), self.before)
        self.assertEqual(self.fixture.source.read_bytes(), self.before)

    def test_schema_stale_and_permission_refusals_never_write(self):
        for case in ("schema", "stale", "permission"):
            with self.subTest(case=case):
                self.fixture.source.write_bytes(self.before)
                request = self.fixture.request("modify", value=3 if case == "schema" else "after")
                if case == "stale":
                    request["expected_state"]["sha256"] = "0" * 64
                bindings = self.fixture.bindings(request, mode="preview" if case == "permission" else "execute")
                with patch("connector_toml_write.replace_source") as writer:
                    result = self.fixture.run_request(request, bindings)
                writer.assert_not_called()
                expected_code = {"schema": "schema_invalid", "stale": "stale_state", "permission": "permission_denied"}[case]
                self.assertEqual(result["errors"][0]["code"], expected_code)
                self.assertEqual(result["effects"], [])
                self.assertEqual(self.fixture.source.read_bytes(), self.before)

    def test_lossy_materialization_refuses_before_writer(self):
        import tomlkit
        request = self.fixture.request("modify")
        bindings = self.fixture.bindings(request)
        with patch.object(tomlkit, "dumps", return_value="normalized = true\n"), patch("connector_toml_write.replace_source") as writer:
            result = self.fixture.run_request(request, bindings)
        writer.assert_not_called()
        self.assertEqual(result["errors"][0]["code"], "schema_invalid")
        self.assertEqual(result["effects"], [])
        self.assertEqual(self.fixture.source.read_bytes(), self.before)

    def test_write_error_after_effect_retains_error_and_exact_known_evidence(self):
        def write_then_error(path, payload):
            replace_source(path, payload)
            raise OSError("reported after replacement")
        with patch("connector_toml_write.replace_source", side_effect=write_then_error):
            result = self.run_modify()
        self.assertEqual(result["errors"][0]["code"], "backend_failure")
        self.assert_known_effect(result, self.after)
        self.assertEqual(result["data"]["source_text"].encode(), self.after)

    def test_failed_write_with_original_bytes_returns_no_effect(self):
        with patch("connector_toml_write.replace_source", side_effect=OSError("before replacement")):
            result = self.run_modify()
        self.assertEqual(result["errors"][0]["code"], "backend_failure")
        self.assertEqual(result["effects"], [])
        self.assertEqual(self.fixture.source.read_bytes(), self.before)

    def test_different_readback_preserves_unknown_effect_instead_of_success(self):
        observed = self.after.replace(b'"after"', b'"other"')
        def substitute(path, payload):
            replace_source(path, observed)
        with patch("connector_toml_write.replace_source", side_effect=substitute):
            result = self.run_modify()
        self.assertEqual(result["errors"][0]["code"], "effect_uncertain")
        self.assertIsNone(result["current_state"])
        self.assertEqual(result["effects"][0]["state"], "unknown")
        self.assertEqual(result["effects"][0]["evidence"]["after_sha256"], hashlib.sha256(observed).hexdigest())
        self.assertEqual(result["effects"][0]["evidence"]["proposed_sha256"], hashlib.sha256(self.after).hexdigest())
        self.assertEqual(self.fixture.source.read_bytes(), observed)

    def test_unavailable_postwrite_observation_does_not_erase_effect(self):
        error = ConnectorBindingError("backend_failure", "independent readback unavailable", None)
        with patch("connector_toml_write.capture_source", side_effect=error):
            result = self.run_modify()
        self.assertEqual(result["errors"][0]["code"], "effect_uncertain")
        self.assertEqual(result["effects"][0]["state"], "unknown")
        self.assertEqual(result["effects"][0]["evidence"]["observation_error"], error.record())
        self.assertEqual(self.fixture.source.read_bytes(), self.after)

    def test_native_typed_read_boundary_remains_refused_without_public_codec(self):
        source = self.before + b'date = 2026-10-13\r\n'
        self.fixture.source.write_bytes(source)
        request = self.fixture.request("modify")
        with patch("connector_toml_write.replace_source") as writer:
            result = self.fixture.run_request(request, validate_document=lambda _: None)
        writer.assert_not_called()
        self.assertEqual(result["errors"][0]["code"], "schema_invalid")
        self.assertEqual(result["effects"], [])
        self.assertEqual(self.fixture.source.read_bytes(), source)

    def test_schema_authority_change_after_preparation_refuses_before_writer(self):
        request = self.fixture.request("modify")
        bindings = self.fixture.bindings(request)
        def change_authority(document):
            self.fixture.validate(document)
            if document["name"] == "after":
                (self.fixture.root / "schema.json").write_text('{"changed":true}')
        with patch("connector_toml_write.replace_source") as writer:
            result = self.fixture.run_request(request, bindings, validate_document=change_authority)
        writer.assert_not_called()
        self.assertEqual(result["errors"][0]["code"], "stale_state")
        self.assertEqual(result["effects"], [])
        self.assertEqual(self.fixture.source.read_bytes(), self.before)

    def test_readback_schema_error_preserves_known_written_effect(self):
        observations = []
        def refuse_readback(document):
            self.fixture.validate(document)
            observations.append(document["name"])
            if len(observations) == 3:
                raise ValueError("Readback no longer satisfies receiving schema")
        result = self.run_modify(validate_document=refuse_readback)
        self.assertEqual(observations, ["before", "after", "after"])
        self.assertEqual(result["errors"][0]["code"], "schema_invalid")
        self.assertIsNone(result["data"])
        self.assert_known_effect(result, self.after)


if __name__ == "__main__":
    unittest.main()
