"""Selected Project readers and the admitted gateway subprocess boundary."""
# ruff: noqa: E402
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

MCP = Path(__file__).resolve().parents[1]
ROOT = MCP.parents[2]
TOOLS = MCP.parent / "FEATURE_TOOLS"
sys.path[:0] = [str(MCP), str(TOOLS)]

from project_selection import bind_selection, resolve_project
from artifact_metadata import configured_timezone, project_identity
from project_settings_values import control_root
from scope_declaration_test_support import write_scope_unit_declarations


class ProjectContextTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=tempfile.gettempdir(), ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.selections = []
        for name in ("alpha", "beta"):
            root = self.base / name
            control = root / (".caprmedio_" + name)
            control.mkdir(parents=True)
            (control / "caprmedio_project_settings.toml").write_text(
                f'[project]\nname="{name}"\nkey="{name}"\nrepository_slug="{name}"\n'
                f'[paths]\ncontrol_root=".caprmedio_{name}"\n'
                f'[artifacts.identity]\nproject_prefix="{name.upper()}"\n'
                '[artifact_timestamps]\ntimezone="UTC"\n')
            write_scope_unit_declarations(root, control_root=control)
            self.selections.append(resolve_project(root))

    def test_named_readers_use_the_bound_project_without_git(self):
        for selection in self.selections:
            with bind_selection(selection):
                self.assertEqual(selection.control_root, control_root(selection.root))
                self.assertEqual(selection.settings["project"]["name"], project_identity(selection.root)["project"]["name"])
                self.assertEqual("UTC", str(configured_timezone(selection.root)))

    def test_runtime_namespace_properties_are_selected_and_read_only(self):
        for selection in self.selections:
            runtime = selection.root / ".caprmedio_runtime/runtime"
            self.assertEqual(runtime / "project_mcp" / selection.instance_id, selection.launcher_state)
            self.assertFalse(runtime.exists())
            self.assertFalse((selection.root / ".caprmedio_install").exists())


    def test_foreign_root_and_outside_project_source_refuse(self):
        alpha, beta = self.selections
        with bind_selection(alpha):
            with self.assertRaises(ValueError):
                control_root(beta.root)

    def test_docker_entrypoint_forwards_only_admitted_selection_arguments(self):
        import importlib.util
        path = MCP / "docker/entrypoint.py"
        specification = importlib.util.spec_from_file_location("project_selection_entrypoint", path)
        entrypoint = importlib.util.module_from_spec(specification)
        specification.loader.exec_module(entrypoint)
        selection = self.selections[0]
        values = {"CAPRMEDIO_CONTROL_ROOT": selection.control_relative.as_posix(),
                  "CAPRMEDIO_PROJECT_INSTANCE_ID": selection.instance_id,
                  "CAPRMEDIO_HOST_PROJECT_ROOT": str(selection.host_root),
                  "CAPRMEDIO_MCP_HTTP_SECRET_TOKEN": "private"}
        with patch.object(sys, "argv", ["entrypoint", "mcp-http"]), patch.dict(os.environ, values), patch.object(os, "execv") as execute:
            entrypoint.main()
        arguments = execute.call_args.args[1]
        self.assertEqual(selection.control_relative.as_posix(), arguments[arguments.index("--control-root") + 1])
        self.assertEqual(selection.instance_id, arguments[arguments.index("--instance-id") + 1])
        self.assertNotIn("private", arguments)



if __name__ == "__main__":
    unittest.main()
