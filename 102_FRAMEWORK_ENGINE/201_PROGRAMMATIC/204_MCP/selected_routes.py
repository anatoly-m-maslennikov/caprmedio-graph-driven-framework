"""Closed selected-Workflow MCP projection; execution remains in shared support.

The implementation is split by responsibility, while this module keeps the
historic import surface used by MCP callers and tests.
"""

from __future__ import annotations

import importlib  # noqa: F401 - retained as a patch point for release tests
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "201_TOOLS"))

from project_selection import bound_selection  # noqa: F401 - retained as a patch point
import selected_route_adapter as _route_adapter
import selected_route_manifest as _route_manifest
import selected_route_queue as _route_queue
import selected_route_registration as _route_registration
import selected_route_release as _route_release
import selected_route_spec as _route_spec
import selected_route_support as _route_support
import selected_route_validation as _route_validation

DEFAULT_CONTROL_ROOT = _route_spec.DEFAULT_CONTROL_ROOT
MANIFEST_FILENAME = _route_spec.MANIFEST_FILENAME
PROJECT_SETTINGS_REF = _route_spec.PROJECT_SETTINGS_REF
ORIGINAL_SELECTED_ROUTE_NAMES = _route_spec.ORIGINAL_SELECTED_ROUTE_NAMES
QUERY_ROUTE_NAMES = _route_spec.QUERY_ROUTE_NAMES
SELECTED_ROUTE_NAMES = _route_spec.SELECTED_ROUTE_NAMES
OPTIONAL_SELECTED_ROUTE_NAMES = _route_spec.OPTIONAL_SELECTED_ROUTE_NAMES
ADMITTED_SELECTED_ROUTE_NAMES = _route_spec.ADMITTED_SELECTED_ROUTE_NAMES
DirectLocalReleaseRequest = _route_spec.DirectLocalReleaseRequest
DirectReleaseDraft = _route_spec.DirectReleaseDraft
DirectPublicReleaseRequest = _route_spec.DirectPublicReleaseRequest
SelectedRouteError = _route_spec.SelectedRouteError
_ATOM_ID = _route_spec._ATOM_ID
_DIGEST = _route_spec._DIGEST
_FRESHNESS_FIELDS = _route_spec._FRESHNESS_FIELDS
_OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME = _route_spec._OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME
_OPTIONAL_RELEASE_ROUTE_NAME = _route_spec._OPTIONAL_RELEASE_ROUTE_NAME
_ORIGINAL_SELECTED_SOURCE_REGISTRY_REF = _route_spec._ORIGINAL_SELECTED_SOURCE_REGISTRY_REF
_QUERY_SOURCE_ADMISSION_FIELDS = _route_spec._QUERY_SOURCE_ADMISSION_FIELDS
_QUERY_SOURCE_ADMISSION_SPECS = _route_spec._QUERY_SOURCE_ADMISSION_SPECS
_REQUEST_ID = _route_spec._REQUEST_ID
SelectedRouteAdapter = _route_adapter.SelectedRouteAdapter
_QueueBackedSelectedSupport = _route_queue._QueueBackedSelectedSupport
_configured_control_root = _route_manifest._configured_control_root
_current_pin = _route_manifest._current_pin
_frontmatter_value = _route_manifest._frontmatter_value
_manifest_path = _route_manifest._manifest_path
_query_admission_specs = _route_manifest._query_admission_specs
_safe_path = _route_manifest._safe_path
_selected_authority_ref = _route_manifest._selected_authority_ref
_validate_pin = _route_manifest._validate_pin
canonical_digest = _route_manifest.canonical_digest
canonical_json = _route_manifest.canonical_json
selected_manifest_contract = _route_manifest.selected_manifest_contract
selected_manifest_ref = _route_manifest.selected_manifest_ref
_SelectedRouteAdapterBase = _route_support._SelectedRouteAdapterBase
_guard_public_call = _route_support._guard_public_call
_log_structured_failure = _route_support._log_structured_failure
_public_boundary_result = _route_support._public_boundary_result
_public_logger = _route_support._public_logger
_definition_sequence = _route_validation._definition_sequence
_find_shadow_manifest_fields = _route_validation._find_shadow_manifest_fields
_require_digest = _route_validation._require_digest
_unique_manifest_object = _route_validation._unique_manifest_object
_validate_query_source_admissions = _route_validation._validate_query_source_admissions
_validate_route = _route_validation._validate_route
load_selected_manifest = _route_validation.load_selected_manifest
validate_selected_manifest_document = _route_validation.validate_selected_manifest_document
register_selected_routes = _route_registration.register_selected_routes


_direct_release_request = _route_release.direct_release_request
_direct_release_call = _route_release.direct_release_call
_direct_release_record = _route_release.direct_release_record


def _invoke_direct_release(root: Path, route: str, request: Any) -> dict[str, Any]:
    try:
        normalized = _direct_release_request(root, route, request)
    except (TypeError, ValueError, OSError) as error:
        return {"outcome": "failed", "diagnostics": [str(error)]}
    if route == _OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME and "content_draft" not in normalized:
        return {
            "outcome": "input_required",
            "run_id": normalized["run_id"],
            "project_root": str(root),
            "prompt": "Provide content_draft with description and summary.",
        }
    started, start_error = _direct_release_record(root, route, normalized, "started", None)
    try:
        result = _direct_release_call(root, route, normalized)
    except (AttributeError, ImportError, OSError, RuntimeError, TypeError, ValueError) as error:
        result = {"outcome": "failed", "diagnostics": [str(error)]}
    outcome = result.get("outcome", "failed")
    _, terminal_error = _direct_release_record(
        root,
        route,
        normalized,
        "completed" if outcome == "completed" else "failed",
        started,
        outcome,
    )
    result.update(run_id=normalized["run_id"], project_root=str(root))
    errors = [error for error in (start_error, terminal_error) if error is not None]
    if errors:
        result["recording_error"] = "; ".join(errors)
    return result


__all__ = [
    "SelectedRouteAdapter",
    "_SelectedRouteAdapterBase",
    "_QueueBackedSelectedSupport",
    "register_selected_routes",
    "load_selected_manifest",
    "validate_selected_manifest_document",
    "canonical_json",
    "canonical_digest",
    "selected_manifest_ref",
    "selected_manifest_contract",
]
