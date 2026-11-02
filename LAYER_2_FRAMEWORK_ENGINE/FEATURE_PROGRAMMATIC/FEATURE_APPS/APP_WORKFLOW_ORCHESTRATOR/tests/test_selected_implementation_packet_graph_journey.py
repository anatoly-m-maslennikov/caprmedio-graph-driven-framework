"""An actual O016 graph carries server-bound preparation observations."""

from __future__ import annotations

import copy
from collections.abc import Mapping
from pathlib import Path
import sys
from typing import Any, cast
import unittest


APP = Path(__file__).resolve().parents[1]
for location in (APP, Path(__file__).resolve().parent):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_execution_run_plan import build_requested_runs  # noqa: E402
from selected_graph_executor import execute_graph  # noqa: E402
from selected_integrated_action_outcome import binding_digest  # noqa: E402
from selected_integrated_dispatch_test_support import IntegratedDispatchTestCase  # noqa: E402
from selected_integrated_session import create_checkpoint  # noqa: E402
from workflow_run_support import (  # noqa: E402
    RunTracker,
    _canonical_digest,
    _proposal,
    _validate_common,
)


class SelectedImplementationPacketGraphJourneyTests(IntegratedDispatchTestCase):
    def _reseal(self, frozen: dict[str, Any], tracker: RunTracker) -> None:
        request = cast(dict[str, Any], frozen["request"])
        execution, graph = request["execution"], frozen["graph"]
        parameters = cast(dict[str, Any], execution["parameters"])
        execution["parameters_digest"] = _canonical_digest(parameters)
        execution["requested_runs"] = build_requested_runs(
            graph, request["run_id"], parameters["run_visit_limits"]
        )
        parsed = _validate_common(execution)
        proposal = _proposal(parsed, tracker._observe(parsed))
        execution["proposal_receipt"] = proposal
        execution["proposal_receipt_digest"] = _canonical_digest(proposal)
        execution["operator_authorization"] = {
            **execution["operator_authorization"],
            "parameters_digest": execution["parameters_digest"],
            "proposal_receipt_digest": execution["proposal_receipt_digest"],
        }

    def test_actual_graph_handoff_carries_o231_plan_to_o232(self) -> None:
        frozen, tracker = self.frozen("packet-graph-journey")
        request = cast(dict[str, Any], frozen["request"])
        execution = cast(dict[str, Any], request["execution"])
        graph = cast(dict[str, Any], frozen["graph"])
        first, second = cast(list[dict[str, Any]], graph["steps"])[:2]
        first["on_result"] = [{"result": "evaluation_ready", "next": "CA-O-232"}]
        second["on_result"] = [{"result": "prepared", "terminal": "completed"}]
        execution["parameters"] = copy.deepcopy(execution["parameters"])
        parameters = cast(dict[str, Any], execution["parameters"])
        cast(dict[str, Any], parameters["base_packet"]).pop("plan_item")
        self._reseal(frozen, tracker)
        plan = {"plan_id": "actual", "item_id": "item", "dod": ["prepared"], "estimated_minutes": 1}
        seen: list[dict[str, object]] = []

        def prepare(context: dict[str, object]) -> dict[str, object]:
            packet = cast(Mapping[str, Any], context["parameters"])
            return {
                "result": "evaluation_ready",
                "effect_refs": [],
                "native_result": {
                    "outputs": {"plan_item": plan},
                    "evidence": [],
                    "candidate": copy.deepcopy(packet["candidate"]),
                    "binding_digest": binding_digest(packet),
                },
            }

        def test(context: dict[str, object]) -> dict[str, object]:
            seen.append(dict(cast(Mapping[str, Any], context["parameters"])))
            return {"result": "prepared", "effect_refs": [], "native_result": {}}

        result = execute_graph(
            self.root,
            {"CA-O-017": prepare, "CA-O-018": test},
            frozen,
            create_checkpoint(self.root, frozen, tracker),
        )

        self.assertEqual("completed", result["outcome"])
        self.assertEqual([plan], [packet["plan_item"] for packet in seen])


if __name__ == "__main__":
    unittest.main()
