# CA-E-796@2
"""Retained Revert behavior after AI Agent runtime retirement."""

from __future__ import annotations
import copy
from pathlib import Path
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
REPOSITORY = APP.parents[3]
TOOLS = APP.parents[1] / "FEATURE_TOOLS"
REVERT = TOOLS / "WORKFLOW_OPERATIONS/REVERT_CHANGES"
PROMPTS = (
    REPOSITORY
    / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_AGENTIC/FEATURE_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW"
)
for path in (
    APP,
    APP / "tests",
    TOOLS,
    REVERT,
    REVERT / "tests",
    PROMPTS,
    TOOLS.parent / "FEATURE_MCP/tests",
):
    sys.path.insert(0, str(path))
import backend  # noqa: E402
import lifecycle_intents  # noqa: E402
import test_native_revert_provider as revert_fixture  # noqa: E402
from native_revert_provider import make_native_revert_service  # noqa: E402
from selected_execution import SelectedExecution, build_requested_runs  # noqa: E402
from selected_native_providers import SelectedNativeProviders  # noqa: E402
from selected_workflows_docker_fixture import GoldenCase, GoldenProject, W10_LIFECYCLE_TIMESTAMP  # noqa: E402
from test_selected_routes_mcp import copy_complete_selected_guard_fixture  # noqa: E402


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


class Session:
    """One lazy selected lineage; repeated bridge access reuses the Action."""

    def __init__(self):
        self.started = {}
        self.finished = []

    def start_run(self, requested):
        return self.started.setdefault(requested, {"run_id": f"actual-{len(self.started) + 1}"})

    def finish_run(self, run_id, **result):
        row = {"run_id": run_id, "disposition": "terminal", **result}
        self.finished.append(row)
        return row


class CurrentProviderGoldenProject(GoldenProject):
    def _copy_reviewed_manifest(self):
        settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        prior = settings.read_bytes()
        try:
            return copy_complete_selected_guard_fixture(self.root)
        finally:
            settings.write_bytes(prior)


class SelectedNativeProvidersTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.project = CurrentProviderGoldenProject(
            REPOSITORY, self.root, GoldenCase("W10", "revert_changes")
        )
        self.manifest = self.project.prepare()

    def freeze(self, route, parameters, run_id="native-selected"):
        execution = {
            "mode": "execute",
            "operation_route": route,
            "workflow_run_id": run_id,
            "parameters": parameters,
            "source_freshness": self.manifest["source_freshness"],
            "definition_manifest": {
                "manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
                "manifest_digest": self.manifest["canonical_manifest_sha256"],
            },
        }
        selected = SelectedExecution(self.root)
        graph = selected._validate_graph(execution)
        execution["requested_runs"] = build_requested_runs(
            graph, run_id, parameters.get("run_visit_limits")
        )
        return selected.freeze(
            {"operation": "enqueue_selected", "run_id": run_id, "execution": execution}
        )

    def registered_dispatch(self, frozen):
        providers = SelectedNativeProviders(self.root)
        dbos = RegisteredDBOS()
        engine = type("Engine", (), {"root": self.root})()
        backend.register_execution(dbos, engine, selected_providers=providers)
        session = Session()

        def execute_selected(_root, handlers, saved, **_kwargs):
            from selected_graph_executor import execute_graph

            return execute_graph(self.root, handlers, saved, session)

        with patch("selected_dispatch_state.shared_dispatch", side_effect=execute_selected):
            result = dbos.workflows[backend.SELECTED_WORKFLOW](frozen["request"]["run_id"])
        return result, session

    def lifecycle_request(self):
        request = copy.deepcopy(
            self.project.native_revert_parameters()["approved_reversal_manifest"]["request"]
        )
        target = request["ordered_effects"][0]["capability_binding"]["target"]
        path = self.root / target["path"]
        return request, path, path.read_bytes()

    def legacy_manifest(self, request):
        """Model a retained pre-repair packet; current admission must reject it."""
        service = make_native_revert_service(
            {"project_root": str(self.root), "approved_reversal_request": request}
        )
        admitted = service.admit(request)
        self.assertEqual("blocked", admitted["outcome"])
        return {
            "manifest_id": "reversal-" + revert_fixture.canonical_digest(request)[:24],
            "request": request,
            "admitted_target_hashes": request["current_hashes"],
        }

    def test_registered_synthetic_lifecycle_revert_with_unbound_evidence_is_blocked(self):
        request, path, before = self.lifecycle_request()
        request["operator_decision"]["evidence_hash"] = "0" * 64
        prior = path.read_bytes()
        frozen = self.freeze(
            "revert_changes", {"approved_reversal_manifest": self.legacy_manifest(request)}
        )
        result, session = self.registered_dispatch(frozen)
        self.assertEqual("interrupted_pending", result["outcome"])
        self.assertEqual(prior, path.read_bytes())
        self.assertEqual(3, len(session.started))
        self.assertEqual(3, len(session.finished))
        self.assertEqual("blocked", result["step_results"][0]["result"])

    def test_registered_current_lifecycle_revert_performs_exact_effect_once(self):
        with patch.object(
            lifecycle_intents, "current_timestamp", return_value=W10_LIFECYCLE_TIMESTAMP
        ):
            request, path, before = self.lifecycle_request()
            service = make_native_revert_service(
                {"project_root": str(self.root), "approved_reversal_request": request}
            )
            admitted = service.admit(request)
            self.assertEqual("admitted", admitted["outcome"])
            frozen = self.freeze(
                "revert_changes",
                {"approved_reversal_manifest": admitted["approved_reversal_manifest"]},
            )
            result, session = self.registered_dispatch(frozen)
        self.assertEqual("completed", result["outcome"])
        self.assertEqual("reverted", result["step_results"][0]["result"])
        self.assertNotEqual(before, path.read_bytes())
        self.assertIn(b"Reverted detail.", path.read_bytes())
        self.assertEqual(3, len(session.started))
        self.assertEqual(3, len(session.finished))

    def test_registered_synthetic_lifecycle_revert_forecast_is_blocked_without_effect(self):
        helper = revert_fixture.NativeRevertProviderTests()
        target_path = self.project._authority_dir / "CA-R-100--target.md"
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as forecast_raw:
            forecast = Path(forecast_raw)
            (forecast / ".git").mkdir()
            control = forecast / ".caprmedio_caprmedio"
            control.mkdir()
            (control / "caprmedio_project_settings.toml").write_text(
                (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").read_text(),
                encoding="utf-8",
            )
            forecast_path = forecast / target_path.relative_to(self.root)
            forecast_path.parent.mkdir(parents=True, exist_ok=True)
            forecast_path.write_bytes(target_path.read_bytes())
            with patch.object(
                lifecycle_intents, "current_timestamp", return_value="2026-10-05 12:00:00 +0000"
            ):
                lifecycle_intents.update_atom_action(
                    forecast,
                    {
                        "target": lifecycle_intents.carrier_descriptor(forecast, "CA-R-100"),
                        "proposed": helper._proposal(forecast_path),
                        "change_class": "semantic_revision",
                    },
                    execute=True,
                    authorized=True,
                )
                target = lifecycle_intents.carrier_descriptor(self.root, "CA-R-100")
                effect = {
                    "effect_id": "lifecycle",
                    "target_id": "atom:CA-R-100",
                    "expected_before": "version 1",
                    "expected_after": "version 2",
                    "expected_current_hash": revert_fixture.canonical_digest(target),
                    "expected_result_hash": revert_fixture.normalized_carrier_result_hash(
                        forecast, "CA-R-100"
                    ),
                    "before_evidence": "before:lifecycle",
                    "after_evidence": "after:lifecycle",
                    "capability_binding": helper._binding(
                        "lifecycle.update_atom",
                        {
                            "target": target,
                            "proposed": helper._proposal(target_path),
                            "change_class": "semantic_revision",
                        },
                        target,
                        before="before:lifecycle",
                        after="after:lifecycle",
                    ),
                }
                request = helper._request(effect, effect["expected_current_hash"])
                frozen = self.freeze(
                    "revert_changes", {"approved_reversal_manifest": self.legacy_manifest(request)}
                )
                result, session = self.registered_dispatch(frozen)
        self.assertEqual("interrupted_pending", result["outcome"])
        self.assertNotIn("Semantic reversal detail.", target_path.read_text())
        self.assertIn("Stable summary", target_path.read_text())
        self.assertFalse(list(target_path.parent.rglob("CA-R-100--target@1.md")))
        self.assertEqual(3, len(session.finished))

    def test_unsupported_and_denied_revert_are_truthful_without_effects(self):
        for capability, granted in (
            ("file.write", True),
            ("structure.rollback_scope_unit_change", False),
        ):
            with self.subTest(capability=capability, granted=granted):
                request, path, before = self.lifecycle_request()
                binding = request["ordered_effects"][0]["capability_binding"]
                binding["capability_id"] = capability
                binding["permission_evidence"].update(capability_id=capability, granted=granted)
                frozen = self.freeze(
                    "revert_changes",
                    {"approved_reversal_manifest": {"request": request}},
                    run_id=f"denied-{granted}",
                )
                prior = path.read_bytes()
                result, _ = self.registered_dispatch(frozen)
                self.assertEqual("interrupted_pending", result["outcome"])
                self.assertEqual(prior, path.read_bytes())
                self.assertEqual("blocked", result["step_results"][0]["result"])

    def test_real_dbos_queue_executes_native_revert(self):
        from dbos import DBOS
        from contracts import Status

        _, url = backend.database(self.root)
        DBOS(
            config={
                "name": backend.APPLICATION,
                "system_database_url": url,
                "run_admin_server": False,
                "enable_otlp": False,
                "application_version": backend.APP_VERSION,
            }
        )
        session = Session()

        def execute_selected(_root, handlers, saved, **_kwargs):
            from selected_graph_executor import execute_graph

            return execute_graph(self.root, handlers, saved, session)

        try:
            backend.register_execution(DBOS, type("Engine", (), {"root": self.root})())
            DBOS.launch()
            DBOS.register_queue(backend.QUEUE, worker_concurrency=1, polling_interval_sec=0.1)
            with (
                patch.object(
                    lifecycle_intents, "current_timestamp", return_value=W10_LIFECYCLE_TIMESTAMP
                ),
                patch("selected_dispatch_state.shared_dispatch", side_effect=execute_selected),
            ):
                request, path, before = self.lifecycle_request()
                service = make_native_revert_service(
                    {"project_root": str(self.root), "approved_reversal_request": request}
                )
                admitted = service.admit(request)
                self.assertEqual("admitted", admitted["outcome"])
                frozen = self.freeze(
                    "revert_changes",
                    {"approved_reversal_manifest": admitted["approved_reversal_manifest"]},
                )
                queued = backend.enqueue_selected(self.root, frozen["request"])
                self.assertEqual("queued", queued["outcome"])
                deadline = time.monotonic() + 60
                observed = {}
                while time.monotonic() < deadline:
                    observed = backend.status(self.root, Status(run_id=frozen["request"]["run_id"]))
                    if observed.get("scheduler_status") in {"SUCCESS", "ERROR", "CANCELLED"}:
                        break
                    time.sleep(0.1)
                self.assertEqual("SUCCESS", observed.get("scheduler_status"), observed)
                self.assertEqual("completed", observed.get("outcome"), observed)
                self.assertNotEqual(before, path.read_bytes())
                self.assertIn(b"Reverted detail.", path.read_bytes())
        finally:
            DBOS.destroy()
