"""Closed selected-Workflow MCP projection; execution remains in shared support."""
from __future__ import annotations

import hashlib
import importlib
import json
import re
import sys
import tomllib
import copy
from pathlib import Path
from typing import Any, Callable, Mapping
from pydantic import ConfigDict
from typing_extensions import NotRequired, TypedDict

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '201_TOOLS'))
from project_selection import bound_selection


DEFAULT_CONTROL_ROOT = Path(".caprmedio_caprmedio")
MANIFEST_FILENAME = "selected_workflow_bindings.json"
PROJECT_SETTINGS_REF = DEFAULT_CONTROL_ROOT / "caprmedio_project_settings.toml"
ORIGINAL_SELECTED_ROUTE_NAMES = (
    "create_atom", "update_atom", "replace_atom", "change_atom_status",
    "create_scope_unit", "rename_scope_unit", "move_scope_unit", "remove_scope_unit",
    "run_implementation_workflow", "revert_changes", "build_entities_graph",
    "build_terms_graph", "build_applicable_methodology",
)
QUERY_ROUTE_NAMES = ("find_and_fetch_artifacts", "find_and_fetch_journal_events")
SELECTED_ROUTE_NAMES = (*ORIGINAL_SELECTED_ROUTE_NAMES, *QUERY_ROUTE_NAMES)
_OPTIONAL_RELEASE_ROUTE_NAME = "release_version"
_OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME = "public.release"


class DirectLocalReleaseRequest(TypedDict):
    __pydantic_config__ = ConfigDict(extra="forbid", strict=True)
    project_root: str
    run_id: str


class DirectReleaseDraft(TypedDict):
    __pydantic_config__ = ConfigDict(extra="forbid", strict=True)
    description: str
    summary: list[str]


class DirectPublicReleaseRequest(DirectLocalReleaseRequest):
    content_draft: NotRequired[DirectReleaseDraft]


_DIGEST = re.compile(r"^[0-9a-f]{64}$")
_ATOM_ID = re.compile(r"^CA-[A-Z]+-[0-9]+$")
_REQUEST_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")
_FRESHNESS_FIELDS = {
    "selected_source_registry_ref", "selected_source_registry_version",
    "selected_source_registry_digest", "selected_binding_ref", "selected_binding_digest",
}
_ORIGINAL_SELECTED_SOURCE_REGISTRY_REF = (
    ".caprmedio_caprmedio/02_analysis/"
    "CA-A-1142-ANALYSIS_RPRT--prepare-the-selected-source-to-rmed-handoff.md"
)
_ORIGINAL_SELECTED_SOURCE_REGISTRY_VERSION = 2
_QUERY_SOURCE_ADMISSION_FIELDS = {
    "route", "acceptance_frontier", "workflow", "ordered_steps", "ordered_actions",
}
_QUERY_SOURCE_ADMISSION_SPECS = (
    {
        "route": "find_and_fetch_artifacts",
        "acceptance_frontier": {
            "atom_id": "CA-P-1618", "version": 1,
            "source_path": ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/29-CA-P-1618-TASK--accept-current-artifact-query-source-frontier.md",
            "digest": "bdf10c928c10c102dc489c8e3e526ffe73e8a33d492f4dabc8b5d0129c453b1f",
        },
        "workflow": {
            "atom_id": "CA-O-158", "version": 4,
            "source_path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/09_operations/CA-O-158-CORE_META_MODEL-WORKFLOW--find-and-fetch-artifacts.md",
            "digest": "d7fdaebdd1d0c6ca7dac9aced25552c487336f2a51f18c0f03ef65d16ff4618a",
        },
        "ordered_steps": [{
            "step": {
                "atom_id": "CA-O-160", "version": 2,
                "source_path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/09_operations/CA-O-160-CORE_META_MODEL-STEP--run-the-artifact-query-and-fetch.md",
                "digest": "a743a84fd24db32123ac8162e7a2178e6d83b1b727cbe54477b6020914537384",
            },
            "action": {
                "atom_id": "CA-O-159", "version": 2,
                "source_path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/09_operations/CA-O-159-CORE_META_MODEL-ACTION--query-and-fetch-artifacts.md",
                "digest": "3fd33badbff039e58c1c0b31dfbf3608c37a58d779a1b3ebc14d7bb5ee27dc08",
            },
        }],
        "ordered_actions": [{
            "atom_id": "CA-O-159", "version": 2,
            "source_path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/09_operations/CA-O-159-CORE_META_MODEL-ACTION--query-and-fetch-artifacts.md",
            "digest": "3fd33badbff039e58c1c0b31dfbf3608c37a58d779a1b3ebc14d7bb5ee27dc08",
        }],
    },
    {
        "route": "find_and_fetch_journal_events",
        "acceptance_frontier": {
            "atom_id": "CA-P-1535", "version": 2,
            "source_path": ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/15-CA-P-1535-TASK--accept-final-journal-query-source.md",
            "digest": "6246b46d2961d795e29eeb224f01b14979434d4ad24cf3f4913c490268cf52dc",
        },
        "workflow": {
            "atom_id": "CA-O-161", "version": 2,
            "source_path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/09_operations/CA-O-161-CORE_META_MODEL-WORKFLOW--find-and-fetch-journal-events.md",
            "digest": "362b9d3848a796a14e7374cfa0bf0b561c4f2035b7b2bf87bd9b56fc97a6724d",
        },
        "ordered_steps": [{
            "step": {
                "atom_id": "CA-O-163", "version": 4,
                "source_path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/09_operations/CA-O-161-CORE_META_MODEL-WORKFLOW--find-and-fetch-journal-events/CA-O-163-CORE_META_MODEL-STEP--query-the-stable-journal-event-snapshot.md",
                "digest": "1e47a2e59581a18cc0869efedfeefb6474a404ce5f761123a1c65718726f3727",
            },
            "action": {
                "atom_id": "CA-O-162", "version": 2,
                "source_path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/09_operations/CA-O-162-CORE_META_MODEL-ACTION--query-journal-events.md",
                "digest": "71301ecf9531c70adeba03d6cf7f39761a237a081cee43eb0f9f7ce40e12f9fe",
            },
        }],
        "ordered_actions": [{
            "atom_id": "CA-O-162", "version": 2,
            "source_path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/09_operations/CA-O-162-CORE_META_MODEL-ACTION--query-journal-events.md",
            "digest": "71301ecf9531c70adeba03d6cf7f39761a237a081cee43eb0f9f7ce40e12f9fe",
        }],
    },
)


