"""Checked-in source bytes for disposable selected-workflow Projects."""
from __future__ import annotations

import copy
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import re
from typing import Any


_CORPUS = Path(__file__).with_name("selected_workflows_golden_corpus.json")
_PREPARATION_BINDING_IDS = (
    "CA-R-866", "CA-R-1093", "CA-O-030", "CA-M-371", "CA-D-425", "CA-E-304",
)


def _advertised_pins(value: object, label: str = "manifest") -> list[tuple[str, dict[str, Any]]]:
    if isinstance(value, dict):
        if {"source_path", "version"} <= set(value) and isinstance(
            value.get("digest") or value.get("sha256"), str
        ):
            return [(label, value)]
        return [pin for key, child in value.items() for pin in _advertised_pins(child, f"{label}.{key}")]
    if isinstance(value, list):
        return [pin for index, child in enumerate(value) for pin in _advertised_pins(child, f"{label}[{index}]")]
    return []


def _validate_source_pins(payload: dict[str, Any]) -> None:
    files = payload["files"]
    pins = _advertised_pins(payload["manifest"])
    pins.extend((f"implementation_bindings[{index}]", {
        "atom_id": row["atom_id"], "source_path": row["path"], "version": row["version"],
        "sha256": row["sha256"],
    }) for index, row in enumerate(payload["implementation_bindings"]))
    for name in ("complete_carrier_authority", "graph_authority", "publication_bindings", "behavior_bindings"):
        pins.extend((f"{name}.{atom_id}", {"atom_id": atom_id, **row})
                    for atom_id, row in payload[name].items())
    pins.append(("base_revise_binding", {
        "atom_id": payload["base_revise_binding"]["atom_id"],
        "source_path": payload["base_revise_binding"]["path"],
        "version": payload["base_revise_binding"]["version"],
        "sha256": payload["base_revise_binding"]["sha256"],
    }))
    bound: dict[str, tuple[str, int, str]] = {}
    for label, pin in pins:
        path, version = pin["source_path"], pin["version"]
        digest = pin.get("digest") or pin.get("sha256")
        raw = files.get(path)
        if not isinstance(path, str) or type(version) is not int or not isinstance(digest, str) or not isinstance(raw, str):
            raise AssertionError("frozen source pin is malformed: " + label)
        header = raw.split("\n---\n", 1)[0]
        match = re.search(r"(?m)^version:\s*[\"']?([0-9]+)[\"']?\s*$", header)
        source_atom_id = re.search(r"(?m)^atom_id:\s*[\"']?([^\"'\s]+)[\"']?\s*$", header)
        atom_id = pin.get("atom_id")
        if (hashlib.sha256(raw.encode("utf-8")).hexdigest() != digest or match is None
                or int(match[1]) != version
                or (isinstance(atom_id, str) and (source_atom_id is None or source_atom_id[1] != atom_id))):
            raise AssertionError("frozen source pin disagrees with its bytes: " + label)
        if isinstance(atom_id, str):
            existing = bound.setdefault(atom_id, (path, version, digest))
            if existing != (path, version, digest):
                raise AssertionError("frozen source pins disagree for Atom: " + atom_id)


@lru_cache(maxsize=1)
def _payload() -> dict[str, Any]:
    payload = json.loads(_CORPUS.read_text(encoding="utf-8"))
    if (payload.get("schema_version") != 1 or not isinstance(payload.get("files"), dict)
            or not isinstance(payload.get("selected_root_paths"), list)
            or not isinstance(payload.get("complete_carrier_authority"), dict)
            or not isinstance(payload.get("graph_authority"), dict)
            or not isinstance(payload.get("publication_bindings"), dict)
            or not isinstance(payload.get("behavior_bindings"), dict)
            or any(identifier not in payload["behavior_bindings"] for identifier in _PREPARATION_BINDING_IDS)):
        raise AssertionError("selected-workflow frozen corpus is malformed")
    selected_root_paths = payload["selected_root_paths"]
    if (len(selected_root_paths) != 177
            or not all(isinstance(path, str) and path in payload["files"] for path in selected_root_paths)
            or len(set(selected_root_paths)) != 177):
        raise AssertionError("selected-workflow frozen root is malformed")
    _validate_source_pins(payload)
    return payload


def frozen_manifest() -> dict[str, Any]:
    """Return the fixed fifteen-route binding projection, never a live read."""
    return copy.deepcopy(_payload()["manifest"])


def frozen_implementation_bindings() -> list[dict[str, Any]]:
    """Return the reviewed W09 binding frontier stored with this corpus."""
    return copy.deepcopy(_payload()["implementation_bindings"])


def frozen_base_revise_binding() -> dict[str, Any]:
    return copy.deepcopy(_payload()["base_revise_binding"])


def frozen_complete_carrier_authority() -> dict[str, dict[str, Any]]:
    """Return static original locators/pins for complete-carrier admission."""
    return copy.deepcopy(_payload()["complete_carrier_authority"])


def frozen_graph_authority() -> dict[str, dict[str, Any]]:
    """Return the remaining fixed graph-admission closure."""
    return copy.deepcopy(_payload()["graph_authority"])


def frozen_publication_bindings() -> dict[str, dict[str, Any]]:
    """Return static publication-carrier pins captured with this corpus."""
    return copy.deepcopy(_payload()["publication_bindings"])


def frozen_behavior_bindings() -> dict[str, dict[str, Any]]:
    """Return the static current-source closure for fixture behavior checks."""
    return copy.deepcopy(_payload()["behavior_bindings"])


def frozen_preparation_bindings() -> dict[str, dict[str, Any]]:
    """Return the six static authorities used by direct Subject preparation."""
    behavior = _payload()["behavior_bindings"]
    return {identifier: copy.deepcopy(behavior[identifier]) for identifier in _PREPARATION_BINDING_IDS}


def frozen_source_paths() -> tuple[str, ...]:
    """List the finite corpus members without reading a Project."""
    return tuple(_payload()["files"])


def frozen_selected_root_paths() -> tuple[str, ...]:
    """List the fixed selected-route root without supplemental behavior inputs."""
    return tuple(_payload()["selected_root_paths"])


def frozen_source_bytes(relative: str | Path, expected_digest: str | None = None) -> bytes:
    """Read one exact frozen carrier by its fixture-Project relative path."""
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts:
        raise AssertionError("frozen source path escapes the corpus")
    value = _payload()["files"].get(path.as_posix())
    if not isinstance(value, str):
        raise AssertionError(f"frozen source is missing: {path.as_posix()}")
    raw = value.encode("utf-8")
    if expected_digest is not None and hashlib.sha256(raw).hexdigest() != expected_digest:
        raise AssertionError(f"frozen source digest changed: {path.as_posix()}")
    return raw


def write_frozen_source(root: Path, relative: str | Path, expected_digest: str | None = None) -> Path:
    """Materialize one static corpus member inside a disposable Project only."""
    path = Path(relative)
    raw = frozen_source_bytes(path, expected_digest)
    destination = root / path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(raw)
    return destination


def frozen_source_root(root: Path) -> Path:
    """Populate and return a finite frozen authority root for a test Project."""
    for relative in frozen_selected_root_paths():
        write_frozen_source(root, relative)
    return root
