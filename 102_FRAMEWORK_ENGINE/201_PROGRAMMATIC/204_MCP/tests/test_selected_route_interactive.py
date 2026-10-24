"""Focused public transport checks for the Integrated continuation request."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest
from unittest.mock import ANY, patch

from pydantic import ValidationError


MCP = Path(__file__).resolve().parents[1]
APP = MCP.parent / "203_APPS" / "WORKFLOW_ORCHESTRATOR"
TOOLS = MCP.parent / "201_TOOLS"
for location in (MCP, APP, TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from contracts import SubmitResult  # noqa: E402
from selected_route_adapter import SelectedRouteAdapter  # noqa: E402
import selected_route_interactive  # noqa: E402
import selected_route_adapter  # noqa: E402


class _Adapter:
    root = Path("/selected-project")

    @staticmethod
    def _result(_request, disposition, outcome, diagnostic):
        return {"disposition": disposition, "outcome": outcome, "diagnostics": [diagnostic]}


def _request() -> dict[str, object]:
    return {
        "operation": "submit_result",
        "run_id": "workflow-run",
        "action_run_id": "action-run",
        "continuation_id": "a" * 64,
        "result": {"result": "complete", "outputs": {}, "evidence": [], "blockers": []},
    }


class SelectedRouteInteractiveTests(unittest.TestCase):
    def test_current_integrated_gate_requires_the_current_source_only(self) -> None:
        route = {
            "entry_step": "CA-O-231",
            "workflow": {"atom_id": "CA-O-016", "version": 18},
        }
        execution = {
            "mode": "execute",
            "parameters": {
                "base_packet": {"context": "Integrated", "methods": []},
                "step_packets": {"CA-O-231": {"context": "Integrated"}},
            },
        }
        self.assertTrue(selected_route_interactive.is_current_integrated_execute(route, execution))
        self.assertFalse(
            selected_route_interactive.is_current_integrated_execute(
                {**route, "workflow": {"atom_id": "CA-O-016", "version": 17}}, execution
            )
        )
        self.assertTrue(
            selected_route_interactive.is_current_integrated_execute(
                route,
                {
                    **execution,
                    "parameters": {
                        "base_packet": {"context": "Integrated"},
                        "step_packets": {"CA-O-231": {"context": "Isolated"}},
                    },
                },
            )
        )
        self.assertTrue(
            selected_route_interactive.is_current_integrated_execute(
                route,
                {
                    **execution,
                    "parameters": {
                        "base_packet": {
                            "context": "Integrated",
                            "methods": [],
                            "method_projection": {"compatibility": "retained"},
                        },
                        "step_packets": {"CA-O-231": {"context": "Integrated"}},
                    },
                },
            )
        )

    def test_current_route_malformed_packet_cannot_fall_back_to_queue(self) -> None:
        route = {
            "entry_step": "CA-O-231",
            "workflow": {"atom_id": "CA-O-016", "version": 18},
        }
        request = {"mode": "execute", "parameters": {"base_packet": {}}}

        class Support:
            @staticmethod
            def run_selected_operation(_request):
                raise AssertionError("legacy queue support must not run")

        class Adapter:
            routes = {"run_implementation_workflow": route}

            @staticmethod
            def _support():
                return Support()

        expected = {"disposition": "blocked", "outcome": "blocked"}
        adapter = Adapter()
        with patch.object(
            selected_route_adapter, "invoke_integrated_execute", return_value=expected
        ) as call:
            result = SelectedRouteAdapter._invoke_validated(
                adapter, "run_implementation_workflow", request
            )

        self.assertEqual(expected, result)
        call.assert_called_once_with(adapter, request, ANY)

    def test_contract_is_strict_and_has_no_caller_digest(self) -> None:
        request = _request()
        parsed = SubmitResult.model_validate(request)
        self.assertEqual("complete", parsed.result.result)
        for extra in ("result_digest", "unexpected"):
            with self.subTest(extra=extra), self.assertRaises(ValidationError):
                SubmitResult.model_validate({**request, extra: "caller-supplied"})
        for unsafe in ({"opaque": object()}, {"nonfinite": float("nan")}):
            with self.subTest(unsafe=unsafe), self.assertRaises(ValidationError):
                SubmitResult.model_validate(
                    {**request, "result": {**request["result"], "outputs": unsafe}}
                )

    def test_transport_passes_only_selected_project_root_and_validated_data(self) -> None:
        request = _request()
        captured: dict[str, object] = {}

        class Orchestrator:
            SubmitResult = SubmitResult

            @staticmethod
            def run(root, value):
                captured.update(root=root, value=value)
                return {"disposition": "started", "status": "pending_action"}

        with patch.object(selected_route_interactive, "_orchestrator", return_value=Orchestrator):
            result = selected_route_interactive.invoke_submit_result(_Adapter(), request)

        self.assertEqual({"disposition": "started", "status": "pending_action"}, result)
        self.assertEqual(_Adapter.root, captured["root"])
        self.assertEqual(request, captured["value"])

    def test_invalid_submit_is_rejected_before_orchestrator_run(self) -> None:
        request = {**_request(), "unknown": True}
        result = selected_route_interactive.invoke_submit_result(_Adapter(), request)
        self.assertEqual("rejected", result["disposition"])
        self.assertIn("submit_result is invalid", result["diagnostics"][0])

    def test_pending_response_has_a_bound_follow_up_without_private_definitions(self) -> None:
        continuation_id = "a" * 64
        value = {
            "status": "pending_action",
            "workflow_run_id": "workflow-run",
            "action_run_id": "action-run",
            "continuation_id": continuation_id,
            "capture": {
                "prompt": "Perform the captured Action.",
                "packet": {"bound": True},
                "output_schema": {"type": "object"},
                "definitions": {"trusted_methods": ["private"]},
            },
        }

        result = selected_route_interactive._public_pending(value)

        self.assertEqual("Perform the captured Action.", result["capture"]["prompt"])
        self.assertNotIn("definitions", result["capture"])
        self.assertEqual(
            {
                "tool": "run_implementation_workflow",
                "request": {
                    "operation": "submit_result",
                    "run_id": "workflow-run",
                    "action_run_id": "action-run",
                    "continuation_id": continuation_id,
                },
                "result_schema": {"type": "object"},
            },
            result["next_call"],
        )


if __name__ == "__main__":
    unittest.main()
