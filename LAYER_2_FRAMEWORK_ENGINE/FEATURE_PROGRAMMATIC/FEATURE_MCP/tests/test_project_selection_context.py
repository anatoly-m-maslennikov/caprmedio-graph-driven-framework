"""Selected Project readers and the admitted gateway subprocess boundary."""
# ruff: noqa: E402
import hashlib
import os
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

MCP = Path(__file__).resolve().parents[1]
ROOT = MCP.parents[2]
TOOLS = MCP.parent / "FEATURE_TOOLS"
WORKFLOW_TESTS = MCP.parent / "FEATURE_APPS" / "APP_WORKFLOW_ORCHESTRATOR" / "tests"
sys.path[:0] = [str(MCP), str(TOOLS), str(TOOLS / "VALIDATE_ATOMS"), str(WORKFLOW_TESTS)]

from project_selection import bind_selection, resolve_project
from artifact_metadata import configured_timezone, project_identity
from authoritative_status_models import _configured_control_root
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier
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
                self.assertEqual(selection.control_root, _configured_control_root(selection.root))
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
                _configured_control_root(beta.root)

    def test_typed_source_admission_uses_selected_carriers_and_keeps_byte_pin(self):
        selection = self.selections[0]
        (selection.control_root / "operators_registry.toml").write_text("schema_version=1\n")
        with bind_selection(selection), patch.object(proposed_carrier, "_source", return_value={"binding": {"atom_id": "CA-D-1"}}), patch.object(proposed_carrier, "resolve_context", return_value=SimpleNamespace()), patch.object(proposed_carrier, "load_operators_registry", return_value={}):
            context = proposed_carrier.source_context_from_project(selection.root)
            self.assertEqual(selection.control_relative.as_posix(), context.inputs["control_relative"])
            self.assertEqual(selection.root.name, context.inputs["structure"]["scope_units"][0]["scope_unit_name"])
        pin = {"source_path": ".caprmedio_caprmedio/fixture.md", "version": 1, "sha256": "a" * 64}
        path = selection.control_root / "fixture.md"
        raw = b"---\natom_id: CA-D-1\ncontent_role: Delivery\nstatus: Active\nversion: 2\n---\n# Current rule\n"
        binding = {"atom_id": "CA-D-1", "version": 2, "path": str(path),
                   "sha256": hashlib.sha256(raw).hexdigest()}
        row = {"binding": binding, "text": raw.decode(),
               "metadata": proposed_carrier.parse_carrier(raw, path).metadata}
        path.write_bytes(raw)
        with bind_selection(selection), patch.object(proposed_carrier, "_entry", return_value=pin), patch.object(proposed_carrier, "load_source", return_value=row) as load:
            observed = proposed_carrier._source(selection.root, "CA-D-1", object(), {})
        self.assertEqual(path, load.call_args.args[0])
        self.assertIsNone(load.call_args.args[1])
        self.assertEqual(binding, observed["binding"])
        reader = proposed_carrier.ReadContext(roots=[str(selection.root)], limits=dict(proposed_carrier.CEILINGS))
        report = {"bindings": {}, "coverage": {"gaps": []}}
        admitted = proposed_carrier.load_source(path, binding, reader, report)
        self.assertEqual(binding["sha256"], admitted["binding"]["sha256"])
        self.assertIsNone(proposed_carrier.load_source(
            path, {**binding, "sha256": pin["sha256"]}, reader, report))

    def test_docker_entrypoint_forwards_only_admitted_selection_arguments(self):
        import importlib.util
        path = MCP.parent / "FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker/entrypoint.py"
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
