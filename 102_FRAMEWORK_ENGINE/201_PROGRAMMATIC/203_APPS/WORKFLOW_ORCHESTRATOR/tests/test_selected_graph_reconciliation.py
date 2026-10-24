"""Focused persistence-boundary checks for extracted graph reconciliation."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
REPOSITORY = APP.parents[3]
TOOLS = APP.parents[1] / "201_TOOLS"
for location in (APP, TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import selected_execution_run_plan  # noqa: E402
import selected_graph_reconciliation as reconciliation  # noqa: E402
from workflow_run_support import LazyRunTracker, RunExecutionSession  # noqa: E402


class _Session:
    def __init__(self, run_id: str, step_id: str, action_id: str, effect_refs: list[str]) -> None:
        self.actual = {
            run_id: {"run_id": "actual-workflow"},
            step_id: {"run_id": "actual-step"},
            action_id: {"run_id": "actual-action"},
        }
        self.terminal = {
            step_id: self._receipt("actual-step", effect_refs),
            run_id: self._receipt("actual-workflow", effect_refs),
        }
        self.interrupted: dict[str, dict[str, object]] = {}

    @staticmethod
    def _receipt(run_id: str, effect_refs: list[str]) -> dict[str, object]:
        return {
            "run_id": run_id,
            "disposition": "terminal",
            "outcome": "completed",
            "result_ref": "runs/graph-1/graph_result.json",
            "effect_refs": effect_refs,
        }


class _Tracker:
    def _observe(self, execution: object) -> dict[str, object]:
        del execution
        return {}


class SelectedGraphReconciliationTests(unittest.TestCase):
    def test_observation_is_read_only_and_persistence_order_is_stable(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPOSITORY / ".caprmedio_tmp") as temporary:
            root = Path(temporary).resolve()
            folder = root / "runs/graph-1"
            folder.mkdir(parents=True)
            accepted_path = folder / "accepted.json"
            accepted_path.write_text(json.dumps({"result": {"disposition": "started"}}))
            accepted_before = accepted_path.read_bytes()
            run_id = "graph-1"
            step_id = f"{run_id}:step:1"
            action_id = f"{step_id}:action:1"
            effect_refs = ["outputs/graph.md"]
            session = _Session(run_id, step_id, action_id, effect_refs)
            tracker = _Tracker()
            request = {"run_id": run_id, "execution": {"request_id": "request-1"}}
            graph = {
                "route": "build_entities_graph",
                "workflow": {"atom_id": "CA-O-015"},
                "steps": [
                    {
                        "atom_id": "CA-S-1",
                        "actions": [{"atom_id": "CA-O-1", "result_map": {"completed": "built"}}],
                    }
                ],
            }
            progress = {
                "result": "old",
                "action_run_id": "actual-action",
                "graph_construction_observation": {"output_effects": {"paths": effect_refs}},
                "native_result": {"completion": {"state": "retained"}},
            }
            aggregate = {
                "outcome": "interrupted_pending",
                "workflow_run_id": "actual-workflow",
                "workflow_definition_id": "CA-O-015",
            }
            row = {
                "action_run_id": "actual-action",
                "step_run_id": "actual-step",
                "action_definition_id": "CA-O-1",
                "step_definition_id": "CA-S-1",
                "effect_refs": effect_refs,
                "result": "old",
            }
            progress_path = folder / f"{action_id}.json"
            aggregate_path = folder / "graph_result.json"
            progress_ref = progress_path.relative_to(root).as_posix()
            aggregate_ref = aggregate_path.relative_to(root).as_posix()
            read_progress = (progress, progress_path, progress_ref, effect_refs, "completed")
            read_aggregate = (aggregate, aggregate_path, aggregate_ref, row)
            final_result = {"disposition": "terminal", "outcome": "completed"}
            with (
                patch.object(reconciliation, "_request_and_graph", return_value=(request, graph)),
                patch.object(reconciliation, "_validate_common", return_value=request["execution"]),
                patch.object(reconciliation, "shared_tracker", return_value=tracker),
                patch.object(
                    reconciliation, "read_selected_run_evidence", return_value={"events": []}
                ),
                patch.object(RunExecutionSession, "restore", return_value=session),
                patch.object(
                    selected_execution_run_plan, "requested_step_id", return_value=step_id
                ),
                patch.object(reconciliation, "run_directory", return_value=folder),
                patch.object(reconciliation, "_read_progress", return_value=read_progress),
                patch.object(reconciliation, "_read_aggregate", return_value=read_aggregate),
                patch.object(
                    reconciliation, "finalize_graph_result", return_value={"outcome": "completed"}
                ),
                patch.object(reconciliation, "confirmed_graph_terminal", return_value=True),
                patch.object(reconciliation, "_proposal", return_value={}),
                patch.object(LazyRunTracker, "_session_result", return_value=final_result),
                patch.object(reconciliation, "atomic_write") as write,
            ):
                observed = reconciliation.reconcile_graph_recording(root, {}, {}, persist=False)
                self.assertEqual(final_result, observed)
                write.assert_not_called()
                self.assertEqual(accepted_before, accepted_path.read_bytes())

                reconciliation.reconcile_graph_recording(root, {}, {}, persist=True)
                self.assertEqual(
                    [progress_path, aggregate_path, accepted_path],
                    [call.args[0] for call in write.call_args_list],
                )


if __name__ == "__main__":
    unittest.main()
