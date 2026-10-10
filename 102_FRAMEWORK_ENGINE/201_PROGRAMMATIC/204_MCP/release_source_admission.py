"""Read-only D572-derived Release admission for a canonical manifest loader.

This module does not load/write a manifest, validate its self-digest, register a
route, inspect an Operator approval, or create any Run/effect. The owning loader
retains those existing boundaries and calls this check before shared support.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import tomllib
from typing import Any, Mapping


AUTHORITY_REF = (
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "205_FEATURE_PROJECT_TOOLS/07_delivery/"
    "CA-D-572-PROJECT_TOOLS-DELIVERY--serialize-additive-release-route-source-admission.md"
)
AUTHORITY_PIN = {
    "atom_id": "CA-D-572", "version": 36, "source_path": AUTHORITY_REF,
    "digest": "f0f114ed0426b00951c5ea0bfa0d15f1fe08178e17023d97477205a82f729911",
}
_PIN_FIELDS = frozenset({"atom_id", "version", "source_path", "digest"})
_ADMISSION_FIELDS = frozenset({"route", "acceptance_frontier", "workflow", "ordered_steps",
                               "ordered_actions", "rmed_frontier", "mutation_capable",
                               "native_action_calls"})
_ATOM = re.compile(r"CA-[A-Z]+-[0-9]+")
_DIGEST = re.compile(r"[0-9a-f]{64}")
_MAX_SOURCE_BYTES = 1024 * 1024
_RELEASE_STOP_RESULT = "missing, stale, unauthorized, failed, partial, or unsafe result"
_RELEASE_STOP_OUTCOME = "stop with actual evidence; do not clear, copy, retry, or recurse implicitly"
_CONTROL_ROOT = ".caprmedio_caprmedio"
_OPERATIONS_ROOT = f"{_CONTROL_ROOT}/09_operations"
_PROJECT_TOOLS_ROOT = (
    f"{_CONTROL_ROOT}/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "205_FEATURE_PROJECT_TOOLS"
)
_TOOLS_ROOT = (
    f"{_CONTROL_ROOT}/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "201_FEATURE_TOOLS"
)
_RMED_ROOTS = {
    "requirements": f"{_PROJECT_TOOLS_ROOT}/04_requirement",
    "methods": f"{_PROJECT_TOOLS_ROOT}/05_method",
    "evaluations": f"{_PROJECT_TOOLS_ROOT}/06_evaluation",
    "deliveries": f"{_PROJECT_TOOLS_ROOT}/07_delivery",
}
_TOOLS_RMED_ROOTS = {
    "requirements": f"{_TOOLS_ROOT}/04_requirement",
    "methods": f"{_TOOLS_ROOT}/05_method",
    "evaluations": f"{_TOOLS_ROOT}/06_evaluation",
    "deliveries": f"{_TOOLS_ROOT}/07_delivery",
}
_RMED_ROLES = {
    "requirements": "Requirement", "methods": "Method",
    "evaluations": "Evaluation", "deliveries": "Delivery",
}


class ReleaseSourceAdmissionError(ValueError):
    """A closed Release source record cannot be admitted without new authority."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


def _reject(message: str, *, code: str = "release-source-admission-invalid") -> None:
    raise ReleaseSourceAdmissionError(code, message)


def _project_root(root: str | Path) -> Path:
    try:
        project = Path(root).resolve(strict=True)
    except (OSError, ValueError, TypeError) as error:
        raise ReleaseSourceAdmissionError("release-project-unavailable", "Project root is unavailable") from error
    if not project.is_dir():
        _reject("Project root must be a directory", code="release-project-unavailable")
    return project


def _pin_shape(pin: Any) -> dict[str, Any]:
    if not isinstance(pin, Mapping) or set(pin) != _PIN_FIELDS:
        _reject("each source pin must have exactly atom_id, version, source_path and digest")
    atom_id, version, relative, digest = (pin[field] for field in ("atom_id", "version", "source_path", "digest"))
    if not isinstance(atom_id, str) or _ATOM.fullmatch(atom_id) is None:
        _reject("source pin identity is invalid")
    if type(version) is not int or version < 1:
        _reject("source pin version must be a positive integer")
    if not isinstance(digest, str) or _DIGEST.fullmatch(digest) is None:
        _reject("source pin digest must be lowercase SHA-256")
    if not isinstance(relative, str) or not relative or "\\" in relative or ":" in relative:
        _reject("source pin path must be a safe Project-relative file")
    path = PurePosixPath(relative)
    if not path.parts or path.is_absolute() or relative != path.as_posix() or any(part in {".", ".."} for part in path.parts):
        _reject("source pin path must be a canonical safe Project-relative file")
    return dict(pin)


