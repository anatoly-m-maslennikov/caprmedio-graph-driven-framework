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
_EXPECTED_V3 = {
    "schema_version": 3,
    "registration_id": "epic1848-current-local-release-frontier-20261010",
    "authorization_ref": ".caprmedio_caprmedio/03_plan/17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles.md",
    "repair_task_id": "CA-P-1866",
    "input_manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
    "input_manifest_sha256": "3b8d7c34376b68b964d7713cace6a4aff90166b265ce053c9a699f36934560dc",
    "input_canonical_manifest_sha256": "0bf0c7000b83af54b25ac4d1729df9858276b8ce2012779dd154a04af80c330e",
    "input_route_count": 16,
    "preserved_route_count": 15,
    "release_frontier": {
        "authority_pin": {
            "atom_id": "CA-D-572",
            "version": 36,
            "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/205_FEATURE_PROJECT_TOOLS/07_delivery/CA-D-572-PROJECT_TOOLS-DELIVERY--serialize-additive-release-route-source-admission.md",
            "digest": "f0f114ed0426b00951c5ea0bfa0d15f1fe08178e17023d97477205a82f729911",
        },
        "route": "release_version",
        "route_occurrences": 1,
        "admission_occurrences": 1,
    },
}
_EXPECTED_V4 = {
    "schema_version": 4,
    "registration_id": "epic1848-exact-three-pin-binding-repair-20261011",
    "authorization_ref": ".caprmedio_caprmedio/03_plan/17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles.md",
    "repair_task_id": "CA-P-1866",
    "input_manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
    "input_manifest_sha256": "bee103e7604ddbe5912bce5ea31d79d18c3e9efbec22bd6557ef0875222b78bf",
    "input_canonical_manifest_sha256": "80b0cecd066fa421608a517b296664580ffe575a56e8dbd4bdb28ea4df682774",
    "input_route_count": 17,
    "pin_occurrences": 3,
    "replacements": [
        {
            "target": "route",
            "route": "update_atom",
            "occurrences": ["native_action_calls[0]"],
            "prior_pin": {
                "atom_id": "CA-O-030", "version": 5,
                "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/09_operations/CA-O-030-TOOLS-ACTION--update-sealed-caprmedio-atom-carriers.md",
                "digest": "99e18ebce351c72e7e6c684455057439209d107faa217a53782e58b8747c7edc",
            },
            "prior_receipt_ref": ".caprmedio_caprmedio/_projection/core-entity-review/stage2/task-1987.receipt.json",
            "current_pin": {
                "atom_id": "CA-O-030", "version": 6,
                "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/09_operations/CA-O-030-TOOLS-ACTION--update-sealed-caprmedio-atom-carriers.md",
                "digest": "19097af83287005dae4d55e4b4da2234acce9e9f92b0f70671afb831bd8b256b",
            },
        },
        {
            "target": "release_source_admission", "route": "release_version", "admission_index": 0,
            "occurrences": ["rmed_frontier[11]"],
            "prior_pin": {
                "atom_id": "CA-M-343", "version": 5,
                "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/205_FEATURE_PROJECT_TOOLS/05_method/CA-M-343-PROJECT_TOOLS-METHOD--discover-run-and-attest-the-declared-release-suite.md",
                "digest": "a9ff112abe8c5834a5f03e5267450cc97a997ecf8e76ff6d6d537a694dc8ddfe",
            },
            "prior_archive_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/205_FEATURE_PROJECT_TOOLS/05_method/archive/CA-M-343-PROJECT_TOOLS-METHOD--discover-run-and-attest-the-declared-release-suite@5.md",
            "current_pin": {
                "atom_id": "CA-M-343", "version": 6,
                "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/205_FEATURE_PROJECT_TOOLS/05_method/CA-M-343-PROJECT_TOOLS-METHOD--discover-run-and-attest-the-declared-release-suite.md",
                "digest": "3cb5cda089a625e451884de2a485e2887839e7dfc37f686170ed591de905aaa1",
            },
        },
        {
            "target": "release_source_admission", "route": "release_version", "admission_index": 0,
            "occurrences": ["rmed_frontier[31]"],
            "prior_pin": {
                "atom_id": "CA-D-579", "version": 7,
                "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/205_FEATURE_PROJECT_TOOLS/07_delivery/CA-D-579-PROJECT_TOOLS-DELIVERY--deliver-the-release-suite-driver-and-junit-report-boundary.md",
                "digest": "58226c140f4dac0d946cad880bbcf55e993edcdbbd9ad65446a5c2ddead94740",
            },
            "prior_archive_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/205_FEATURE_PROJECT_TOOLS/07_delivery/archive/CA-D-579-PROJECT_TOOLS-DELIVERY--deliver-the-release-suite-driver-and-junit-report-boundary@7.md",
            "current_pin": {
                "atom_id": "CA-D-579", "version": 8,
                "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/205_FEATURE_PROJECT_TOOLS/07_delivery/CA-D-579-PROJECT_TOOLS-DELIVERY--deliver-the-release-suite-driver-and-junit-report-boundary.md",
                "digest": "9b140abfd9518daa6842db370c66ee9fc4b6818cbc3856822c582a21c15eb8e4",
            },
        },
    ],
    "expected_manifest_sha256": "6d1e3aaacf33d4c3cb645f9ed46641dac38b6480773a080074bac51249c143f4",
    "expected_selected_binding_digest": "6a3629975109bb402570e20021072a51df9114715ed785eacc6e7479042c9164",
    "expected_canonical_manifest_sha256": "f903ad67c3b92d7edd2415107f467be42bce1c53d259f440ac1fdb513fa69d5f",
}
_EXPECTED_V5 = {
    "schema_version": 5,
    "registration_id": "epic1848-exact-o030-v7-binding-repair-20261011",
    "authorization_ref": ".caprmedio_caprmedio/03_plan/17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles.md",
    "repair_task_id": "CA-P-1866",
    "input_manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
    "input_manifest_sha256": "6d1e3aaacf33d4c3cb645f9ed46641dac38b6480773a080074bac51249c143f4",
    "input_canonical_manifest_sha256": "f903ad67c3b92d7edd2415107f467be42bce1c53d259f440ac1fdb513fa69d5f",
    "input_route_count": 17,
    "pin_occurrences": 1,
    "replacements": [
        {
            "target": "route",
            "route": "update_atom",
            "occurrences": ["native_action_calls[0]"],
            "prior_pin": {
                "atom_id": "CA-O-030", "version": 6,
                "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/09_operations/CA-O-030-TOOLS-ACTION--update-sealed-caprmedio-atom-carriers.md",
                "digest": "19097af83287005dae4d55e4b4da2234acce9e9f92b0f70671afb831bd8b256b",
            },
            "prior_archive_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/09_operations/archive/CA-O-030-TOOLS-ACTION--update-sealed-caprmedio-atom-carriers@6.md",
            "current_pin": {
                "atom_id": "CA-O-030", "version": 7,
                "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/09_operations/CA-O-030-TOOLS-ACTION--update-sealed-caprmedio-atom-carriers.md",
                "digest": "c2d70fa275a075d2fbc978cab246158cfd8413cec88716521336736d0bf060cc",
            },
        },
    ],
    "expected_manifest_sha256": "f898d30aeabe712ee8ae2545d732e6acde94efc8a5597db11229380937fbff52",
    "expected_selected_binding_digest": "cd05362d6f805902cf922151bc5135a91cb7ef267b0e85bfadf8e5d265a09284",
    "expected_canonical_manifest_sha256": "2c1bd6a93b1362fe1b2a457c2f5bf413a825748825027e607bb4d0f17ec55e25",
}
_EXPECTED_BY_SCHEMA = {1: _EXPECTED_V1, 2: _EXPECTED_V2, 3: _EXPECTED_V3, 4: _EXPECTED_V4, 5: _EXPECTED_V5}

