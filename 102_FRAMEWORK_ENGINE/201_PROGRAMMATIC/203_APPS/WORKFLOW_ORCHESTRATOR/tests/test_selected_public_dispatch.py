"""No-effect bridge checks for the D613 public selected-session dispatch."""
from __future__ import annotations

import copy
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
PUBLIC_RELEASE = APP.parents[1] / "201_TOOLS/PUBLIC_RELEASE"
for path in (APP, PUBLIC_RELEASE):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import public_release  # noqa: E402
import selected_host  # noqa: E402
from selected_execution import SelectedExecution, SelectedExecutionError  # noqa: E402
from selected_native_providers import SelectedNativeProviders  # noqa: E402


class _Session:
    terminal = {}

    def start_run(self, requested):
        return {"run_id": requested}

    def finish_run(self, actual, **result):
        self.finished = (actual, result)


class SelectedPublicDispatchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        pairs = (
            ("CA-O-189", "CA-O-190"), ("CA-O-191", "CA-O-192"),
            ("CA-O-193", "CA-O-194"), ("CA-O-195", "CA-O-196"),
            ("CA-O-197", "CA-O-198"),
        )
        self.graph = {
            "route": "public.release", "workflow": {"atom_id": "CA-O-188"},
            "entry_step": "CA-O-189", "native_action_calls": [],
            "steps": [
                {"atom_id": step, "actions": [{"atom_id": action}]}
                for step, action in pairs
            ],
        }
        self.frozen = {
            "request": {"run_id": "public-fixture", "execution": {
                "operation_route": "public.release", "parameters": {"source": {
                    "readme_ref": "README.md", "pr_body_ref": "PR_DESCRIPTION.md",
                    "version_history_ref": "VERSION_HISTORY.md"}},
            }},
            "graph": copy.deepcopy(self.graph),
        }
        self.providers = SelectedNativeProviders(self.root, implementation_agent=lambda *_args: {})

    def execution(self) -> SelectedExecution:
        return self.providers.execution(copy.deepcopy(self.frozen))

    def test_dispatches_the_existing_session_once_without_generic_workflow_start(self) -> None:
        selected = self.execution()
        session = _Session()
        host = object()
        calls = []
        hooks = SimpleNamespace(run_selected_public_release=lambda *args, **kwargs: calls.append((args, kwargs)) or {"status": "published"})
        with patch.object(selected, "_revalidate", return_value=copy.deepcopy(self.graph)) as revalidate, \
                patch.object(selected_host, "create_selected_public_bindings", return_value=host) as create, \
                patch.object(public_release, "SelectedPublicSessionPhases", return_value="phases"), \
                patch.object(self.providers, "_project_release_module", return_value=hooks), \
                patch.object(self.providers, "_public_release_changes", return_value=["fix: selected change"]), \
                patch.object(SelectedExecution, "_execute_graph", side_effect=AssertionError("generic start")) as generic:
            self.assertIsNone(selected._execute_admitted_session(self.frozen, session))

        revalidate.assert_called_once_with(self.frozen)
        create.assert_called_once_with(self.root, self.frozen, session)
        self.assertEqual(len(calls), 1)
        self.assertIs(calls[0][1]["bindings"], host)
        self.assertEqual(calls[0][1]["phases"], "phases")
        self.assertEqual(session.finished[1]["outcome"], "completed")
        self.assertTrue((self.root / session.finished[1]["result_ref"]).is_file())
        generic.assert_not_called()

    def test_one_text_prompt_has_no_project_write_workspace(self) -> None:
        path = self.root / "PROJECT_TOOLS/PUBLIC_RELEASE/pr_description_prompt.md"
        path.parent.mkdir(parents=True)
        path.write_text("Return the release arrays.")
        calls = []
        output = {"whats_new": ["new"], "whats_fixed": ["fix"], "version_history_bullets": ["summary"]}
        self.providers.implementation_agent = lambda prompt, packet: calls.append((prompt, packet)) or {
            "result": "complete", "outputs": output, "blockers": []}
        self.assertEqual(self.providers._public_release_prompt(self.root, "0.4.2", ["fix"]), output)
        self.assertEqual(len(calls), 1)
        self.assertNotEqual(Path(calls[0][1]["workspace"]), self.root)
        self.assertNotIn("permissions", calls[0][1])

    def test_incomplete_text_prompt_cannot_generate_documents(self) -> None:
        path = self.root / "PROJECT_TOOLS/PUBLIC_RELEASE/pr_description_prompt.md"
        path.parent.mkdir(parents=True)
        path.write_text("Return the release arrays.")
        self.providers.implementation_agent = lambda *_: {"result": "blocked", "outputs": {}, "blockers": ["missing evidence"]}
        with self.assertRaisesRegex(SelectedExecutionError, "did not complete"):
            self.providers._public_release_prompt(self.root, "0.4.2", ["fix"])

    def test_missing_current_admission_refuses_before_private_host_creation(self) -> None:
        selected = self.execution()
        with patch.object(selected, "_revalidate", side_effect=SelectedExecutionError("missing admission")), \
                patch.object(selected_host, "create_selected_public_bindings") as create:
            with self.assertRaisesRegex(SelectedExecutionError, "no current canonical source admission"):
                selected._execute_admitted_session(self.frozen, _Session())
        create.assert_not_called()

    def test_noncanonical_public_graph_refuses_before_private_host_creation(self) -> None:
        selected = self.execution()
        graph = copy.deepcopy(self.graph)
        graph["steps"][0]["actions"][0]["atom_id"] = "CA-O-999"
        with patch.object(selected, "_revalidate", return_value=graph), \
                patch.object(selected_host, "create_selected_public_bindings") as create:
            with self.assertRaisesRegex(SelectedExecutionError, "exact D613-selected graph"):
                selected._execute_admitted_session(self.frozen, _Session())
        create.assert_not_called()

    def test_missing_private_host_refuses_before_generic_workflow_start(self) -> None:
        selected = self.execution()
        with patch.object(selected, "_revalidate", return_value=copy.deepcopy(self.graph)), \
                patch.dict(sys.modules, {"selected_host": None}), \
                patch.object(SelectedExecution, "_execute_graph", side_effect=AssertionError("generic start")) as generic:
            with self.assertRaisesRegex(SelectedExecutionError, "private selected host is unavailable"):
                selected._execute_admitted_session(self.frozen, _Session())
        generic.assert_not_called()


if __name__ == "__main__":
    unittest.main()
