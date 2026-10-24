"""Reusable request and execute fixtures for selected error-boundary tests."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
import sys
from typing import Any, NoReturn, Protocol, cast

TOOLS = Path(__file__).resolve().parents[3] / "201_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from workflow_run_support import RunExecutionSession, RunTracker, _canonical_digest  # noqa: E402


FIXTURE_JOURNAL_CONTEXT = {"author": "fixture", "timezone": "UTC"}


class _TrackerFactory(Protocol):
    def __call__(
        self,
        root: Path,
        *,
        source_observer: Callable[[dict[str, Any]], Mapping[str, Any]],
        executor: Callable[[dict[str, Any], RunExecutionSession], NoReturn],
        journal_context: Mapping[str, str],
    ) -> RunTracker: ...


def make_tracker(
    root: Path,
    executor: Callable[[dict[str, Any], RunExecutionSession], NoReturn],
) -> RunTracker:
    """Create the lazy tracker with complete Journal metadata for fixtures."""
    factory = cast(_TrackerFactory, RunTracker)
    return factory(
        root,
        source_observer=lambda _request: {
            "selected": True,
            "current": True,
            "observed": {"fixture": "current"},
        },
        executor=executor,
        journal_context=FIXTURE_JOURNAL_CONTEXT,
    )


def build_request(request_id: str = "selected-error") -> dict[str, object]:
    """Build the common valid request used by every boundary case."""
    parameters = {"value": "bounded"}
    frontier = ["target.md"]
    effects = [{"type": "write", "target": "target.md"}]
    return {
        "request_id": request_id,
        "operation_route": "fixture.route",
        "parameters": parameters,
        "parameters_digest": _canonical_digest(parameters),
        "target_frontier": frontier,
        "target_frontier_digest": _canonical_digest(frontier),
        "effects": effects,
        "effects_digest": _canonical_digest(effects),
        "definition_manifest": {"manifest_ref": "manifest.json", "manifest_digest": "a" * 64},
        "source_freshness": {
            "selected_source_registry_ref": "registry.json",
            "selected_source_registry_version": 1,
            "selected_source_registry_digest": "b" * 64,
            "selected_binding_ref": "binding.json",
            "selected_binding_digest": "c" * 64,
        },
        "initiative": {
            "initiative_id": "initiative",
            "instruction_summary": "exercise failure",
        },
        "requested_runs": [
            {
                "requested_run_id": "workflow",
                "kind": "workflow",
                "definition": {
                    "atom_id": "W",
                    "version": 1,
                    "path": "workflow.md",
                    "digest": "d" * 64,
                },
            }
        ],
    }


def execute_request(tracker: RunTracker, request: dict[str, object]) -> dict[str, Any]:
    """Promote a valid preview into the exact execute request."""
    preview = tracker.run_selected_operation(request)
    execute = {
        **request,
        "mode": "execute",
        "proposal_receipt": preview["proposal_receipt"],
        "proposal_receipt_digest": preview["proposal_receipt_digest"],
        "assigned_action_id": "A",
        "operator_authorization": {
            "authorization_ref": "authorization.json",
            "authorization_freshness": {"state": "current", "digest": "e" * 64},
            "request_id": request["request_id"],
            "operation_route": request["operation_route"],
            "proposal_receipt_digest": preview["proposal_receipt_digest"],
            "parameters_digest": request["parameters_digest"],
            "target_frontier_digest": request["target_frontier_digest"],
            "effects_digest": request["effects_digest"],
            "definition_manifest": request["definition_manifest"],
            "source_freshness": request["source_freshness"],
        },
    }
    return tracker.run_selected_operation(execute)


__all__ = ["FIXTURE_JOURNAL_CONTEXT", "build_request", "execute_request", "make_tracker"]
