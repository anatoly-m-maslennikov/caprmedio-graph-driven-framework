# CA-E-796@2
"""Retained DBOS registration and removed-route admission checks."""

from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))

import backend  # noqa: E402
import orchestrator  # noqa: E402
from selected_execution_contracts import SelectedExecutionError  # noqa: E402


class RegisteredDBOS:
    def __init__(self):
        self.steps = {}
        self.workflows = {}

    def step(self, *, name):
        def register(function):
            self.steps[name] = function
            return function

        return register

    def workflow(self, *, name):
        def register(function):
            self.workflows[name] = function
            return function

        return register


class AgentRetirementTests(unittest.TestCase):
    def test_worker_fingerprint_includes_the_retained_compiler(self):
        from engine import runtime_fingerprint

        before = runtime_fingerprint()
        read_bytes = Path.read_bytes

        def changed(path):
            raw = read_bytes(path)
            return raw + b"\n" if path.name == "compile_applicable_methodology.py" else raw

        with patch.object(Path, "read_bytes", new=changed):
            self.assertNotEqual(before, runtime_fingerprint())

    def test_retained_selected_queue_registers_only_deterministic_dispatch(self):
        dbos = RegisteredDBOS()
        providers = type("Providers", (), {"dispatch": lambda _self, run_id: {"run_id": run_id}})()
        backend.register_execution(
            dbos, type("Engine", (), {"root": Path.cwd()})(), selected_providers=providers
        )
        self.assertEqual({"selected-workflow-dispatch"}, set(dbos.steps))
        self.assertEqual({backend.SELECTED_WORKFLOW}, set(dbos.workflows))
        self.assertEqual(
            {"run_id": "retained"}, dbos.workflows[backend.SELECTED_WORKFLOW]("retained")
        )

    def test_retired_operations_are_not_public_request_variants(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            base = {
                "operation": "enqueue",
                "run_id": "removed-base",
                "selection": [],
                "criteria_paths": ["rule.md"],
                "author": "operator",
                "scope": "test",
            }
            selected = {
                "operation": "enqueue_selected",
                "run_id": "removed-selected",
                "execution": {"operation_route": "run_implementation_workflow"},
            }
            with self.assertRaises(ValueError):
                orchestrator.run(root, base)
            with self.assertRaisesRegex(ValueError, "Unsupported.*removed"):
                orchestrator.run(root, selected)
            self.assertFalse((root / ".caprmedio_install").exists())

    def test_direct_freeze_refuses_retired_route_without_writing(self):
        from selected_execution import SelectedExecution

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            selected = SelectedExecution(root)
            request = {
                "operation": "enqueue_selected",
                "run_id": "removed-selected",
                "execution": {
                    "operation_route": "run_implementation_workflow",
                    "workflow_run_id": "removed-selected",
                },
            }
            with self.assertRaisesRegex(SelectedExecutionError, "Unsupported.*removed"):
                selected.freeze(request)
            self.assertFalse((root / ".caprmedio_install").exists())


if __name__ == "__main__":
    unittest.main()
