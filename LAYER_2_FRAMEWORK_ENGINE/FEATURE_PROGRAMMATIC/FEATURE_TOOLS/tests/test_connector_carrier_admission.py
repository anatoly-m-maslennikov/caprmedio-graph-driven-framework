"""Real admission mechanics, negative error propagation only; no carrier effect."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import test_connector_bindings as real_fixtures
from connector_bindings import ConnectorBindingError
from connector_carrier_adapter import modify


class CarrierAdmissionErrorTests(unittest.TestCase):
    def setUp(self):
        self.fixture = real_fixtures.ConnectorBindingTests(
            "test_receiving_mapping_binds_nested_request_and_uses_real_source_bytes"
        )
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.request = {**self.fixture.request, "operation": "modify",
                        "delta": {"logical_change": "fixture"},
                        "expected_state": {"fixture": "before"}}

    def refused(self, bindings, code, field, *, request=None):
        resolver = Mock(side_effect=AssertionError("Admission refusal must not resolve a carrier plan."))
        result = modify(request or self.request, bindings=bindings, resolve_plan=resolver)
        resolver.assert_not_called()
        self.assertEqual(result["effects"], [])
        self.assertIsNone(result["data"])
        self.assertIsNone(result["current_state"])
        self.assertEqual(len(result["errors"]), 1)
        self.assertEqual(result["errors"][0]["code"], code)
        self.assertEqual(result["errors"][0]["field"], field)
        self.assertFalse((self.fixture.root / "journal").exists())
        return result

    def test_real_selected_preview_refusal_preserves_authorization_field(self):
        self.refused(self.fixture.bindings(request=self.request, mode="preview"),
                     "permission_denied", "authorization")

    def test_real_selected_permission_reference_mismatch_preserves_authorization_field(self):
        request = {**self.request, "authorization": "not-the-bound-permission"}
        self.refused(self.fixture.bindings(request=request), "permission_denied", "authorization",
                     request=request)

    def test_stale_authority_preserves_expected_state_field_before_plan_resolution(self):
        bindings = self.fixture.bindings(request=self.request)
        path = self.fixture.root / "schema.md"
        path.write_bytes(path.read_bytes() + b" changed after binding")
        self.refused(bindings, "stale_state", "expected_state")

    def test_structured_schema_refusal_preserves_explicit_none_field(self):
        def refuse_schema(request):
            raise ConnectorBindingError("schema_invalid", "Fixture complete schema refusal", None)
        self.refused(self.fixture.bindings(request=self.request, validator=refuse_schema),
                     "schema_invalid", None)

    def test_nonstructured_refusal_keeps_context_and_safe_generic_message(self):
        def refuse_schema(request):
            raise ValueError("sensitive fixture diagnostic")
        result = self.refused(self.fixture.bindings(request=self.request, validator=refuse_schema),
                              "backend_failure", "context")
        self.assertNotIn("sensitive", result["errors"][0]["message"])


if __name__ == "__main__":
    unittest.main()