_EXPECTED_O030_RECEIPT = {
    "task": "CA-P-1987",
    "checks": "PASS: exact IDs, owner/status, Summary preserved, Version+1 and canonical body headings; full packet acceptance remains CA-P-1981",
    "files": [
        {
            "atom_id": "CA-O-030",
            "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/09_operations/CA-O-030-TOOLS-ACTION--update-sealed-caprmedio-atom-carriers.md",
            "before_version": 5,
            "after_version": 6,
            "before_sha256": "99e18ebce351c72e7e6c684455057439209d107faa217a53782e58b8747c7edc",
            "after_sha256": "19097af83287005dae4d55e4b4da2234acce9e9f92b0f70671afb831bd8b256b",
        },
        {
            "atom_id": "CA-O-046",
            "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_SEARCH/09_operations/CA-O-046-ATOM_SEARCH-ACTION--search-caprmedio-atom-carriers.md",
            "before_version": 3,
            "after_version": 4,
            "before_sha256": "66528adfb7b6af7570b10af158a4855f74f0c956650d5cefea81fff067aa21a6",
            "after_sha256": "6e8194cc18c0377344b785d8bf89897c8c785aa83cd1eb51e32cf1d479a6bfe5",
        },
    ],
}


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
    if value["schema_version"] in {1, 2} and type(value["pin_occurrences"]) is not int:
        raise RegisteredSourceRefreshError("registration schema version and occurrence count must be strict integers")
    if value["schema_version"] == 1:
        for field in ("prior_pin", "current_pin", "requirement_pin"):
            _validate_pin_shape(value[field])
    elif value["schema_version"] == 2:
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
    elif value["schema_version"] == 3:
        if (type(value["input_route_count"]) is not int
                or type(value["preserved_route_count"]) is not int
                or value["input_route_count"] != len(SELECTED_ROUTE_NAMES) + 1
                or value["preserved_route_count"] != len(SELECTED_ROUTE_NAMES)):
            raise RegisteredSourceRefreshError("schema-3 route counts are invalid")
        frontier = value["release_frontier"]
        if (not isinstance(frontier, Mapping)
                or set(frontier) != {"authority_pin", "route", "route_occurrences", "admission_occurrences"}
                or not isinstance(frontier["route"], str)
                or type(frontier["route_occurrences"]) is not int
                or type(frontier["admission_occurrences"]) is not int
                or frontier["route_occurrences"] != 1
                or frontier["admission_occurrences"] != 1):
            raise RegisteredSourceRefreshError("schema-3 Release frontier shape is invalid")
        _validate_pin_shape(frontier["authority_pin"])
    elif value["schema_version"] == 4:
        if (type(value["input_route_count"]) is not int
                or type(value["pin_occurrences"]) is not int
                or value["input_route_count"] != len(SELECTED_ROUTE_NAMES) + 2
                or value["pin_occurrences"] != 3):
            raise RegisteredSourceRefreshError("schema-4 route or pin occurrence count is invalid")
        rows = value["replacements"]
        if not isinstance(rows, list) or len(rows) != value["pin_occurrences"]:
            raise RegisteredSourceRefreshError("schema-4 replacement rows are invalid")
        expected_locations = (
            ("route", "update_atom", None, ["native_action_calls[0]"],
             {"target", "route", "occurrences", "prior_pin", "prior_receipt_ref", "current_pin"}),
            ("release_source_admission", "release_version", 0, ["rmed_frontier[11]"],
             {"target", "route", "admission_index", "occurrences", "prior_pin", "prior_archive_path", "current_pin"}),
            ("release_source_admission", "release_version", 0, ["rmed_frontier[31]"],
             {"target", "route", "admission_index", "occurrences", "prior_pin", "prior_archive_path", "current_pin"}),
        )
        for row, (target, route, index, occurrences, fields) in zip(rows, expected_locations, strict=True):
            if (not isinstance(row, Mapping) or set(row) != fields
                    or row.get("target") != target or row.get("route") != route
                    or row.get("occurrences") != occurrences):
                raise RegisteredSourceRefreshError("schema-4 replacement row shape is invalid")
            if index is None:
                if not isinstance(row["prior_receipt_ref"], str):
                    raise RegisteredSourceRefreshError("schema-4 O030 receipt reference is invalid")
            elif type(row.get("admission_index")) is not int or row["admission_index"] != index or not isinstance(row["prior_archive_path"], str):
                raise RegisteredSourceRefreshError("schema-4 Release replacement location is invalid")
            _validate_pin_shape(row["prior_pin"])
            _validate_pin_shape(row["current_pin"])
    else:
        if (type(value["input_route_count"]) is not int
                or type(value["pin_occurrences"]) is not int
                or value["input_route_count"] != len(SELECTED_ROUTE_NAMES) + 2
                or value["pin_occurrences"] != 1):
            raise RegisteredSourceRefreshError("schema-5 route or pin occurrence count is invalid")
        rows = value["replacements"]
        if not isinstance(rows, list) or len(rows) != 1:
            raise RegisteredSourceRefreshError("schema-5 replacement rows are invalid")
        row = rows[0]
        fields = {"target", "route", "occurrences", "prior_pin", "prior_archive_path", "current_pin"}
        if (not isinstance(row, Mapping) or set(row) != fields
                or row.get("target") != "route" or row.get("route") != "update_atom"
                or row.get("occurrences") != ["native_action_calls[0]"]
                or not isinstance(row.get("prior_archive_path"), str)):
            raise RegisteredSourceRefreshError("schema-5 replacement row shape is invalid")
        _validate_pin_shape(row["prior_pin"])
        _validate_pin_shape(row["current_pin"])
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


