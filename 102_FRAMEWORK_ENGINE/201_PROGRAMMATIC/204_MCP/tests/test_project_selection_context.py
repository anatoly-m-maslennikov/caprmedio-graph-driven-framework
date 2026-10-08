"""Selected Project readers and the admitted gateway subprocess boundary."""
import asyncio
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

MCP = Path(__file__).resolve().parents[1]
TOOLS = MCP.parent / "201_TOOLS"
sys.path[:0] = [str(MCP), str(TOOLS), str(TOOLS / "VALIDATE_ATOMS")]

from project_selection import bind_selection, resolve_project
from atom_operations import control_root, project_identity_prefix, resolve_repository
from artifact_metadata import configured_timezone, project_identity
from authoritative_status_models import _configured_control_root
from capability_discovery.service import Service
from hot_reload import Gateway
import selected_routes
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier


class ProjectContextTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True)
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
            (control / "project_structure.toml").write_text('schema_version=1\nscope_units=[]\n')
            self.selections.append(resolve_project(root))

    def test_named_readers_use_the_bound_project_without_git(self):
        for selection in self.selections:
            with bind_selection(selection):
                self.assertEqual(selection.root, resolve_repository(selection.root))
                self.assertEqual(selection.control_root, control_root(selection.root))
                self.assertEqual(selection.control_root, Service(selection.root)._control_root())
                self.assertEqual(selection.control_root, _configured_control_root(selection.root))
                self.assertEqual(selection.settings["project"]["name"], project_identity(selection.root)["project"]["name"])
                self.assertEqual(selection.settings["artifacts"]["identity"]["project_prefix"], project_identity_prefix(selection.root))
                self.assertEqual("UTC", str(configured_timezone(selection.root)))
                self.assertEqual(selection.control_relative.as_posix() + "/_projection/selected_workflow_bindings.json",
                                 selected_routes.selected_manifest_ref(selection.root))

    def test_foreign_root_and_outside_project_source_refuse(self):
        alpha, beta = self.selections
        with bind_selection(alpha):
            for reader in (control_root, _configured_control_root, selected_routes.selected_manifest_ref):
                with self.assertRaises(ValueError):
                    reader(beta.root)
            with self.assertRaises(ValueError):
                Service(beta.root)._control_root()
            with self.assertRaises(selected_routes.SelectedRouteError):
                selected_routes._safe_path(alpha.root, "../beta/.caprmedio_beta/project_structure.toml")

    def test_wrong_project_binding_and_registry_refuse_even_with_valid_digest(self):
        selection = self.selections[0]
        with bind_selection(selection):
            registry_ref = selected_routes._selected_authority_ref(selection.root,
                selected_routes._ORIGINAL_SELECTED_SOURCE_REGISTRY_REF)
            registry = selection.root / registry_ref
            registry.parent.mkdir(parents=True)
            registry.write_bytes(b"valid registry fixture")
            freshness = {"selected_source_registry_ref": registry_ref,
                "selected_source_registry_version": 2,
                "selected_source_registry_digest": hashlib.sha256(registry.read_bytes()).hexdigest(),
                "selected_binding_ref": ".caprmedio_beta/_projection/selected_workflow_bindings.json#/routes",
                "selected_binding_digest": selected_routes.canonical_digest([])}
            manifest = {"schema_version": 1, "source_freshness": freshness,
                        "query_source_admissions": [], "routes": []}
            for field, value, message in (
                ("selected_binding_ref", freshness["selected_binding_ref"], "binding reference"),
                ("selected_source_registry_ref", selected_routes._ORIGINAL_SELECTED_SOURCE_REGISTRY_REF, "registry authority")):
                candidate = json.loads(json.dumps(manifest))
                candidate["source_freshness"][field] = value
                candidate["canonical_manifest_sha256"] = selected_routes.canonical_digest(candidate)
                with self.assertRaisesRegex(selected_routes.SelectedRouteError, message):
                    selected_routes.validate_selected_manifest_document(selection.root, candidate)

    def test_query_frontier_keeps_exact_pins_but_refuses_another_control(self):
        selection = self.selections[0]
        with bind_selection(selection):
            admitted = selected_routes._query_admission_specs(selection.root)
            self.assertEqual(selected_routes._QUERY_SOURCE_ADMISSION_SPECS[0]["workflow"]["digest"], admitted[0]["workflow"]["digest"])
            routes = [{**row, "mutation_capable": False} for row in admitted]
            with patch.object(selected_routes, "_validate_pin", side_effect=lambda root, pin: dict(pin)):
                self.assertEqual(list(admitted), selected_routes._validate_query_source_admissions(selection.root, list(admitted), routes))
                with self.assertRaisesRegex(selected_routes.SelectedRouteError, "accepted source frontier"):
                    selected_routes._validate_query_source_admissions(selection.root, list(selected_routes._QUERY_SOURCE_ADMISSION_SPECS), routes)

    def test_typed_source_admission_uses_selected_carriers_and_keeps_byte_pin(self):
        selection = self.selections[0]
        (selection.control_root / "operators_registry.toml").write_text("schema_version=1\n")
        with bind_selection(selection), patch.object(proposed_carrier, "_source", return_value={}), patch.object(proposed_carrier, "resolve_context", return_value=SimpleNamespace()), patch.object(proposed_carrier, "load_operators_registry", return_value={}):
            context = proposed_carrier.source_context_from_project(selection.root)
            self.assertEqual(selection.control_relative.as_posix(), context.inputs["control_relative"])
            self.assertEqual(1, context.inputs["structure"]["schema_version"])
        pin = {"source_path": ".caprmedio_caprmedio/fixture.md", "version": 1, "sha256": "a" * 64}
        with bind_selection(selection), patch.object(proposed_carrier, "_entry", return_value=pin), patch.object(proposed_carrier, "load_source", return_value={}) as load:
            proposed_carrier._source(selection.root, "CA-D-1", object(), {})
        self.assertEqual(selection.control_root / "fixture.md", load.call_args.args[0])
        self.assertEqual(pin["sha256"], load.call_args.args[1]["sha256"])

    def test_docker_entrypoint_forwards_only_admitted_selection_arguments(self):
        import importlib.util
        path = MCP.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/docker/entrypoint.py"
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

    async def test_gateway_child_retains_explicit_binding_and_filters_credentials(self):
        selection = self.selections[0]
        observed = {}
        class FakeGeneration:
            def __init__(self, params, fingerprint):
                observed["params"] = params
                self.ready = asyncio.get_running_loop().create_future()
                self.ready.set_result(None)
                self.tools = []
            async def close(self):
                pass
        gateway = Gateway(selection.root, selection=selection)
        self.assertEqual(selection.reload_state, gateway.storage)
        self.assertNotEqual(gateway.storage, Gateway(self.selections[1].root, selection=self.selections[1]).storage)
        with patch("hot_reload.Generation", FakeGeneration), patch.object(gateway, "fingerprint", return_value="fixed"), patch.dict(os.environ, {"CAPRMEDIO_MCP_HTTP_SECRET_TOKEN": "private"}):
            await gateway.prepare("fixed")
        args = observed["params"].args
        for flag, value in (("--project-root", str(selection.root)), ("--control-root", selection.control_relative.as_posix()),
                            ("--instance-id", selection.instance_id), ("--host-project-root", str(selection.host_root))):
            self.assertEqual(value, args[args.index(flag) + 1])
        self.assertNotIn("CAPRMEDIO_MCP_HTTP_SECRET_TOKEN", observed["params"].env)


if __name__ == "__main__":
    unittest.main()