def _metadata(raw: bytes) -> tuple[str, int]:
    try:
        lines = raw.decode("utf-8").splitlines()
        if not lines or lines[0] != "---":
            raise ValueError("frontmatter is absent")
        end = lines.index("---", 1)
        values = {}
        for field in ("atom_id", "version"):
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
        atom_id, version = values["atom_id"], values["version"]
        if not isinstance(atom_id, str) or _ATOM.fullmatch(atom_id) is None:
            raise ValueError("Atom identity is invalid")
        if not isinstance(version, str) or re.fullmatch(r"[1-9][0-9]*", version) is None:
            raise ValueError("Revision Version is not a positive integer")
        return atom_id, int(version)
    except (UnicodeDecodeError, ValueError, TypeError, IndexError) as error:
        raise ReleaseSourceAdmissionError("release-source-identity-invalid", "source identity/version frontmatter is invalid") from error


def _read_pin(root: Path, value: Any, *, atom_source: bool = True) -> bytes:
    pin = _pin_shape(value)
    relative = PurePosixPath(pin["source_path"])
    cursor = root
    for part in relative.parts:
        cursor /= part
        if cursor.is_symlink():
            _reject(f"source symlinks are not admitted: {relative}", code="release-source-path-unsafe")
    try:
        if not cursor.is_file() or cursor.stat().st_size > _MAX_SOURCE_BYTES:
            raise OSError("source file is absent or exceeds the bounded read")
        raw = cursor.read_bytes()
    except OSError as error:
        raise ReleaseSourceAdmissionError("release-source-unavailable", f"source pin is unavailable: {relative}") from error
    if len(raw) > _MAX_SOURCE_BYTES:
        _reject(f"source exceeds the bounded read: {relative}", code="release-source-unavailable")
    if hashlib.sha256(raw).hexdigest() != pin["digest"]:
        _reject(f"source pin is stale: {relative}", code="release-source-pin-stale")
    if atom_source and _metadata(raw) != (pin["atom_id"], pin["version"]):
        _reject(f"source identity/version differs: {relative}", code="release-source-identity-invalid")
    return raw


def _frontmatter(raw: bytes) -> dict[str, str]:
    """Read the small closed subset used to identify an active source Atom."""
    try:
        lines = raw.decode("utf-8").splitlines()
        if not lines or lines[0] != "---":
            raise ValueError("frontmatter is absent")
        end = lines.index("---", 1)
        values: dict[str, str] = {}
        for line in lines[1:end]:
            if not line or line.startswith((" ", "\t", "#")) or ":" not in line:
                continue
            field, value = line.split(":", 1)
            if field in values:
                raise ValueError(f"{field} occurs more than once")
            value = value.strip()
            if value.startswith('"'):
                loaded = json.loads(value)
                if not isinstance(loaded, str):
                    raise ValueError(f"{field} is not a scalar")
                value = loaded
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            values[field] = value
        return values
    except (UnicodeDecodeError, ValueError, TypeError, json.JSONDecodeError) as error:
        raise ReleaseSourceAdmissionError(
            "release-source-identity-invalid", "source frontmatter is malformed"
        ) from error


def _checked_source_root(root: Path, source_root: str) -> tuple[Path, PurePosixPath]:
    if not isinstance(source_root, str) or not source_root:
        _reject("source root must be a nonempty Project-relative path", code="release-source-path-unsafe")
    relative = PurePosixPath(source_root)
    if (relative.is_absolute() or relative.as_posix() != source_root or "\\" in source_root
            or ":" in source_root or any(part in {".", ".."} for part in relative.parts)):
        _reject("source root must be a canonical Project-relative path", code="release-source-path-unsafe")
    allowed = {PurePosixPath(_OPERATIONS_ROOT), *map(PurePosixPath, _RMED_ROOTS.values()),
               *map(PurePosixPath, _TOOLS_RMED_ROOTS.values())}
    if relative not in allowed:
        _reject("source root is outside the declared Project authoring boundary", code="release-source-unregistered")
    path = root.joinpath(*relative.parts)
    cursor = root
    for part in relative.parts:
        cursor /= part
        if cursor.is_symlink():
            _reject("source root contains a symlink", code="release-source-path-unsafe")
    if not path.is_dir():
        _reject("source root is unavailable", code="release-source-unavailable")
    return path, relative


