"""Direct Project-local Release MCP route contract."""
from __future__ import annotations

import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


MCP = Path(__file__).resolve().parents[1]
PROJECT = MCP.parents[2]
if str(MCP) not in sys.path:
    sys.path.insert(0, str(MCP))
TOOLS = MCP.parent / "201_TOOLS"
for directory in (TOOLS, TOOLS / "VALIDATE_ATOMS"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))
from selected_routes import register_selected_routes  # noqa: E402
from capability_discovery.service import Query, Service  # noqa: E402


class _Annotations:
    def __init__(self, **values: object) -> None:
        self.values = values


class _Server:
    def __init__(self) -> None:
        self.tools: dict[str, object] = {}
        self.annotations: dict[str, _Annotations] = {}

    def tool(self, *, name: str, structured_output: bool, annotations: _Annotations):
        del structured_output

        def decorate(function):
            self.tools[name] = function
            self.annotations[name] = annotations
            return function

        return decorate


class SimpleLocalReleaseRouteTest(unittest.TestCase):
    def register(self) -> tuple[_Server, object]:
        server = _Server()
        mcp = types.ModuleType("mcp")
        mcp_types = types.ModuleType("mcp.types")
        mcp_types.ToolAnnotations = _Annotations
        mcp.types = mcp_types
        with patch.dict(sys.modules, {"mcp": mcp, "mcp.types": mcp_types}), \
                patch("selected_routes.load_selected_manifest", side_effect=ValueError("ordinary admission unavailable")):
            adapter = register_selected_routes(server, PROJECT)
        return server, adapter

    def test_direct_routes_are_registered_without_old_admission(self) -> None:
        server, adapter = self.register()
        self.assertIn("release_version", server.tools)
        self.assertIn("release_version", adapter.public_route_names)
        self.assertIn("public.release", adapter.public_route_names)
        self.assertNotIn("recover_selected_release", server.tools)
        self.assertTrue(server.annotations["release_version"].values["destructive_hint"])
        self.assertFalse(server.annotations["release_version"].values["idempotent_hint"])

    def test_rejects_foreign_root_without_loading_a_release_runner(self) -> None:
        server, _adapter = self.register()
        foreign = server.tools["release_version"]({"project_root": str(MCP.parents[1]), "run_id": "local-release-3"})
        sealed = server.tools["release_version"]({
            "project_root": str(PROJECT), "run_id": "local-release-4", "mode": "preview"})
        self.assertEqual("failed", foreign["outcome"])
        self.assertIn("does not match", foreign["diagnostics"][0])
        self.assertEqual("failed", sealed["outcome"])
        self.assertIn("only project_root and run_id", sealed["diagnostics"][0])

    def test_routes_forward_run_id_to_the_concrete_entrypoints(self) -> None:
        server, _adapter = self.register()
        loader = types.SimpleNamespace(exec_module=lambda _module: None)
        local_spec = types.SimpleNamespace(name="fixture_local_release", loader=loader)
        public_spec = types.SimpleNamespace(name="fixture_public_release", loader=loader)
        local_module = types.SimpleNamespace(run_local_release=Mock(return_value={"outcome": "completed"}))
        public_module = types.SimpleNamespace(run_public_release=Mock(return_value={"outcome": "completed"}))
        journal_events: list[dict] = []
        def event_record(**values):
            return {**values, "event_id": f"event-{len(journal_events)}"}
        def append_record(_root, record):
            journal_events.append(record)
        with patch("selected_routes.importlib.util.spec_from_file_location", side_effect=(local_spec, public_spec)), \
                patch("selected_routes.importlib.util.module_from_spec", side_effect=(local_module, public_module)), \
                patch("work_journal.event_record", side_effect=event_record), \
                patch("work_journal.append_record", side_effect=append_record):
            local = server.tools["release_version"]({"project_root": str(PROJECT), "run_id": "local-release-1"})
            public = server.tools["public.release"]({
                "project_root": str(PROJECT), "run_id": "public-release-1",
                "content_draft": {"description": "new", "summary": ["history"]},
            })
        local_module.run_local_release.assert_called_once_with(PROJECT, run_id="local-release-1")
        public_module.run_public_release.assert_called_once_with(
            PROJECT, run_id="public-release-1", content_draft={"description": "new", "summary": ["history"]})
        self.assertEqual("completed", local["outcome"])
        self.assertEqual("completed", public["outcome"])
        self.assertEqual(["started", "completed", "started", "completed"], [event["event"] for event in journal_events])
        self.assertEqual("event-0", journal_events[1]["preceding_event"])
        self.assertEqual("event-2", journal_events[3]["preceding_event"])

    def test_terminal_journal_failure_is_distinct_from_the_release_outcome(self) -> None:
        server, _adapter = self.register()
        loader = types.SimpleNamespace(exec_module=lambda _module: None)
        spec = types.SimpleNamespace(name="fixture_local_release", loader=loader)
        module = types.SimpleNamespace(run_local_release=Mock(return_value={"outcome": "completed"}))
        with patch("selected_routes.importlib.util.spec_from_file_location", return_value=spec), \
                patch("selected_routes.importlib.util.module_from_spec", return_value=module), \
                patch("work_journal.event_record", side_effect=lambda **values: {**values, "event_id": "started"}), \
                patch("work_journal.append_record", side_effect=(None, OSError("journal unavailable"))):
            result = server.tools["release_version"]({"project_root": str(PROJECT), "run_id": "local-release-5"})
        self.assertEqual("completed", result["outcome"])
        self.assertIn("journal unavailable", result["recording_error"])

    def test_public_release_prompts_once_without_a_draft(self) -> None:
        server, _adapter = self.register()
        prompt = server.tools["public.release"]({"project_root": str(PROJECT), "run_id": "public-release-1"})
        self.assertEqual("input_required", prompt["outcome"])
        self.assertIn("content_draft", prompt["prompt"])

    def test_unknown_fields_and_invalid_draft_never_load_runner(self) -> None:
        server, _adapter = self.register()
        with patch("selected_routes._direct_release_call", side_effect=AssertionError("runner called")):
            for route, extra in (("release_version", {"runner": "foreign"}),
                                 ("public.release", {"content_draft": {"description": "body", "summary": [], "apply": True}})):
                result = server.tools[route]({"project_root": str(PROJECT), "run_id": "refused", **extra})
                self.assertEqual("failed", result["outcome"])

    def test_start_journal_failure_does_not_prevent_actual_release(self) -> None:
        server, _adapter = self.register()
        with patch("selected_routes._direct_release_call", return_value={"outcome": "completed"}) as runner, \
                patch("work_journal.append_record", side_effect=OSError("journal unavailable")):
            result = server.tools["release_version"]({"project_root": str(PROJECT), "run_id": "local-release-6"})
        runner.assert_called_once()
        self.assertEqual("completed", result["outcome"])
        self.assertIn("journal unavailable", result["recording_error"])

    def test_fixed_project_runner_is_loaded_and_symlink_parent_refuses(self) -> None:
        from selected_routes import _direct_release_call
        with tempfile.TemporaryDirectory(dir=PROJECT / ".caprmedio_tmp/tests") as directory:
            root = Path(directory).resolve()
            source = root / "PROJECT_TOOLS/RELEASE_VERSION/local_release.py"
            source.parent.mkdir(parents=True)
            source.write_text('def run_local_release(root, *, run_id):\n    return {"outcome": "completed", "observed": str(root), "run_id": run_id}\n')
            request = {"project_root": str(root), "run_id": "fixed-runner"}
            self.assertEqual(str(root), _direct_release_call(root, "release_version", request)["observed"])
            source.parent.rename(source.parent.with_name("original"))
            source.parent.symlink_to("original", target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "symlink"):
                _direct_release_call(root, "release_version", request)

    def test_admitted_host_root_maps_only_to_bound_local_project(self) -> None:
        server, _adapter = self.register()
        host_root = Path("/host/selected/project")
        with patch("selected_routes.bound_selection", return_value=types.SimpleNamespace(host_root=host_root)), \
                patch("selected_routes._direct_release_call", return_value={"outcome": "completed"}) as runner, \
                patch("work_journal.append_record"):
            result = server.tools["release_version"]({"project_root": str(host_root), "run_id": "host-release"})
        self.assertEqual("completed", result["outcome"])
        self.assertEqual(PROJECT, runner.call_args.args[0])

    def test_runner_failure_is_preserved_when_journal_also_fails(self) -> None:
        server, _adapter = self.register()
        with patch("selected_routes._direct_release_call", return_value={"outcome": "failed", "diagnostics": ["tests failed"]}), \
                patch("work_journal.append_record", side_effect=OSError("journal unavailable")):
            result = server.tools["release_version"]({"project_root": str(PROJECT), "run_id": "failed-release"})
        self.assertEqual("failed", result["outcome"])
        self.assertEqual(["tests failed"], result["diagnostics"])
        self.assertIn("journal unavailable", result["recording_error"])

    def test_existing_discovery_and_context_expose_direct_routes_without_a_manifest(self) -> None:
        service = Service.__new__(Service)
        service.exposed = {"release_version", "public.release"}
        service.root = PROJECT
        issues: list[str] = []
        with patch("selected_routes.load_selected_manifest", side_effect=ValueError("legacy manifest unavailable")):
            rows = service._admitted_selected_route_tools(issues)
        service.catalog = lambda: ({}, rows, issues)
        operations = service.discover(Query(query="release", limit=10), operations=True)
        self.assertEqual(["public.release", "release_version"], [row["name"] for row in operations["matches"]])
        context = service.context(types.SimpleNamespace(id="public.release"))
        request = context["input_schema"]["properties"]["request"]
        self.assertEqual(["request"], context["input_schema"]["required"])
        draft = request["properties"]["content_draft"]
        self.assertEqual(["description", "summary"], draft["required"])
        self.assertEqual({"type": "array", "items": {"type": "string"}}, draft["properties"]["summary"])
        self.assertEqual("public.release", context["definition"]["id"])
        self.assertNotIn("definition_manifest", context["definition"])



if __name__ == "__main__":
    unittest.main()
