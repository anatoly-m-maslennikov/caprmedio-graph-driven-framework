"""Private CA-D-588 derivation for the one registered selected-source refresh."""
from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any, Mapping

from selected_routes import (
    SELECTED_ROUTE_NAMES,
    SelectedRouteError,
    canonical_digest,
    validate_selected_manifest_document,
)


_REGISTRATION_REF = PurePosixPath(
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "204_FEATURE_MCP/07_delivery/"
    "CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh.md"
)
_REGISTRATION_HEADING = "### Accepted source revision"
_DIGEST = re.compile(r"^[0-9a-f]{64}$")
_PIN_FIELDS = frozenset({"atom_id", "version", "source_path", "digest"})
_EXPECTED_V1 = {
    "schema_version": 1,
    "registration_id": "prepared-successors-o128-v4-20261006",
    "authorization_ref": ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations.md",
    "repair_task_id": "CA-P-1799",
    "input_manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
    "input_manifest_sha256": "5ca6c9907a4dffbe84319b7d4e391c6242e1969cfea5902845e50f0bd8ae3012",
    "input_canonical_manifest_sha256": "c0edfd130a32386258397da81796d9efab6c1154b17666419edc988d76efc9ba",
    "routes": ["create_atom", "update_atom", "replace_atom", "change_atom_status"],
    "pin_occurrences": 8,
    "prior_pin": {"atom_id": "CA-O-128", "version": 3, "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md", "digest": "b5d052e97bae6ada98849380199e5c67cbf090900beb33ca202f7872d56301e8"},
    "prior_archive_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes@3.md",
    "current_pin": {"atom_id": "CA-O-128", "version": 4, "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md", "digest": "ea36b940a171676977507d366daca9400825e8685018d9c201c15fc5b97eea1c"},
    "requirement_pin": {"atom_id": "CA-R-1041", "version": 8, "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/REPLACE_ATOM/04_requirement/CA-R-1041-TOOLS--coordinate-atom-replacement-intent.md", "digest": "45a87fc9dbb416111b66b22875c844abcce0cd362f0a421190406897413bd9bc"},
}

_EXPECTED_V2 = {
    "schema_version": 2,
    "registration_id": "epic1848-graph-successors-release-frontier-20261010",
    "authorization_ref": ".caprmedio_caprmedio/03_plan/17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles.md",
    "repair_task_id": "CA-P-1866",
    "input_manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
    "input_manifest_sha256": "dc75baa2d7748ced0683067e5de0047b09bc990b842355334cc877e7f6df4839",
    "input_canonical_manifest_sha256": "f944ead9f582956a1d74b6cbe07255d09586ddb13cb7ef01687992bc1a23a8f5",
    "pin_occurrences": 4,
    "replacements": [
        {
            "route": "build_entities_graph",
            "occurrences": ["ordered_steps[0].action", "ordered_actions[0]"],
            "prior_pin": {
                "atom_id": "CA-O-134",
                "version": 2,
                "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-134-CORE_META_MODEL-ACTION--construct-entities-graph-projection.md",
                "digest": "b94eebdd85eab9f7080680e85999c68022e82cdfa7945bf0d840b429ebad037a",
            },
            "prior_archive_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-134-CORE_META_MODEL-ACTION--construct-entities-graph-projection@2.md",
            "current_pin": {
                "atom_id": "CA-O-134",
                "version": 3,
                "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-134-CORE_META_MODEL-ACTION--construct-entities-graph-projection.md",
                "digest": "8a3dcb7cfdb3369ec268726cc54f3f0e0c1bfbc947841792deb87bb844245414",
            },
        },
        {
            "route": "build_terms_graph",
            "occurrences": ["ordered_steps[0].action", "ordered_actions[0]"],
            "prior_pin": {
                "atom_id": "CA-O-137",
                "version": 2,
                "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-137-CORE_META_MODEL-ACTION--construct-terms-graph-projection.md",
                "digest": "6c154852b99df16961fe63c8fd869dbf86f8d75ecc950b25b189e41c3c1c5dad",
            },
            "prior_archive_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-137-CORE_META_MODEL-ACTION--construct-terms-graph-projection@2.md",
            "current_pin": {
                "atom_id": "CA-O-137",
                "version": 3,
                "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-137-CORE_META_MODEL-ACTION--construct-terms-graph-projection.md",
                "digest": "8ea08ef172a82515db7f145bf642a3943ecc41fc6decf4a86a69bea78ce494fd",
            },
        },
    ],
    "release_frontier": {
        "authority_atom_id": "CA-D-572",
        "route": "release_version",
        "admission_occurrences": 1,
    },
}
_EXPECTED_BY_SCHEMA = {1: _EXPECTED_V1, 2: _EXPECTED_V2}