def _registered_scope(root: Path, scope_unit: str, authority_path: str) -> None:
    """Require the current Project structure to register a source authority root."""
    structure = root / _CONTROL_ROOT / "project_structure.toml"
    if structure.is_symlink() or not structure.is_file():
        _reject("Project structure is unavailable", code="release-source-unregistered")
    try:
        document = tomllib.loads(structure.read_text(encoding="utf-8"))
        rows = document.get("scope_units")
        if not isinstance(rows, list):
            raise ValueError("scope_units is absent")
        matches = [row for row in rows if isinstance(row, dict)
                   and row.get("scope_unit_name") == scope_unit
                   and row.get("authority_path") == authority_path]
        if len(matches) != 1:
            raise ValueError("source scope registration is not unique")
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError, ValueError) as error:
        raise ReleaseSourceAdmissionError(
            "release-source-unregistered", "source scope registration is invalid"
        ) from error


def _scan_current_source_root(
    root: Path,
    source_root: str,
    expected_scope: str,
    registered_root: str | None,
) -> tuple[tuple[Path, bytes, dict[str, str]], ...]:
    """Capture one checked source-root snapshot for one admission derivation.

    The snapshot has only derivation lifetime.  It avoids repeatedly walking
    the same declared authoring root while leaving every selected source pin
    physically reopened by ``_read_pin`` below.
    """
    if registered_root is not None:
        _registered_scope(root, expected_scope, registered_root)
    base, _relative_base = _checked_source_root(root, source_root)
    rows: list[tuple[Path, bytes, dict[str, str]]] = []
    for path in sorted(base.rglob("*.md")):
        relative = path.relative_to(root)
        if "archive" in relative.parts:
            continue
        cursor = root
        for part in relative.parts:
            cursor /= part
            if cursor.is_symlink():
                _reject("source Atom path contains a symlink", code="release-source-path-unsafe")
        if not path.is_file() or path.stat().st_size > _MAX_SOURCE_BYTES:
            _reject("source Atom is unavailable", code="release-source-unavailable")
        try:
            raw = path.read_bytes()
        except OSError as error:
            raise ReleaseSourceAdmissionError(
                "release-source-unavailable", "source Atom is unavailable"
            ) from error
        rows.append((path, raw, _frontmatter(raw)))
    return tuple(rows)


