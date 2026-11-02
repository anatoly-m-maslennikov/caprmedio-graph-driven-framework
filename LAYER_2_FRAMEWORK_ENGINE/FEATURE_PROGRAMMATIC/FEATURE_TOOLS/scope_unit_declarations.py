"""Read current Scope Unit Declaration Atoms; no declaration writing lives here."""

from __future__ import annotations

import hashlib
from pathlib import Path
import re
from typing import Any

from scope_declaration_parse import (
    ScopeDeclarationError,
    ScopeUnitDeclarations,
    assemble_scope_unit_declarations,
    parse_scope_unit_declaration,
)
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS


_IGNORED = frozenset({"archive", "archived", "draft", "generated", "_projection", ".caprmedio_runtime", ".caprmedio_tmp"})
_DECLARATION_FORM = re.compile(
    r"(?m)^(?:form|type):[ \t]*(?:Scope Unit Declaration|\"Scope Unit Declaration\"|'Scope Unit Declaration')[ \t]*(?:#.*)?$"
)
_PROJECTION = re.compile(r"(?m)^projection:\s*(?:$|\{)")


def _control(root: Path, control_root: Path | str) -> Path:
    value = Path(control_root)
    if value.is_absolute():
        control = value
    else:
        control = root / value
    if (control.parent != root or not control.name.startswith(".caprmedio_")
            or control.name == ".caprmedio_"):
        raise ScopeDeclarationError("control root must be one direct Project control directory")
    return control


def _current_requirement_paths(reader: ReadContext, control: Path) -> tuple[Path, ...]:
    paths = []
    for path in reader.inventory(control, remember=False):
        relative = path.relative_to(control)
        is_requirement_carrier = "04_requirement" in relative.parts
        is_project_declaration_candidate = (
            path.parent == control and path.name.startswith("CA-R-")
        )
        if (path.suffix != ".md" or path.is_symlink()
                or not (is_requirement_carrier or is_project_declaration_candidate)
                or any(part.casefold() in _IGNORED for part in relative.parts)):
            continue
        paths.append(path)
    return tuple(sorted(paths, key=lambda path: path.as_posix()))


def _digest(pins: dict[str, dict[str, Any]]) -> str:
    payload = "".join(
        f"{path}\0{pin['sha256']}\0{pin['atom_id']}\0{pin['version']}\n"
        for path, pin in sorted(pins.items())
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _selects_declaration_form(raw: bytes) -> bool:
    """Use only the canonical Form line to decide whether this reader owns a carrier."""
    try:
        text = raw.decode("utf-8").replace("\r\n", "\n")
    except UnicodeDecodeError:
        return False
    if not text.startswith("---\n"):
        return False
    closing = text.find("\n---\n", 4)
    return closing >= 0 and _DECLARATION_FORM.search(text[4:closing]) is not None


def _is_projection(raw: bytes) -> bool:
    """Exclude the existing frontmatter projection marker before parsing authority."""
    try:
        text = raw.decode("utf-8").replace("\r\n", "\n")
    except UnicodeDecodeError:
        return False
    if not text.startswith("---\n"):
        return False
    closing = text.find("\n---\n", 4)
    return closing >= 0 and _PROJECTION.search(text[4:closing]) is not None


def read_scope_unit_declarations(
    root: Path, control_root: Path | str, *, reader: ReadContext | None = None,
) -> ScopeUnitDeclarations:
    """Read the exact current declaration set below the selected Project control root."""
    root = Path(root)
    control = _control(root, control_root)
    reader = reader if reader is not None else ReadContext(roots=[str(root)], limits=dict(CEILINGS))
    try:
        reader.allowed(root)
        reader.allowed(control)
        rows = []
        pins: dict[str, dict[str, Any]] = {}
        candidates = _current_requirement_paths(reader, control)
        for path in candidates:
            raw = reader.read(path, remember=False)
            if _is_projection(raw) or not _selects_declaration_form(raw):
                continue
            try:
                declaration = parse_scope_unit_declaration(raw, path)
            except ScopeDeclarationError as error:
                # A selected declaration carrier cannot fall back to an unrelated Requirement.
                if "not an active Requirement Scope Unit Declaration" in str(error):
                    raise ScopeDeclarationError(f"{path}: declaration Form contradicts its required carrier fields") from error
                raise
            if declaration.is_root != (path.parent == control):
                raise ScopeDeclarationError(
                    "Project Scope Unit Declaration must be at the control root; nonroot declarations must use 04_requirement"
                )
            relative = path.relative_to(root).as_posix()
            rows.append(declaration)
            pins[relative] = {
                "sha256": hashlib.sha256(raw).hexdigest(),
                "atom_id": declaration.atom_id,
                "version": declaration.version,
            }
        if not rows:
            raise ScopeDeclarationError("no current Scope Unit Declarations found")
        if _current_requirement_paths(reader, control) != candidates:
            raise ScopeDeclarationError("Scope Unit Declaration source frontier changed during discovery")
        for declaration in rows:
            expected = pins[declaration.source.relative_to(root).as_posix()]["sha256"]
            if hashlib.sha256(reader.read(declaration.source, remember=False)).hexdigest() != expected:
                raise ScopeDeclarationError("Scope Unit Declaration sources changed during discovery")
        return assemble_scope_unit_declarations(
            rows, project_root=root, control_root=control, source_pins=pins, digest=_digest(pins),
        )
    except ScopeDeclarationError:
        raise
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise ScopeDeclarationError("Scope Unit Declaration source discovery is unavailable or unsafe") from error


__all__ = ["ScopeDeclarationError", "ScopeUnitDeclarations", "read_scope_unit_declarations"]