def _derive_schema3_successor(
    manifest: Mapping[str, Any], registered: Mapping[str, Any], *,
    release_route: Mapping[str, Any], release_admission: Mapping[str, Any],
) -> dict[str, Any]:
    """Replace only the one current Release route and its sole admission."""
    if (not isinstance(manifest, Mapping) or not isinstance(manifest.get("routes"), list)
            or not isinstance(release_route, Mapping) or not isinstance(release_admission, Mapping)):
        raise RegisteredSourceRefreshError("schema-3 refresh input or Release frontier is malformed")
    frontier = registered["release_frontier"]
    if (release_route.get("route") != frontier["route"]
            or release_admission.get("route") != frontier["route"]):
        raise RegisteredSourceRefreshError("current Release frontier does not match the registration")
    candidate = copy.deepcopy(dict(manifest))
    routes = candidate["routes"]
    expected_names = [*SELECTED_ROUTE_NAMES, frontier["route"]]
    if (len(routes) != registered["input_route_count"]
            or [row.get("route") if isinstance(row, Mapping) else None for row in routes] != expected_names):
        raise RegisteredSourceRefreshError("schema-3 input route registry differs")
    admissions = candidate.get("release_source_admissions")
    if (not isinstance(admissions, list)
            or len(admissions) != frontier["admission_occurrences"]):
        raise RegisteredSourceRefreshError("schema-3 Release admission occurrence count differs")
    release_indexes = [index for index, row in enumerate(routes)
                       if isinstance(row, Mapping) and row.get("route") == frontier["route"]]
    if len(release_indexes) != frontier["route_occurrences"]:
        raise RegisteredSourceRefreshError("schema-3 Release route occurrence count differs")
    before_preserved = copy.deepcopy(routes[:registered["preserved_route_count"]])
    before_freshness = copy.deepcopy(candidate.get("source_freshness"))
    candidate["routes"][release_indexes[0]] = copy.deepcopy(dict(release_route))
    candidate["release_source_admissions"] = [copy.deepcopy(dict(release_admission))]
    candidate = _recompute_manifest_digests(candidate)
    if candidate["routes"][:registered["preserved_route_count"]] != before_preserved:
        raise RegisteredSourceRefreshError("schema-3 changed a preserved route")
    if not isinstance(before_freshness, Mapping) or not isinstance(candidate.get("source_freshness"), Mapping):
        raise RegisteredSourceRefreshError("schema-3 input source freshness is malformed")
    for field, value in before_freshness.items():
        if field != "selected_binding_digest" and candidate["source_freshness"].get(field) != value:
            raise RegisteredSourceRefreshError("schema-3 changed source registry freshness")
    return candidate


