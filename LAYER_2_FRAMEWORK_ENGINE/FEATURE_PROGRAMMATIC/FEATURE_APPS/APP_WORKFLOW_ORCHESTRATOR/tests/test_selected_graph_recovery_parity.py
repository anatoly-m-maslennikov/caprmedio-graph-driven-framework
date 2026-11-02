from __future__ import annotations

from collections.abc import Mapping
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from typing import Any


APP = Path(__file__).resolve().parents[1]
TESTS = Path(__file__).resolve().parent
for location in (APP, TESTS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_evidence_io import atomic_write as write_evidence  # noqa: E402
from selected_execution_contracts import ActionHandler, SelectedExecutionError  # noqa: E402
from selected_graph_executor import execute_graph  # noqa: E402
from selected_graph_recovery_fixtures import (  # noqa: E402
    RecoverySession,
    UnconfirmedProjectionSession,
    frozen_graph,
    frozen_request,
)
import selected_graph_terminal  # noqa: E402
from selected_graph_terminal import (  # noqa: E402
    finish_graph_terminal,
    result_writer,
    terminal_transition,
)


class SelectedGraphRecoveryParityTest(unittest.TestCase):
    def test_recovery_snapshots_actual_action_membership_before_start(self) -> None:
        graph = frozen_graph("change_atom_status")
        for already_restored in (False, True):
            with self.subTest(already_restored=already_restored):
                run_id = f"golden-recovery-{str(already_restored).lower()}"
                action_id = f"{run_id}:step:1:action:1"
                existing = {action_id: {"run_id": action_id, "kind": "action"}}
                session = RecoverySession(existing if already_restored else None)
                observed: list[bool] = []

                def handler(context: dict[str, Any]) -> Mapping[str, Any]:
                    observed.append(context["restored_action"] is True)
                    return {"result": "applied", "terminal_outcome": "completed", "effect_refs": []}

                with tempfile.TemporaryDirectory() as directory:
                    result = execute_graph(
                        Path(directory),
                        {"CA-O-128": handler},
                        frozen_request(graph, run_id, {}),
                        session,
                        recovery=True,
                    )
                self.assertEqual("completed", result["outcome"], result)
                self.assertEqual([already_restored], observed)

    def test_frozen_o016_multistep_revisit_preserves_order_and_ids(self) -> None:
        graph = frozen_graph("run_implementation_workflow")
        run_id = "frozen-o016-revisit"
        step_packets = {
            step["atom_id"]: {"context": "Integrated", "retained_state": {}}
            for step in graph["steps"]
        }
        parameters = {
            "base_packet": {"context": "Integrated", "retained_state": {}},
            "step_packets": step_packets,
            "run_visit_limits": {"CA-O-094": 2},
        }
        results = {
            "CA-O-091": ["evaluation ready"],
            "CA-O-092": ["tests prepared"],
            "CA-O-093": ["implementation delivered"],
            "CA-O-094": ["checks fail", "checks pass"],
            "CA-O-095": ["repair admission"],
            "CA-O-096": ["retry admitted"],
            "CA-O-099": ["repair completed"],
        }
        calls: list[str] = []
        step_ids: list[str] = []
        counts: dict[str, int] = {}

        def handler(context: dict[str, Any]) -> Mapping[str, Any]:
            step_id = str(context["step_definition_id"])
            index = counts.get(step_id, 0)
            counts[step_id] = index + 1
            calls.append(str(context["requested_action_run_id"]))
            step_ids.append(step_id)
            return {"result": results[step_id][index], "effect_refs": []}

        handlers: dict[str, ActionHandler] = {
            action["atom_id"]: handler for step in graph["steps"] for action in step["actions"]
        }
        with tempfile.TemporaryDirectory() as directory:
            result = execute_graph(
                Path(directory),
                handlers,
                frozen_request(graph, run_id, parameters),
                RecoverySession(),
            )
        self.assertEqual("completed", result["outcome"], result)
        self.assertEqual(
            [
                f"{run_id}:step:1:action:1",
                f"{run_id}:step:2:action:1",
                f"{run_id}:step:3:action:1",
                f"{run_id}:step:4:action:1",
                f"{run_id}:step:5:action:1",
                f"{run_id}:step:6:action:1",
                f"{run_id}:step:7:action:1",
                f"{run_id}:step:4:visit:2:action:1",
            ],
            calls,
        )
        self.assertEqual(
            [
                "CA-O-091",
                "CA-O-092",
                "CA-O-093",
                "CA-O-094",
                "CA-O-095",
                "CA-O-096",
                "CA-O-099",
                "CA-O-094",
            ],
            step_ids,
        )

    def test_projection_rewrites_pending_after_unconfirmed_receipts(self) -> None:
        graph = {"route": "build_entities_graph", "workflow": {"atom_id": "CA-O-133"}}
        session = UnconfirmedProjectionSession()
        trace = session.trace
        writes: list[dict[str, Any]] = []

        def record_write(path: Path, value: object) -> None:
            if not isinstance(value, Mapping):
                raise AssertionError("projection evidence must remain a mapping")
            writes.append(dict(value))
            trace.append(f"write:{len(writes)}")
            write_evidence(path, value)

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(selected_graph_terminal, "atomic_write", side_effect=record_write):
                result = finish_graph_terminal(
                    root,
                    session,
                    graph,
                    {"run_id": "projection-trace"},
                    [{"effect_refs": []}],
                    "requested-step",
                    "step-run",
                    "workflow-run",
                    [],
                    "completed",
                    recovery=False,
                )
            saved = json.loads(
                (
                    root
                    / ".caprmedio_install/workflow_orchestrator/runs/projection-trace/graph_result.json"
                ).read_text(encoding="utf-8")
            )
        self.assertEqual(["write:1", "finish:step-run", "finish:workflow-run", "write:2"], trace)
        self.assertEqual(
            ["interrupted_pending", "interrupted_pending"], [row["outcome"] for row in writes]
        )
        self.assertEqual("interrupted_pending", result["outcome"])
        self.assertEqual("interrupted_pending", saved["outcome"])

    def test_exact_writer_and_terminal_diagnostics_are_preserved(self) -> None:
        expected_writers = {
            owner: f"{owner} result writer requires an evidence mapping"
            for owner in ("creation", "lifecycle", "replacement")
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for owner, expected in expected_writers.items():
                with self.subTest(owner=owner):
                    invalid: Any = []
                    with self.assertRaises(SelectedExecutionError) as raised:
                        result_writer(root, root / f"{owner}.json", owner)(invalid)
                    self.assertEqual(expected, str(raised.exception))
        for value, expected in (
            (None, "selected terminal result is invalid"),
            ("bogus", "selected terminal result is not a truthful Run outcome"),
        ):
            with self.subTest(value=value):
                with self.assertRaises(SelectedExecutionError) as raised:
                    terminal_transition(value)
                self.assertEqual(expected, str(raised.exception))


if __name__ == "__main__":
    unittest.main()
