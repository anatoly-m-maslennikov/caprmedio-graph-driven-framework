"""Actual selected Step-input handoff proof for O016."""
from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
TESTS = Path(__file__).resolve().parent
TOOLS = APP.parents[1] / "FEATURE_TOOLS"
MCP = APP.parents[1] / "FEATURE_MCP"
PROMPTS = ROOT / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_AGENTIC/FEATURE_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW"
for location in (TESTS, MCP, APP, TOOLS, PROMPTS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import implementation_actions  # noqa: E402
from selected_execution import SelectedExecution  # noqa: E402
from frozen_selected_workflows import frozen_implementation_bindings, write_frozen_source  # noqa: E402


class SelectedStepInputsTest(unittest.TestCase):
    """Retain generic selected execution coverage after retiring obsolete structure routes."""

    def test_o016_wrapper_supplies_its_selected_project_root(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "selected-project"
            for binding in frozen_implementation_bindings():
                write_frozen_source(project, binding["path"], binding["sha256"])
            workspace = project / "disposable-workspace"
            workspace.mkdir()
            sources = implementation_actions.current_source_bindings(project)
            methods = [row["path"] for row in sources if row["atom_id"].startswith("CA-M-")]
            candidate = {"id": "candidate-1"}
            packet = {
                "context": "Isolated",
                "step_marker": "CA-O-093",
                "selected_project": {
                    "kind": "selected_project",
                    "source_root": ".caprmedio_caprmedio",
                    "source_references": sources,
                },
                "source_bindings": sources,
                "permissions": {"allowed": True, "implementation_workspace": {
                    "kind": "disposable_workspace", "path": str(workspace), "allow_write": True,
                }},
                "workspace": str(workspace),
                "method_projection": implementation_actions.prepare_method_projection(methods, project),
                "requirements": implementation_actions.prepare_input_bindings(["CA-R-1843"], project),
                "delivery": implementation_actions.prepare_input_bindings(["CA-D-544"], project),
                "evaluations": implementation_actions.prepare_input_bindings(["CA-E-563"], project),
                "plan_item": {"plan_id": "plan-1", "item_id": "item-1",
                               "dod": ["implemented and checked"], "owned_paths": ["."],
                               "estimated_minutes": 1},
                "red": {"expectation": "ready is true", "fixtures": ["fixture"],
                        "commands": ["python fixture_test.py"], "scope": "selected item"},
                "candidate": candidate, "phase": "implementation",
                "golden_e2e": ["disposable executable assertion"],
                "baseline_command": "python fixture_test.py",
                "confidence": {"observed": 1.0, "effective": 0.9, "source": "default-settings"},
                "retry": {"consumed": 0, "effective_limit": 1,
                          "source": "CA-M-295:default-settings", "remaining_failure": True,
                          "admitted": True},
                "coverage": {"required": ["CA-E-563"], "checked": [], "complete": False,
                             "candidate": candidate, "phase": "implementation"},
                "handoff_complete": True,
                "retained_state": {},
            }
            calls: list[dict[str, object]] = []

            def agent(_prompt: str, supplied: dict[str, object]) -> dict[str, object]:
                calls.append(supplied)
                return {"result": "implemented", "outputs": {"candidate": supplied["candidate"],
                                                                    "phase": supplied["phase"],
                                                                    "changed_paths": ["x.py"]},
                        "evidence": ["performed"]}

            runner = SelectedExecution(project, implementation_agent=agent)
            output = runner.handlers["CA-O-019"]({"parameters": packet})

            self.assertEqual(project.resolve(), runner.root)
            self.assertNotEqual(project.resolve(), implementation_actions.ROOT.resolve())
            self.assertEqual("implemented", output["result"])
            self.assertEqual([packet], calls)


if __name__ == "__main__":
    unittest.main()
