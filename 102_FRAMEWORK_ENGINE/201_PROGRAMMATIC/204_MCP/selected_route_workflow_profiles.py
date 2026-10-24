"""MCP adapter for the canonical reviewed O016 version profiles."""

# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431

from __future__ import annotations

from collections.abc import Mapping
import sys
from pathlib import Path


def _workflow_profile(value: object) -> str | None:
    """Load the WFO-owned version map without relying on MCP import order."""

    app = Path(__file__).resolve().parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"
    if str(app) not in sys.path:
        sys.path.insert(0, str(app))
    from shared_context_validation_sources import workflow_version_profile

    return workflow_version_profile(value)


def is_direct_integrated_version(value: object) -> bool:
    """Whether one explicitly reviewed O016 revision uses direct Methods."""

    return _workflow_profile(value) == "direct_methods"


def workflow_version(route: object) -> object:
    """Return the O016 revision carried by one selected route, if present."""

    if not isinstance(route, Mapping):
        return None
    workflow = route.get("workflow")
    return workflow.get("version") if isinstance(workflow, Mapping) else None


def is_current_integrated_execute(route: object, request: object) -> bool:
    """Keep reviewed direct O016 and unknown revisions on the strict path."""

    if not isinstance(route, Mapping) or not isinstance(request, Mapping):
        return False
    workflow = route.get("workflow")
    if not (
        request.get("mode") == "execute"
        and route.get("entry_step") == "CA-O-231"
        and isinstance(workflow, Mapping)
        and workflow.get("atom_id") == "CA-O-016"
    ):
        return False
    version = workflow.get("version")
    # Unknown O016 revisions must be rejected by the strict path rather than
    # silently entering the legacy queue fallback.
    return is_direct_integrated_version(version) or _workflow_profile(version) is None


__all__ = [
    "is_current_integrated_execute",
    "is_direct_integrated_version",
    "workflow_version",
]
