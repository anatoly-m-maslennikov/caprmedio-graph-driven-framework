"""Read D613's closed public-release source admission without changing a manifest.

This reader is deliberately not an admission writer, route registrar, or
publication command.  It only derives the one source-controlled record that a
separate canonical-manifest owner may validate before its existing processing.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
from typing import Any, Mapping


AUTHORITY_REF = (
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "201_FEATURE_TOOLS/07_delivery/CA-D-613-TOOLS-DELIVERY--serialize-public-release-workflow-bindings.md"
)
AUTHORITY_PIN = {
    "atom_id": "CA-D-613", "version": 4, "source_path": AUTHORITY_REF,
    "digest": "e34709070c0687946907a0d73457d8d64fe96319a98a4ddaa4aae2233193f091",
}
_PIN_FIELDS = frozenset({"atom_id", "version", "source_path", "digest"})
_RECORD_FIELDS = frozenset({
    "route", "acceptance_frontier", "workflow", "ordered_steps", "ordered_actions",
    "rmed_frontier", "mutation_capable", "native_action_calls",
})
_RMED_COLLECTIONS = ("requirements", "methods", "evaluations", "deliveries")
_RMED_CARDINALITIES = (("requirements", 10), ("methods", 5), ("evaluations", 10), ("deliveries", 9))
_ATOM = re.compile(r"CA-[A-Z]+-[0-9]+")
_DIGEST = re.compile(r"[0-9a-f]{64}")
_MAX_SOURCE_BYTES = 1024 * 1024


class PublicReleaseSourceAdmissionError(ValueError):
    """D613 does not support the requested closed source admission."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


def _reject(message: str, *, code: str = "public-release-source-admission-invalid") -> None:
    raise PublicReleaseSourceAdmissionError(code, message)


def _project_root(root: str | Path) -> Path:
    try:
        project = Path(root).resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise PublicReleaseSourceAdmissionError(
            "public-release-project-unavailable", "Project root is unavailable"
        ) from error
    if not project.is_dir():
        _reject("Project root must be a directory", code="public-release-project-unavailable")
    return project


def _pin_shape(value: Any) -> dict[str, Any]:
    if not isinstance(value, Mapping) or set(value) != _PIN_FIELDS:
        _reject("each source pin must have exactly atom_id, version, source_path and digest")
    atom_id, version, source_path, digest = (
        value[field] for field in ("atom_id", "version", "source_path", "digest")
    )
    if not isinstance(atom_id, str) or _ATOM.fullmatch(atom_id) is None:
        _reject("source pin identity is invalid")
    if type(version) is not int or version < 1:
        _reject("source pin version must be a positive integer")
    if not isinstance(digest, str) or _DIGEST.fullmatch(digest) is None:
        _reject("source pin digest must be a lowercase SHA-256")
    if not isinstance(source_path, str) or not source_path or "\\" in source_path or ":" in source_path:
        _reject("source pin path must be a safe Project-relative file")
    path = PurePosixPath(source_path)
    if (not path.parts or path.is_absolute() or source_path != path.as_posix()
            or any(part in {".", ".."} for part in path.parts)):
        _reject("source pin path must be a canonical safe Project-relative file")
    return dict(value)


def _frontmatter(raw: bytes, *, need_status: bool = False) -> dict[str, Any]:
    try:
        lines = raw.decode("utf-8").splitlines()
        if not lines or lines[0] != "---":
            raise ValueError("frontmatter is absent")
        end = lines.index("---", 1)
        fields = ["atom_id", "version"] + (["status"] if need_status else [])
        values: dict[str, Any] = {}
        for field in fields:
            matches = [line.split(":", 1)[1].strip() for line in lines[1:end]
                       if line.startswith(f"{field}:")]
            if len(matches) != 1:
                raise ValueError(f"{field} must occur exactly once")
            value = matches[0]
            if value.startswith('"'):
                value = json.loads(value)
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            values[field] = value
        if not isinstance(values["atom_id"], str) or _ATOM.fullmatch(values["atom_id"]) is None:
            raise ValueError("Atom identity is invalid")
        if (not isinstance(values["version"], str)
                or re.fullmatch(r"[1-9][0-9]*", values["version"]) is None):
            raise ValueError("Revision Version is invalid")
        values["version"] = int(values["version"])
        if need_status and not isinstance(values["status"], str):
            raise ValueError("status is invalid")
        return values
    except (UnicodeDecodeError, ValueError, TypeError, IndexError, json.JSONDecodeError) as error:
        raise PublicReleaseSourceAdmissionError(
            "public-release-source-identity-invalid", "source identity/version frontmatter is invalid"
        ) from error


