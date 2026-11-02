"""Small typed fakes and graph builders for selected-graph parity tests."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from frozen_selected_workflows import frozen_manifest


class RecoverySession:
    def __init__(self, actual: Mapping[str, Mapping[str, Any]] | None = None) -> None:
        self.actual = {key: dict(value) for key, value in (actual or {}).items()}
        self.terminal: dict[str, dict[str, Any]] = {}
        self.interrupted: dict[str, dict[str, Any]] = {}
        self.start_order: list[str] = []

    def start_run(self, requested_id: str) -> dict[str, Any]:
        self.start_order.append(requested_id)
        existing = self.actual.get(requested_id)
        if existing is not None:
            return dict(existing)
        row: dict[str, Any] = {"run_id": requested_id}
        if ":action:" in requested_id:
            row.update({"kind": "action", "parent_run_id": requested_id.rsplit(":action:", 1)[0]})
        elif ":step:" in requested_id:
            row.update({"kind": "step", "parent_run_id": requested_id.split(":step:", 1)[0]})
        else:
            row["kind"] = "workflow"
        self.actual[requested_id] = row
        return dict(row)

    def finish_run(self, run_id: str, **result: Any) -> dict[str, Any]:
        receipt = {"run_id": run_id, "disposition": "terminal", **result}
        self.terminal[run_id] = receipt
        return dict(receipt)


class UnconfirmedProjectionSession:
    def __init__(self) -> None:
        self.trace: list[str] = []

    def finish_run(self, run_id: str, **result: Any) -> dict[str, Any]:
        self.trace.append(f"finish:{run_id}")
        return {"run_id": run_id, "disposition": "started", **result}


def frozen_graph(route_name: str) -> dict[str, Any]:
    route = next(row for row in frozen_manifest()["routes"] if row["route"] == route_name)
    steps: list[dict[str, Any]] = []
    for ordered in route["ordered_steps"]:
        step = dict(ordered["step"])
        step["actions"] = [dict(ordered["action"])]
        step["on_result"] = []
        for edge in route["on_result"]:
            if edge["from"] != step["atom_id"]:
                continue
            transition: dict[str, Any] = {"result": edge["condition"]}
            transition["terminal" if edge["to"] == "complete" else "next"] = (
                "completed" if edge["to"] == "complete" else edge["to"]
            )
            step["on_result"].append(transition)
        steps.append(step)
    return {
        "route": route["route"],
        "workflow": dict(route["workflow"]),
        "entry_step": route["entry_step"],
        "steps": steps,
    }


def frozen_request(
    graph: Mapping[str, Any], run_id: str, parameters: Mapping[str, Any]
) -> dict[str, Any]:
    return {
        "graph": graph,
        "request": {
            "run_id": run_id,
            "execution": {
                "request_id": run_id,
                "operation_route": graph["route"],
                "parameters": dict(parameters),
            },
        },
    }
