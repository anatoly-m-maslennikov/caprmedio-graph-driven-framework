"""Functional red case for the current O016 graph at the native boundary."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1]
PROJECT_ROOT = APP.parents[3]
for location in (APP, APP / "tests"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))


from selected_execution import SelectedExecution  # noqa: E402
from shared_context_current_fixture import CurrentSharedContextFixture  # noqa: E402
from selected_workflows_docker_fixture import GoldenCase, GoldenProject  # noqa: E402


class _Session:
    """Small shared-Run recorder for one native graph case."""

    def __init__(self) -> None:
        self.actual: dict[str, dict[str, object]] = {}

    def start_run(self, requested_id: str) -> dict[str, object]:
        actual: dict[str, object] = {
            "run_id": f"actual:{len(self.actual) + 1}",
            "requested_run_id": requested_id,
        }
        self.actual[requested_id] = actual
        return actual

    def finish_run(self, run_id: str, **result: object) -> dict[str, object]:
        return {"run_id": run_id, "disposition": "terminal", **result}


class SharedContextNativeGraphTests(unittest.TestCase):
    """The current graph must not be routed through the legacy Step map."""

    def test_current_fixture_is_source_pinned_without_live_authority_reads(self) -> None:
        fixture = CurrentSharedContextFixture.load()
        fixture.verify()
        graph = fixture.graph()
        self.assertEqual("CA-O-231", graph["entry_step"])
        self.assertEqual(
            [
                "CA-O-231",
                "CA-O-232",
                "CA-O-233",
                "CA-O-094",
                "CA-O-234",
                "CA-O-096",
                "CA-O-099",
                "CA-O-230",
            ],
            [row["atom_id"] for row in graph["steps"]],
        )
        self.assertEqual(17, len(fixture.source_pins()))

    def test_current_fixture_materializes_only_its_declared_source_closure(self) -> None:
        fixture = CurrentSharedContextFixture.load()
        parent = PROJECT_ROOT / ".caprmedio_tmp" / "shared-context-current-fixture"
        parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=parent) as raw:
            project = fixture.materialize(Path(raw) / "project")
            self.assertTrue((project / ".git").is_dir())
            for pin in fixture.source_pins():
                target = project / str(pin["source_path"])
                self.assertEqual(
                    str(pin["sha256"]), hashlib.sha256(target.read_bytes()).hexdigest()
                )
            self.assertEqual(39, len(fixture.method_source_pins()))
            for pin in fixture.method_source_pins():
                target = project / str(pin["path"])
                self.assertEqual(
                    str(pin["sha256"]), hashlib.sha256(target.read_bytes()).hexdigest()
                )

    def test_current_prepare_step_runs_through_the_native_graph_adapter(self) -> None:
        parent = PROJECT_ROOT / ".caprmedio_tmp" / "shared-context-native-red"
        parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=parent) as raw:
            root = Path(raw)
            fixture = GoldenProject(root, root, GoldenCase("W09", "run_implementation_workflow"))
            fixture.prepare()
            parameters = fixture.native_implementation_parameters()
            old_packets = parameters["step_packets"]
            parameters["step_packets"] = {"CA-O-231": old_packets["CA-O-091"]}
            parameters["run_visit_limits"] = {"CA-O-231": 1}
            graph = {
                "route": "run_implementation_workflow",
                "workflow": {"atom_id": "CA-O-016"},
                "entry_step": "CA-O-231",
                "steps": [
                    {
                        "atom_id": "CA-O-231",
                        "actions": [
                            {
                                "atom_id": "CA-O-017",
                                "result_map": {"evaluation_ready": "evaluation_ready"},
                            }
                        ],
                        "on_result": [{"result": "evaluation_ready", "terminal": "completed"}],
                    }
                ],
            }
            frozen = {
                "request": {
                    "run_id": "current-native-red",
                    "execution": {"parameters": parameters},
                },
                "graph": graph,
            }
            result = SelectedExecution(root)._execute_graph(frozen, _Session())
            run_dir = root / ".caprmedio_install/workflow_orchestrator/runs/current-native-red"
            progress = [
                json.loads(path.read_text(encoding="utf-8"))
                for path in run_dir.glob("*.json")
                if "native_result" in json.loads(path.read_text(encoding="utf-8"))
            ]
            native = progress[0]["native_result"]
            self.assertEqual("CA-O-231", native["step"], result)


if __name__ == "__main__":
    unittest.main()
