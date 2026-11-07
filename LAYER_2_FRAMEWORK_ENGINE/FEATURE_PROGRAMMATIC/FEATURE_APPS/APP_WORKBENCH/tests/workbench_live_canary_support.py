# CA-E-794@2
"""Pure support for the opt-in Workbench live canary."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import shutil
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from uuid import uuid4

from scope_declaration_parse import parse_scope_unit_declaration
from scope_declaration_render import render_scope_declaration
from scope_unit_declarations import read_scope_unit_declarations
from selected_route_manifest import _configured_control_root
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier


class LiveCanaryError(RuntimeError):
    """An explicit live canary preflight or cleanup condition failed."""


@dataclass(frozen=True)
class CanaryScope:
    name: str
    scope_unit_id: str
    atom_id: str
    parent: str
    version: int = 1

    def with_changes(self, **changes: object) -> "CanaryScope":
        return CanaryScope(
            name=str(changes.get("name", self.name)),
            scope_unit_id=str(changes.get("scope_unit_id", self.scope_unit_id)),
            atom_id=str(changes.get("atom_id", self.atom_id)),
            parent=str(changes.get("parent", self.parent)),
            version=int(changes.get("version", self.version)),
        )


def request(url: str, *, method: str = "GET", payload: dict | None = None) -> tuple[int, object]:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    request_data = Request(url, data=body, method=method, headers={"content-type": "application/json"})
    try:
        with urlopen(request_data, timeout=90) as response:  # noqa: S310 -- explicit local canary endpoint
            raw = response.read().decode("utf-8")
            return response.status, json.loads(raw) if response.headers.get_content_type() == "application/json" else raw
    except HTTPError as error:
        with error:
            raw = error.read().decode("utf-8")
        return error.code, json.loads(raw) if raw else {}
    except URLError as error:
        raise LiveCanaryError(f"live Workbench is unavailable: {error.reason}") from error


def atomic_publish(staged: Path, target: Path) -> str:
    if not target.parent.is_dir():
        raise LiveCanaryError(f"parent Scope Unit authority is missing: {target.parent}")
    try:
        os.link(staged, target)
    except FileExistsError as error:
        raise LiveCanaryError(f"canary target appeared before publication: {target}") from error
    staged.unlink()
    return hashlib.sha256(target.read_bytes()).hexdigest()


def atomic_replace(staged: Path, target: Path) -> str:
    if not target.is_file():
        raise LiveCanaryError(f"canary source is missing for replacement: {target}")
    os.replace(staged, target)
    return hashlib.sha256(target.read_bytes()).hexdigest()


def remove_owned_file(path: Path, expected_hash: str) -> None:
    if not path.exists():
        return
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected_hash:
        raise LiveCanaryError(f"refusing to remove externally changed canary Declaration: {path}")
    path.unlink()


def current_atom_id_exists(root: Path, atom_id: str) -> bool:
    ignored = {"archive", "archived", "draft", "drafts"}
    control = _configured_control_root(root)
    control = control if control.is_absolute() else root / control
    prefix = f"{atom_id}-"
    return any(
        path.name.startswith(prefix)
        for path in control.rglob("*.md")
        if not ignored.intersection(part.casefold() for part in path.parts)
    )


def new_scope_unit_id(existing_ids: set[str]) -> str:
    for _ in range(100):
        candidate = f"CA-SU-{900000000 + (uuid4().int % 99_999_999)}"
        if candidate not in existing_ids:
            return candidate
    raise LiveCanaryError("could not allocate an unused numeric Scope Unit ID")


def new_atom_id(root: Path, reserved: set[str]) -> str:
    for _ in range(100):
        candidate = f"CA-R-{900000000 + (uuid4().int % 99_999_999)}"
        if candidate not in reserved and not current_atom_id_exists(root, candidate):
            reserved.add(candidate)
            return candidate
    raise LiveCanaryError("could not allocate an unused Current Atom ID")


def declaration_target(parent_authority: Path, scope: CanaryScope) -> Path:
    return parent_authority / "04_requirement" / f"{scope.atom_id}-{scope.name.casefold()}-scope-unit-declaration.md"


def scope_authority(parent_authority: Path, scope: CanaryScope) -> Path:
    return parent_authority / f"{scope.scope_unit_id}_FEATURE_{scope.name}"


def scope_carrier(scope: CanaryScope, project_name: str, updated_at: str) -> str:
    carrier = render_scope_declaration(
        name=scope.name, project_name=project_name, atom_id=scope.atom_id,
        updated_at=updated_at, scope_id=scope.scope_unit_id, label="FEATURE",
        ordered=False, parent=scope.parent, version=scope.version,
    )
    return carrier.replace(f"## Summary\n\nDeclare {scope.name}\n", "## Summary\n\nDeclare Scope Unit\n")


def atom_carrier(
    atom_id: str,
    version: int,
    *,
    scope: CanaryScope,
    destination: Path,
    root: Path,
) -> str:
    """Return an Atom carrier whose Header matches its current carrier location."""
    relative_destination = destination.relative_to(root)
    return (
        "---\n"
        "identity:\n"
        f"  atom_id: {atom_id}\n"
        f"  ref_id: {atom_id}\n"
        "context:\n"
        "  container:\n"
        f"    scope_unit: {scope.scope_unit_id}\n"
        "  role: Requirement\n"
        "  form: Definition\n"
        f"  scope_unit_name: {scope.name}\n"
        "  topics:\n"
        "    main_subject: Subject/Graph/Node/Project Model/Atom\n"
        "    dependencies: []\n"
        "relations: {}\n"
        "state:\n"
        "  status: Active\n"
        f"  version: {version}\n"
        "  updated_at: '2026-11-06 00:00:00 +0000'\n"
        "destination:\n"
        "  file:\n"
        f"    name: {destination.name}\n"
        f"    path: {relative_destination.parent.as_posix()}\n"
        "---\n## Summary\n\nThis is a temporary Workbench canary.\n"
        "\n## Claim\n\n### Prose Claim\n\nThis Atom is a temporary Workbench canary.\n"
    )


def validate_atom_carrier(path: Path) -> None:
    parse_carrier(path.read_bytes(), path)


def authority_path(declarations: object, root: Path, name: str) -> Path:
    rows = declarations.as_structure()["scope_units"]  # type: ignore[attr-defined]
    return root / str(next(row for row in rows if row["scope_unit_name"] == name)["authority_path"])


def copy_declaration_tree(root: Path, control: Path, declarations: object, destination: Path) -> Path:
    control = control if control.is_absolute() else root / control
    staged_control = destination / control.relative_to(root)
    staged_control.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(control / "caprmedio_project_settings.toml", staged_control / "caprmedio_project_settings.toml")
    for source in declarations.paths:  # type: ignore[attr-defined]
        target = destination / source.relative_to(root)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    return staged_control


def validate_declaration_tree(root: Path, control: Path) -> object:
    return read_scope_unit_declarations(root, control)


def write_scope_declaration(path: Path, scope: CanaryScope, project_name: str) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(scope_carrier(scope, project_name, "2026-11-06 00:00:00 +0000"), encoding="utf-8")
    parsed = parse_scope_unit_declaration(path.read_bytes(), path)
    if (parsed.name, parsed.scope_unit_id, parsed.parent, parsed.version) != (
        scope.name, scope.scope_unit_id, scope.parent, scope.version,
    ):
        raise LiveCanaryError(f"staged Scope Unit Declaration did not parse as {scope.name}")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stage_carrier(report_directory: Path, name: str, content: str) -> Path:
    staged = report_directory / f".{name}-{uuid4().hex}.md"
    staged.write_text(content, encoding="utf-8")
    return staged


def remove_owned_authority(authority: Path) -> None:
    requirement = authority / "04_requirement"
    if requirement.exists() and not any(requirement.iterdir()):
        requirement.rmdir()
    if authority.exists() and not any(authority.iterdir()):
        authority.rmdir()