def _read_pin(root: Path, value: Any, *, need_status: bool = False) -> tuple[bytes, dict[str, Any]]:
    pin = _pin_shape(value)
    relative = PurePosixPath(pin["source_path"])
    cursor = root
    for part in relative.parts:
        cursor /= part
        if cursor.is_symlink():
            _reject(f"source symlinks are not admitted: {relative}", code="public-release-source-path-unsafe")
    try:
        if not cursor.is_file() or cursor.stat().st_size > _MAX_SOURCE_BYTES:
            raise OSError("source is absent or too large")
        raw = cursor.read_bytes()
    except OSError as error:
        raise PublicReleaseSourceAdmissionError(
            "public-release-source-unavailable", f"source pin is unavailable: {relative}"
        ) from error
    if len(raw) > _MAX_SOURCE_BYTES:
        _reject(f"source exceeds the bounded read: {relative}", code="public-release-source-unavailable")
    if hashlib.sha256(raw).hexdigest() != pin["digest"]:
        _reject(f"source pin is stale: {relative}", code="public-release-source-pin-stale")
    metadata = _frontmatter(raw, need_status=need_status)
    if (metadata["atom_id"], metadata["version"]) != (pin["atom_id"], pin["version"]):
        _reject(f"source identity/version differs: {relative}", code="public-release-source-identity-invalid")
    return raw, metadata


def _tables(text: str) -> list[list[list[str]]]:
    tables: list[list[list[str]]] = []
    current: list[list[str]] = []
    for line in text.splitlines():
        if line.startswith("|"):
            current.append([cell.strip() for cell in line.strip("|").split("|")])
        elif current:
            tables.append(current)
            current = []
    if current:
        tables.append(current)
    expected_headers = [
        ["atom_id", "version", "source_path", "sha256", "required_status"],
        ["atom_id", "version", "source_path", "sha256"],
        ["position", "step_atom_id", "step_version", "step_source_path", "step_sha256",
         "action_atom_id", "action_version", "action_source_path", "action_sha256"],
        ["collection", "position", "atom_id", "version", "source_path", "sha256"],
    ]
    if len(tables) != 4 or [table[0] for table in tables] != expected_headers:
        _reject("D613 pin tables cannot be parsed", code="public-release-authority-invalid")
    for table in tables:
        if len(table) < 3 or any(not re.fullmatch(r":?-{3,}:?", cell) for cell in table[1]):
            _reject("D613 pin table separator is malformed", code="public-release-authority-invalid")
    return tables


def _text_pin(atom_id: str, version: str, source_path: str, digest: str) -> dict[str, Any]:
    if re.fullmatch(r"[1-9][0-9]*", version) is None:
        _reject("D613 source pin version is malformed", code="public-release-authority-invalid")
    return _pin_shape({"atom_id": atom_id, "version": int(version),
                       "source_path": source_path.strip("`"), "digest": digest.strip("`")})


def _single_pin(table: list[list[str]], *, acceptance: bool = False) -> tuple[dict[str, Any], str | None]:
    rows = table[2:]
    expected_width = 5 if acceptance else 4
    if len(rows) != 1 or len(rows[0]) != expected_width:
        _reject("D613 singleton pin table is incomplete or ambiguous", code="public-release-authority-invalid")
    row = rows[0]
    pin = _text_pin(*row[:4])
    if acceptance:
        if row[4] != "Done":
            _reject("D613 acceptance status must be exactly Done", code="public-release-authority-invalid")
        return pin, row[4]
    return pin, None