class RegisteredSourceRefreshError(ValueError):
    """The closed registration or its exact successor is unavailable."""


def _project_root(root: str | Path | None) -> Path:
    try:
        value = Path(root) if root is not None else Path(__file__).resolve().parents[3]
        value = value.resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise RegisteredSourceRefreshError("Project root is unavailable") from error
    if value.is_symlink() or not value.is_dir():
        raise RegisteredSourceRefreshError("Project root is unavailable")
    return value


def _safe_regular(root: Path, reference: str | PurePosixPath, *, label: str) -> Path:
    relative = PurePosixPath(reference)
    if relative.is_absolute() or not relative.parts or any(part in {"", ".", ".."} for part in relative.parts):
        raise RegisteredSourceRefreshError(f"{label} is not a safe Project-relative carrier")
    cursor = root
    try:
        for part in relative.parts:
            cursor /= part
            if cursor.is_symlink():
                raise RegisteredSourceRefreshError(f"{label} has a symlinked ancestor")
        if not cursor.is_file():
            raise RegisteredSourceRefreshError(f"{label} is unavailable")
    except OSError as error:
        raise RegisteredSourceRefreshError(f"{label} is unavailable") from error
    return cursor


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise RegisteredSourceRefreshError("registration JSON contains a duplicate key")
        value[key] = item
    return value


def _validate_registration(value: Any) -> dict[str, Any]:
    if not isinstance(value, Mapping) or type(value.get("schema_version")) is not int:
        raise RegisteredSourceRefreshError("registration is not a closed CA-D-588 authority revision")
    expected = _EXPECTED_BY_SCHEMA.get(value["schema_version"])
    if expected is None or dict(value) != expected:
        raise RegisteredSourceRefreshError("registration is not the one closed CA-D-588 authority revision")
    # Keep these checks explicit so future edits cannot accidentally make bool an integer.
    if type(value["pin_occurrences"]) is not int:
        raise RegisteredSourceRefreshError("registration schema version and occurrence count must be strict integers")
    if value["schema_version"] == 1:
        for field in ("prior_pin", "current_pin", "requirement_pin"):
            _validate_pin_shape(value[field])
    else:
        rows = value["replacements"]
        if not isinstance(rows, list) or len(rows) != 2:
            raise RegisteredSourceRefreshError("schema-2 replacement rows are invalid")
        for row in rows:
            if (not isinstance(row, Mapping)
                    or set(row) != {"route", "occurrences", "prior_pin", "prior_archive_path", "current_pin"}
                    or not isinstance(row["route"], str)
                    or not isinstance(row["occurrences"], list)
                    or not all(isinstance(item, str) for item in row["occurrences"])
                    or not isinstance(row["prior_archive_path"], str)):
                raise RegisteredSourceRefreshError("schema-2 replacement row shape is invalid")
            _validate_pin_shape(row["prior_pin"])
            _validate_pin_shape(row["current_pin"])
        frontier = value["release_frontier"]
        if (not isinstance(frontier, Mapping)
                or set(frontier) != {"authority_atom_id", "route", "admission_occurrences"}
                or not isinstance(frontier["authority_atom_id"], str)
                or not isinstance(frontier["route"], str)
                or type(frontier["admission_occurrences"]) is not int):
            raise RegisteredSourceRefreshError("schema-2 Release frontier shape is invalid")
    return copy.deepcopy(dict(value))


def _validate_pin_shape(value: Any) -> None:
    if (not isinstance(value, Mapping) or set(value) != _PIN_FIELDS
            or not isinstance(value["atom_id"], str)
            or type(value["version"]) is not int
            or not isinstance(value["source_path"], str)
            or not isinstance(value["digest"], str)
            or _DIGEST.fullmatch(value["digest"]) is None):
        raise RegisteredSourceRefreshError("registration pin shape is invalid")