class _CurrentSourceIndex:
    """One non-shareable source snapshot used by a single D572 derivation."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self._roots: dict[
            tuple[str, str, str | None], tuple[tuple[Path, bytes, dict[str, str]], ...]
        ] = {}

    def rows(
        self,
        source_root: str,
        expected_scope: str,
        registered_root: str | None,
    ) -> tuple[tuple[Path, bytes, dict[str, str]], ...]:
        key = (source_root, expected_scope, registered_root)
        if key not in self._roots:
            self._roots[key] = _scan_current_source_root(
                self.root, source_root, expected_scope, registered_root
            )
        return self._roots[key]


def resolve_current_source_pin(
    project_root: str | Path,
    atom_id: str,
    *,
    role: str,
    operation_type: str | None = None,
    _source_index: _CurrentSourceIndex | None = None,
) -> dict[str, Any]:
    """Return one physically current, registered active Project source pin.

    ``role`` is the source frontmatter ``content_role``.  ``operation_type``
    is required for Operations atoms and omitted for RMED atoms.  The resolver
    never accepts installed copies, archive candidates, caller-supplied pins,
    or an ambiguous current definition.
    """
    root = _project_root(project_root)
    if _source_index is None:
        _source_index = _CurrentSourceIndex(root)
    elif _source_index.root != root:
        _reject("source index belongs to another Project", code="release-source-unavailable")
    if not isinstance(atom_id, str) or _ATOM.fullmatch(atom_id) is None:
        _reject("source Atom identity is invalid", code="release-source-identity-invalid")
    if role == "Operations":
        if operation_type not in {"Workflow", "Step", "Action"}:
            _reject("Operations source type is required", code="release-source-identity-invalid")
    else:
        if operation_type is not None or role not in set(_RMED_ROLES.values()):
            _reject("RMED source role/type is invalid", code="release-source-identity-invalid")
        family = next(key for key, value in _RMED_ROLES.items() if value == role)
        source_roots = ((_RMED_ROOTS[family], "PROJECT_TOOLS", _PROJECT_TOOLS_ROOT),
                        (_TOOLS_RMED_ROOTS[family], "TOOLS", _TOOLS_ROOT))
    if role == "Operations":
        source_roots = ((_OPERATIONS_ROOT, "caprmedio", None),)
    candidates: list[tuple[Path, bytes, dict[str, str]]] = []
    for source_root, expected_scope, registered_root in source_roots:
        for path, raw, frontmatter in _source_index.rows(source_root, expected_scope, registered_root):
            if frontmatter.get("atom_id") != atom_id or frontmatter.get("status") != "Active":
                continue
            if frontmatter.get("current_scope_unit") != expected_scope:
                _reject("current source Atom has the wrong registered scope", code="release-source-unregistered")
            candidates.append((path, raw, frontmatter))
    if len(candidates) != 1:
        _reject("current source Atom is missing or ambiguous", code="release-source-unregistered")
    path, raw, frontmatter = candidates[0]
    if (frontmatter.get("content_role") != role
            or (role == "Operations" and frontmatter.get("type") != operation_type)):
        _reject("current source Atom has the wrong registered role", code="release-source-unregistered")
    try:
        version = int(frontmatter["version"])
    except (KeyError, ValueError) as error:
        raise ReleaseSourceAdmissionError(
            "release-source-identity-invalid", "current source Atom version is invalid"
        ) from error
    if str(version) != frontmatter["version"] or version < 1:
        _reject("current source Atom version is invalid", code="release-source-identity-invalid")
    relative = path.relative_to(root).as_posix()
    pin = _pin_shape({"atom_id": atom_id, "version": version, "source_path": relative,
                      "digest": hashlib.sha256(raw).hexdigest()})
    # The index is a bounded discovery snapshot, never pin evidence.  Reopen
    # the selected member so every pin reflects bytes available at resolution.
    _read_pin(root, pin)
    return pin


def _tables(text: str) -> list[list[list[str]]]:
    tables, current = [], []
    for line in text.splitlines():
        if line.startswith("|"):
            current.append([cell.strip() for cell in line.strip("|").split("|")])
        elif current:
            tables.append(current)
            current = []
    if current:
        tables.append(current)
    if len(tables) != 3 or [table[0] for table in tables] != [
            ["Atom", "Version", "Source path", "SHA-256"],
            ["Order", "Step pin", "Action pin"],
            ["Atom", "Version", "Source path", "SHA-256"]]:
        _reject("accepted D572 pin tables cannot be parsed", code="release-authority-invalid")
    return tables


def _table_pin(row: list[str]) -> dict[str, Any]:
    if len(row) != 4 or re.fullmatch(r"[1-9][0-9]*", row[1]) is None:
        _reject("D572 source pin table row is malformed", code="release-authority-invalid")
    return _pin_shape({"atom_id": row[0], "version": int(row[1]),
                       "source_path": row[2].strip("`"), "digest": row[3].strip("`")})


def _occurrence_pin(value: str) -> dict[str, Any]:
    match = re.fullmatch(r"(CA-O-[0-9]+)@([1-9][0-9]*) `([^`]+)` `([0-9a-f]{64})`", value)
    if match is None:
        _reject("D572 ordered occurrence is malformed", code="release-authority-invalid")
    return _pin_shape({"atom_id": match[1], "version": int(match[2]),
                       "source_path": match[3], "digest": match[4]})


def _route_serialization_metadata(text: str) -> dict[str, Any]:
    """Read D572's one typed route-serialization declaration, fail closed."""
    matches = re.findall(r"^## Route serialization metadata\n+```json\n(.*?)\n```$", text, re.MULTILINE | re.DOTALL)
    if len(matches) != 1:
        _reject("D572 must define exactly one typed Release route serialization metadata block",
                code="release-authority-invalid")
    try:
        metadata = json.loads(matches[0])
    except json.JSONDecodeError as error:
        raise ReleaseSourceAdmissionError(
            "release-authority-invalid", "D572 Release route serialization metadata is not JSON"
        ) from error
    if (not isinstance(metadata, dict)
            or set(metadata) != {"mutation_capable", "native_action_calls"}
            or type(metadata["mutation_capable"]) is not bool
            or metadata["native_action_calls"] != []):
        _reject("D572 Release route serialization metadata is not the closed typed declaration",
                code="release-authority-invalid")
    if text.count(_GENERIC_STOP_CONTRACT) != 1:
        _reject("D572 does not retain the generic executor catch-all stop contract",
                code="release-authority-invalid")
    return metadata