def _paired_pins(table: list[list[str]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rows = table[2:]
    if len(rows) != 5:
        _reject("D613 ordered Step/Action table must have exactly five rows", code="public-release-authority-invalid")
    steps, actions = [], []
    for position, row in enumerate(rows, 1):
        if len(row) != 9 or row[0] != str(position):
            _reject("D613 Step/Action positions are incomplete or reordered", code="public-release-authority-invalid")
        steps.append(_text_pin(*row[1:5]))
        actions.append(_text_pin(*row[5:9]))
    _unique_pins(steps + actions)
    return steps, actions


def _rmed_pins(table: list[list[str]]) -> dict[str, list[dict[str, Any]]]:
    expected_occurrences = [
        (collection, position)
        for collection, cardinality in _RMED_CARDINALITIES
        for position in range(1, cardinality + 1)
    ]
    rows = table[2:]
    if len(rows) != len(expected_occurrences):
        _reject("D613 RMED rows are incomplete or contain extra members", code="public-release-authority-invalid")
    result = {key: [] for key in _RMED_COLLECTIONS}
    for row, (collection, position) in zip(rows, expected_occurrences, strict=True):
        if (len(row) != 6 or row[0] != collection or row[1] != str(position)):
            _reject("D613 RMED row is malformed", code="public-release-authority-invalid")
        result[collection].append(_text_pin(*row[2:]))
    _unique_pins([pin for collection in _RMED_COLLECTIONS for pin in result[collection]])
    return result


def _unique_pins(pins: list[dict[str, Any]]) -> None:
    identities = [(pin["atom_id"], pin["version"], pin["source_path"]) for pin in pins]
    if len(identities) != len(set(identities)):
        _reject("D613 source pins must be unambiguous", code="public-release-authority-invalid")


def _workflow_order(raw: bytes) -> list[tuple[str, str]]:
    tables: list[list[list[str]]] = []
    current: list[list[str]] = []
    for line in raw.decode("utf-8").splitlines():
        if line.startswith("|"):
            current.append([cell.strip() for cell in line.strip("|").split("|")])
        elif current:
            tables.append(current)
            current = []
    if current:
        tables.append(current)
    matches = [table for table in tables if table and table[0] == ["Step", "Action", "Result boundary"]]
    if len(matches) != 1 or len(matches[0]) != 7:
        _reject("public workflow Step/Action declaration is invalid", code="public-release-authority-invalid")
    rows = matches[0][2:]
    if any(len(row) != 3 or _ATOM.fullmatch(row[0]) is None or _ATOM.fullmatch(row[1]) is None for row in rows):
        _reject("public workflow Step/Action declaration is invalid", code="public-release-authority-invalid")
    order = [(row[0], row[1]) for row in rows]
    if len(order) != len(set(order)):
        _reject("public workflow Step/Action declaration is ambiguous", code="public-release-authority-invalid")
    return order


def _record_shape(record: Any) -> dict[str, Any]:
    if not isinstance(record, Mapping) or set(record) != _RECORD_FIELDS:
        _reject("public-release admission record has unknown, shadow, or missing fields")
    if record["route"] != "public.release" or record["mutation_capable"] is not True or record["native_action_calls"] != []:
        _reject("public-release admission record has an invalid closed route declaration")
    _pin_shape(record["acceptance_frontier"])
    _pin_shape(record["workflow"])
    if not isinstance(record["ordered_steps"], list) or not isinstance(record["ordered_actions"], list):
        _reject("public-release ordered pins must be arrays")
    for pin in record["ordered_steps"] + record["ordered_actions"]:
        _pin_shape(pin)
    if not isinstance(record["rmed_frontier"], Mapping) or set(record["rmed_frontier"]) != set(_RMED_COLLECTIONS):
        _reject("public-release RMED frontier has unknown, shadow, or missing fields")
    for key in _RMED_COLLECTIONS:
        pins = record["rmed_frontier"][key]
        if not isinstance(pins, list):
            _reject("public-release RMED collections must be arrays")
        for pin in pins:
            _pin_shape(pin)
    return copy.deepcopy(dict(record))


def derive_public_release_source_admission(root: str | Path) -> dict[str, Any]:
    """Reopen D613 and all 46 current source pins as one closed record."""
    project = _project_root(root)
    authority_raw, _ = _read_pin(project, AUTHORITY_PIN)
    acceptance_table, workflow_table, pairs_table, rmed_table = _tables(authority_raw.decode("utf-8"))
    acceptance, required_status = _single_pin(acceptance_table, acceptance=True)
    workflow, _ = _single_pin(workflow_table)
    steps, actions = _paired_pins(pairs_table)
    rmed = _rmed_pins(rmed_table)
    all_pins = [acceptance, workflow, *steps, *actions,
                *(pin for collection in _RMED_COLLECTIONS for pin in rmed[collection])]
    _unique_pins(all_pins)
    if any(pin["atom_id"] == AUTHORITY_PIN["atom_id"] or pin["source_path"] == AUTHORITY_REF for pin in all_pins):
        _reject("D613 cannot admit itself as source evidence", code="public-release-authority-invalid")
    _, acceptance_metadata = _read_pin(project, acceptance, need_status=True)
    if acceptance_metadata["status"] != required_status:
        _reject("acceptance source is not actually Done", code="public-release-source-status-invalid")
    workflow_raw, _ = _read_pin(project, workflow)
    if _workflow_order(workflow_raw) != [(step["atom_id"], action["atom_id"])
                                        for step, action in zip(steps, actions, strict=True)]:
        _reject("D613 Step/Action table does not match the public workflow", code="public-release-authority-invalid")
    for pin in [*steps, *actions, *(pin for collection in _RMED_COLLECTIONS for pin in rmed[collection])]:
        _read_pin(project, pin)
    return {
        "route": "public.release", "acceptance_frontier": acceptance, "workflow": workflow,
        "ordered_steps": steps, "ordered_actions": actions, "rmed_frontier": rmed,
        "mutation_capable": True, "native_action_calls": [],
    }


def validate_public_release_source_admission(root: str | Path, record: Any) -> dict[str, Any]:
    """Require a caller-supplied public-release record to equal current D613 evidence."""
    candidate = _record_shape(record)
    expected = derive_public_release_source_admission(root)
    if candidate != expected:
        _reject("public-release admission record differs from current D613 source evidence")
    return copy.deepcopy(expected)
