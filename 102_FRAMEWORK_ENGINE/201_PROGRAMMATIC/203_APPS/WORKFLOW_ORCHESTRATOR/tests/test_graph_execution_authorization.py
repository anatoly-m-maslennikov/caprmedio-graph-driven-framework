"""Isolated fixture proof for executor-bound graph authorization, not live admission."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
GRAPH_TOOL = TOOLS / "GENERATE_ENTITY_GRAPH"
for location in (APP, TOOLS, GRAPH_TOOL):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from generate_entity_graph import is_actual_recording_context  # noqa: E402
from selected_graph_inputs import graph_parameters_with_actual_recording  # noqa: E402


class GraphExecutionAuthorizationTests(unittest.TestCase):
    """Exercise the helper/factory boundary without a route, Journal, or effects."""

    def setUp(self) -> None:
        digest = "a" * 64
        self.receipt = {
            "event_id": "fixture-action-start",
            "action_id": "CA-O-134",
            "event_digest": digest,
            "carrier": "fixture/journal.ndjson",
            "line": 1,
            "previous_carrier_digest": digest,
            "appended_carrier_digest": digest,
        }
        self.actual = {
            "workflow": {
                "run_id": "fixture-workflow",
                "kind": "workflow",
                "definition": {"atom_id": "FIXTURE-O-1", "version": 1},
            },
            "step": {
                "run_id": "fixture-step",
                "kind": "step",
                "parent_run_id": "fixture-workflow",
                "definition": {"atom_id": "FIXTURE-O-2", "version": 1},
            },
            "action": {
                "run_id": "fixture-action",
                "kind": "action",
                "parent_run_id": "fixture-step",
                "definition": {"atom_id": "CA-O-134", "version": 1},
            },
        }
        self.authorization = {
            "authorization_ref": "fixture/operator-authorization.json",
            "authorization_freshness": {"state": "current", "digest": digest},
            "request_id": "fixture-admitted-request",
            "operation_route": "build_entities_graph",
            "proposal_receipt_digest": digest,
            "parameters_digest": digest,
            "target_frontier_digest": digest,
            "effects_digest": digest,
            "definition_manifest": {
                "manifest_ref": "fixture/selected-workflow-bindings.json",
                "manifest_digest": digest,
            },
            "source_freshness": {
                "selected_source_registry_ref": "fixture/source-registry.json",
                "selected_source_registry_version": 1,
                "selected_source_registry_digest": digest,
                "selected_binding_ref": "fixture/selected-binding.json",
                "selected_binding_digest": digest,
            },
        }
        forged_authorization = deepcopy(self.authorization)
        forged_authorization["authorization_ref"] = "fixture/caller-forgery.json"
        self.parameters = {
            "operator_authorization": forged_authorization,
            "run_recording_context": {"receipt_refs": ["caller-forged-receipt"]},
            "graph_request": {
                "operator_authorization": deepcopy(forged_authorization),
                "capability_permission_evidence": {"authorized": True},
            },
        }

    def invoke(self, session: SimpleNamespace) -> object:
        return graph_parameters_with_actual_recording(
            self.parameters, session,
            workflow_run_id="fixture-workflow",
            step_run_id="fixture-step",
            action_run_id="fixture-action",
        )

    def session(self, request: object) -> SimpleNamespace:
        return SimpleNamespace(actual=deepcopy(self.actual), request=request)

    def assert_no_authorization(self, session: SimpleNamespace) -> None:
        context = self.invoke(session)["run_recording_context"]
        self.assertTrue(is_actual_recording_context(context))
        self.assertIsNone(context.authorization_evidence())

    def test_admitted_session_wins_over_top_level_and_nested_caller_forgery(self) -> None:
        before = deepcopy(self.parameters)
        context = self.invoke(self.session({"operator_authorization": self.authorization}))["run_recording_context"]
        self.assertTrue(is_actual_recording_context(context))
        self.assertEqual(context.authorization_evidence(), self.authorization)
        self.assertEqual(dict(context.action_run), self.actual["action"])
        self.assertEqual(
            (context.workflow_run_id, context.step_run_id, context.action_run_id),
            ("fixture-workflow", "fixture-step", "fixture-action"),
        )
        self.assertEqual(self.parameters, before)

    def test_session_authorization_is_frozen_before_later_nested_mutation(self) -> None:
        expected = deepcopy(self.authorization)
        context = self.invoke(self.session({"operator_authorization": self.authorization}))["run_recording_context"]
        self.authorization["authorization_freshness"]["state"] = "changed"
        self.authorization["definition_manifest"]["manifest_digest"] = "b" * 64
        self.assertEqual(context.authorization_evidence(), expected)

    def test_exposed_authorization_evidence_is_a_detached_copy(self) -> None:
        context = self.invoke(self.session({"operator_authorization": self.authorization}))["run_recording_context"]
        evidence = context.authorization_evidence()
        evidence["source_freshness"]["selected_binding_digest"] = "b" * 64
        self.assertEqual(context.authorization_evidence(), self.authorization)

    def test_missing_session_request_does_not_inherit_caller_authorization(self) -> None:
        self.assert_no_authorization(SimpleNamespace(actual=deepcopy(self.actual)))

    def test_receipts_without_actual_runs_cannot_bind_caller_context(self) -> None:
        result = self.invoke(
            SimpleNamespace(
                receipts=[self.receipt],
                request={"operator_authorization": self.authorization},
            )
        )
        self.assertIs(result, self.parameters)
        self.assertFalse(is_actual_recording_context(result["run_recording_context"]))

    def test_wrong_actual_parent_cannot_bind_caller_context(self) -> None:
        for run in ("step", "action"):
            with self.subTest(run=run):
                session = self.session({"operator_authorization": self.authorization})
                session.actual[run]["parent_run_id"] = "wrong-parent"
                result = self.invoke(session)
                self.assertIs(result, self.parameters)
                self.assertFalse(is_actual_recording_context(result["run_recording_context"]))

    def test_nonmapping_session_request_does_not_inherit_caller_authorization(self) -> None:
        for request in (None, [], "caller-request", True):
            with self.subTest(request=request):
                self.assert_no_authorization(self.session(request))

    def test_missing_session_authorization_grants_no_actual_permission(self) -> None:
        self.assert_no_authorization(self.session({}))

    def test_nonmapping_session_authorization_grants_no_actual_permission(self) -> None:
        for authorization in (None, [], "caller-authorization", True):
            with self.subTest(authorization=authorization):
                self.assert_no_authorization(self.session({"operator_authorization": authorization}))

    def test_invalid_session_authorization_cannot_fall_back_to_caller_forgery(self) -> None:
        result = self.invoke(self.session({"operator_authorization": {"authorized": True}}))
        self.assertIs(result, self.parameters)
        self.assertFalse(is_actual_recording_context(result["run_recording_context"]))


if __name__ == "__main__":
    unittest.main()