def _private_carriers(text: str) -> list[dict[str, str]]:
    """D572-only source-byte pins; these add no manifest or request fields."""
    matches = re.findall(r"^## Private implementation carriers\n+```json\n(.*?)\n```$",
                         text, re.MULTILINE | re.DOTALL)
    if len(matches) != 1:
        _reject("D572 must declare exactly one private implementation carrier block",
                code="release-authority-invalid")
    try:
        rows = json.loads(matches[0])
    except json.JSONDecodeError as error:
        raise ReleaseSourceAdmissionError("release-authority-invalid", "D572 private carriers are not JSON") from error
    if not isinstance(rows, list) or not rows:
        _reject("D572 private carriers must be a nonempty ordered source-pin list", code="release-authority-invalid")
    paths = []
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"source_path", "sha256"}:
            _reject("D572 private carrier fields are not closed", code="release-authority-invalid")
        _pin_shape({**AUTHORITY_PIN, "source_path": row["source_path"], "digest": row["sha256"]})
        if (not row["source_path"].startswith("102_FRAMEWORK_ENGINE/")
                or row["source_path"] in {
                    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/release_source_admission.py",
                    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_routes.py"}):
            _reject("D572 private carrier creates an authority cycle or leaves the implementation boundary",
                    code="release-authority-invalid")
        paths.append(row["source_path"])
    if paths != sorted(set(paths)):
        _reject("D572 private carrier paths must be unique and source-path sorted", code="release-authority-invalid")
    return rows


def derive_release_private_carriers(project_root: str | Path) -> list[dict[str, str]]:
    """Reopen the D572-only carrier declarations without changing admission serialization."""
    root = _project_root(project_root)
    text = _read_pin(root, AUTHORITY_PIN).decode("utf-8")
    rows = _private_carriers(text)
    for row in rows:
        _read_pin(root, {**AUTHORITY_PIN, "source_path": row["source_path"], "digest": row["sha256"]},
                  atom_source=False)
    return copy.deepcopy(rows)


def derive_unknown_effect_resolver_authority(project_root: str | Path) -> list[dict[str, Any]]:
    """Read the separate closed recovery-control pins; never extend Release admission."""
    root = _project_root(project_root)
    text = _read_pin(root, AUTHORITY_PIN).decode("utf-8")
    matches = re.findall(
        r"^## Unknown-effect resolver authority\n+\x60\x60\x60json\n(.*?)\n\x60\x60\x60$",
        text, re.MULTILINE | re.DOTALL,
    )
    if len(matches) != 1:
        _reject("D572 must carry exactly one unknown-effect resolver authority block",
                code="release-resolver-authority-invalid")
    try:
        rows = json.loads(matches[0])
    except json.JSONDecodeError as error:
        raise ReleaseSourceAdmissionError(
            "release-resolver-authority-invalid", "resolver authority is not closed JSON"
        ) from error
    ids = ("CA-R-1895", "CA-M-351", "CA-E-594", "CA-D-589")
    if not isinstance(rows, list) or len(rows) != len(ids):
        _reject("resolver authority must contain exactly four ordered pins",
                code="release-resolver-authority-invalid")
    pins = [_pin_shape(row) for row in rows]
    if tuple(pin["atom_id"] for pin in pins) != ids:
        _reject("resolver authority identities or order differ",
                code="release-resolver-authority-invalid")
    derive_release_private_carriers(root)
    for pin in pins:
        _read_pin(root, pin)
    return copy.deepcopy(pins)


def _rmed_membership(text: str) -> list[tuple[str, str]]:
    """Read D572's one ID-only current RMED membership table."""
    tables = _tables_from_text(text)
    matches = [table for table in tables if table and table[0] == ["role", "position", "atom_id"]]
    if len(matches) != 1:
        _reject("D572 must define exactly one ID-only RMED membership table", code="release-authority-invalid")
    rows = matches[0][2:]
    expected_role_order = tuple(_RMED_ROLES)
    memberships: list[tuple[str, str]] = []
    positions = {role: 0 for role in expected_role_order}
    for row in rows:
        if len(row) != 3 or row[0] not in positions or not re.fullmatch(r"[1-9][0-9]*", row[1]):
            _reject("D572 RMED membership row is malformed", code="release-authority-invalid")
        role, position, atom_id = row
        if int(position) != positions[role] + 1 or _ATOM.fullmatch(atom_id) is None:
            _reject("D572 RMED membership order or Atom identity is invalid", code="release-authority-invalid")
        positions[role] += 1
        memberships.append((role, atom_id))
    if not memberships or any(positions[role] == 0 for role in expected_role_order):
        _reject("D572 RMED membership must cover every declared role", code="release-authority-invalid")
    if len({atom_id for _, atom_id in memberships}) != len(memberships):
        _reject("D572 RMED membership contains a duplicate Atom", code="release-authority-invalid")
    return memberships


def _tables_from_text(text: str) -> list[list[list[str]]]:
    tables, current = [], []
    for line in text.splitlines():
        if line.startswith("|"):
            current.append([cell.strip() for cell in line.strip("|").split("|")])
        elif current:
            tables.append(current)
            current = []
    if current:
        tables.append(current)
    return tables


def _workflow_step_pairs(raw: bytes) -> list[tuple[str, str]]:
    """Open the declared Steps table; no inferred or reordered graph is allowed."""
    try:
        text = raw.decode("utf-8")
        tables = _tables_from_text(text)
        matches = [table for table in tables if table and table[0] == ["Step", "Action", "Bound phase"]]
        if len(matches) != 1:
            raise ValueError("Steps table is absent")
        rows = matches[0][2:]
        pairs = [(row[0], row[1]) for row in rows]
        if (len(rows) != 10 or any(len(row) != 3 for row in rows)
                or any(_ATOM.fullmatch(step) is None or _ATOM.fullmatch(action) is None
                       for step, action in pairs)):
            raise ValueError("Steps table is malformed")
        return pairs
    except (UnicodeDecodeError, TypeError, ValueError, IndexError) as error:
        raise ReleaseSourceAdmissionError(
            "release-authority-invalid", "accepted O164 Steps table cannot be parsed"
        ) from error


def _derive_release_source_admission(root: Path, source_index: _CurrentSourceIndex) -> dict[str, Any]:
    """Derive one admission from a single bounded current-source snapshot."""
    text = _read_pin(root, AUTHORITY_PIN).decode("utf-8")
    memberships = _rmed_membership(text)
    workflow = resolve_current_source_pin(
        root, "CA-O-164", role="Operations", operation_type="Workflow", _source_index=source_index
    )
    pairs = _workflow_step_pairs(_read_pin(root, workflow))
    steps = [{
        "step": resolve_current_source_pin(
            root, step, role="Operations", operation_type="Step", _source_index=source_index
        ),
        "action": resolve_current_source_pin(
            root, action, role="Operations", operation_type="Action", _source_index=source_index
        ),
    } for step, action in pairs]
    rmed = [resolve_current_source_pin(root, atom_id, role=_RMED_ROLES[role], _source_index=source_index)
            for role, atom_id in memberships]
    return {"route": "release_version", "acceptance_frontier": copy.deepcopy(workflow),
            "workflow": workflow, "ordered_steps": steps,
            "ordered_actions": [copy.deepcopy(row["action"]) for row in steps],
            "rmed_frontier": rmed, "mutation_capable": True, "native_action_calls": []}


def derive_release_source_admission(project_root: str | Path) -> dict[str, Any]:
    """Derive the one D572@36 admission record from current registered source.

    D572 records only membership and route shape.  Every pin is reopened from
    the active Project authoring carrier, so a stale, missing, renamed, or
    ambiguous source cannot silently reuse an installed or historical pin.
    """
    root = _project_root(project_root)
    return _derive_release_source_admission(root, _CurrentSourceIndex(root))


def _release_workflow_graph(raw: bytes, admission: Mapping[str, Any]) -> dict[str, Any]:
    """Extract the closed route graph from the accepted O164 Workflow source."""
    try:
        text = raw.decode("utf-8")
        sections: dict[str, list[str]] = {"Steps": [], "Transitions": []}
        current: str | None = None
        for line in text.splitlines():
            if line in {"## Steps", "## Transitions"}:
                current = line.removeprefix("## ")
            elif current is not None and line.startswith("## "):
                current = None
            elif current is not None:
                sections[current].append(line)

        def rows(section: str, header: list[str]) -> list[list[str]]:
            table = [[cell.strip() for cell in line.strip("|").split("|")]
                     for line in sections[section] if line.startswith("|")]
            if len(table) < 2 or table[0] != header or not all(set(cell) <= {"-", " ", ":"} for cell in table[1]):
                raise ValueError(f"{section} table header is invalid")
            return table[2:]

        step_rows = rows("Steps", ["Step", "Action", "Bound phase"])
        expected_pairs = [(row["step"]["atom_id"], row["action"]["atom_id"])
                          for row in admission["ordered_steps"]]
        if (len(step_rows) != len(expected_pairs)
                or [(row[0], row[1]) for row in step_rows] != expected_pairs):
            raise ValueError("Steps do not match the accepted occurrence sequence")
        transition_rows = rows("Transitions", ["Step result", "Next step or outcome"])
        if (len(transition_rows) != len(expected_pairs) + 1
                or transition_rows[-1] != [_RELEASE_STOP_RESULT, _RELEASE_STOP_OUTCOME]):
            raise ValueError("Transitions omit or alter the required unmatched-result stop")
        step_ids = [step for step, _ in expected_pairs]
        transitions = []
        for source, row in zip(step_ids, transition_rows[:-1], strict=True):
            event, target = row
            if not event or not target:
                raise ValueError("Transitions contain an empty result edge")
            transitions.append({"from": source, "condition": event, "to": target})
        if (len(transitions) != len(expected_pairs)
                or [edge["from"] for edge in transitions] != step_ids
                or any(edge["to"] not in {*step_ids, "complete"} for edge in transitions)):
            raise ValueError("Transitions do not define the accepted Release graph")
    except (UnicodeDecodeError, KeyError, TypeError, ValueError) as error:
        raise ReleaseSourceAdmissionError(
            "release-authority-invalid", "accepted O164 Workflow graph cannot be parsed"
        ) from error
    return {"entry_step": step_ids[0], "on_result": transitions}


def derive_release_route_graph(project_root: str | Path) -> dict[str, Any]:
    """Derive the exact Release route graph for a future manifest publisher.

    D572 derives O164 and its ten Step/Action occurrences; this helper reads that
    current Workflow source and returns the remaining route fields which a
    publisher must serialize unchanged.  It has no manifest or registry side
    effects.
    """
    return derive_release_graph_admission(project_root)[0]


def derive_release_graph_admission(project_root: str | Path) -> tuple[dict[str, Any], dict[str, Any]]:
    """Return the source-derived closed Release route and its D572 admission.

    The pair is intended for a future publisher.  It is read-only and preserves
    the existing eight-field route schema; the O164 unmatched-result stop is
    validated here rather than serialized as a non-schema route member.
    """
    root = _project_root(project_root)
    admission = _derive_release_source_admission(root, _CurrentSourceIndex(root))
    workflow_raw = _read_pin(root, admission["workflow"])
    graph = _release_workflow_graph(workflow_raw, admission)
    route = {"route": "release_version", "workflow": copy.deepcopy(admission["workflow"]),
             "ordered_steps": copy.deepcopy(admission["ordered_steps"]),
             "ordered_actions": copy.deepcopy(admission["ordered_actions"]), **graph,
             "mutation_capable": admission["mutation_capable"],
             "native_action_calls": copy.deepcopy(admission["native_action_calls"])}
    return route, copy.deepcopy(admission)


def _record_shape(record: Any) -> dict[str, Any]:
    if not isinstance(record, Mapping) or set(record) != _ADMISSION_FIELDS or record["route"] != "release_version":
        _reject("Release admission has unknown, absent or unsupported fields")
    _pin_shape(record["acceptance_frontier"])
    _pin_shape(record["workflow"])
    if type(record["mutation_capable"]) is not bool or record["native_action_calls"] != []:
        _reject("Release admission typed route metadata is invalid")
    for field, count in (("ordered_steps", 10), ("ordered_actions", 10)):
        if not isinstance(record[field], list) or len(record[field]) != count:
            _reject(f"Release admission {field} must contain exactly {count} ordered entries")
    if not isinstance(record["rmed_frontier"], list) or not record["rmed_frontier"]:
        _reject("Release admission rmed_frontier must contain the D572-defined ordered entries")
    for item in record["ordered_steps"]:
        if not isinstance(item, Mapping) or set(item) != {"step", "action"}:
            _reject("Release Step occurrence must have exactly step and action")
        _pin_shape(item["step"])
        _pin_shape(item["action"])
    for pin in [*record["ordered_actions"], *record["rmed_frontier"]]:
        _pin_shape(pin)
    return dict(record)


def validate_release_source_admissions(project_root: str | Path, manifest: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Validate the optional file-level additive record before shared support.

    ``manifest`` is the owner's parsed canonical manifest, not D527's two-field
    request ``definition_manifest``. Overall manifest schema/digest, registry,
    other routes and query admissions remain the existing loader's obligation.
    No Release route means the field must be absent and D572 need not be present.
    """
    if not isinstance(manifest, Mapping) or not isinstance(manifest.get("routes"), list):
        _reject("a parsed canonical manifest route list is required")
    routes = manifest["routes"]
    if len(routes) > 16 or any(not isinstance(route, Mapping) or not isinstance(route.get("route"), str) for route in routes):
        _reject("canonical route identities are malformed or exceed the additive portfolio")
    release = [route for route in routes if route["route"] == "release_version"]
    if not release:
        if "release_source_admissions" in manifest:
            _reject("a manifest without release_version must omit Release admission")
        return []
    if len(release) != 1:
        _reject("canonical manifest must contain exactly one Release route")
    admissions = manifest.get("release_source_admissions")
    if not isinstance(admissions, list) or len(admissions) != 1:
        _reject("Release route requires exactly one source admission")
    actual = _record_shape(admissions[0])
    root = _project_root(project_root)
    expected = _derive_release_source_admission(root, _CurrentSourceIndex(root))
    if actual != expected:
        _reject("Release admission differs from the accepted D572 source frontier")
    # Python considers True == 1; route pins must retain the same strict types
    # as admission pins even when this helper is called before the route loader.
    graph = _release_workflow_graph(_read_pin(root, expected["workflow"]), expected)
    route_shape = {**expected, **{field: release[0].get(field)
                                  for field in ("workflow", "ordered_steps", "ordered_actions")}}
    _record_shape(route_shape)
    for field in ("workflow", "ordered_steps", "ordered_actions"):
        if release[0].get(field) != expected[field]:
            _reject(f"Release admission {field} differs from the selected route")
    for field in ("entry_step", "on_result"):
        if release[0].get(field) != graph[field]:
            _reject(f"Release route {field} differs from the accepted Workflow graph")
    for field in ("native_action_calls", "mutation_capable"):
        if release[0].get(field) != expected[field]:
            _reject(f"Release route {field} differs from the accepted source admission")
    pins = [expected["acceptance_frontier"], expected["workflow"],
            *[pin for row in expected["ordered_steps"] for pin in (row["step"], row["action"])],
            *expected["ordered_actions"], *expected["rmed_frontier"]]
    # This is the current D572 table's unique coverage, not a separately
    # maintained cardinality. Equality above keeps every occurrence and pin
    # exact; the mapping only avoids rereading intentionally repeated Actions.
    for pin in {pin["source_path"]: pin for pin in pins}.values():
        _read_pin(root, pin)
    return [expected]