def registered_source_refresh(root: str | Path | None = None) -> dict[str, Any]:
    """Read and close the sole D588 JSON registration; callers cannot supply one."""
    project_root = _project_root(root)
    source = _safe_regular(project_root, _REGISTRATION_REF, label="source-refresh registration")
    try:
        text = source.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        raise RegisteredSourceRefreshError("source-refresh registration is unreadable") from error
    match = re.search(rf"(?ms)^{re.escape(_REGISTRATION_HEADING)}\s*\n\s*```json\s*\n(.*?)\n```\s*$", text)
    if match is None:
        raise RegisteredSourceRefreshError("source-refresh registration has no closed JSON object")
    try:
        value = json.loads(match.group(1), object_pairs_hook=_unique_object)
    except (json.JSONDecodeError, RegisteredSourceRefreshError) as error:
        raise RegisteredSourceRefreshError("source-refresh registration JSON is invalid") from error
    return _validate_registration(value)


def _frontmatter_value(text: str, field: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(field)}:\s*[\"']?([^\n\"']+)", text)
    return None if match is None else match.group(1).strip()


def _read_registered_pin(root: Path, pin: Mapping[str, Any], *, label: str, active: bool) -> None:
    path = _safe_regular(root, str(pin["source_path"]), label=label)
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
    except (OSError, UnicodeDecodeError) as error:
        raise RegisteredSourceRefreshError(f"{label} is unreadable") from error
    if hashlib.sha256(raw).hexdigest() != pin["digest"]:
        raise RegisteredSourceRefreshError(f"{label} digest is stale")
    if (_frontmatter_value(text, "atom_id") != pin["atom_id"]
            or _frontmatter_value(text, "version") != str(pin["version"])):
        raise RegisteredSourceRefreshError(f"{label} metadata differs from its registered pin")
    if active and _frontmatter_value(text, "status") != "Active":
        raise RegisteredSourceRefreshError(f"{label} is not Active")


def _validate_current_pin(root: Path, pin: Mapping[str, Any], *, label: str) -> None:
    _read_registered_pin(root, pin, label=label, active=True)


def _validate_prior_archive(root: Path, pin: Mapping[str, Any], archive_path: str, *, label: str) -> None:
    archive_pin = dict(pin)
    archive_pin["source_path"] = archive_path
    _read_registered_pin(root, archive_pin, label=label, active=False)


def _replace_pins(value: Any, *, prior: Mapping[str, Any], current: Mapping[str, Any], allowed_route: bool, count: list[int]) -> Any:
    if isinstance(value, Mapping):
        if dict(value) == dict(prior):
            if not allowed_route:
                raise RegisteredSourceRefreshError("prior pin occurs outside the registered routes")
            count[0] += 1
            return copy.deepcopy(dict(current))
        return {key: _replace_pins(item, prior=prior, current=current, allowed_route=allowed_route, count=count)
                for key, item in value.items()}
    if isinstance(value, list):
        return [_replace_pins(item, prior=prior, current=current, allowed_route=allowed_route, count=count) for item in value]
    return copy.deepcopy(value)


def _recompute_manifest_digests(candidate: dict[str, Any]) -> dict[str, Any]:
    freshness = candidate.get("source_freshness")
    if not isinstance(freshness, Mapping) or "selected_binding_digest" not in freshness:
        raise RegisteredSourceRefreshError("refresh input source freshness is malformed")
    candidate["source_freshness"] = dict(freshness)
    candidate["source_freshness"]["selected_binding_digest"] = canonical_digest(candidate["routes"])
    candidate.pop("canonical_manifest_sha256", None)
    candidate["canonical_manifest_sha256"] = canonical_digest(candidate)
    return candidate


