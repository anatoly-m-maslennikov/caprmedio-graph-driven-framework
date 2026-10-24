"""Static schema and route names for the selected MCP projection."""

from __future__ import annotations

import json
import re
from pathlib import Path

from pydantic import ConfigDict
from typing_extensions import NotRequired, TypedDict


DEFAULT_CONTROL_ROOT = Path(".caprmedio_caprmedio")
MANIFEST_FILENAME = "selected_workflow_bindings.json"
PROJECT_SETTINGS_REF = DEFAULT_CONTROL_ROOT / "caprmedio_project_settings.toml"
ORIGINAL_SELECTED_ROUTE_NAMES = (
    "create_atom",
    "update_atom",
    "replace_atom",
    "change_atom_status",
    "create_scope_unit",
    "rename_scope_unit",
    "move_scope_unit",
    "remove_scope_unit",
    "run_implementation_workflow",
    "revert_changes",
    "build_entities_graph",
    "build_terms_graph",
    "build_applicable_methodology",
)
QUERY_ROUTE_NAMES = ("find_and_fetch_artifacts", "find_and_fetch_journal_events")
SELECTED_ROUTE_NAMES = (*ORIGINAL_SELECTED_ROUTE_NAMES, *QUERY_ROUTE_NAMES)
OPTIONAL_SELECTED_ROUTE_NAMES = ("move_atom",)
ADMITTED_SELECTED_ROUTE_NAMES = (
    *ORIGINAL_SELECTED_ROUTE_NAMES[:4],
    *OPTIONAL_SELECTED_ROUTE_NAMES,
    *ORIGINAL_SELECTED_ROUTE_NAMES[4:],
    *QUERY_ROUTE_NAMES,
)
_OPTIONAL_RELEASE_ROUTE_NAME = "release_version"
_OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME = "public.release"


class DirectLocalReleaseRequest(TypedDict):
    __pydantic_config__ = ConfigDict(extra="forbid", strict=True)  # type: ignore[misc]
    project_root: str
    run_id: str


class DirectReleaseDraft(TypedDict):
    __pydantic_config__ = ConfigDict(extra="forbid", strict=True)  # type: ignore[misc]
    description: str
    summary: list[str]


class DirectPublicReleaseRequest(DirectLocalReleaseRequest):
    content_draft: NotRequired[DirectReleaseDraft]


_DIGEST = re.compile(r"^[0-9a-f]{64}$")
_ATOM_ID = re.compile(r"^CA-[A-Z]+-[0-9]+$")
_REQUEST_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")
_FRESHNESS_FIELDS = {
    "selected_source_registry_ref",
    "selected_source_registry_version",
    "selected_source_registry_digest",
    "selected_binding_ref",
    "selected_binding_digest",
}
_ORIGINAL_SELECTED_SOURCE_REGISTRY_REF = (
    ".caprmedio_caprmedio/02_analysis/"
    "CA-A-1142-ANALYSIS_RPRT--prepare-the-selected-source-to-rmed-handoff.md"
)
_QUERY_SOURCE_ADMISSION_FIELDS = {
    "route",
    "acceptance_frontier",
    "workflow",
    "ordered_steps",
    "ordered_actions",
}
_QUERY_SOURCE_ADMISSION_SPECS = tuple(
    json.loads(
        (Path(__file__).with_name("selected_route_query_admission_specs.json")).read_text(
            encoding="utf-8"
        )
    )
)


class SelectedRouteError(ValueError):
    """A rejected MCP projection request or stale source binding."""
