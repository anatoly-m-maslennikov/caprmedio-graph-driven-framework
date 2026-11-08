"""Read current Scope Unit Declaration Atoms; no declaration writing lives here."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
import re
from typing import Any

from scope_declaration_parse import (
    ScopeDeclarationError,
    ScopeUnitDeclarations,
    _carrier,
    assemble_scope_unit_declarations,
    parse_scope_unit_declaration,
)
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext, open_regular
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS


_STRUCTURAL_FORM_VALUE = r"(?:Scope Unit Declaration|Scope Delegation|\"Scope Unit Declaration\"|\"Scope Delegation\"|'Scope Unit Declaration'|'Scope Delegation')"
_STRUCTURAL_FORM_HINT = re.compile(
    rf"^(?:form|type):[ \t]*{_STRUCTURAL_FORM_VALUE}[ \t]*(?:#.*)?$"
)
_FLOW_STRUCTURAL_FORM_HINT = re.compile(
    rf"(?:^|[{{,][ \t]*)(?:form|type):[ \t]*{_STRUCTURAL_FORM_VALUE}(?=[ \t]*(?:,|}}|$))"
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


def _direct_markdown_paths(reader: ReadContext, directory: Path) -> tuple[Path, ...]:
    """List one Current role directory without recursively touching its descendants."""
    try:
        reader.allowed(directory)
        descriptor = open_regular(directory, directory=True)
    except FileNotFoundError:
        return ()
    try:
        with os.scandir(descriptor) as entries:
            return tuple(sorted(
                (directory / entry.name for entry in entries
                 if entry.name != ".DS_Store" and entry.name.endswith(".md")
                 and entry.is_file(follow_symlinks=False)),
                key=lambda path: path.as_posix(),
            ))
    finally:
        os.close(descriptor)


def _digest(pins: dict[str, dict[str, Any]]) -> str:
    payload = "".join(
        f"{path}\0{pin['sha256']}\0{pin['atom_id']}\0{pin['version']}\n"
        for path, pin in sorted(pins.items())
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _selects_structural_form(raw: bytes, source: Path | None = None) -> bool:
    """Use the safe Header read view; a malformed structural hint fails closed later."""
    try:
        text = raw.decode("utf-8").replace("\r\n", "\n")
    except UnicodeDecodeError:
        return False
    if not text.startswith("---\n"):
        return False
    closing = text.find("\n---\n", 4)
    if closing < 0:
        return False
    frontmatter = text[4:closing]
    try:
        header, _ = _carrier(raw, source or Path("<structural carrier>"))
    except ScopeDeclarationError:
        return _structural_form_hint(frontmatter)
    return header.get("form") in {"Scope Unit Declaration", "Scope Delegation"}


def _structural_form_hint(frontmatter: str) -> bool:
    """Fail closed for malformed canonical forms without treating nested data as authority."""
    direct_indent: int | None = None
    child_indent: int | None = None
    for line in frontmatter.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" \t"))
        stripped = line[indent:]
        if indent == 0:
            direct_indent = None
            child_indent = None
            key, separator, value = stripped.partition(":")
            if key == "context" and separator:
                direct_indent = 0
                if value.lstrip().startswith("{"):
                    return _FLOW_STRUCTURAL_FORM_HINT.search(value) is not None
            elif _STRUCTURAL_FORM_HINT.fullmatch(stripped):
                return True
            continue
        if direct_indent is None:
            continue
        if child_indent is None:
            child_indent = indent
        if indent < child_indent:
            direct_indent = None
            child_indent = None
            continue
        if indent == child_indent and _STRUCTURAL_FORM_HINT.fullmatch(stripped):
            return True
    return False


# Compatibility for current consumers; structural forms now include Delegation.
_selects_declaration_form = _selects_structural_form


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


def _declaration_candidates(
    reader: ReadContext, directory: Path, *, root: bool,
) -> tuple[tuple[Path, bytes], ...]:
    """Read only direct Current candidates in a declared authority location."""
    candidates = []
    for path in _direct_markdown_paths(reader, directory):
        if root and not path.name.startswith("CA-R-"):
            continue
        try:
            raw = reader.read(path, remember=False)
        except FileNotFoundError:
            continue
        if not _is_projection(raw) and _selects_structural_form(raw, path):
            candidates.append((path, raw))
    return tuple(candidates)


def _child_authority(parent_authority: Path, declaration: Any) -> Path:
    parts = [declaration.scope_unit_id]
    if declaration.label:
        parts.append(declaration.label)
    if declaration.ordered:
        parts.append(str(declaration.local_order))
    parts.append(declaration.name)
    return parent_authority / "_".join(parts)


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
        frontier: dict[tuple[Path, bool], tuple[Path, ...]] = {}

        def read_candidates(directory: Path, *, root: bool) -> tuple[tuple[Path, bytes], ...]:
            candidates = _declaration_candidates(reader, directory, root=root)
            key = (directory, root)
            expected = tuple(path for path, _ in candidates)
            if key in frontier and frontier[key] != expected:
                raise ScopeDeclarationError("Scope Unit Declaration source frontier changed during discovery")
            frontier[key] = expected
            return candidates

        def admit(path: Path, raw: bytes, *, parent: Any | None) -> Any:
            try:
                declaration = parse_scope_unit_declaration(raw, path)
            except ScopeDeclarationError as error:
                # A selected structural carrier cannot fall back to an unrelated Requirement.
                if "not an active Requirement Scope Unit Declaration" in str(error):
                    raise ScopeDeclarationError(f"{path}: declaration Form contradicts its required carrier fields") from error
                raise
            if parent is None and declaration.form != "Scope Unit Declaration":
                raise ScopeDeclarationError("Project Scope Unit must use Scope Unit Declaration")
            if parent is not None and declaration.form not in {"Scope Unit Declaration", "Scope Delegation"}:
                raise ScopeDeclarationError("non-Project Scope Unit must use Scope Unit Declaration or Scope Delegation")
            if declaration.is_root != (parent is None):
                raise ScopeDeclarationError(
                    "Project Scope Unit Declaration must be at the control root; nonroot declarations must use 04_requirement"
                )
            if parent is not None and declaration.parent != parent.name:
                raise ScopeDeclarationError("Scope Unit Declaration is not in its declared parent authority")
            relative = path.relative_to(root).as_posix()
            rows.append(declaration)
            pins[relative] = {
                "sha256": hashlib.sha256(raw).hexdigest(),
                "atom_id": declaration.atom_id,
                "version": declaration.version,
            }
            return declaration

        roots = [admit(path, raw, parent=None) for path, raw in read_candidates(control, root=True)]
        if len(roots) == 1:
            pending = [(roots[0], control)]
            while pending:
                parent, authority = pending.pop()
                for path, raw in read_candidates(authority / "04_requirement", root=False):
                    declaration = admit(path, raw, parent=parent)
                    pending.append((declaration, _child_authority(authority, declaration)))
        if not rows:
            raise ScopeDeclarationError("no current Scope Unit Declarations found")
        for (directory, is_root), expected in frontier.items():
            if tuple(path for path, _ in _declaration_candidates(reader, directory, root=is_root)) != expected:
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
