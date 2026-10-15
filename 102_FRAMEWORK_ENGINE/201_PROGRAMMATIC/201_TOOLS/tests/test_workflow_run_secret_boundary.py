"""Exact connector/query state fields are not general token exemptions."""

import copy
from collections.abc import Mapping
import sys
from typing import Any
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from workflow_run_support import (  # noqa: E402
    SelectedRunError,
    _canonical_digest,
    _reject_parameter_secrets,
    _reject_secrets,
    _validate_common,
)


def _continuation() -> dict[str, Any]:
    return {
        "query_request": {
            "snapshot": {
                "reference": "snapshot:opaque-handle",
                "token": "opaque-handle",
                "digest": "a" * 64,
            },
            "cursor": "opaque-cursor",
        }
    }


def _request(
    parameters: Mapping[str, Any], route: str = "find_and_fetch_artifacts"
) -> dict[str, Any]:
    frontier = ["fixture/source.md"]
    effects: list[dict[str, Any]] = []
    return {
        "request_id": "query-continuation",
        "operation_route": route,
        "parameters": parameters,
        "parameters_digest": _canonical_digest(parameters),
        "target_frontier": frontier,
        "target_frontier_digest": _canonical_digest(frontier),
        "effects": effects,
        "effects_digest": _canonical_digest(effects),
        "definition_manifest": {
            "manifest_ref": "fixture/manifest.json",
            "manifest_digest": "b" * 64,
        },
        "source_freshness": {
            "selected_source_registry_ref": "fixture/registry.md",
            "selected_source_registry_version": 1,
            "selected_source_registry_digest": "c" * 64,
            "selected_binding_ref": "fixture/bindings.json",
            "selected_binding_digest": "d" * 64,
        },
        "initiative": {
            "initiative_id": "query",
            "instruction_summary": "continue the retained query",
        },
    }


class SelectedRunSecretBoundaryTests(unittest.TestCase):
    def test_artifact_continuation_is_admitted_without_mutation(self) -> None:
        parameters = _continuation()
        before = copy.deepcopy(parameters)
        parsed = _validate_common(_request(parameters))
        self.assertEqual(before, parsed["parameters"])
        self.assertEqual(before, parameters)

    def test_artifact_handle_exception_does_not_apply_to_other_routes(self) -> None:
        for route in (
            "find_and_fetch_journal_events",
            "create_atom",
            "update_atom",
            "selected.repeat",
        ):
            with self.subTest(route=route), self.assertRaises(SelectedRunError) as failure:
                _validate_common(_request(_continuation(), route))
            self.assertEqual("secret-input", failure.exception.code)

    def test_artifact_handle_must_be_a_nonempty_string(self) -> None:
        token: object
        for token in ("", None, True, 123, {}, [], {"token": "nested-credential"}):
            parameters = _continuation()
            parameters["query_request"]["snapshot"]["token"] = token
            with self.subTest(token=token), self.assertRaises(SelectedRunError) as failure:
                _validate_common(_request(parameters))
            self.assertEqual("invalid-request", failure.exception.code)

    def test_artifact_handle_exception_preserves_all_other_secret_fields(self) -> None:
        snapshot = _continuation()["query_request"]["snapshot"]
        cases = (
            {"token": "credential"},
            {"snapshot": snapshot},
            {"query_request.snapshot": snapshot},
            {"query_request": {"snapshot.token": "credential"}},
            {"query_request": {"snapshot": [snapshot]}},
            {"query_request": [{"snapshot": snapshot}]},
            {"nested": _continuation()},
            {"query_request": {"nested": {"snapshot": snapshot}}},
            {"query_request": {"snapshot": {**snapshot, "password": "credential"}}},
            {"query_request": {"snapshot": {"token": "credential"}}},
            {"query_request": {"snapshot": {**snapshot, "Token": "credential"}}},
            {"query_request": {"snapshot": snapshot, "access_token": "credential"}},
            {**_continuation(), "password": "credential"},
        )
        for parameters in cases:
            with (
                self.subTest(parameters=parameters),
                self.assertRaises(SelectedRunError) as failure,
            ):
                _reject_parameter_secrets(parameters, "find_and_fetch_artifacts")
            self.assertEqual("secret-input", failure.exception.code)
        for location in ("effects", "source observer observed"):
            with self.subTest(location=location), self.assertRaises(SelectedRunError) as failure:
                _reject_secrets(_continuation(), location)
            self.assertEqual("secret-input", failure.exception.code)

    def test_exact_expected_source_digest_is_admitted(self) -> None:
        _reject_secrets({"expected_state": {"source_token": "a" * 64}})
        _reject_secrets(
            {"expected_state": [{"source_token": "a" * 64}, {"source_token": "b" * 64}]}
        )

    def test_source_digest_must_be_lowercase_sha256(self) -> None:
        value: object
        for value in (
            "secret",
            "a" * 63,
            "a" * 65,
            "A" * 64,
            "g" * 64,
            None,
            True,
            123,
            {},
            [],
            {"token": "a" * 64},
        ):
            with self.subTest(value=value), self.assertRaises(SelectedRunError) as failure:
                _reject_secrets({"expected_state": {"source_token": value}})
            self.assertEqual("invalid-request", failure.exception.code)
            with self.subTest(row_value=value), self.assertRaises(SelectedRunError) as failure:
                _reject_secrets({"expected_state": [{"source_token": value}]})
            self.assertEqual("invalid-request", failure.exception.code)

    def test_token_exemption_does_not_extend_to_other_fields_or_locations(self) -> None:
        for value in (
            {"source_token": "a" * 64},
            {"expected_state": {"token": "a" * 64}},
            {"expected_state": {"Source_Token": "a" * 64}},
            {"expected_state": {"source_token": "a" * 64, "password": "hidden"}},
            {"context": {"expected_state": {"source_token": "a" * 64}}},
            {"expected_state[0]": {"source_token": "a" * 64}},
            {"expected_state[0].source_token": "a" * 64},
            {"expected_state": {"[0]": {"source_token": "a" * 64}}},
            {"expected_state": [[{"source_token": "a" * 64}]]},
            {"expected_state": [{"nested": {"source_token": "a" * 64}}]},
            {"expected_state": [{"source_token": "a" * 64, "password": "hidden"}]},
        ):
            with self.subTest(value=value), self.assertRaises(SelectedRunError) as failure:
                _reject_secrets(value)
            self.assertEqual("secret-input", failure.exception.code)
        for location in ("effects", "source observer observed"):
            with self.subTest(location=location), self.assertRaises(SelectedRunError):
                _reject_secrets({"expected_state": {"source_token": "a" * 64}}, location)


if __name__ == "__main__":
    unittest.main()