def _validate_schema4_receipt(root: Path, replacement: Mapping[str, Any]) -> None:
    """Require the closed CA-P-1987 evidence for the one O030 transition."""
    receipt = _safe_regular(root, str(replacement["prior_receipt_ref"]), label="registered O030 prior receipt")
    try:
        value = json.loads(receipt.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, RegisteredSourceRefreshError) as error:
        raise RegisteredSourceRefreshError("registered O030 prior receipt is invalid") from error
    if value != _EXPECTED_O030_RECEIPT:
        raise RegisteredSourceRefreshError("registered O030 prior receipt differs")


def _validate_schema4_prior_archive(root: Path, replacement: Mapping[str, Any]) -> None:
    """Confirm prior Release history without treating Archived bytes as active bytes."""
    archive = _safe_regular(root, str(replacement["prior_archive_path"]), label="registered prior archive")
    try:
        text = archive.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        raise RegisteredSourceRefreshError("registered prior archive is unreadable") from error
    prior = replacement["prior_pin"]
    if (_frontmatter_value(text, "atom_id") != prior["atom_id"]
            or _frontmatter_value(text, "version") != str(prior["version"])
            or _frontmatter_value(text, "status") != "Archived"):
        raise RegisteredSourceRefreshError("registered prior archive metadata differs")