def _derive_schema1_successor(manifest: Mapping[str, Any], registered: Mapping[str, Any]) -> dict[str, Any]:
    """Purely derive the historical eight-pin successor without an effect."""
    if not isinstance(manifest, Mapping) or not isinstance(manifest.get("routes"), list):
        raise RegisteredSourceRefreshError("refresh input has no route collection")
    candidate = copy.deepcopy(dict(manifest))
    route_names = registered["routes"]
    routes = candidate["routes"]
    if [row.get("route") if isinstance(row, Mapping) else None for row in routes].count(None):
        raise RegisteredSourceRefreshError("refresh input route collection is malformed")
    if len({row["route"] for row in routes}) != len(routes):
        raise RegisteredSourceRefreshError("refresh input route registry is duplicate")
    if any(name not in {row["route"] for row in routes} for name in route_names):
        raise RegisteredSourceRefreshError("registered refresh route is unavailable")
    count = [0]
    candidate["routes"] = [
        _replace_pins(row, prior=registered["prior_pin"], current=registered["current_pin"],
                      allowed_route=row["route"] in route_names, count=count)
        for row in routes
    ]
    if count[0] != registered["pin_occurrences"]:
        raise RegisteredSourceRefreshError("registered prior pin occurrence count differs")
    return _recompute_manifest_digests(candidate)


def _schema2_route(candidate: dict[str, Any], route_name: str) -> dict[str, Any]:
    routes = candidate.get("routes")
    expected_names = [*SELECTED_ROUTE_NAMES, "release_version"]
    if (not isinstance(routes, list)
            or [row.get("route") if isinstance(row, Mapping) else None for row in routes] != expected_names):
        raise RegisteredSourceRefreshError("schema-2 input route registry differs")
    matches = [row for row in routes if isinstance(row, dict) and row.get("route") == route_name]
    if len(matches) != 1:
        raise RegisteredSourceRefreshError("registered schema-2 route is unavailable")
    return matches[0]


def _schema2_targets(route: dict[str, Any], occurrences: list[str]) -> list[tuple[Any, Any]]:
    """Resolve only the two closed schema-2 locations; never traverse pins."""
    if occurrences != ["ordered_steps[0].action", "ordered_actions[0]"]:
        raise RegisteredSourceRefreshError("schema-2 replacement locations differ")
    steps = route.get("ordered_steps")
    actions = route.get("ordered_actions")
    if (not isinstance(steps, list) or len(steps) < 1 or not isinstance(steps[0], dict)
            or not isinstance(actions, list) or len(actions) < 1
            or not isinstance(steps[0].get("action"), dict) or not isinstance(actions[0], dict)):
        raise RegisteredSourceRefreshError("schema-2 replacement locations are unavailable")
    return [(steps[0], "action"), (actions, 0)]


def _replace_schema2_rows(candidate: dict[str, Any], registered: Mapping[str, Any]) -> None:
    count = 0
    for row in registered["replacements"]:
        route = _schema2_route(candidate, row["route"])
        for owner, key in _schema2_targets(route, row["occurrences"]):
            if owner[key] != row["prior_pin"]:
                raise RegisteredSourceRefreshError("registered prior pin differs at its schema-2 location")
            owner[key] = copy.deepcopy(row["current_pin"])
            count += 1
    if count != registered["pin_occurrences"]:
        raise RegisteredSourceRefreshError("schema-2 prior pin occurrence count differs")


def _derive_schema2_successor(
    manifest: Mapping[str, Any], registered: Mapping[str, Any], *,
    release_route: Mapping[str, Any], release_admission: Mapping[str, Any],
) -> dict[str, Any]:
    if not isinstance(manifest, Mapping) or not isinstance(manifest.get("routes"), list):
        raise RegisteredSourceRefreshError("refresh input has no route collection")
    if (not isinstance(release_route, Mapping) or release_route.get("route") != registered["release_frontier"]["route"]
            or not isinstance(release_admission, Mapping)
            or release_admission.get("route") != registered["release_frontier"]["route"]):
        raise RegisteredSourceRefreshError("current Release frontier does not match the registration")
    candidate = copy.deepcopy(dict(manifest))
    _replace_schema2_rows(candidate, registered)
    release_route_target = _schema2_route(candidate, registered["release_frontier"]["route"])
    admissions = candidate.get("release_source_admissions")
    if (not isinstance(admissions, list)
            or len(admissions) != registered["release_frontier"]["admission_occurrences"]):
        raise RegisteredSourceRefreshError("schema-2 Release admission occurrence count differs")
    release_index = candidate["routes"].index(release_route_target)
    candidate["routes"][release_index] = copy.deepcopy(dict(release_route))
    candidate["release_source_admissions"] = [copy.deepcopy(dict(release_admission))]
    return _recompute_manifest_digests(candidate)