class SelectedRouteError(ValueError):
    """A rejected MCP projection request or stale source binding."""


def canonical_json(value: Any) -> str:
    """RFC 8785-compatible canonical JSON for the closed manifest schema."""
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":"))


def canonical_digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def _configured_control_root(root: Path) -> Path:
    """Read the Project-local control root, retaining caprmedio as the default."""
    selection = bound_selection(root)
    if selection is not None:
        return selection.control_relative
    settings_path = root / PROJECT_SETTINGS_REF
    if settings_path.is_symlink():
        raise SelectedRouteError("project settings carrier is unavailable")
    if not settings_path.exists():
        return DEFAULT_CONTROL_ROOT
    if not settings_path.is_file():
        raise SelectedRouteError("project settings carrier is unavailable")
    try:
        settings = tomllib.loads(settings_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise SelectedRouteError("project settings carrier is invalid") from error
    paths = settings.get("paths")
    value = paths.get("control_root") if isinstance(paths, Mapping) else None
    if value is None:
        return DEFAULT_CONTROL_ROOT
    if not isinstance(value, str) or not value:
        raise SelectedRouteError("paths.control_root must be a safe repository-relative path")
    candidate = Path(value)
    if candidate.is_absolute() or candidate == Path(".") or ".." in candidate.parts:
        raise SelectedRouteError("paths.control_root must be a safe repository-relative path")
    resolved = (root / candidate).resolve()
    if root != resolved and root not in resolved.parents:
        raise SelectedRouteError("paths.control_root escapes project root")
    return candidate


def _selected_authority_ref(root: Path, reference: str) -> str:
    """Bind a trusted authority location without changing its exact byte pin."""
    selection = bound_selection(root)
    path = Path(reference)
    if selection is not None and path.is_relative_to(DEFAULT_CONTROL_ROOT):
        return (selection.control_relative / path.relative_to(DEFAULT_CONTROL_ROOT)).as_posix()
    return reference


def _query_admission_specs(root: Path) -> tuple[dict[str, Any], ...]:
    specifications = copy.deepcopy(_QUERY_SOURCE_ADMISSION_SPECS)
    def bind(value):
        if isinstance(value, dict):
            for key, child in value.items():
                if key == 'source_path':
                    value[key] = _selected_authority_ref(root, child)
                else:
                    bind(child)
        elif isinstance(value, list):
            for child in value:
                bind(child)
    bind(list(specifications))
    return specifications


def selected_manifest_ref(root: str | Path | None = None) -> str:
    """Return the one derived binding projection for this Project authority root."""
    if root is None:
        control_root = DEFAULT_CONTROL_ROOT
    else:
        project_root = Path(root).resolve(strict=True)
        control_root = _configured_control_root(project_root)
    return (control_root / "_projection" / MANIFEST_FILENAME).as_posix()


def selected_manifest_contract(root: str | Path | None = None) -> dict[str, Any]:
    """Publish the immutable manifest boundary consumed by queue and Docker callers.

    ``load_selected_manifest`` is the only loader: it validates this schema,
    the manifest self-digest, and every live source pin before returning data.
    The returned contract contains no mutable project state.
    """
    return {
        "manifest_ref": selected_manifest_ref(root),
        "schema_version": 1,
        "canonical_digest": {
            "algorithm": "sha256",
            "serialization": "RFC8785",
            "self_field": "canonical_manifest_sha256",
            "self_field_omitted_from_digest": True,
        },
        "outer_fields": ["schema_version", "source_freshness", "query_source_admissions", "routes", "canonical_manifest_sha256"],
        "source_freshness_fields": sorted(_FRESHNESS_FIELDS),
        "query_source_admission_fields": ["route", "acceptance_frontier", "workflow", "ordered_steps", "ordered_actions"],
        "route_fields": [
            "route", "workflow", "ordered_steps", "ordered_actions", "native_action_calls",
            "entry_step", "on_result", "mutation_capable",
        ],
        "definition_pin_fields": ["atom_id", "version", "source_path", "digest"],
        "on_result_fields": ["from", "condition", "to"],
        "on_result_terminal_target": "complete",
        "route_names": list(SELECTED_ROUTE_NAMES),
    }


def _safe_path(root: Path, relative: str) -> Path:
    bound_selection(root)
    if not isinstance(relative, str) or not relative or relative.startswith("/") or "\\" in relative:
        raise SelectedRouteError("source_path must be a safe repository-relative path")
    path = (root / relative).resolve()
    if root != path and root not in path.parents:
        raise SelectedRouteError("source_path escapes project root")
    return path


def _frontmatter_value(contents: str, field: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(field)}:\s*[\"']?([^\n\"']+)", contents)
    return match.group(1).strip() if match else None


def _validate_pin(root: Path, pin: Any) -> dict[str, Any]:
    if not isinstance(pin, Mapping) or set(pin) != {"atom_id", "version", "source_path", "digest"}:
        raise SelectedRouteError("definition pin must contain atom_id, version, source_path, and digest")
    atom_id, version, source_path, digest = (pin["atom_id"], pin["version"], pin["source_path"], pin["digest"])
    if not isinstance(atom_id, str) or not atom_id or not isinstance(version, int) or version < 1:
        raise SelectedRouteError("definition pin has invalid identity or version")
    if not isinstance(digest, str) or not _DIGEST.fullmatch(digest):
        raise SelectedRouteError("definition pin has invalid digest")
    path = _safe_path(root, source_path)
    selection = bound_selection(root)
    relative_parts = path.relative_to(root).parts
    if (selection is not None and relative_parts and relative_parts[0].startswith('.caprmedio_')
            and not path.is_relative_to(selection.control_root)):
        raise SelectedRouteError("source pin belongs to another Project authority")
    if not path.is_file():
        raise SelectedRouteError(f"source pin is unavailable: {source_path}")
    contents = path.read_bytes()
    if hashlib.sha256(contents).hexdigest() != digest:
        raise SelectedRouteError(f"source pin is stale: {source_path}")
    try:
        text = contents.decode("utf-8")
    except UnicodeDecodeError as error:
        raise SelectedRouteError(f"source pin is not UTF-8: {source_path}") from error
    if _frontmatter_value(text, "atom_id") != atom_id or _frontmatter_value(text, "version") != str(version):
        raise SelectedRouteError(f"source pin metadata differs: {source_path}")
    return dict(pin)


def _manifest_path(root: Path) -> Path:
    return _safe_path(root, selected_manifest_ref(root))


def _definition_sequence(route: Mapping[str, Any]) -> list[dict[str, Any]]:
    return [route["workflow"], *[item["step"] for item in route["ordered_steps"]], *route["ordered_actions"]]


def _validate_route(root: Path, entry: Any) -> dict[str, Any]:
    required = {"route", "workflow", "ordered_steps", "ordered_actions", "native_action_calls",
                "entry_step", "on_result", "mutation_capable"}
    if not isinstance(entry, Mapping) or set(entry) != required:
        raise SelectedRouteError("route binding has an incomplete or unknown schema")
    if entry["route"] not in SELECTED_ROUTE_NAMES or not isinstance(entry["entry_step"], str):
        raise SelectedRouteError("route binding has an unsupported route or entry step")
    if not isinstance(entry["mutation_capable"], bool) or not isinstance(entry["ordered_steps"], list) or not entry["ordered_steps"]:
        raise SelectedRouteError("route binding has no ordered step graph")
    if not isinstance(entry["ordered_actions"], list) or not isinstance(entry["native_action_calls"], list):
        raise SelectedRouteError("route binding has an invalid ordered Action list")
    pin_validator = _validate_pin
    result = dict(entry)
    result["workflow"] = pin_validator(root, entry["workflow"])
    steps: list[dict[str, Any]] = []
    for item in entry["ordered_steps"]:
        if not isinstance(item, Mapping) or set(item) != {"step", "action"}:
            raise SelectedRouteError("ordered step binding must have one Step and one Action")
        steps.append({"step": pin_validator(root, item["step"]), "action": pin_validator(root, item["action"])})
    step_ids = {item["step"]["atom_id"] for item in steps}
    if entry["entry_step"] not in step_ids:
        raise SelectedRouteError("route entry step is not in its ordered Step list")
    actions = [pin_validator(root, item) for item in entry["ordered_actions"]]
    if [item["action"]["atom_id"] for item in steps] != [item["atom_id"] for item in actions]:
        raise SelectedRouteError("ordered Action list differs from Step Action bindings")
    if not isinstance(entry["on_result"], list):
        raise SelectedRouteError("route on_result must be an ordered list")
    for edge in entry["on_result"]:
        if not isinstance(edge, Mapping) or set(edge) != {"from", "condition", "to"} or not all(
                isinstance(edge[key], str) and edge[key] for key in ("from", "condition", "to")):
            raise SelectedRouteError("route on_result edge is malformed")
        if edge["from"] not in step_ids:
            raise SelectedRouteError("route on_result source is not in its ordered Step list")
        if edge["to"] != "complete" and edge["to"] not in step_ids:
            raise SelectedRouteError("route on_result target is not in its ordered Step list or complete")
    result.update(ordered_steps=steps, ordered_actions=actions,
                  native_action_calls=[pin_validator(root, item) for item in entry["native_action_calls"]])
    return result


def _validate_query_source_admissions(
    root: Path, admissions: Any, routes: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Validate the two admission-frontier proofs without creating a registry."""
    specifications = _query_admission_specs(root)
    if not isinstance(admissions, list) or len(admissions) != len(specifications):
        raise SelectedRouteError("selected query-source admissions must contain exactly two routes")
    by_route = {entry["route"]: entry for entry in routes}
    validated: list[dict[str, Any]] = []
    for value, expected in zip(admissions, specifications, strict=True):
        if not isinstance(value, Mapping) or set(value) != _QUERY_SOURCE_ADMISSION_FIELDS:
            raise SelectedRouteError("query-source admission has an incomplete or unknown schema")
        if value.get("route") != expected["route"]:
            raise SelectedRouteError("query-source admission route order or identity differs")
        route = by_route.get(value["route"])
        if route is None or route["route"] not in QUERY_ROUTE_NAMES or route["mutation_capable"]:
            raise SelectedRouteError("query-source admission does not bind one read-only selected route")
        if not isinstance(value.get("ordered_steps"), list) or not isinstance(value.get("ordered_actions"), list):
            raise SelectedRouteError("query-source admission definitions are malformed")
        admission = {
            "route": value["route"],
            "acceptance_frontier": _validate_pin(root, value["acceptance_frontier"]),
            "workflow": _validate_pin(root, value["workflow"]),
            "ordered_steps": [],
            "ordered_actions": [],
        }
        for item in value["ordered_steps"]:
            if not isinstance(item, Mapping) or set(item) != {"step", "action"}:
                raise SelectedRouteError("query-source admission Step binding is malformed")
            admission["ordered_steps"].append({
                "step": _validate_pin(root, item["step"]),
                "action": _validate_pin(root, item["action"]),
            })
        admission["ordered_actions"] = [_validate_pin(root, item) for item in value["ordered_actions"]]
        if admission != expected:
            raise SelectedRouteError("query-source admission differs from the accepted source frontier")
        for key in ("workflow", "ordered_steps", "ordered_actions"):
            if admission[key] != route[key]:
                raise SelectedRouteError("query-source admission definitions differ from the selected route")
        validated.append(admission)
    return validated


def _unique_manifest_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    """Reject duplicate JSON members before the parser silently collapses them."""
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise SelectedRouteError(f"selected workflow binding manifest has duplicate JSON member: {key}")
        result[key] = value
    return result


def validate_selected_manifest_document(root: str | Path, manifest: Any) -> dict[str, Any]:
    """Validate one in-memory selected binding document without touching its carrier."""
    project_root = Path(root).resolve(strict=True)
    manifest_ref = selected_manifest_ref(project_root)
    required = {"schema_version", "source_freshness", "query_source_admissions", "routes", "canonical_manifest_sha256"}
    if (not isinstance(manifest, Mapping) or set(manifest) != required
            or manifest["schema_version"] != 1):
        raise SelectedRouteError("selected workflow binding manifest schema is invalid")
    if not isinstance(manifest["canonical_manifest_sha256"], str) or not _DIGEST.fullmatch(manifest["canonical_manifest_sha256"]):
        raise SelectedRouteError("selected workflow binding manifest digest is invalid")
    without_self = {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
    if canonical_digest(without_self) != manifest["canonical_manifest_sha256"]:
        raise SelectedRouteError("selected workflow binding manifest canonical digest differs")
    freshness = manifest["source_freshness"]
    if not isinstance(freshness, Mapping) or set(freshness) != _FRESHNESS_FIELDS:
        raise SelectedRouteError("selected workflow binding manifest source freshness is invalid")
    if not all(isinstance(freshness[key], str) and freshness[key] for key in _FRESHNESS_FIELDS - {"selected_source_registry_version"}) or type(freshness["selected_source_registry_version"]) is not int or freshness["selected_source_registry_version"] < 1:
        raise SelectedRouteError("selected workflow binding manifest source freshness is incomplete")
    if not _DIGEST.fullmatch(freshness["selected_source_registry_digest"]) or not _DIGEST.fullmatch(freshness["selected_binding_digest"]):
        raise SelectedRouteError("selected workflow binding manifest freshness digest is invalid")
    if (freshness["selected_source_registry_ref"] != _selected_authority_ref(project_root, _ORIGINAL_SELECTED_SOURCE_REGISTRY_REF)
            or freshness["selected_source_registry_version"] != _ORIGINAL_SELECTED_SOURCE_REGISTRY_VERSION):
        raise SelectedRouteError("selected workflow binding manifest does not retain the CA-A-1142 registry authority")
    if freshness["selected_binding_ref"] != f"{manifest_ref}#/routes":
        raise SelectedRouteError("selected workflow binding manifest does not retain its binding reference")
    registry = _safe_path(project_root, freshness["selected_source_registry_ref"])
    if not registry.is_file() or hashlib.sha256(registry.read_bytes()).hexdigest() != freshness["selected_source_registry_digest"]:
        raise SelectedRouteError("selected source registry pin is stale")
    routes = manifest["routes"]
    if not isinstance(routes, list) or len(routes) != len(SELECTED_ROUTE_NAMES):
        raise SelectedRouteError("selected workflow binding manifest must contain fifteen routes")
    expected_names = SELECTED_ROUTE_NAMES
    validated = [_validate_route(project_root, entry) for entry in routes]
    if tuple(entry["route"] for entry in validated) != expected_names or len({entry["route"] for entry in validated}) != len(expected_names):
        raise SelectedRouteError("selected workflow route registry is incomplete or duplicate")
    admissions = _validate_query_source_admissions(project_root, manifest["query_source_admissions"], validated)
    if canonical_digest(validated) != freshness["selected_binding_digest"]:
        raise SelectedRouteError("selected workflow route binding digest differs")
    result = {"manifest_ref": manifest_ref, "schema_version": 1, "source_freshness": dict(freshness),
              "query_source_admissions": admissions, "routes": validated,
              "canonical_manifest_sha256": manifest["canonical_manifest_sha256"]}
    return result


def load_selected_manifest(root: str | Path) -> dict[str, Any]:
    """Verify all fifteen ordinary route source bindings without dispatch."""
    project_root = Path(root).resolve(strict=True)
    try:
        manifest = json.loads(_manifest_path(project_root).read_text(encoding="utf-8"),
                              object_pairs_hook=_unique_manifest_object)
    except (OSError, json.JSONDecodeError) as error:
        raise SelectedRouteError("selected workflow binding manifest is unreadable") from error
    return validate_selected_manifest_document(project_root, manifest)


def _find_shadow_manifest_fields(
    value: Any, *, allowed_definition_manifest: bool = False, _path: tuple[str | int, ...] = ()
) -> bool:
    if isinstance(value, Mapping):
        for key, child in value.items():
            if key in {"definition_manifest_ref", "definition_manifest_digest"}:
                return True
            if key == "definition_manifest" and not (
                allowed_definition_manifest
                and _path in {(), ("operator_authorization",), ("proposal_receipt",)}
            ):
                return True
            if _find_shadow_manifest_fields(
                child, allowed_definition_manifest=allowed_definition_manifest, _path=(*_path, key)
            ):
                return True
    elif isinstance(value, list):
        return any(_find_shadow_manifest_fields(
            item, allowed_definition_manifest=allowed_definition_manifest, _path=(*_path, index)
        ) for index, item in enumerate(value))
    return False


def _require_digest(value: Any, message: str) -> str:
    if not isinstance(value, str) or not _DIGEST.fullmatch(value):
        raise SelectedRouteError(message)
    return value


def _direct_release_request(root: Path, route: str, request: Any) -> dict[str, Any]:
    required = {"project_root", "run_id"}
    allowed = required | (
        {"content_draft"} if route == _OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME else set()
    )
    if not isinstance(request, Mapping) or not required <= set(request) <= allowed:
        raise SelectedRouteError(
            "request requires only project_root and run_id, plus optional public content_draft"
        )
    run_id = request["run_id"]
    pattern = (
        _REQUEST_ID
        if route == _OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME
        else re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")
    )
    if not isinstance(run_id, str) or not pattern.fullmatch(run_id):
        raise SelectedRouteError("run_id is invalid")
    selection = bound_selection(root)
    expected = (
        selection.host_root if selection is not None and selection.host_root is not None else root
    )
    if request["project_root"] != str(expected):
        raise SelectedRouteError("project_root does not match the bound Project root")
    if "content_draft" in request:
        draft = request["content_draft"]
        if (
            not isinstance(draft, Mapping)
            or set(draft) != {"description", "summary"}
            or not isinstance(draft["description"], str)
            or not isinstance(draft["summary"], list)
            or not all(isinstance(item, str) for item in draft["summary"])
        ):
            raise SelectedRouteError("content_draft is invalid")
    return dict(request)


def _direct_release_call(root: Path, route: str, request: Mapping[str, Any]) -> dict[str, Any]:
    public = route == _OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME
    relative = Path(
        "PROJECT_TOOLS/PUBLIC_RELEASE/public_release.py"
        if public
        else "PROJECT_TOOLS/RELEASE_VERSION/local_release.py"
    )
    current = root
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            raise SelectedRouteError("Release implementation path is a symlink")
    if not current.is_file():
        raise SelectedRouteError("Release implementation is unavailable")
    spec = importlib.util.spec_from_file_location(
        "_caprmedio_direct_public_release" if public else "_caprmedio_direct_local_release", current
    )
    if spec is None or spec.loader is None:
        raise SelectedRouteError("Release implementation is unavailable")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
        kwargs = {"run_id": request["run_id"]}
        if public:
            kwargs["content_draft"] = request["content_draft"]
        result = getattr(module, "run_public_release" if public else "run_local_release")(
            root, **kwargs
        )
    finally:
        sys.modules.pop(spec.name, None)
    if not isinstance(result, Mapping):
        raise SelectedRouteError("Release returned an invalid result")
    return dict(result)


def _direct_release_record(
    root: Path,
    route: str,
    request: Mapping[str, Any],
    event: str,
    preceding: str | None,
    outcome: str | None = None,
) -> tuple[str | None, str | None]:
    try:
        from work_journal import append_record, event_record

        record = event_record(
            root=root,
            event=event,
            action_id=request["run_id"],
            kind="workflow",
            scope="project",
            operation=route,
            session_id=request["run_id"],
            subjects=[],
            outputs=[],
            preceding_event=preceding,
            details={"outcome": outcome} if outcome is not None else {},
        )
        append_record(root, record)
        return record.get("event_id"), None
    except (ImportError, OSError, RuntimeError, TypeError, ValueError) as error:
        return None, f"Release {event} recording failed: {error}"


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


class _SelectedRouteAdapterBase:
    """Validates the closed projection then calls the shared selected-run service once."""

    def __init__(self, root: str | Path, service: Any | None = None, *, strict_manifest: bool = True) -> None:
        self.root = Path(root).resolve(strict=True)
        self.manifest: dict[str, Any] | None = None
        self.routes: dict[str, dict[str, Any]] = {}
        if strict_manifest:
            self.manifest = load_selected_manifest(self.root)
            self.routes = {entry["route"]: entry for entry in self.manifest["routes"]}
        self.service = service

    def _result(self, request: Any, disposition: str, outcome: str, diagnostic: str) -> dict[str, Any]:
        value = {"disposition": disposition, "outcome": outcome, "diagnostics": [diagnostic]}
        if isinstance(request, Mapping) and isinstance(request.get("request_id"), str):
            value["request_id"] = request["request_id"]
        return value

    def _support(self) -> Any | None:
        if self.service is not None:
            return self.service
        return _QueueBackedSelectedSupport(self.root, self)


class _QueueBackedSelectedSupport:
    """Thin MCP composition of shared preview support and the existing queue APP.

    It deliberately does not execute Actions.  Preview uses the shared
    ``RunTracker`` admission implementation; execute only forwards the exact
    request to the already-owned ``enqueue_selected`` APP variant.
    """

    def __init__(self, root: Path, adapter: "SelectedRouteAdapter") -> None:
        self.root, self.adapter = root, adapter

    def _tracker(self) -> Any:
        # Code is loaded from the immutable MCP image; ``root`` is only the
        # caller's Project authority/data root and need not contain code.
        tools = Path(__file__).resolve().parents[1] / "201_TOOLS"
        if str(tools) not in sys.path:
            sys.path.insert(0, str(tools))
        module = importlib.import_module("workflow_run_support")

        def observe(request: dict[str, Any]) -> dict[str, Any]:
            try:
                manifest = load_selected_manifest(self.root)
                selected = request.get("operation_route") in {entry["route"] for entry in manifest["routes"]}
                current = dict(request.get("definition_manifest", {})) == {
                    "manifest_ref": manifest["manifest_ref"], "manifest_digest": manifest["canonical_manifest_sha256"]
                } and dict(request.get("source_freshness", {})) == manifest["source_freshness"]
                lifecycle_admission = None
                if request.get("operation_route") == "change_atom_status":
                    app = Path(__file__).resolve().parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"
                    if str(app) not in sys.path:
                        sys.path.insert(0, str(app))
                    selected_execution = importlib.import_module("selected_execution")
                    lifecycle_admission = selected_execution.preflight_selected_lifecycle(
                        self.root, "change_atom_status", request.get("parameters"),
                    )
            except (ImportError, SelectedRouteError, TypeError, ValueError, RuntimeError):
                selected, current, lifecycle_admission = False, False, None
            return {"selected": selected, "current": current, "observed": {
                "manifest_ref": request.get("definition_manifest", {}).get("manifest_ref") if isinstance(request.get("definition_manifest"), Mapping) else None,
                "manifest_digest": request.get("definition_manifest", {}).get("manifest_digest") if isinstance(request.get("definition_manifest"), Mapping) else None,
                **({"lifecycle_admission": lifecycle_admission}
                   if lifecycle_admission is not None else {}),
            }}

        def never_execute(_request: dict[str, Any], _session: Any) -> Mapping[str, Any]:
            raise RuntimeError("MCP delegates selected execution to enqueue_selected")

        return module.RunTracker(self.root, source_observer=observe, executor=never_execute)

    @staticmethod
    def _workflow_run_id(request: Mapping[str, Any]) -> str:
        rows = request.get("requested_runs")
        if not isinstance(rows, list):
            raise SelectedRouteError("execute has no requested Workflow Run identity")
        workflow = [row for row in rows if isinstance(row, Mapping) and row.get("kind") == "workflow"]
        if len(workflow) != 1 or not isinstance(workflow[0].get("requested_run_id"), str):
            raise SelectedRouteError("execute must carry one requested Workflow Run identity")
        return str(workflow[0]["requested_run_id"])

    def run_selected_operation(self, request: dict[str, Any]) -> dict[str, Any]:
        if request["mode"] == "preview":
            return self._tracker().run_selected_operation(request)
        preview = {key: value for key, value in request.items() if key not in {
            "proposal_receipt", "proposal_receipt_digest", "assigned_action_id", "operator_authorization", "requested_runs"
        }}
        preview["mode"] = "preview"
        prepared = self._tracker().run_selected_operation(preview)
        if prepared.get("disposition") != "preview" or request.get("proposal_receipt") != prepared.get("proposal_receipt") or request.get("proposal_receipt_digest") != prepared.get("proposal_receipt_digest"):
            return {"request_id": request["request_id"], "disposition": "blocked", "outcome": "blocked",
                    "source_freshness": prepared.get("source_freshness"), "diagnostics": ["exact current preview receipt is required before enqueue"]}
        try:
            app = Path(__file__).resolve().parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"
            if str(app) not in sys.path:
                sys.path.insert(0, str(app))
            orchestrator = importlib.import_module("orchestrator")
            return orchestrator.run(self.root, {"operation": "enqueue_selected", "run_id": self._workflow_run_id(request), "execution": request})
        except (ImportError, SelectedRouteError, ValueError, RuntimeError, OSError) as error:
            return {"request_id": request["request_id"], "disposition": "blocked", "outcome": "blocked",
                    "source_freshness": prepared.get("source_freshness"),
                    "diagnostics": [f"enqueue_selected did not admit the exact request: {error}"]}

    def get_selected_workflow_run(self, request: dict[str, Any]) -> dict[str, Any]:
        try:
            app = Path(__file__).resolve().parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"
            if str(app) not in sys.path:
                sys.path.insert(0, str(app))
            return importlib.import_module("orchestrator").run(self.root, {"operation": "status", "run_id": request["run_id"]})
        except (ImportError, ValueError, RuntimeError, OSError) as error:
            return {"disposition": "blocked", "outcome": "blocked", "diagnostics": [f"selected Run observation unavailable: {error}"]}

    def get_selected_action_run(self, request: dict[str, Any]) -> dict[str, Any]:
        try:
            app = Path(__file__).resolve().parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"
            if str(app) not in sys.path:
                sys.path.insert(0, str(app))
            manifest = load_selected_manifest(self.root)
            observer = importlib.import_module("selected_action_observation")
            return observer.observe_selected_action(self.root, request["action_run_id"], manifest)
        except (ImportError, ValueError, RuntimeError, OSError) as error:
            return {"action_run_id": request["action_run_id"], "disposition": "blocked", "outcome": "blocked",
                    "diagnostics": [f"selected Action observation is unavailable: {error}"]}


class SelectedRouteAdapter(_SelectedRouteAdapterBase):

    def _preflight_lifecycle(self, request: Mapping[str, Any]) -> dict[str, Any] | None:
        """Reject one source-invalid status request before shared preview admission."""
        if request.get("operation_route") != "change_atom_status":
            return None
        app = Path(__file__).resolve().parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"
        if str(app) not in sys.path:
            sys.path.insert(0, str(app))
        try:
            selected_execution = importlib.import_module("selected_execution")
        except (ImportError, AttributeError, TypeError, ValueError, RuntimeError) as error:
            return self._result(request, "blocked", "blocked", f"source-derived lifecycle admission unavailable: {error}")
        try:
            current = selected_execution.preflight_selected_lifecycle(
                self.root, "change_atom_status", request.get("parameters"),
            )
            if request.get("mode") == "execute":
                receipt = request.get("proposal_receipt")
                freshness = receipt.get("source_freshness") if isinstance(receipt, Mapping) else None
                observed = freshness.get("observed") if isinstance(freshness, Mapping) else None
                expected = observed.get("lifecycle_admission") if isinstance(observed, Mapping) else None
                if not isinstance(expected, Mapping):
                    raise selected_execution.LifecycleAdmissionError(
                        "status-preview-admission-missing",
                        "status execution requires the source-derived preview admission",
                    )
                if canonical_digest(dict(expected)) != canonical_digest(current):
                    raise selected_execution.LifecycleAdmissionError(
                        "status-model-stale",
                        "authoritative status-model source changed after lifecycle admission",
                    )
        except selected_execution.LifecycleAdmissionError as error:
            result = self._result(request, "blocked", "blocked", str(error))
            result["effect_refs"] = []
            result["lifecycle_error"] = error.record()
            return result
        except (AttributeError, TypeError, ValueError, RuntimeError) as error:
            return self._result(request, "blocked", "blocked", f"source-derived lifecycle admission unavailable: {error}")
        return None

    def _validate_request(self, route: str, request: Any) -> dict[str, Any]:
        if not isinstance(request, Mapping):
            raise SelectedRouteError("request must be an object")
        allowed = {"operation_route", "mode", "request_id", "parameters", "parameters_digest", "target_frontier",
                   "target_frontier_digest", "effects", "effects_digest", "definition_manifest", "source_freshness",
                   "expected_definition_revisions", "initiative", "lineage", "proposal_receipt",
                   "proposal_receipt_digest", "assigned_action_id", "requested_runs", "operator_authorization"}
        unknown = set(request) - allowed
        if unknown or _find_shadow_manifest_fields(request, allowed_definition_manifest=True):
            raise SelectedRouteError("request contains unknown or shadow manifest fields")
        normalized = dict(request)
        normalized.setdefault("mode", "preview")
        if normalized.get("operation_route") != route or route not in self.routes:
            raise SelectedRouteError("request route is not the selected MCP route")
        if normalized["mode"] not in {"preview", "execute"}:
            raise SelectedRouteError("mode must be preview or execute")
        if not isinstance(normalized.get("request_id"), str) or not _REQUEST_ID.fullmatch(normalized["request_id"]):
            raise SelectedRouteError("request_id must be a stable safe identity")
        if not isinstance(normalized.get("parameters"), Mapping) or canonical_digest(normalized["parameters"]) != _require_digest(normalized.get("parameters_digest"), "parameters_digest differs"):
            raise SelectedRouteError("parameters or parameters_digest differs")
        frontier = normalized.get("target_frontier")
        if not isinstance(frontier, list) or not frontier or not all(isinstance(ref, str) and ref and not ref.startswith("/") and ".." not in Path(ref).parts for ref in frontier):
            raise SelectedRouteError("target_frontier is invalid")
        if len(set(frontier)) != len(frontier) or canonical_digest(frontier) != _require_digest(normalized.get("target_frontier_digest"), "target_frontier_digest differs"):
            raise SelectedRouteError("target_frontier_digest differs")
        effects = normalized.get("effects")
        if not isinstance(effects, list) or any(not isinstance(effect, Mapping) or not isinstance(effect.get("type"), str) or not effect["type"] for effect in effects):
            raise SelectedRouteError("effects are invalid")
        if canonical_digest(effects) != _require_digest(normalized.get("effects_digest"), "effects_digest differs"):
            raise SelectedRouteError("effects_digest differs")
        manifest = normalized.get("definition_manifest")
        if not isinstance(manifest, Mapping) or set(manifest) != {"manifest_ref", "manifest_digest"}:
            raise SelectedRouteError("definition_manifest is invalid")
        if manifest != {"manifest_ref": self.manifest["manifest_ref"], "manifest_digest": self.manifest["canonical_manifest_sha256"]}:
            raise SelectedRouteError("definition_manifest is stale or does not identify the canonical binding")
        freshness = normalized.get("source_freshness")
        if not isinstance(freshness, Mapping) or dict(freshness) != self.manifest["source_freshness"]:
            raise SelectedRouteError("source_freshness is stale or incomplete")
        initiative = normalized.get("initiative")
        if not isinstance(initiative, Mapping) or not set(initiative) <= {"initiative_id", "instruction_summary", "initiative_ref"} or not all(isinstance(initiative.get(key), str) and initiative[key] for key in ("initiative_id", "instruction_summary")) or ("initiative_ref" in initiative and (not isinstance(initiative["initiative_ref"], str) or not initiative["initiative_ref"] or initiative["initiative_ref"].startswith("/") or ".." in Path(initiative["initiative_ref"]).parts)):
            raise SelectedRouteError("initiative must be an explicit sealed authorization boundary")
        if "lineage" in normalized:
            lineage = normalized["lineage"]
            if not isinstance(lineage, list) or any(not isinstance(value, str) or not value for value in lineage):
                raise SelectedRouteError("lineage must contain only actual parent Run references")
        if "expected_definition_revisions" in normalized:
            expected = normalized["expected_definition_revisions"]
            source = self._expected_revisions(route)
            if not isinstance(expected, list) or expected != source:
                raise SelectedRouteError("expected definition revisions differ from the selected route binding")
        return normalized

    def _expected_revisions(self, route: str) -> list[dict[str, Any]]:
        entry = self.routes[route]
        rows: list[dict[str, Any]] = []
        for kind, pin in [("workflow", entry["workflow"]), *[("step", item["step"]) for item in entry["ordered_steps"]], *[("action", item) for item in entry["ordered_actions"]]]:
            row = {"kind": kind, "atom_id": pin["atom_id"], "version": pin["version"], "path": pin["source_path"], "digest": pin["digest"]}
            if row not in rows:
                rows.append(row)
        return sorted(rows, key=lambda item: (item["kind"], item["atom_id"], item["version"], item["path"]))

    def _validate_execute(self, request: Mapping[str, Any]) -> str | None:
        required = {"proposal_receipt", "proposal_receipt_digest", "assigned_action_id", "requested_runs", "operator_authorization"}
        missing = [name for name in sorted(required) if name not in request]
        if missing:
            return "execute requires exact preview receipt and Operator authorization"
        receipt = request["proposal_receipt"]
        if not isinstance(receipt, Mapping) or not receipt or not _DIGEST.fullmatch(str(request["proposal_receipt_digest"])):
            return "execute proposal receipt is invalid"
        if canonical_digest(receipt) != request["proposal_receipt_digest"]:
            return "execute proposal receipt digest differs"
        if not isinstance(request["assigned_action_id"], str) or not request["assigned_action_id"]:
            return "execute assigned_action_id is invalid"
        requested = request["requested_runs"]
        if not isinstance(requested, list) or not requested:
            return "execute requested Run identities are invalid"
        authorization = request["operator_authorization"]
        if not isinstance(authorization, Mapping) or not isinstance(authorization.get("authorization_ref"), str) or not authorization["authorization_ref"]:
            return "execute lacks explicit sealed Operator authorization"
        required_bindings = {
            "request_id": request["request_id"], "operation_route": request["operation_route"],
            "proposal_receipt_digest": request["proposal_receipt_digest"], "parameters_digest": request["parameters_digest"],
            "target_frontier_digest": request["target_frontier_digest"],
            "effects_digest": request["effects_digest"], "definition_manifest": request["definition_manifest"],
            "source_freshness": request["source_freshness"],
        }
        if any(authorization.get(key) != value for key, value in required_bindings.items()):
            return "Operator authorization is not bound to the exact preview and current source frontier"
        freshness = authorization.get("authorization_freshness")
        if not isinstance(freshness, Mapping) or set(freshness) != {"state", "digest"} or freshness.get("state") != "current" or not isinstance(freshness.get("digest"), str) or not _DIGEST.fullmatch(freshness["digest"]):
            return "Operator authorization freshness is invalid"
        if set(authorization) != {"authorization_ref", "authorization_freshness", *required_bindings}:
            return "Operator authorization contains unknown or incomplete bindings"
        return None

    def invoke(self, route: str, request: Any) -> dict[str, Any]:
        if route in {_OPTIONAL_RELEASE_ROUTE_NAME, _OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME}:
            return _invoke_direct_release(self.root, route, request)
        try:
            self.manifest = load_selected_manifest(self.root)
            self.routes = {entry["route"]: entry for entry in self.manifest["routes"]}
            normalized = self._validate_request(route, request)
        except SelectedRouteError as error:
            return self._result(request, "rejected", "rejected", str(error))
        if normalized["mode"] == "execute":
            blocked = self._validate_execute(normalized)
            if blocked:
                return self._result(normalized, "blocked", "blocked", blocked)
        lifecycle_refusal = self._preflight_lifecycle(normalized)
        if lifecycle_refusal is not None:
            return lifecycle_refusal
        support = self._support()
        if support is None:
            return {"request_id": normalized["request_id"], "disposition": "blocked", "outcome": "implementation_gap",
                    "source_freshness": normalized["source_freshness"], "diagnostics": ["shared implement_run_support is unavailable"]}
        try:
            handler: Callable[[dict[str, Any]], dict[str, Any]] = getattr(support, "run_selected_operation")
            result = handler(normalized)
            return result
        except (AttributeError, TypeError, ValueError, RuntimeError) as error:
            return self._result(normalized, "blocked", "blocked", f"shared support rejected request: {error}")

    def _observe(self, method: str, request: Any, required_key: str) -> dict[str, Any]:
        if not isinstance(request, Mapping) or set(request) != {required_key} or not isinstance(request[required_key], str) or not request[required_key]:
            return self._result(request, "rejected", "rejected", f"{method} requires one exact {required_key}")
        support = self._support()
        if support is None or not hasattr(support, method):
            return self._result(request, "blocked", "implementation_gap", "shared implement_run_support observation is unavailable")
        try:
            return getattr(support, method)(dict(request))
        except (TypeError, ValueError, RuntimeError) as error:
            return self._result(request, "blocked", "blocked", f"shared support rejected observation: {error}")

    def get_workflow_run(self, request: Any) -> dict[str, Any]:
        return self._observe("get_selected_workflow_run", request, "run_id")

    def get_action_run(self, request: Any) -> dict[str, Any]:
        return self._observe("get_selected_action_run", request, "action_run_id")

def register_selected_routes(
    server: Any, root: str | Path, *, tool_blacklist: frozenset[str] = frozenset(),
) -> SelectedRouteAdapter:
    """Register direct Release commands and only fully admitted ordinary routes."""
    from mcp.types import ToolAnnotations

    adapter = SelectedRouteAdapter(root, strict_manifest=False)
    try:
        adapter.manifest = load_selected_manifest(adapter.root)
        adapter.routes = {entry["route"]: entry for entry in adapter.manifest["routes"]
                          if entry["route"] in SELECTED_ROUTE_NAMES}
    except (OSError, ValueError):
        pass
    selected_annotations = ToolAnnotations(read_only_hint=False, destructive_hint=False, idempotent_hint=True, open_world_hint=False)
    query_annotations = ToolAnnotations(read_only_hint=True, destructive_hint=False, idempotent_hint=True, open_world_hint=False)
    observation_annotations = ToolAnnotations(read_only_hint=True, destructive_hint=False, idempotent_hint=True, open_world_hint=False)
    release_annotations = ToolAnnotations(read_only_hint=False, destructive_hint=True, idempotent_hint=False, open_world_hint=False)

    public_route_names = (*adapter.routes, _OPTIONAL_RELEASE_ROUTE_NAME, _OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME)
    adapter.public_route_names = frozenset(public_route_names) - tool_blacklist

    for route_name in sorted(adapter.routes.keys() - tool_blacklist):
        def add_route(route: str) -> None:
            @server.tool(name=route, structured_output=True,
                         annotations=(query_annotations if route in QUERY_ROUTE_NAMES else selected_annotations))
            def selected_route(request: dict[str, Any]) -> dict[str, Any]:
                """Preview ordinary routes before their explicit authorized execute."""
                return adapter.invoke(route, request)
        add_route(route_name)

    def release_version(request: DirectLocalReleaseRequest) -> dict[str, Any]:
        """Run only the connected Project's direct local release."""
        return adapter.invoke(_OPTIONAL_RELEASE_ROUTE_NAME, request)

    def public_release(request: DirectPublicReleaseRequest) -> dict[str, Any]:
        """Run only the connected Project's public release with its supplied draft."""
        return adapter.invoke(_OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME, request)

    def get_selected_workflow_run(request: dict[str, Any]) -> dict[str, Any]:
        """Read one saved selected Workflow Run without dispatch."""
        return adapter.get_workflow_run(request)

    def get_selected_action_run(request: dict[str, Any]) -> dict[str, Any]:
        """Read one saved selected Action Run without dispatch."""
        return adapter.get_action_run(request)

    controls = {
        _OPTIONAL_RELEASE_ROUTE_NAME: (release_version, release_annotations),
        _OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME: (public_release, release_annotations),
        "get_selected_workflow_run": (get_selected_workflow_run, observation_annotations),
        "get_selected_action_run": (get_selected_action_run, observation_annotations),
    }
    for name in sorted(controls.keys() - tool_blacklist):
        handler, tool_annotations = controls[name]
        server.tool(name=name, structured_output=True, annotations=tool_annotations)(handler)
    return adapter