def _schema4_route(candidate: dict[str, Any], route_name: str) -> dict[str, Any]:
    routes = candidate.get("routes")
    expected_names = [*SELECTED_ROUTE_NAMES, "release_version", "public.release"]
    if (not isinstance(routes, list)
            or [row.get("route") if isinstance(row, Mapping) else None for row in routes] != expected_names):
        raise RegisteredSourceRefreshError("schema-4 input route registry differs")
    route = routes[expected_names.index(route_name)]
    if not isinstance(route, dict):
        raise RegisteredSourceRefreshError("schema-4 registered route is unavailable")
    return route


def _schema4_replacement_target(candidate: dict[str, Any], replacement: Mapping[str, Any]) -> tuple[Any, Any]:
    """Resolve only the three registered schema-4 Pin locations."""
    target = replacement["target"]
    if target == "route":
        route = _schema4_route(candidate, replacement["route"])
        calls = route.get("native_action_calls")
        if replacement["occurrences"] != ["native_action_calls[0]"] or not isinstance(calls, list) or not calls:
            raise RegisteredSourceRefreshError("schema-4 O030 replacement location is unavailable")
        return calls, 0
    admissions = candidate.get("release_source_admissions")
    if (target != "release_source_admission" or replacement["route"] != "release_version"
            or replacement["admission_index"] != 0 or not isinstance(admissions, list)
            or len(admissions) != 1 or not isinstance(admissions[0], dict)
            or admissions[0].get("route") != "release_version"):
        raise RegisteredSourceRefreshError("schema-4 Release replacement location is unavailable")
    frontier = admissions[0].get("rmed_frontier")
    occurrence = replacement["occurrences"]
    if not isinstance(frontier, list) or occurrence not in (["rmed_frontier[11]"], ["rmed_frontier[31]"]):
        raise RegisteredSourceRefreshError("schema-4 Release replacement location is unavailable")
    index = 11 if occurrence == ["rmed_frontier[11]"] else 31
    if len(frontier) <= index:
        raise RegisteredSourceRefreshError("schema-4 Release replacement location is unavailable")
    return frontier, index


def _count_exact(value: Any, expected: Mapping[str, Any]) -> int:
    if isinstance(value, Mapping):
        return (1 if dict(value) == dict(expected) else 0) + sum(
            _count_exact(item, expected) for item in value.values()
        )
    if isinstance(value, list):
        return sum(_count_exact(item, expected) for item in value)
    return 0