def derive_registered_source_successor(
    manifest: Mapping[str, Any], registration: Mapping[str, Any], *,
    release_route: Mapping[str, Any] | None = None,
    release_admission: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Purely derive one closed registered successor without an effect.

    Schema 1 is retained for the archived historical fixture.  Schema 2 needs
    the caller to supply the already re-derived D572 route and admission; the
    root-bound reader below is the only production path that obtains them.
    """
    registered = _validate_registration(registration)
    if registered["schema_version"] == 1:
        if release_route is not None or release_admission is not None:
            raise RegisteredSourceRefreshError("schema-1 successor does not accept a Release frontier")
        return _derive_schema1_successor(manifest, registered)
    if release_route is None or release_admission is None:
        raise RegisteredSourceRefreshError("schema-2 successor requires the current Release frontier")
    return _derive_schema2_successor(
        manifest, registered, release_route=release_route, release_admission=release_admission,
    )


def derive_registered_source_refresh(root: str | Path) -> tuple[dict[str, Any], dict[str, Any], bytes, Path]:
    """Open the exact historical input, validate active carriers, and derive its successor."""
    project_root = _project_root(root)
    registration = registered_source_refresh(project_root)
    input_path = _safe_regular(project_root, registration["input_manifest_ref"], label="registered input manifest")
    raw = input_path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != registration["input_manifest_sha256"]:
        raise RegisteredSourceRefreshError("registered input manifest bytes differ")
    try:
        manifest = json.loads(raw, object_pairs_hook=_unique_object)
    except (json.JSONDecodeError, RegisteredSourceRefreshError) as error:
        raise RegisteredSourceRefreshError("registered input manifest is invalid") from error
    if not isinstance(manifest, Mapping) or manifest.get("canonical_manifest_sha256") != registration["input_canonical_manifest_sha256"]:
        raise RegisteredSourceRefreshError("registered input manifest canonical digest differs")
    if registration["schema_version"] == 1:
        _validate_prior_archive(
            project_root, registration["prior_pin"], registration["prior_archive_path"],
            label="registered prior archive",
        )
        _validate_current_pin(project_root, registration["current_pin"], label="registered current Action source")
        _validate_current_pin(project_root, registration["requirement_pin"], label="registered current Requirement source")
        candidate = derive_registered_source_successor(manifest, registration)
    else:
        for row in registration["replacements"]:
            _validate_prior_archive(
                project_root, row["prior_pin"], row["prior_archive_path"],
                label=f"registered prior archive for {row['route']}",
            )
            _validate_current_pin(
                project_root, row["current_pin"], label=f"registered current Action source for {row['route']}",
            )
        try:
            from release_source_admission import AUTHORITY_PIN, derive_release_graph_admission

            if (not isinstance(AUTHORITY_PIN, Mapping)
                    or AUTHORITY_PIN.get("atom_id") != registration["release_frontier"]["authority_atom_id"]):
                raise RegisteredSourceRefreshError("current Release authority differs from the registration")
            release_route, release_admission = derive_release_graph_admission(project_root)
        except RegisteredSourceRefreshError:
            raise
        except (ImportError, OSError, TypeError, ValueError) as error:
            raise RegisteredSourceRefreshError("current Release frontier is unavailable") from error
        candidate = derive_registered_source_successor(
            manifest, registration, release_route=release_route, release_admission=release_admission,
        )
    try:
        validate_selected_manifest_document(project_root, candidate)
    except (OSError, TypeError, ValueError, SelectedRouteError) as error:
        raise RegisteredSourceRefreshError("registered successor does not satisfy the complete selected-manifest contract") from error
    payload = (json.dumps(candidate, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    return dict(manifest), candidate, payload, input_path


__all__ = [
    "RegisteredSourceRefreshError", "registered_source_refresh", "derive_registered_source_successor",
    "derive_registered_source_refresh",
]
