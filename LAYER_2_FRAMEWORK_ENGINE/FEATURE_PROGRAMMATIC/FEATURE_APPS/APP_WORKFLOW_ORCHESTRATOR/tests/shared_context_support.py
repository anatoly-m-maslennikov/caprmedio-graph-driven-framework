from __future__ import annotations
import hashlib
import re
from pathlib import Path
from typing import Any, Mapping

_ATOM = re.compile(r'^atom_id: "?([^"\\n]+)"?$', re.MULTILINE)
_VERSION = re.compile(r'^version: "?([0-9]+)"?$', re.MULTILINE)


class CurrentFixtureError(RuntimeError):
    pass


def checked_bytes(root: Path, relative_path: str, expected: str, label: str) -> bytes:
    try:
        raw = (root / relative_path).read_bytes()
    except OSError as error:
        raise CurrentFixtureError(f"fixture source is unavailable: {label}") from error
    if hashlib.sha256(raw).hexdigest() != expected:
        raise CurrentFixtureError(f"fixture source digest changed: {label}")
    return raw


def support_rows(inventory: Mapping[str, Any]) -> tuple[Mapping[str, Any], ...]:
    groups = [inventory["required_authority"]]
    groups.extend(
        inventory["applicable_rde"][key] for key in ("requirements", "deliveries", "evaluations")
    )
    selected: dict[str, Mapping[str, Any]] = {}
    for group in groups:
        for row in group:
            selected[str(row["atom_id"])] = row
    return tuple(selected.values())


def support_source_bytes(root: Path, inventory: Mapping[str, Any], atom_id: str) -> bytes:
    matches = [row for row in support_rows(inventory) if row.get("atom_id") == atom_id]
    if len(matches) != 1:
        raise CurrentFixtureError(f"support source is not unique: {atom_id}")
    row = matches[0]
    return checked_bytes(root, str(row["fixture_path"]), row["sha256"], atom_id)


def method_source_bytes(root: Path, inventory: Mapping[str, Any], atom_id: str) -> bytes:
    matches = [
        row for row in inventory["method_projection"]["sources"] if row.get("atom_id") == atom_id
    ]
    if len(matches) != 1:
        raise CurrentFixtureError(f"method source is not unique: {atom_id}")
    row = matches[0]
    return checked_bytes(root, str(row["fixture_path"]), row["sha256"], atom_id)


def method_projection_content(root: Path, inventory: Mapping[str, Any]) -> str:
    spec = inventory["method_projection"]
    raw = checked_bytes(
        root, str(spec["fixture_path"]), spec["content_sha256"], "method_projection"
    )
    return raw.decode("utf-8")


def verify_identity(raw: bytes, pin: Mapping[str, Any]) -> None:
    text = raw.decode("utf-8")
    atom = _ATOM.search(text)
    version = _VERSION.search(text)
    if atom is None or atom.group(1).strip('"') != pin.get("atom_id"):
        raise CurrentFixtureError("fixture source Atom identity is inconsistent")
    if version is None or int(version.group(1)) != pin.get("version"):
        raise CurrentFixtureError("fixture source version is inconsistent")
