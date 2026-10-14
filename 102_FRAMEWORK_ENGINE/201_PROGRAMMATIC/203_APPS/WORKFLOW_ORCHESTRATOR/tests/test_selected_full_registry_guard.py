"""Whole-registry refusal at the shared selected queue boundary."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TESTS = Path(__file__).resolve().parent
sys.path.insert(0, str(TESTS))
import test_selected_execution as queue_tests  # noqa: E402
from selected_execution import SelectedExecution, SelectedExecutionError, build_requested_runs  # noqa: E402
import selected_routes  # noqa: E402
sys.path.insert(0, str(queue_tests.MCP / "tests"))
import test_selected_routes_mcp as route_tests  # noqa: E402


class SelectedFullRegistryGuardTest(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = queue_tests.SelectedExecutionTests("test_freeze_rejects_a_stale_manifest_before_any_dispatch")
        self.fixture.isolate_registry_admission = False
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.runner = self.fixture.executor({})

    def _legacy_frozen(self, request: dict) -> dict:
        """An already-frozen pre-guard request, not an admitted positive fixture."""
        manifest = json.loads(self.fixture.manifest_path.read_text())
        route = manifest["routes"][0]
        steps = []
        for source in route["steps"]:
            step = self.runner._definition(source, expected_kind="step")
            step["actions"] = [self.runner._definition(action, expected_kind="action") for action in source["actions"]]
            step["on_result"] = copy.deepcopy(source["on_result"])
            steps.append(step)
        return {"request": request, "graph": {
            "route": route["route"],
            "workflow": self.runner._definition(route["workflow"], expected_kind="workflow"),
            "steps": steps, "entry_step": steps[0]["atom_id"], "native_action_calls": [],
            "manifest_ref": self.fixture.manifest_path.relative_to(self.fixture.root).as_posix(),
            "manifest_digest": manifest["canonical_manifest_sha256"],
        }}

    def test_physically_valid_selected_route_in_partial_registry_refuses_before_freeze(self) -> None:
        request = self.fixture.request("partial-freeze")
        with self.assertRaisesRegex(SelectedExecutionError, "complete selected definition manifest"):
            self.runner.freeze(request)
        self.assertFalse(self.runner.run_directory(request["run_id"]).exists())
        self.assertFalse((self.fixture.root / ".caprmedio_caprmedio/_journal").exists())

    def test_previously_frozen_partial_registry_refuses_before_dispatch_or_run(self) -> None:
        request = self.fixture.request("partial-dispatch")
        frozen = self._legacy_frozen(request)
        calls = []
        with self.assertRaisesRegex(SelectedExecutionError, "complete selected definition manifest"):
            self.runner.dispatch(frozen, run_support=lambda *args: calls.append(args) or {"outcome": "completed"})
        self.assertEqual([], calls)
        self.assertFalse(self.runner.run_directory(request["run_id"]).exists())
        self.assertFalse((self.fixture.root / ".caprmedio_caprmedio/_journal").exists())

    def test_release_request_does_not_use_the_route_only_virtual_manifest(self) -> None:
        request = self.fixture.request("partial-release")
        request["execution"]["operation_route"] = "release_version"
        with patch.object(selected_routes, "load_release_execution_manifest", side_effect=AssertionError("route-only Release admission called")):
            with self.assertRaisesRegex(SelectedExecutionError, "complete selected definition manifest"):
                self.runner.freeze(request)
        self.assertFalse(self.runner.run_directory(request["run_id"]).exists())

    def test_retained_completed_result_is_inspected_without_replay(self) -> None:
        request = self.fixture.request("retained-complete")
        frozen = self._legacy_frozen(request)
        result = {"disposition": "completed", "outcome": "completed", "workflow_run_id": request["run_id"]}
        self.runner._write(self.runner.run_directory(request["run_id"]) / "accepted.json", {"result": result})
        calls = []
        self.assertEqual(result, self.runner.dispatch(frozen, run_support=lambda *args: calls.append(args)))
        self.assertEqual([], calls)
        self.assertFalse((self.fixture.root / ".caprmedio_caprmedio/_journal").exists())

    def test_retained_uncertain_intent_never_dispatches_again(self) -> None:
        request = self.fixture.request("retained-uncertain")
        frozen = self._legacy_frozen(request)
        self.runner._write(self.runner.run_directory(request["run_id"]) / "dispatch-intent.json", {"state": "dispatching"})
        calls = []
        result = self.runner.dispatch(frozen, run_support=lambda *args: calls.append(args))
        self.assertEqual("recording_pending", result["disposition"])
        self.assertEqual([], calls)
        self.assertFalse((self.fixture.root / ".caprmedio_caprmedio/_journal").exists())


class CompleteSelectedRegistryQueueTest(unittest.TestCase):
    """Real complete fifteen-route validation, not seventeen-route readiness."""

    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(dir=route_tests.TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.manifest = route_tests.copy_complete_selected_guard_fixture(self.root)
        self.runner = SelectedExecution(self.root)

    def _request(self, run_id: str) -> dict:
        execution = {"mode": "execute", "operation_route": "create_atom", "workflow_run_id": run_id,
                     "source_freshness": self.manifest["source_freshness"],
                     "definition_manifest": {"manifest_ref": self.manifest["manifest_ref"],
                                             "manifest_digest": self.manifest["canonical_manifest_sha256"]}}
        graph = self.runner._validate_graph(execution)
        execution["requested_runs"] = build_requested_runs(graph, run_id)
        return {"operation": "enqueue_selected", "run_id": run_id, "execution": execution}

    def _drift_unselected_source(self) -> None:
        route = next(row for row in self.manifest["routes"] if row["route"] == "update_atom")
        source = self.root / route["native_action_calls"][0]["source_path"]
        source.write_bytes(source.read_bytes() + b"\nUnselected native source drift\n")

    def test_real_complete_fifteen_route_document_admits_every_graph_and_freeze(self) -> None:
        self.assertEqual(15, len(self.manifest["routes"]))
        for route in self.manifest["routes"]:
            execution = {"mode": "execute", "operation_route": route["route"],
                         "source_freshness": self.manifest["source_freshness"],
                         "definition_manifest": {"manifest_ref": self.manifest["manifest_ref"],
                                                 "manifest_digest": self.manifest["canonical_manifest_sha256"]}}
            self.assertEqual(route["route"], self.runner._validate_graph(execution)["route"])
        frozen = self.runner.freeze(self._request("complete-fifteen"))
        self.assertEqual("create_atom", frozen["graph"]["route"])
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())

    def test_unselected_native_source_drift_blocks_freeze_before_queue_write(self) -> None:
        request = self._request("unselected-freeze")
        self._drift_unselected_source()
        with self.assertRaisesRegex(SelectedExecutionError, "complete selected definition manifest"):
            self.runner.freeze(request)
        self.assertFalse(self.runner.run_directory(request["run_id"]).exists())

    def test_unselected_native_source_drift_blocks_dispatch_before_intent_or_run(self) -> None:
        frozen = self.runner.freeze(self._request("unselected-dispatch"))
        self._drift_unselected_source()
        calls = []
        with self.assertRaisesRegex(SelectedExecutionError, "complete selected definition manifest"):
            self.runner.dispatch(frozen, run_support=lambda *args: calls.append(args))
        self.assertEqual([], calls)
        self.assertFalse((self.runner.run_directory("unselected-dispatch") / "dispatch-intent.json").exists())
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())


if __name__ == "__main__":
    unittest.main()
