# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
"""Real MCP continuation checks for the current direct O016@18 fixture."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import unittest
from typing import Any


TESTS = Path(__file__).resolve().parent
if str(TESTS) not in sys.path:
    sys.path.insert(0, str(TESTS))

from interactive_mcp_journey_support import (  # noqa: E402
    build_execute_request,
    call_tool,
    diagnostic_text,
    journey_session,
    pending_capture,
    result_payload,
    source_drift_path,
    submit_request,
)


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
def _plan_outputs(fixture: Any) -> dict[str, Any]:
    base = fixture.current_context_packet["base_packet"]
    return {
        "plan_item": copy.deepcopy(base["plan_item"]),
        "test_inputs": copy.deepcopy(base["red"]),
        "tests": copy.deepcopy(base["golden_e2e"]),
        "commands": [base["baseline_command"]],
    }


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
class InteractiveMcpJourneyTests(unittest.IsolatedAsyncioTestCase):
    async def test_current_integrated_pending_continuation_and_terminal_block(self) -> None:
        async with journey_session() as (fixture, client):
            execute, first, first_capture = await self._start_pending(fixture, client)
            original_submission, second, second_capture = await self._submit_evaluation(
                fixture, client, first
            )
            duplicate = await call_tool(client, "run_implementation_workflow", original_submission)
            self.assertEqual(second, duplicate)
            await self._assert_conflict(fixture, client, first)
            third, third_capture = await self._submit_prepared(fixture, client, second)
            captures = [first_capture, second_capture, third_capture]
            self.assertGreaterEqual(len(captures), 3)
            self.assertEqual([capture["step_id"] for capture in captures], ["CA-O-231", "CA-O-232", "CA-O-231"])
            terminal = await self._submit_blocked(client, third)
            self.assertEqual(("terminal", "interrupted_pending"), (terminal.get("disposition"), terminal.get("status")))
            self.assertEqual("interrupted_pending", terminal["graph_result"]["outcome"])
            workflow_run_id = first.get("workflow_run_id") or execute["requested_runs"][0]["requested_run_id"]
            status = await call_tool(
                client,
                "get_selected_workflow_run",
                {"run_id": workflow_run_id},
            )
            self.assertEqual(("terminal", "interrupted_pending"), (status.get("disposition"), status.get("outcome")))

    async def test_source_sha_drift_is_refused_after_preview(self) -> None:
        async with journey_session() as (fixture, client):
            preview = await call_tool(client, "run_implementation_workflow", fixture.execution_request)
            execute = build_execute_request(fixture, preview)
            source = source_drift_path(fixture)
            source.write_bytes(source.read_bytes() + b"\n# direct-journey-drift\n")
            refused = await call_tool(client, "run_implementation_workflow", execute)
            self.assertIn(refused.get("disposition"), {"blocked", "rejected"})
            self.assertNotIn("pending_action", refused)
            self.assertRegex(diagnostic_text(refused), r"stale|drift|source|fresh")

    async def test_trusted_methods_are_independent_of_packet_rows(self) -> None:
        async with journey_session() as (fixture, client):
            request = copy.deepcopy(fixture.execution_request)
            methods = request["parameters"]["base_packet"]["methods"]
            methods[0]["content"] = "tampered packet Method"
            from selected_route_manifest import canonical_digest

            request["parameters_digest"] = canonical_digest(request["parameters"])
            preview = await call_tool(client, "run_implementation_workflow", request)
            execute = build_execute_request(fixture, preview, request)
            refused = await call_tool(client, "run_implementation_workflow", execute)
            self.assertIn(refused.get("disposition"), {"blocked", "rejected"})
            self.assertRegex(diagnostic_text(refused), r"method|authority|trusted|stale|source")

    async def test_aggregate_frontier_overflow_is_refused(self) -> None:
        async with journey_session() as (fixture, client):
            _preview, execute = await self._preview_and_execute_request(fixture, client)
            first = await call_tool(client, "run_implementation_workflow", execute)
            pending_capture(first, fixture)
            oversized = "x" * (512 * 1024)
            response = result_payload("evaluation_ready", {**_plan_outputs(fixture), "overflow": oversized})
            submission = submit_request(first, response)
            measured = len(json.dumps(submission, sort_keys=True, separators=(",", ":")).encode())
            self.assertGreater(measured, 512 * 1024)
            refused = await call_tool(client, "run_implementation_workflow", submission)
            self.assertIn(refused.get("disposition"), {"blocked", "rejected"})
            self.assertRegex(diagnostic_text(refused), r"bounded|carrier|overflow|512")

    async def _preview_and_execute_request(self, fixture: Any, client: Any) -> tuple[dict[str, Any], dict[str, Any]]:
        preview = await call_tool(client, "run_implementation_workflow", fixture.execution_request)
        return preview, build_execute_request(fixture, preview)

    async def _start_pending(self, fixture: Any, client: Any) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
        _preview, execute = await self._preview_and_execute_request(fixture, client)
        first = await call_tool(client, "run_implementation_workflow", execute)
        capture = pending_capture(first, fixture)
        self._assert_public_pending(first, capture)
        status = await call_tool(client, "get_selected_workflow_run", {"run_id": first["workflow_run_id"]})
        self.assertNotIn("definitions", status.get("capture", {}))
        self.assertEqual("CA-O-231", capture["step_id"])
        return execute, first, capture

    async def _submit_evaluation(
        self, fixture: Any, client: Any, first: dict[str, Any]
    ) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
        submission = submit_request(first, result_payload("evaluation_ready", _plan_outputs(fixture)))
        second = await call_tool(client, "run_implementation_workflow", submission)
        capture = pending_capture(second, fixture)
        self._assert_public_pending(second, capture)
        self.assertEqual("CA-O-232", capture["step_id"])
        self._assert_retained_plan_inputs(capture)
        return submission, second, capture

    async def _assert_conflict(self, fixture: Any, client: Any, first: dict[str, Any]) -> None:
        conflict = await call_tool(
            client,
            "run_implementation_workflow",
            submit_request(
                first,
                result_payload("blocked", {"reason": "conflicting repeat"}, blockers=["conflict"]),
            ),
        )
        self.assertIn(conflict.get("disposition"), {"blocked", "rejected"})
        self.assertIn("conflict", diagnostic_text(conflict))

    async def _submit_prepared(
        self, fixture: Any, client: Any, second: dict[str, Any]
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        outputs = {"plan_item": _plan_outputs(fixture)["plan_item"]}
        third = await call_tool(
            client, "run_implementation_workflow", submit_request(second, result_payload("prepared", outputs))
        )
        next_capture = pending_capture(third, fixture)
        self._assert_public_pending(third, next_capture)
        self.assertEqual("CA-O-231", next_capture["step_id"])
        return third, next_capture

    async def _submit_blocked(self, client: Any, third: dict[str, Any]) -> dict[str, Any]:
        return await call_tool(
            client,
            "run_implementation_workflow",
            submit_request(
                third,
                result_payload("blocked", {"reason": "journey stop"}, blockers=["journey stop"]),
            ),
        )

    def _assert_retained_plan_inputs(self, capture: dict[str, Any]) -> None:
        packet = capture["packet"]
        retained = packet["retained_state"]["prior_results"]
        row = next(item for item in retained if item.get("result") == "evaluation_ready")
        self.assertIn("plan_item", row["outputs"])
        self.assertIn("test_inputs", row["outputs"])

    # implementation of:
    # Requirement: CA-R-2117
    # Method: CA-M-431
    def _assert_public_pending(self, result: dict[str, Any], capture: dict[str, Any]) -> None:
        self.assertNotIn("definitions", capture)
        next_call = result.get("next_call")
        self.assertIsInstance(next_call, dict)
        assert isinstance(next_call, dict)
        self.assertEqual("run_implementation_workflow", next_call.get("tool"))
        self.assertEqual(
            {
                "operation": "submit_result",
                "run_id": result["workflow_run_id"],
                "action_run_id": result["action_run_id"],
                "continuation_id": result["continuation_id"],
            },
            next_call.get("request"),
        )
        self.assertEqual(capture["output_schema"], next_call.get("result_schema"))


if __name__ == "__main__":
    unittest.main()