def _derive_schema4_successor(manifest: Mapping[str, Any], registered: Mapping[str, Any]) -> dict[str, Any]:
    """Derive only the closed O030/M343/D579 seventeen-route successor."""
    if not isinstance(manifest, Mapping) or not isinstance(manifest.get("routes"), list):
        raise RegisteredSourceRefreshError("schema-4 refresh input has no route collection")
    candidate = copy.deepcopy(dict(manifest))
    if len(candidate["routes"]) != registered["input_route_count"]:
        raise RegisteredSourceRefreshError("schema-4 input route count differs")
    _schema4_route(candidate, "update_atom")
    if (not isinstance(candidate.get("query_source_admissions"), list)
            or len(candidate["query_source_admissions"]) != 2
            or not isinstance(candidate.get("public_release_source_admissions"), list)
            or len(candidate["public_release_source_admissions"]) != 1):
        raise RegisteredSourceRefreshError("schema-4 input admission registry differs")
    replacements = registered["replacements"]
    if sum(_count_exact(candidate, row["prior_pin"]) for row in replacements) != registered["pin_occurrences"]:
        raise RegisteredSourceRefreshError("schema-4 registered prior pin occurrence count differs")
    locations: set[tuple[int, int | str]] = set()
    for replacement in replacements:
        owner, key = _schema4_replacement_target(candidate, replacement)
        location = (id(owner), key)
        if location in locations or owner[key] != replacement["prior_pin"]:
            raise RegisteredSourceRefreshError("registered prior pin differs at its schema-4 location")
        locations.add(location)
        owner[key] = copy.deepcopy(replacement["current_pin"])
    candidate = _recompute_manifest_digests(candidate)
    if candidate["source_freshness"]["selected_binding_digest"] != registered["expected_selected_binding_digest"]:
        raise RegisteredSourceRefreshError("schema-4 selected-binding digest differs")
    if candidate["canonical_manifest_sha256"] != registered["expected_canonical_manifest_sha256"]:
        raise RegisteredSourceRefreshError("schema-4 canonical-manifest digest differs")
    payload = (json.dumps(candidate, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    if hashlib.sha256(payload).hexdigest() != registered["expected_manifest_sha256"]:
        raise RegisteredSourceRefreshError("schema-4 serialized manifest digest differs")
    return candidate


def _schema5_route(candidate: dict[str, Any]) -> dict[str, Any]:
    """Resolve the sole schema-5 target; no route discovery is permitted."""
    routes = candidate.get("routes")
    expected_names = [*SELECTED_ROUTE_NAMES, "release_version", "public.release"]
    if (not isinstance(routes, list)
            or [row.get("route") if isinstance(row, Mapping) else None for row in routes] != expected_names):
        raise RegisteredSourceRefreshError("schema-5 input route registry differs")
    route = routes[expected_names.index("update_atom")]
    if not isinstance(route, dict):
        raise RegisteredSourceRefreshError("schema-5 registered route is unavailable")
    return route


def _schema5_replacement_target(candidate: dict[str, Any], replacement: Mapping[str, Any]) -> tuple[list[Any], int]:
    """Resolve only ``update_atom.native_action_calls[0]`` for O030@6 -> @7."""
    if (replacement.get("target") != "route" or replacement.get("route") != "update_atom"
            or replacement.get("occurrences") != ["native_action_calls[0]"]):
        raise RegisteredSourceRefreshError("schema-5 O030 replacement location differs")
    calls = _schema5_route(candidate).get("native_action_calls")
    if not isinstance(calls, list) or len(calls) < 1:
        raise RegisteredSourceRefreshError("schema-5 O030 replacement location is unavailable")
    return calls, 0


def _derive_schema5_successor(manifest: Mapping[str, Any], registered: Mapping[str, Any]) -> dict[str, Any]:
    """Derive the one closed O030@6 -> @7 seventeen-route repair."""
    if not isinstance(manifest, Mapping) or not isinstance(manifest.get("routes"), list):
        raise RegisteredSourceRefreshError("schema-5 refresh input has no route collection")
    candidate = copy.deepcopy(dict(manifest))
    if len(candidate["routes"]) != registered["input_route_count"]:
        raise RegisteredSourceRefreshError("schema-5 input route count differs")
    if (not isinstance(candidate.get("query_source_admissions"), list)
            or len(candidate["query_source_admissions"]) != 2
            or not isinstance(candidate.get("release_source_admissions"), list)
            or len(candidate["release_source_admissions"]) != 1
            or not isinstance(candidate.get("public_release_source_admissions"), list)
            or len(candidate["public_release_source_admissions"]) != 1):
        raise RegisteredSourceRefreshError("schema-5 input admission registry differs")
    replacement = registered["replacements"][0]
    if _count_exact(candidate, replacement["prior_pin"]) != registered["pin_occurrences"]:
        raise RegisteredSourceRefreshError("schema-5 registered prior pin occurrence count differs")
    owner, key = _schema5_replacement_target(candidate, replacement)
    if owner[key] != replacement["prior_pin"]:
        raise RegisteredSourceRefreshError("registered prior pin differs at its schema-5 location")
    owner[key] = copy.deepcopy(replacement["current_pin"])
    candidate = _recompute_manifest_digests(candidate)
    if candidate["source_freshness"]["selected_binding_digest"] != registered["expected_selected_binding_digest"]:
        raise RegisteredSourceRefreshError("schema-5 selected-binding digest differs")
    if candidate["canonical_manifest_sha256"] != registered["expected_canonical_manifest_sha256"]:
        raise RegisteredSourceRefreshError("schema-5 canonical-manifest digest differs")
    payload = (json.dumps(candidate, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    if hashlib.sha256(payload).hexdigest() != registered["expected_manifest_sha256"]:
        raise RegisteredSourceRefreshError("schema-5 serialized manifest digest differs")
    return candidate


def derive_registered_source_successor(
    manifest: Mapping[str, Any], registration: Mapping[str, Any], *,
    release_route: Mapping[str, Any] | None = None,
    release_admission: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Purely derive one closed registered successor without an effect.

    Schemas 1 through 4 are retained for archived fixtures. Current schema 5
    replaces only the one closed O030@6 Pin occurrence below.
    """
    registered = _validate_registration(registration)
    if registered["schema_version"] == 1:
        if release_route is not None or release_admission is not None:
            raise RegisteredSourceRefreshError("schema-1 successor does not accept a Release frontier")
        return _derive_schema1_successor(manifest, registered)
    if registered["schema_version"] == 4:
        if release_route is not None or release_admission is not None:
            raise RegisteredSourceRefreshError("schema-4 successor does not accept a Release frontier")
        return _derive_schema4_successor(manifest, registered)
    if registered["schema_version"] == 5:
        if release_route is not None or release_admission is not None:
            raise RegisteredSourceRefreshError("schema-5 successor does not accept a Release frontier")
        return _derive_schema5_successor(manifest, registered)
    if release_route is None or release_admission is None:
        raise RegisteredSourceRefreshError(
            f"schema-{registered['schema_version']} successor requires the current Release frontier"
        )
    if registered["schema_version"] == 2:
        return _derive_schema2_successor(
            manifest, registered, release_route=release_route, release_admission=release_admission,
        )
    if registered["schema_version"] == 3:
        return _derive_schema3_successor(
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
    elif registration["schema_version"] == 2:
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
    elif registration["schema_version"] == 3:
        try:
            from release_source_admission import AUTHORITY_PIN, derive_release_graph_admission

            frontier = registration["release_frontier"]
            if not isinstance(AUTHORITY_PIN, Mapping) or dict(AUTHORITY_PIN) != frontier["authority_pin"]:
                raise RegisteredSourceRefreshError("current Release authority differs from the registration")
            _validate_current_pin(
                project_root, frontier["authority_pin"], label="registered current Release authority"
            )
            release_route, release_admission = derive_release_graph_admission(project_root)
        except RegisteredSourceRefreshError:
            raise
        except (ImportError, OSError, TypeError, ValueError) as error:
            raise RegisteredSourceRefreshError("current Release frontier is unavailable") from error
        candidate = derive_registered_source_successor(
            manifest, registration, release_route=release_route, release_admission=release_admission,
        )
    elif registration["schema_version"] == 4:
        for replacement in registration["replacements"]:
            if replacement["target"] == "route":
                _validate_schema4_receipt(project_root, replacement)
            else:
                _validate_schema4_prior_archive(project_root, replacement)
            _validate_current_pin(
                project_root, replacement["current_pin"],
                label=f"registered current source for {replacement['prior_pin']['atom_id']}",
            )
        candidate = derive_registered_source_successor(manifest, registration)
    else:
        replacement = registration["replacements"][0]
        _validate_prior_archive(
            project_root, replacement["prior_pin"], replacement["prior_archive_path"],
            label="registered O030 prior archive",
        )
        _validate_current_pin(
            project_root, replacement["current_pin"],
            label="registered current source for CA-O-030",
        )
        candidate = derive_registered_source_successor(manifest, registration)
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
