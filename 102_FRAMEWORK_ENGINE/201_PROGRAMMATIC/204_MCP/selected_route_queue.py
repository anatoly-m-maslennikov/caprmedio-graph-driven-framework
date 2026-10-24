"""Queue-backed support for selected MCP routes."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path
from typing import Any, Mapping, cast

from selected_route_spec import SelectedRouteError


def _public_module() -> Any:
    return sys.modules.get("selected_routes")


class _QueueBackedSelectedSupport:
    """Compose shared preview support with the existing queue APP."""

    def __init__(self, root: Path, adapter: Any) -> None:
        self.root, self.adapter = root, adapter

    def _tracker(self) -> Any:
        tools = Path(__file__).resolve().parents[1] / "201_TOOLS"
        if str(tools) not in sys.path:
            sys.path.insert(0, str(tools))
        module = importlib.import_module("workflow_run_support")
        public = _public_module()

        def observe(request: dict[str, Any]) -> dict[str, Any]:
            container_lifecycle = None
            try:
                manifest = public.load_selected_manifest(self.root)
                selected = request.get("operation_route") in {
                    entry["route"] for entry in manifest["routes"]
                }
                current = (
                    dict(request.get("definition_manifest", {}))
                    == {
                        "manifest_ref": manifest["manifest_ref"],
                        "manifest_digest": manifest["canonical_manifest_sha256"],
                    }
                    and dict(request.get("source_freshness", {})) == manifest["source_freshness"]
                )
                lifecycle_admission = None
                if request.get("operation_route") == "change_atom_status":
                    app = Path(__file__).resolve().parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"
                    if str(app) not in sys.path:
                        sys.path.insert(0, str(app))
                    selected_execution = importlib.import_module("selected_execution")
                    lifecycle_admission = selected_execution.preflight_selected_lifecycle(
                        self.root, "change_atom_status", request.get("parameters")
                    )
                    admission = importlib.import_module("container_lifecycle_admission")
                    container_lifecycle = admission.seal_contained_status_changes(
                        self.root, request.get("parameters"), lifecycle_admission
                    )
            except ImportError, SelectedRouteError, TypeError, ValueError, RuntimeError:
                selected, current, lifecycle_admission, container_lifecycle = (
                    False,
                    False,
                    None,
                    None,
                )
            definition = request.get("definition_manifest")
            return {
                "selected": selected,
                "current": current,
                "observed": {
                    "manifest_ref": definition.get("manifest_ref")
                    if isinstance(definition, Mapping)
                    else None,
                    "manifest_digest": definition.get("manifest_digest")
                    if isinstance(definition, Mapping)
                    else None,
                    **(
                        {"lifecycle_admission": lifecycle_admission}
                        if lifecycle_admission is not None
                        else {}
                    ),
                    **(
                        {"container_lifecycle": container_lifecycle}
                        if container_lifecycle is not None
                        else {}
                    ),
                },
            }

        def never_execute(_request: dict[str, Any], _session: Any) -> Mapping[str, Any]:
            raise RuntimeError("MCP delegates selected execution to enqueue_selected")

        return module.RunTracker(self.root, source_observer=observe, executor=never_execute)

    @staticmethod
    def _workflow_run_id(request: Mapping[str, Any]) -> str:
        rows = request.get("requested_runs")
        if not isinstance(rows, list):
            raise SelectedRouteError("execute has no requested Workflow Run identity")
        workflow = [
            row for row in rows if isinstance(row, Mapping) and row.get("kind") == "workflow"
        ]
        if len(workflow) != 1 or not isinstance(workflow[0].get("requested_run_id"), str):
            raise SelectedRouteError("execute must carry one requested Workflow Run identity")
        return str(workflow[0]["requested_run_id"])

    def run_selected_operation(self, request: dict[str, Any]) -> dict[str, Any]:
        if request["mode"] == "preview":
            return cast(dict[str, Any], self._tracker().run_selected_operation(request))
        preview = {
            key: value
            for key, value in request.items()
            if key
            not in {
                "proposal_receipt",
                "proposal_receipt_digest",
                "assigned_action_id",
                "operator_authorization",
                "requested_runs",
            }
        }
        preview["mode"] = "preview"
        prepared = self._tracker().run_selected_operation(preview)
        if (
            prepared.get("disposition") != "preview"
            or request.get("proposal_receipt") != prepared.get("proposal_receipt")
            or request.get("proposal_receipt_digest") != prepared.get("proposal_receipt_digest")
        ):
            return {
                "request_id": request["request_id"],
                "disposition": "blocked",
                "outcome": "blocked",
                "source_freshness": prepared.get("source_freshness"),
                "diagnostics": ["exact current preview receipt is required before enqueue"],
            }
        try:
            app = Path(__file__).resolve().parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"
            if str(app) not in sys.path:
                sys.path.insert(0, str(app))
            orchestrator = importlib.import_module("orchestrator")
            return cast(
                dict[str, Any],
                orchestrator.run(
                    self.root,
                    {
                        "operation": "enqueue_selected",
                        "run_id": self._workflow_run_id(request),
                        "execution": request,
                    },
                ),
            )
        except (ImportError, SelectedRouteError, ValueError, RuntimeError, OSError) as error:
            return {
                "request_id": request["request_id"],
                "disposition": "blocked",
                "outcome": "blocked",
                "source_freshness": prepared.get("source_freshness"),
                "diagnostics": [f"enqueue_selected did not admit the exact request: {error}"],
            }

    def get_selected_workflow_run(self, request: dict[str, Any]) -> dict[str, Any]:
        try:
            app = Path(__file__).resolve().parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"
            if str(app) not in sys.path:
                sys.path.insert(0, str(app))
            observed = importlib.import_module("orchestrator").run(
                self.root, {"operation": "status", "run_id": request["run_id"]}
            )
            if not isinstance(observed, Mapping):
                raise ValueError("selected Run observation returned an invalid result")
            from selected_route_interactive import _public_pending

            return _public_pending(observed)
        except (ImportError, ValueError, RuntimeError, OSError) as error:
            return {
                "disposition": "blocked",
                "outcome": "blocked",
                "diagnostics": [f"selected Run observation unavailable: {error}"],
            }

    def get_selected_action_run(self, request: dict[str, Any]) -> dict[str, Any]:
        try:
            app = Path(__file__).resolve().parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"
            if str(app) not in sys.path:
                sys.path.insert(0, str(app))
            observer = importlib.import_module("selected_action_observation")
            return cast(
                dict[str, Any],
                observer.observe_selected_action(self.root, request["action_run_id"]),
            )
        except (ImportError, ValueError, RuntimeError, OSError) as error:
            return {
                "action_run_id": request["action_run_id"],
                "disposition": "blocked",
                "outcome": "blocked",
                "diagnostics": [f"selected Action observation is unavailable: {error}"],
            }
