"""Golden contracts for source-bound selected Workflow queue execution."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
REPOSITORY = APP.parents[3]
PROMPTS = REPOSITORY / "102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW"
MCP = REPOSITORY / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP"
TOOLS = REPOSITORY / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"
for location in (APP, PROMPTS, MCP, MCP / "tests", TOOLS, TOOLS / "tests"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_execution import (  # noqa: E402
    SelectedExecution,
    SelectedExecutionError,
    build_requested_runs,
    canonical_json,
    manifest_relative_path,
    make_revert_action_handler,
)
from selected_routes import SELECTED_ROUTE_NAMES  # noqa: E402
from test_selected_routes_mcp import copy_complete_selected_guard_fixture  # noqa: E402


def digest(value: object) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


class SelectedExecutionTests(unittest.TestCase):
    """Interpreter units isolate registry admission; they do not prove it.

    Actual whole-document admission is covered without mocks in
    test_selected_full_registry_guard.py, not by this minimal graph fixture.
    """

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (self.root / ".git").mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\njournal_root = ".caprmedio_caprmedio/_journal"\n', encoding="utf-8"
        )
        self.manifest_path = control / "_projection/selected_workflow_bindings.json"
        self._write_definitions()
        self._write_manifest()
        if getattr(self, "isolate_registry_admission", True):
            actual_loader = SelectedExecution._load_manifest

            def unit_manifest_loader(queue, execution):
                if queue.root != self.root.resolve():
                    return actual_loader(queue, execution)
                reference = execution["definition_manifest"]["manifest_ref"]
                path = queue._safe_path(reference)
                if path.relative_to(queue.root).as_posix() != manifest_relative_path(queue.root):
                    raise SelectedExecutionError("selected definition manifest location is not admitted")
                manifest = json.loads(path.read_text())
                observed = digest(queue._manifest_without_digest(manifest))
                if manifest.get("canonical_manifest_sha256") != observed or execution["definition_manifest"]["manifest_digest"] != observed:
                    raise SelectedExecutionError("selected definition manifest digest is stale or invalid")
                return manifest, reference, observed

            isolation = patch.object(SelectedExecution, "_load_manifest", autospec=True, side_effect=unit_manifest_loader)
            isolation.start()
            self.addCleanup(isolation.stop)

    def _write_definitions(self) -> None:
        for name, atom_id in (("workflow.md", "CA-O-127"), ("step-one.md", "CA-O-129"),
                              ("step-two.md", "CA-O-130"), ("action-one.md", "CA-O-128"),
                              ("action-two.md", "CA-O-131")):
            self._write_definition(name, atom_id)

    def _write_definition(self, name: str, atom_id: str) -> None:
        path = self.root / "definitions" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f"---\natom_id: {atom_id}\nversion: 1\nstatus: Active\n---\n# Summary\nFixture\n",
            encoding="utf-8",
        )

    def _binding(self, name: str, atom_id: str, kind: str) -> dict[str, object]:
        path = self.root / "definitions" / name
        return {
            "atom_id": atom_id,
            "kind": kind,
            "version": 1,
            "path": path.relative_to(self.root).as_posix(),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }

    def _write_manifest(self) -> None:
        first = self._binding("action-one.md", "CA-O-128", "action")
        second = self._binding("action-two.md", "CA-O-131", "action")
        self._replace_route_steps([
            {
                **self._binding("step-one.md", "CA-O-129", "step"),
                "actions": [first],
                "on_result": [{"result": "prepared", "next": "CA-O-130"}],
            },
            {
                **self._binding("step-two.md", "CA-O-130", "step"),
                "actions": [second],
                "on_result": [{"result": "completed", "terminal": "completed"}],
            },
        ])

    def _replace_route_steps(self, steps: list[dict[str, object]]) -> None:
        value = {
            "routes": [
                {
                    "route": "create_atom",
                    "workflow": self._binding("workflow.md", "CA-O-127", "workflow"),
                    "steps": steps,
                }
            ]
        }
        value["canonical_manifest_sha256"] = digest(value)
        self.manifest_path.parent.mkdir(parents=True, exist_ok=True)
        self.manifest_path.write_text(json.dumps(value), encoding="utf-8")

    def _refresh_execute_seal(self, request: dict[str, object]) -> None:
        """Rebind the fixture preview/authorization after declared input changes."""
        execution = request["execution"]
        assert isinstance(execution, dict)
        execution["parameters_digest"] = digest(execution["parameters"])
        source_freshness = execution["source_freshness"]
        definition_manifest = execution["definition_manifest"]
        proposal = {
            "request_id": execution["request_id"],
            "operation_route": execution["operation_route"],
            "initiative_ref": execution["initiative"]["initiative_ref"],
            "source_freshness": {
                "declared": source_freshness,
                "observed": {
                    "manifest_ref": definition_manifest["manifest_ref"],
                    "manifest_digest": definition_manifest["manifest_digest"],
                },
                "selected": True,
                "current": True,
            },
            "parameters_digest": execution["parameters_digest"],
            "target_frontier_digest": execution["target_frontier_digest"],
            "effects_digest": execution["effects_digest"],
            "definition_manifest": definition_manifest,
        }
        execution["proposal_receipt"] = proposal
        execution["proposal_receipt_digest"] = digest(proposal)
        authorization = execution["operator_authorization"]
        assert isinstance(authorization, dict)
        authorization["proposal_receipt_digest"] = execution["proposal_receipt_digest"]
        authorization["parameters_digest"] = execution["parameters_digest"]

    def _freeze_with_planned_runs(self, request: dict[str, object], handlers: dict[str, object]) -> tuple[SelectedExecution, dict[str, object]]:
        execution = request["execution"]
        assert isinstance(execution, dict)
        runner = self.executor(handlers)
        graph = runner._validate_graph(execution)
        parameters = execution.get("parameters")
        limits = parameters.get("run_visit_limits") if isinstance(parameters, dict) else None
        execution["requested_runs"] = build_requested_runs(graph, request["run_id"], limits)
        self._refresh_execute_seal(request)
        return runner, runner.freeze(request)

    def request(self, run_id: str = "selected-run") -> dict[str, object]:
        manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        manifest_ref = self.manifest_path.relative_to(self.root).as_posix()
        definition_manifest = {
            "manifest_ref": manifest_ref,
            "manifest_digest": manifest["canonical_manifest_sha256"],
        }
        source_freshness = {
            "selected_source_registry_ref": "selected/registry.json",
            "selected_source_registry_version": 1,
            "selected_source_registry_digest": "a" * 64,
            "selected_binding_ref": "selected/create-atom.json",
            "selected_binding_digest": "b" * 64,
        }
        requested_runs = [
            {
                "requested_run_id": run_id,
                "kind": "workflow",
                "definition": {**{key: manifest["routes"][0]["workflow"][key] for key in ("atom_id", "version", "path")},
                               "digest": manifest["routes"][0]["workflow"]["sha256"]},
            }
        ]
        for ordinal, step in enumerate(manifest["routes"][0]["steps"], start=1):
            step_run_id = f"{run_id}:step:{ordinal}"
            requested_runs.append({
                "requested_run_id": step_run_id,
                "kind": "step",
                "definition": {**{key: step[key] for key in ("atom_id", "version", "path")}, "digest": step["sha256"]},
                "parent_requested_run_id": run_id,
            })
            for action_ordinal, action in enumerate(step["actions"], start=1):
                requested_runs.append({
                    "requested_run_id": f"{step_run_id}:action:{action_ordinal}",
                    "kind": "action",
                    "definition": {**{key: action[key] for key in ("atom_id", "version", "path")}, "digest": action["sha256"]},
                    "parent_requested_run_id": step_run_id,
                })
        parameters = {"fixture": True}
        target_frontier = ["definitions/workflow.md"]
        effects = [{"type": "create", "target": "results/fixture.md"}]
        execution = {
            "mode": "execute",
            "request_id": "request-1",
            "operation_route": "create_atom",
            "parameters": parameters,
            "parameters_digest": digest(parameters),
            "target_frontier": target_frontier,
            "target_frontier_digest": digest(target_frontier),
            "effects": effects,
            "effects_digest": digest(effects),
            "definition_manifest": definition_manifest,
            "source_freshness": source_freshness,
            "initiative": {"initiative_id": "initiative-1", "instruction_summary": "fixture",
                           "initiative_ref": "definitions/workflow.md"},
            "requested_runs": requested_runs,
        }
        observed = {"manifest_ref": manifest_ref,
                    "manifest_digest": manifest["canonical_manifest_sha256"]}
        proposal = {
            "request_id": execution["request_id"],
            "operation_route": execution["operation_route"],
            "initiative_ref": execution["initiative"]["initiative_ref"],
            "source_freshness": {"declared": source_freshness, "observed": observed,
                                  "selected": True, "current": True},
            "parameters_digest": execution["parameters_digest"],
            "target_frontier_digest": execution["target_frontier_digest"],
            "effects_digest": execution["effects_digest"],
            "definition_manifest": definition_manifest,
        }
        proposal_digest = digest(proposal)
        execution.update({
            "proposal_receipt": proposal,
            "proposal_receipt_digest": proposal_digest,
            "assigned_action_id": "fixture-assignment",
            "operator_authorization": {
                "authorization_ref": "authorizations/fixture.json",
                "authorization_freshness": {"state": "current", "digest": "d" * 64},
                "request_id": execution["request_id"],
                "operation_route": execution["operation_route"],
                "proposal_receipt_digest": proposal_digest,
                "parameters_digest": execution["parameters_digest"],
                "target_frontier_digest": execution["target_frontier_digest"],
                "effects_digest": execution["effects_digest"],
                "definition_manifest": definition_manifest,
                "source_freshness": source_freshness,
            },
        })
        return {
            "operation": "enqueue_selected",
            "run_id": run_id,
            "execution": execution,
        }

    def executor(self, handlers: dict[str, object]) -> SelectedExecution:
        return SelectedExecution(self.root, handlers=handlers)

    @staticmethod
    def current_manifest_request(
        route_name: str, run_id: str, *, root: Path = REPOSITORY,
    ) -> tuple[SelectedExecution, dict[str, object]]:
        """Use the generic physical portfolio."""
        manifest_path = root / ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        execution: dict[str, object] = {
            "mode": "execute", "operation_route": route_name, "workflow_run_id": run_id,
            "source_freshness": manifest["source_freshness"],
            "definition_manifest": {
                "manifest_ref": manifest_path.relative_to(root).as_posix(),
                "manifest_digest": manifest["canonical_manifest_sha256"],
            },
        }
        selected = SelectedExecution(root)
        graph = selected._validate_graph(execution)
        execution["requested_runs"] = build_requested_runs(graph, run_id)
        return selected, {"operation": "enqueue_selected", "run_id": run_id, "execution": execution}

    def _current_d547_fixture(self) -> tuple[Path, dict[str, object]]:
        """Copy the current fifteen-route sources into a disposable portfolio."""
        fixture_root = self.root / "current-d547"
        manifest = copy_complete_selected_guard_fixture(fixture_root)
        self.assertEqual([row["route"] for row in manifest["routes"]], list(SELECTED_ROUTE_NAMES))
        for route_name, step_id, action_id in (
            ("build_entities_graph", "CA-O-135", "CA-O-134"),
            ("build_terms_graph", "CA-O-138", "CA-O-137"),
        ):
            route = next(row for row in manifest["routes"] if row["route"] == route_name)
            self.assertEqual(
                [(row["step"]["atom_id"], row["action"]["atom_id"])
                 for row in route["ordered_steps"]],
                [(step_id, action_id)],
            )
            self.assertEqual([pin["atom_id"] for pin in route["ordered_actions"]], [action_id])
            self.assertEqual(route["native_action_calls"], [])
            self.assertEqual(route["on_result"], [])
        return fixture_root, manifest

    @staticmethod
    def session(frozen: dict[str, object]) -> object:
        """A lazy tracker mock: graph nodes create actual Run IDs only on entry."""
        requested = {row["requested_run_id"]: row for row in frozen["request"]["execution"]["requested_runs"]}

        class Session:
            def __init__(self) -> None:
                self.actual: dict[str, dict[str, object]] = {}
                self.finished: list[dict[str, object]] = []

            def start_run(self, requested_run_id: str) -> dict[str, object]:
                if requested_run_id not in self.actual:
                    row = requested[requested_run_id]
                    self.actual[requested_run_id] = {
                        "run_id": f"actual-{len(self.actual) + 1}", "kind": row["kind"],
                        "definition": row["definition"],
                    }
                return dict(self.actual[requested_run_id])

            def finish_run(self, run_id: str, **result: object) -> dict[str, object]:
                value = {"run_id": run_id, **result}
                self.finished.append(value)
                return value

        return Session()

    def test_freeze_rejects_a_stale_manifest_before_any_dispatch(self) -> None:
        request = self.request()
        request["execution"]["definition_manifest"]["manifest_digest"] = "0" * 64

        with self.assertRaisesRegex(SelectedExecutionError, "manifest"):
            self.executor({}).freeze(request)
        self.assertFalse((self.root / ".caprmedio_install/workflow_orchestrator/runs/selected-run").exists())

    def test_manifest_path_resolves_configured_control_root(self) -> None:
        configured = self.root / ".caprmedio_selected"
        configured.mkdir()
        (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_selected"\n', encoding="utf-8"
        )

        self.assertEqual(
            ".caprmedio_selected/_projection/selected_workflow_bindings.json",
            manifest_relative_path(self.root),
        )

    def test_interprets_source_graph_with_distinct_workflow_step_and_action_runs(self) -> None:
        calls: list[dict[str, object]] = []

        def first(context: dict[str, object]) -> dict[str, object]:
            calls.append(context)
            return {"result": "prepared", "effects": []}

        def second(context: dict[str, object]) -> dict[str, object]:
            calls.append(context)
            return {"result": "completed", "effects": []}

        execution = self.executor({"CA-O-128": first, "CA-O-131": second})
        frozen = execution.freeze(self.request())
        result = execution.dispatch(
            frozen, run_support=lambda _root, _request, graph: graph(self.session(frozen))
        )

        self.assertEqual(result["outcome"], "completed")
        self.assertEqual([row["action_definition_id"] for row in calls], ["CA-O-128", "CA-O-131"])
        for row in calls:
            self.assertNotEqual(row["workflow_run_id"], row["step_run_id"])
            self.assertNotEqual(row["step_run_id"], row["action_run_id"])
        saved = json.loads((execution.run_directory("selected-run") / "accepted.json").read_text())
        self.assertEqual(saved["result"]["workflow_run_id"], "actual-1")

    def test_shared_run_support_records_actual_workflow_step_and_action_runs(self) -> None:
        execution = self.executor({
            "CA-O-128": lambda _context: {"result": "prepared", "effect_refs": []},
            "CA-O-131": lambda _context: {"result": "completed", "effect_refs": []},
        })
        frozen = execution.freeze(self.request())
        result = execution.dispatch(frozen)

        self.assertEqual(result["disposition"], "terminal")
        self.assertEqual({row["outcome"] for row in result["terminal_runs"]}, {"completed"})
        self.assertEqual(len(result["run_ids"]), 5)
        self.assertEqual(len(set(result["run_ids"])), 5)
        journal = next((self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson"))
        events = [json.loads(line) for line in journal.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(events), 10)
        self.assertEqual({event["run"]["kind"] for event in events}, {"workflow", "step", "action"})

    def test_mcp_preview_receipt_is_accepted_by_real_worker_dispatch(self) -> None:
        sys.path.insert(0, str(APP.parents[1] / "204_MCP"))
        from selected_routes import _QueueBackedSelectedSupport

        request = self.request("mcp-preview-worker")
        execution_request = request["execution"]
        manifest = json.loads(self.manifest_path.read_text())
        manifest["manifest_ref"] = execution_request["definition_manifest"]["manifest_ref"]
        manifest["source_freshness"] = execution_request["source_freshness"]
        preview_request = {key: value for key, value in execution_request.items()
                           if key not in {"proposal_receipt", "proposal_receipt_digest",
                                          "assigned_action_id", "operator_authorization", "requested_runs"}}
        preview_request["mode"] = "preview"
        with patch("selected_routes.load_selected_manifest", return_value=manifest):
            preview = _QueueBackedSelectedSupport(self.root, None)._tracker().run_selected_operation(preview_request)
        execution_request["proposal_receipt"] = preview["proposal_receipt"]
        execution_request["proposal_receipt_digest"] = preview["proposal_receipt_digest"]
        execution_request["operator_authorization"]["proposal_receipt_digest"] = preview["proposal_receipt_digest"]
        runner = self.executor({
            "CA-O-128": lambda _context: {"result": "prepared", "effect_refs": []},
            "CA-O-131": lambda _context: {"result": "completed", "effect_refs": []},
        })
        result = runner.dispatch(runner.freeze(request))

        self.assertEqual(result["disposition"], "terminal", result)
        self.assertEqual({row["outcome"] for row in result["terminal_runs"]}, {"completed"})

    def test_dispatch_rechecks_definition_bindings_after_queue_admission(self) -> None:
        execution = self.executor({"CA-O-128": lambda _context: {"result": "prepared"}})
        frozen = execution.freeze(self.request())
        (self.root / "definitions/action-one.md").write_text("changed", encoding="utf-8")

        with self.assertRaisesRegex(SelectedExecutionError, "definition"):
            execution.dispatch(frozen, run_support=lambda _root, _request, graph: graph(self.session(frozen)))
        self.assertFalse((execution.run_directory("selected-run") / "dispatch-intent.json").exists())

    def test_uncertain_dispatch_intent_never_replays_an_action(self) -> None:
        calls: list[dict[str, object]] = []
        execution = self.executor({"CA-O-128": lambda context: calls.append(context) or {"result": "prepared"}})
        frozen = execution.freeze(self.request())
        intent = execution.run_directory("selected-run") / "dispatch-intent.json"
        intent.write_text(json.dumps({"state": "started"}), encoding="utf-8")

        result = execution.dispatch(
            frozen, run_support=lambda _root, _request, graph: graph(self.session(frozen))
        )
        self.assertEqual(result["disposition"], "recording_pending")
        self.assertEqual(result["outcome"], "interrupted_pending")
        self.assertEqual(calls, [])

    def test_undeclared_action_never_becomes_a_transition(self) -> None:
        execution = self.executor({"CA-O-128": lambda _context: {"result": "invented"}})
        frozen = execution.freeze(self.request())

        result = execution.dispatch(
            frozen, run_support=lambda _root, _request, graph: graph(self.session(frozen))
        )
        self.assertEqual(result["disposition"], "recording_pending")
        self.assertEqual(result["outcome"], "interrupted_pending")

    def test_current_d547_manifest_verifies_all_admitted_routes(self) -> None:
        """Exercise the physical producer schema through its resealed test corpus."""
        fixture_root, manifest = self._current_d547_fixture()
        manifest_path = fixture_root / ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json"
        executor = SelectedExecution(fixture_root)
        accepted: set[str] = set()
        routes = manifest["routes"]
        for route in routes:
            execution = {
                "mode": "execute", "operation_route": route["route"],
                "source_freshness": manifest["source_freshness"],
                "definition_manifest": {
                    "manifest_ref": manifest_path.relative_to(fixture_root).as_posix(),
                    "manifest_digest": manifest["canonical_manifest_sha256"],
                },
            }
            try:
                graph = executor._validate_graph(execution)
            except SelectedExecutionError as error:
                self.fail(f"{route['route']} D547 binding was refused: {error}")
            else:
                accepted.add(graph["route"])
        self.assertEqual(
            [route["route"] for route in routes],
            list(SELECTED_ROUTE_NAMES),
        )
        self.assertEqual(len(accepted), 15)
        self.assertEqual(accepted, {route["route"] for route in routes})
        self.assertIn("run_implementation_workflow", accepted)
        self.assertIn("build_applicable_methodology", accepted)

    def test_current_d547_all_admitted_routes_pass_prequeue_freeze_validation(self) -> None:
        fixture_root, manifest = self._current_d547_fixture()
        frozen_routes: set[str] = set()
        routes = manifest["routes"]
        for ordinal, route in enumerate(routes, start=1):
            selected, request = self.current_manifest_request(
                route["route"], f"current-freeze-{ordinal}", root=fixture_root,
            )
            frozen = selected._validated_freeze(request)
            frozen_routes.add(frozen["graph"]["route"])
        self.assertEqual(frozen_routes, {route["route"] for route in routes})

    def test_current_d547_generic_routes_have_builtin_handlers(self) -> None:
        fixture_root, manifest = self._current_d547_fixture()
        generic = manifest["routes"]
        self.assertEqual([route["route"] for route in generic], list(SELECTED_ROUTE_NAMES))
        generic_actions = {
            entry["action"]["atom_id"]
            for route in generic
            for entry in route["ordered_steps"]
        }
        builtin = SelectedExecution(fixture_root).handlers
        self.assertFalse(generic_actions - set(builtin))
        self.assertIn("CA-O-131", builtin)

    def test_current_d547_update_graph_uses_only_actual_bound_nodes(self) -> None:
        fixture_root, _manifest = self._current_d547_fixture()
        selected, request = self.current_manifest_request("update_atom", "current-update", root=fixture_root)
        calls: list[str] = []
        runner = self.executor({
            "CA-O-067": lambda context: calls.append(context["action_definition_id"]) or {
                "result": "identity-preserving", "effect_refs": [],
            },
            "CA-O-128": lambda context: calls.append(context["action_definition_id"]) or {
                "result": "applied", "terminal_outcome": "completed", "effect_refs": [],
            },
        })
        frozen = {"request": request, "graph": selected._validate_graph(request["execution"])}
        result = runner._execute_graph(frozen, self.session(frozen))

        self.assertEqual(calls, ["CA-O-067", "CA-O-128"])
        self.assertEqual(result["outcome"], "completed")
        self.assertEqual(len(result["step_results"]), 2)

    def test_update_atom_legacy_mapping_runs_o067_assessment_then_o128_effect(self) -> None:
        """Run the real selected route for the explicit legacy R793 mapping."""
        from test_selected_atom_lifecycle import SelectedAtomLifecycleTest
        from test_selected_creation_execution import _Session

        lifecycle_fixture = SelectedAtomLifecycleTest(
            "test_explicit_legacy_r793_header_maps_with_exact_history_and_ignores_noncurrent_copies"
        )
        lifecycle_fixture.setUp()
        self.addCleanup(lifecycle_fixture.tearDown)
        root = lifecycle_fixture.root
        manifest = copy_complete_selected_guard_fixture(root)
        parameters, source, destination, before = lifecycle_fixture._explicit_legacy_r793()

        selected = SelectedExecution(root)
        execution = {
            "mode": "execute", "operation_route": "update_atom",
            "workflow_run_id": "legacy-r793-run001", "request_id": "legacy-r793-request",
            "parameters": parameters, "source_freshness": manifest["source_freshness"],
            "definition_manifest": {
                "manifest_ref": manifest["manifest_ref"],
                "manifest_digest": manifest["canonical_manifest_sha256"],
            },
        }
        graph = selected._validate_graph(execution)
        execution["requested_runs"] = build_requested_runs(graph, "legacy-r793-run001")
        frozen = {
            "request": {"run_id": "legacy-r793-run001", "execution": execution},
            "graph": graph,
        }
        session = _Session(execution["requested_runs"])
        result = selected._execute_graph(frozen, session)

        self.assertEqual("completed", result["outcome"])
        self.assertEqual(
            ["identity-preserving", "applied"],
            [row["result"] for row in result["step_results"]],
        )
        assessment_run = next(
            row["requested_run_id"] for row in execution["requested_runs"]
            if row["kind"] == "action" and row["definition"]["atom_id"] == "CA-O-067"
        )
        assessment_receipt = session.terminal[assessment_run]
        self.assertEqual("completed", assessment_receipt["outcome"])
        assessment_payload = json.loads((root / assessment_receipt["result_ref"]).read_text(encoding="utf-8"))
        self.assertEqual("identity-preserving", assessment_payload["result"])
        self.assertIsNotNone(assessment_payload["native_result"].get("assessment_evidence"))

        effect_run = next(
            row["requested_run_id"] for row in execution["requested_runs"]
            if row["kind"] == "action" and row["definition"]["atom_id"] == "CA-O-128"
        )
        effect_receipt = session.terminal[effect_run]
        effect_payload = json.loads((root / effect_receipt["result_ref"]).read_text(encoding="utf-8"))
        prior_revision = effect_payload["native_result"]["history"]["prior_revision"]
        self.assertEqual(before, (root / prior_revision["path"]).read_bytes())

        self.assertFalse(source.exists())
        self.assertTrue(destination.exists())
        destination_text = destination.read_text(encoding="utf-8")
        self.assertIn('atom_id: "CA-R-793"', destination_text)
        self.assertIn("version: 23", destination_text)
        from atom_operations import frontmatter_scalar, split_frontmatter

        before_frontmatter, before_body = split_frontmatter(before.decode("utf-8"))
        after_frontmatter, after_body = split_frontmatter(destination_text)
        self.assertEqual(before_body, after_body)
        for field in (
            "content_role", "current_scope_unit", "claim_target_scope_unit", "local_tier",
            "global_tier", "author", "status", "subjects", "relations",
        ):
            self.assertEqual(frontmatter_scalar(before_frontmatter, field),
                             frontmatter_scalar(after_frontmatter, field), field)
        effect_refs = set(result["effect_refs"])
        self.assertIn(destination.relative_to(root).as_posix(), effect_refs)

    def test_move_atom_uses_the_canonical_lifecycle_handler(self) -> None:
        expected = {"operation": "move", "outcome": "preview", "effects": []}
        with patch("lifecycle_intents.move_atom_action", return_value=expected) as move:
            selected = SelectedExecution(self.root)
            result = selected.handlers["CA-O-128"]({
                "route": "move_atom",
                "parameters": {
                    "target": {"path": "source.md"},
                    "placement": {
                        "destination_path": "destination.md",
                        "owning_scope_unit": "CORE",
                        "claim_target_scope_unit": "CORE",
                    },
                },
            })

        self.assertEqual(result["result"], "preview")
        move.assert_called_once_with(
            selected.root,
            {
                "target": {"path": "source.md"},
                "placement": {
                    "destination_path": "destination.md",
                    "owning_scope_unit": "CORE",
                    "claim_target_scope_unit": "CORE",
                },
            },
            execute=True,
            authorized=True,
        )

    def test_o016_selects_manifest_step_packets_and_carries_actual_prior_results(self) -> None:
        """Exercise all seven real prompt handlers through their injected Agent."""
        import implementation_actions
        from frozen_selected_workflows import frozen_implementation_bindings, write_frozen_source

        fixture_root, _manifest = self._current_d547_fixture()
        selected, request = self.current_manifest_request(
            "run_implementation_workflow", "current-o016", root=fixture_root,
        )
        # Use the checked-in frozen implementation corpus, whose paths match
        # the reviewed binding hint used by this fixture.  This keeps the
        # disposable Project self-contained without copying moved live bytes
        # or manufacturing project configuration to force ID lookup.
        sources = frozen_implementation_bindings()
        for binding in sources:
            write_frozen_source(self.root, binding["path"], binding["sha256"])
        self.assertEqual(implementation_actions.current_source_bindings(self.root), sources)
        execution = request["execution"]
        assert isinstance(execution, dict)
        execution["request_id"] = "current-o016"
        execution["initiative"] = {
            "initiative_id": "implementation-o016",
            "instruction_summary": "current implementation fixture",
            "initiative_ref": execution["definition_manifest"]["manifest_ref"],
        }
        execution["operator_authorization"] = {
            "authorization_ref": "authorizations/current-o016.json",
            "authorization_freshness": {
                "state": "current", "digest": execution["definition_manifest"]["manifest_digest"]},
            "request_id": "current-o016", "operation_route": "run_implementation_workflow",
            "proposal_receipt_digest": "b" * 64,
            "parameters_digest": "c" * 64,
            "target_frontier_digest": "d" * 64,
            "effects_digest": "e" * 64,
            "definition_manifest": execution["definition_manifest"],
            "source_freshness": execution["source_freshness"],
        }
        method_paths = [row["path"] for row in sources
                        if row["atom_id"].startswith("CA-M-")]
        projection = implementation_actions.prepare_method_projection(method_paths, self.root)
        workspace = self.root / "implementation-workspace"
        workspace.mkdir()
        workspace = workspace.resolve()
        calls: list[dict[str, object]] = []
        evaluation_calls = 0
        entry_calls = 0

        def agent(_prompt: str, packet: dict[str, object]) -> dict[str, object]:
            nonlocal entry_calls, evaluation_calls
            calls.append(packet)
            step = packet["step_marker"]
            outputs: dict[str, object] = {}
            if step == "CA-O-091":
                entry_calls += 1
                entry_results = (
                    "evaluation_ready", "requirement_ready", "evaluation_runnable",
                    "evaluation_runnable", "complete",
                )
                try:
                    result = entry_results[entry_calls - 1]
                except IndexError as error:
                    raise AssertionError("fixture exceeded its declared CA-O-091 visits") from error
                return {"result": result, "outputs": outputs, "evidence": [f"evidence:{step}"]}
            if step == "CA-O-092":
                outputs = {"golden_e2e": ["test"], "commands": ["test"], "expected_outcomes": ["pass"]}
            elif step == "CA-O-093":
                outputs = {"candidate": "fixture", "phase": packet["phase"], "changed_paths": ["fixture.py"]}
            elif step == "CA-O-094":
                evaluation_calls += 1
                if evaluation_calls == 1:
                    return {"result": "failed", "outputs": {"commands": ["test"],
                                                                  "checks": [{"returncode": 1}]},
                            "evidence": ["failure"]}
                outputs = {"candidate": "fixture", "commands": ["test"],
                           "checks": [{"returncode": 0}],
                           "coverage": {"complete": True, "checked": ["CA-E-563"]}}
            elif step == "CA-O-095":
                outputs = {"cause": "fixture assertion failed"}
            elif step == "CA-O-096":
                outputs = {"decision": "retry admitted", "limit_provenance": "fixture settings", "consumed": 0}
            elif step == "CA-O-099":
                outputs = {"candidate": "fixture", "changed_paths": ["fixture.py"],
                           "phase": packet["phase"], "recheck_commands": ["test"], "issue_evidence": ["failure"],
                           "regression_evidence": ["recheck"]}
            results = {"CA-O-091": "evaluation_ready", "CA-O-092": "prepared", "CA-O-093": "implemented",
                       "CA-O-094": "passed", "CA-O-095": "implementation_defect", "CA-O-096": "retry_permitted",
                       "CA-O-099": "repaired"}
            return {"result": results[step], "outputs": outputs, "evidence": [f"evidence:{step}"]}

        base = {
            "selected_project": {
                "kind": "selected_project",
                "source_root": ".caprmedio_caprmedio",
                "source_references": sources,
            },
            "source_bindings": sources,
            "permissions": {"allowed": True, "implementation_workspace": {
                "kind": "disposable_workspace", "path": str(workspace), "allow_write": True,
            }, "retry": {"authorization_ref": execution["operator_authorization"]["authorization_ref"],
                         "source_ref": ".caprmedio_caprmedio/caprmedio_project_settings.toml",
                         "task_ref": execution["workflow_run_id"],
                         "epic_ref": execution["definition_manifest"]["manifest_ref"]}},
            "workspace": str(workspace), "method_projection": projection,
            "requirements": implementation_actions.prepare_input_bindings(["CA-R-1843"], self.root),
            "delivery": implementation_actions.prepare_input_bindings(["CA-D-544"], self.root),
            "evaluations": implementation_actions.prepare_input_bindings(["CA-E-563"], self.root),
            "red": {"expectation": "fixture assertion passes", "fixtures": ["fixture.py"],
                    "commands": ["test"], "scope": "selected implementation item"},
            "plan_item": {"plan_id": "current-o016-plan", "item_id": "current-o016-item",
                          "dod": ["implementation checks pass"], "owned_paths": ["."],
                          "estimated_minutes": 1}, "owned_paths": ["."],
            "candidate": "fixture", "phase": "implementation", "handoff_complete": True,
            "golden_e2e": ["test"], "baseline_command": "test",
            "confidence": {"observed": 1.0, "effective": 0.9,
                            "source": ".caprmedio_caprmedio/caprmedio_project_settings.toml"},
            "retry": {"consumed": 0, "effective_limit": 1,
                      "source": ".caprmedio_caprmedio/caprmedio_project_settings.toml",
                      "remaining_failure": True, "admitted": True},
            "coverage": {"required": ["CA-E-563"], "checked": [], "complete": False,
                         "candidate": "fixture", "phase": "implementation"},
            "operator_authorization": execution["operator_authorization"],
            "retained_state": {"run": "fixture"},
        }
        execution["parameters"] = {
            "base_packet": base,
            "run_visit_limits": {"CA-O-091": 5, "CA-O-094": 2},
            "step_packets": {
                step: {"context": context, "step_marker": step}
                for step, (_action, context) in implementation_actions.ACTION_BY_STEP.items()
            },
        }
        # This is an executable fixture: writes from the implementation run
        # belong in its disposable Project, never in the source checkout.
        runner = SelectedExecution(self.root, implementation_agent=agent)
        graph = selected._validate_graph(execution)
        execution["requested_runs"] = build_requested_runs(
            graph, "current-o016", {"CA-O-091": 5, "CA-O-094": 2},
        )
        frozen = {"request": request, "graph": graph}

        class RevisitSession:
            def __init__(self) -> None:
                self.started: dict[str, dict[str, object]] = {}
                self.finished: list[dict[str, object]] = []

            def start_run(self, requested_run_id: str) -> dict[str, object]:
                if requested_run_id not in self.started:
                    self.started[requested_run_id] = {"run_id": f"actual-{len(self.started) + 1}"}
                return dict(self.started[requested_run_id])

            def finish_run(self, run_id: str, **result: object) -> dict[str, object]:
                value = {"run_id": run_id, **result}
                self.finished.append(value)
                return value

        result = runner._execute_graph(frozen, RevisitSession())

        self.assertEqual(result["outcome"], "completed")
        self.assertEqual([packet["step_marker"] for packet in calls],
                         ["CA-O-091", "CA-O-092", "CA-O-091", "CA-O-093", "CA-O-091", "CA-O-094",
                          "CA-O-095", "CA-O-096", "CA-O-099", "CA-O-091", "CA-O-094", "CA-O-091"])
        self.assertEqual([packet["context"] for packet in calls],
                         ["Integrated", "Isolated", "Integrated", "Isolated", "Integrated", "Integrated",
                          "Isolated", "Integrated", "Isolated", "Integrated", "Integrated", "Integrated"])
        self.assertEqual(calls[1]["prior_results"][0]["step_definition_id"], "CA-O-091")
        self.assertEqual(calls[6]["prior_results"][-1]["result"], "failed")

    def test_o016_rejects_missing_or_mismatched_step_packet(self) -> None:
        fixture_root, _manifest = self._current_d547_fixture()
        selected, request = self.current_manifest_request(
            "run_implementation_workflow", "current-o016-missing", root=fixture_root,
        )
        request["execution"]["parameters"] = {"base_packet": {}, "step_packets": {"CA-O-092": {"context": "Isolated"}}}
        frozen = {"request": request, "graph": selected._validate_graph(request["execution"])}

        with self.assertRaisesRegex(SelectedExecutionError, "no packet for Step CA-O-091"):
            selected._execute_graph(frozen, self.session(frozen))

    def test_shared_session_branched_skip_uses_manifest_step_identity(self) -> None:
        """A skipped manifest Step must not shift the actual Step definition."""
        self._write_definition("step-three.md", "CA-O-132")
        self._write_definition("action-three.md", "CA-O-133")
        self._replace_route_steps([
            {
                **self._binding("step-one.md", "CA-O-129", "step"),
                "actions": [self._binding("action-one.md", "CA-O-128", "action")],
                "on_result": [{"result": "branch", "next": "CA-O-132"}],
            },
            {
                **self._binding("step-two.md", "CA-O-130", "step"),
                "actions": [self._binding("action-two.md", "CA-O-131", "action")],
                "on_result": [{"result": "unused", "terminal": "completed"}],
            },
            {
                **self._binding("step-three.md", "CA-O-132", "step"),
                "actions": [self._binding("action-three.md", "CA-O-133", "action")],
                "on_result": [{"result": "completed", "terminal": "completed"}],
            },
        ])
        calls: list[str] = []
        runner, frozen = self._freeze_with_planned_runs(self.request("branched"), {
            "CA-O-128": lambda context: calls.append(context["requested_action_run_id"]) or {"result": "branch", "effect_refs": []},
            "CA-O-133": lambda context: calls.append(context["requested_action_run_id"]) or {"result": "completed", "effect_refs": []},
        })

        result = runner.dispatch(frozen)

        self.assertEqual(result["disposition"], "terminal")
        self.assertEqual(calls, ["branched:step:1:action:1", "branched:step:3:action:1"])
        self.assertIn("branched:step:3", result["run_ids"])
        self.assertNotIn("branched:step:2", result["run_ids"])
        journal = next((self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson"))
        events = [json.loads(line) for line in journal.read_text(encoding="utf-8").splitlines()]
        started = [event for event in events if event["event"] == "started"]
        third = [event for event in started if event["run"]["kind"] == "step"
                 and event["run"]["definition"]["atom_id"] == "CA-O-132"]
        self.assertEqual(len(third), 1)
        self.assertEqual(third[0]["run"]["run_id"], "branched:step:3")

    def test_shared_session_authorized_loop_uses_distinct_predeclared_visit_ids(self) -> None:
        self._replace_route_steps([
            {
                **self._binding("step-one.md", "CA-O-129", "step"),
                "actions": [self._binding("action-one.md", "CA-O-128", "action")],
                "on_result": [
                    {"result": "again", "next": "CA-O-129"},
                    {"result": "completed", "terminal": "completed"},
                ],
            },
        ])
        calls: list[str] = []

        def loop(context: dict[str, object]) -> dict[str, object]:
            calls.append(context["requested_action_run_id"])
            return {"result": "again" if len(calls) == 1 else "completed", "effect_refs": []}

        request = self.request("loop")
        request["execution"]["parameters"] = {
            "fixture": True,
            "run_visit_limits": {"CA-O-129": 2},
        }
        runner, frozen = self._freeze_with_planned_runs(request, {"CA-O-128": loop})

        result = runner.dispatch(frozen)

        self.assertEqual(result["disposition"], "terminal")
        self.assertEqual(calls, ["loop:step:1:action:1", "loop:step:1:visit:2:action:1"], result)
        self.assertIn("loop:step:1:visit:2", result["run_ids"])
        journal = next((self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson"))
        events = [json.loads(line) for line in journal.read_text(encoding="utf-8").splitlines()]
        repeated = [event for event in events if event["event"] == "started"
                    and event["run"]["run_id"] == "loop:step:1:visit:2:action:1"]
        self.assertEqual(len(repeated), 1)
        self.assertEqual(repeated[0]["run"]["definition"]["atom_id"], "CA-O-128")
        self.assertEqual(repeated[0]["run"]["parent_run_id"], "loop:step:1:visit:2")

    def test_shared_session_exhausts_unregistered_visit_before_second_effect(self) -> None:
        self._replace_route_steps([
            {
                **self._binding("step-one.md", "CA-O-129", "step"),
                "actions": [self._binding("action-one.md", "CA-O-128", "action")],
                "on_result": [{"result": "again", "next": "CA-O-129"}],
            },
        ])
        calls: list[str] = []
        runner, frozen = self._freeze_with_planned_runs(self.request("exhausted"), {
            "CA-O-128": lambda context: calls.append(context["requested_action_run_id"]) or {"result": "again", "effect_refs": []},
        })

        result = runner.dispatch(frozen)

        self.assertEqual(calls, ["exhausted:step:1:action:1"])
        self.assertEqual(result["disposition"], "started")
        self.assertNotIn("exhausted:step:1:visit:2", result["run_ids"])
        self.assertEqual(
            {row["outcome"] for row in result["terminal_runs"]},
            {"completed", "interrupted_pending"},
        )

    def test_freeze_rejects_wrong_or_stale_predeclared_run_rows(self) -> None:
        request = self.request("wrong-planned-row")
        request["execution"]["requested_runs"][1]["requested_run_id"] = "wrong-planned-row:step:9"
        with self.assertRaisesRegex(SelectedExecutionError, "requested Runs"):
            self.executor({}).freeze(request)

        stale = self.request("stale-planned-row")
        stale["execution"]["requested_runs"][1]["definition"]["digest"] = "0" * 64
        with self.assertRaisesRegex(SelectedExecutionError, "requested Runs"):
            self.executor({}).freeze(stale)

    def test_terminal_logging_failure_preserves_outcomes_without_replaying_handlers(self) -> None:
        calls: list[str] = []
        runner, frozen = self._freeze_with_planned_runs(self.request("terminal-pending"), {
            "CA-O-128": lambda context: calls.append(context["requested_action_run_id"]) or {"result": "prepared", "effect_refs": []},
            "CA-O-131": lambda context: calls.append(context["requested_action_run_id"]) or {"result": "completed", "effect_refs": []},
        })
        tools_root = APP.parents[1] / "201_TOOLS"
        sys.path.insert(0, str(tools_root))
        import work_journal

        append = work_journal.append_sealed_events

        def fail_terminal(*args: object, **kwargs: object) -> object:
            events = args[1]
            assert isinstance(events, list)
            if events[0]["event"] != "started":
                raise OSError("fixture terminal Journal failure")
            return append(*args, **kwargs)

        with patch.object(work_journal, "append_sealed_events", side_effect=fail_terminal):
            result = runner.dispatch(frozen)

        self.assertEqual("terminal", result["disposition"])
        self.assertEqual({"completed"}, {run["outcome"] for run in result["terminal_runs"]})
        self.assertEqual(5, len(result["terminal_runs"]))
        self.assertEqual(["fixture terminal Journal failure"] * 5, result["diagnostics"])
        self.assertNotIn("pending_event_ids", result)
        self.assertEqual(calls, ["terminal-pending:step:1:action:1", "terminal-pending:step:2:action:1"])
        self.assertEqual(result, runner.dispatch(frozen))
        self.assertEqual(calls, ["terminal-pending:step:1:action:1", "terminal-pending:step:2:action:1"])

    def test_revert_adapter_does_not_treat_start_as_terminal(self) -> None:
        class RevertService:
            def execute_with_session(self, *_args: object) -> dict[str, object]:
                return {
                    "outcome": "reverted", "manifest_id": "reversal-1",
                    "run_receipt_refs": [{"run_id": "started-run"}],
                    "run_error": "",
                    "effect_account": {"effects": [{"effect_id": "effect-1", "status": "completed"}]},
                }

        output = make_revert_action_handler(RevertService())({
            "parameters": {"approved_reversal_manifest": {"manifest_id": "reversal-1"}},
            "session": object(), "requested_action_run_id": "requested-run",
        })
        self.assertFalse(output["action_terminal_recorded"])
        self.assertEqual(output["terminal_outcome"], "completed")
        self.assertEqual(len(output["effect_refs"]), 1)
        self.assertEqual(output["native_result"]["run_error"], "")

    def test_revert_adapter_uses_the_existing_lazy_action_run(self) -> None:
        frozen = self.executor({}).freeze(self.request())
        session = self.session(frozen)

        class RevertService:
            def execute_with_session(self, manifest: dict[str, object], supplied_session: object,
                                     requested_action_run_id: str, _cancel: object) -> dict[str, object]:
                self.assertEqual(manifest, {"manifest_id": "reversal-1"})
                actual = supplied_session.start_run(requested_action_run_id)
                supplied_session.finish_run(actual["run_id"], outcome="completed",
                                            result_ref="results/revert.json", effect_refs=[])
                return {
                    "outcome": "reverted", "manifest_id": "reversal-1",
                    "effect_account": {"effects": [], "applied_effect_count": 0},
                    "run_receipt_refs": [{"run_id": actual["run_id"]}],
                }

            def assertEqual(self, left: object, right: object) -> None:
                if left != right:
                    raise AssertionError((left, right))

        output = make_revert_action_handler(RevertService())({
            "parameters": {"approved_reversal_manifest": {"manifest_id": "reversal-1"}},
            "session": session, "requested_action_run_id": "selected-run:step:2:action:1",
        })

        self.assertTrue(output["action_terminal_recorded"])
        self.assertEqual(output["terminal_outcome"], "completed")
        self.assertEqual(len(session.finished), 1)


if __name__ == "__main__":
    unittest.main()
