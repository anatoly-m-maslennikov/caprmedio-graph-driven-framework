"""Host preview, freeze and dispatch keep native Artifact pagination intact."""

from __future__ import annotations

import copy
import unittest
from typing import Any, cast

import test_selected_query_execution as query_fixture
from selected_execution import SelectedExecution, SelectedExecutionError


class SelectedArtifactPaginationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = query_fixture.SelectedQueryExecutionTests(
            "test_artifact_query_uses_the_native_tool_result"
        )
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def test_preview_freeze_dispatch_continue_and_reject_tampered_snapshot(self) -> None:
        root = self.fixture.root
        for identity in ("A-1", "A-2"):
            (root / f"{identity}.md").write_text(f"---\nartifact_id: {identity}\n---\n")
        selected, first = self.fixture._execution(
            "find_and_fetch_artifacts", {"query_request": {"limit": 1}}, "artifact-page-one"
        )
        self.assertEqual("terminal", selected.dispatch(first)["disposition"])
        native = cast(dict[str, Any], self.fixture._progress(first)["native_result"])
        self.assertEqual([{"artifact_id": "A-1"}], native["results"])
        parameters: dict[str, Any] = {
            "query_request": {
                "limit": 1,
                "snapshot": native["snapshot"],
                "cursor": native["next_cursor"],
            }
        }
        original = copy.deepcopy(parameters)
        selected, second = self.fixture._execution(
            "find_and_fetch_artifacts", parameters, "artifact-page-two"
        )
        execution = cast(dict[str, Any], second["request"])["execution"]
        self.assertEqual(original, execution["parameters"])
        self.assertEqual(query_fixture.digest(original), execution["parameters_digest"])
        self.assertEqual("terminal", selected.dispatch(second)["disposition"])
        self.assertEqual(
            [{"artifact_id": "A-2"}],
            cast(dict[str, Any], self.fixture._progress(second)["native_result"])["results"],
        )
        altered = copy.deepcopy(parameters)
        altered["query_request"]["snapshot"]["digest"] = "0" * 64
        selected, rejected = self.fixture._execution(
            "find_and_fetch_artifacts", altered, "artifact-tampered"
        )
        failure = selected.dispatch(rejected)
        self.assertEqual("terminal", failure["disposition"])
        self.assertEqual(
            "failed",
            next(
                row["outcome"]
                for row in failure["terminal_runs"]
                if row["run_id"].endswith("action:1")
            ),
        )
        rejected_native = cast(dict[str, Any], self.fixture._progress(rejected)["native_result"])
        self.assertEqual([], rejected_native["results"])
        self.assertEqual(
            "foreign or tampered retained snapshot", rejected_native["findings"][0]["code"]
        )

    def test_queue_secret_scan_preserves_route_shape_and_credential_boundaries(self) -> None:
        snapshot: dict[str, Any] = {
            "reference": "snapshot:opaque",
            "token": "opaque",
            "digest": "a" * 64,
        }
        base: dict[str, Any] = {
            "mode": "execute",
            "operation_route": "find_and_fetch_artifacts",
            "parameters": {"query_request": {"snapshot": snapshot, "cursor": "cursor"}},
        }
        cases = (
            {**base, "operation_route": "find_and_fetch_journal_events"},
            {**base, "parameters": {"query_request.snapshot": snapshot}},
            {**base, "parameters": {"query_request": {"snapshot": [snapshot]}}},
            {**base, "parameters": {"query_request": [{"snapshot": snapshot}]}},
            {
                **base,
                "parameters": {
                    "query_request": {"snapshot": {**snapshot, "password": "credential"}}
                },
            },
            {**base, "parameters": {"query_request": {"snapshot": {"token": "credential"}}}},
            {**base, "parameters": {**base["parameters"], "api_key": "credential"}},
            {**base, "parameters": {**base["parameters"], "api-key": "credential"}},
            {**base, "parameters": {**base["parameters"], "apikey": "credential"}},
            {**base, "effects": [{"token": "credential"}]},
            {**base, "operator_authorization": {"password": "credential"}},
            {**base, "proposal_receipt": {"token": "credential"}},
            {**base, "parameters": [{"token": "credential"}]},
        )
        selected = SelectedExecution(self.fixture.root)
        for execution in cases:
            with (
                self.subTest(execution=execution),
                self.assertRaisesRegex(SelectedExecutionError, "secret field"),
            ):
                selected._validate_graph(execution)
        for token in ("", None, True, {"token": "credential"}):
            malformed = copy.deepcopy(base)
            malformed["parameters"]["query_request"]["snapshot"]["token"] = token
            with (
                self.subTest(token=token),
                self.assertRaisesRegex(SelectedExecutionError, "secret field"),
            ):
                selected._validate_graph(malformed)
        self.assertEqual([], self.fixture._events())
        self.assertEqual([], list(self.fixture.root.rglob("selected_request.json")))


if __name__ == "__main__":
    unittest.main()
