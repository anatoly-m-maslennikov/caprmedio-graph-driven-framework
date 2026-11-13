# CA-D-442@29

"""Read current Scope Unit Declaration Atoms; no declaration writing lives here."""

from __future__ import annotations

import hashlib
import os
from dataclasses import replace
from pathlib import Path
import re
from typing import Any

from settings_carrier import read_settings_carrier
from scope_declaration_parse import (
    ScopeDeclarationError,
    ScopeDelegation,
    ScopeUnitDeclarations,
    _carrier,
    assemble_scope_unit_declarations,
    parse_scope_unit_declaration,
)
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext, open_regular
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS


_STRUCTURAL_FORM_VALUE = r'''(?:Scope Unit Declaration|Scope Delegation|scope_unit_declaration|scope_delegation|"Scope Unit Declaration"|"Scope Delegation"|"scope_unit_declaration"|"scope_delegation"|'Scope Unit Declaration'|'Scope Delegation'|'scope_unit_declaration'|'scope_delegation')'''
_STRUCTURAL_FORM_HINT = re.compile(
    rf"^(?:form|type):[ \t]*{_STRUCTURAL_FORM_VALUE}[ \t]*(?:#.*)?$"
)
_FLOW_STRUCTURAL_FORM_HINT = re.compile(
    rf"(?:^|[{{,][ \t]*)(?:form|type):[ \t]*{_STRUCTURAL_FORM_VALUE}(?=[ \t]*(?:,|}}|$))"
)
_PROJECTION = re.compile(r"(?m)^projection:\s*(?:$|\{)")
_STRUCTURAL_FORM_TEXT = re.compile(r"Scope\s+(?:Unit\s+Declaration|Delegation)|scope_(?:unit_declaration|delegation)")
DELEGATION_ROLE_FOLDERS = ("04_requirement", "05_method", "06_evaluation", "07_delivery", "09_operations")


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
    # Folded values can span lines, and double-quoted YAML can spell a value with escapes.
    if "\\" not in frontmatter and _STRUCTURAL_FORM_TEXT.search(frontmatter) is None:
        return False
    try:
        header, _ = _carrier(raw, source or Path("<structural carrier>"))
    except ScopeDeclarationError:
        return _structural_form_hint(frontmatter)
    return header.get("form") in ("Scope Unit Declaration", "Scope Delegation", "scope_unit_declaration", "scope_delegation")


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
    try:
        directory = reader.allowed(directory)
        descriptor = open_regular(directory, directory=True)
    except FileNotFoundError:
        return ()
    try:
        with os.scandir(descriptor) as entries:
            names = sorted(entry.name for entry in entries
                           if entry.name.endswith(".md") and (not root or entry.name.startswith("CA-R-"))
                           and entry.is_file(follow_symlinks=False))
        for name in names:
            path = directory / name
            try:
                raw = reader.read(path, remember=False, directory_fd=descriptor)
            except FileNotFoundError:
                continue
            if _selects_structural_form(raw, path) and not _is_projection(raw):
                candidates.append((path, raw))
    finally:
        os.close(descriptor)
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

        def admit(path: Path, raw: bytes) -> Any:
            try:
                declaration = parse_scope_unit_declaration(raw, path)
            except ScopeDeclarationError as error:
                # A selected structural carrier cannot fall back to an unrelated Requirement.
                if "not an active Requirement Scope Unit Declaration" in str(error):
                    raise ScopeDeclarationError(f"{path}: declaration Form contradicts its required carrier fields") from error
                raise
            relative = path.relative_to(root).as_posix()
            pins[relative] = {
                "sha256": hashlib.sha256(raw).hexdigest(),
                "atom_id": declaration.atom_id,
                "version": declaration.version,
            }
            return declaration

        roots = [admit(path, raw) for path, raw in read_candidates(control, root=True)]
        if any(isinstance(row, ScopeDelegation) or not row.is_root or row.form != "Scope Unit Declaration" for row in roots):
            raise ScopeDeclarationError("Project Scope Unit Declaration must be at the control root")
        rows.extend(roots)
        if len(roots) == 1:
            pending = [(roots[0], control)]
            while pending:
                parent, authority = pending.pop()
                candidates = []
                for directory, role in zip(DELEGATION_ROLE_FOLDERS,
                                           ("Requirement", "Method", "Evaluation", "Delivery", "Operations")):
                    for path, raw in read_candidates(authority / directory, root=False):
                        candidate = admit(path, raw)
                        if ((isinstance(candidate, ScopeDelegation) and candidate.role != role)
                                or (not isinstance(candidate, ScopeDelegation) and role != "Requirement")):
                            raise ScopeDeclarationError(f"{path}: Scope carrier Role does not match its authority directory")
                        candidates.append(candidate)
                structural: dict[str, list[Any]] = {}
                delegated: dict[str, list[ScopeDelegation]] = {}
                for candidate in candidates:
                    if isinstance(candidate, ScopeDelegation):
                        parent_id = parent.scope_unit_id
                        if parent_id is None:
                            settings = read_settings_carrier(control / "caprmedio_project_settings.toml", read_bytes=reader.read)
                            artifacts = settings.get("artifacts")
                            identity = artifacts.get("identity") if isinstance(artifacts, dict) else None
                            prefix = identity.get("project_prefix") if isinstance(identity, dict) else None
                            if not isinstance(prefix, str) or re.fullmatch(r"[A-Za-z0-9]+", prefix) is None:
                                raise ScopeDeclarationError("Project identity prefix is invalid")
                            parent_id = f"{prefix.upper()}-SU-00"
                        if not isinstance(candidate.parent_id, str) or not candidate.parent_id or candidate.parent_id != parent_id:
                            raise ScopeDeclarationError("Scope Delegation is not in its declared parent authority")
                        delegated.setdefault(candidate.name, []).append(candidate)
                    else:
                        if candidate.is_root or candidate.parent != parent.name:
                            raise ScopeDeclarationError("Scope Unit Declaration is not in its declared parent authority")
                        structural.setdefault(candidate.name, []).append(candidate)
                if set(delegated) - set(structural):
                    raise ScopeDeclarationError("Scope Delegation has no structural declaration in its direct parent authority")
                for name, choices in structural.items():
                    explicit = [row for row in choices if row.form == "Scope Unit Declaration"]
                    legacy = [row for row in choices if row.form == "Scope Delegation"]
                    if len(explicit) > 1 or len(legacy) > 1:
                        raise ScopeDeclarationError("Scope Unit names and IDs require unique structural declarations")
                    declaration = explicit[0] if explicit else legacy[0]
                    if legacy:
                        if explicit:
                            fields = ("scope_unit_id", "label", "ordered", "local_order", "parent")
                            if any(getattr(explicit[0], field) != getattr(legacy[0], field) for field in fields):
                                raise ScopeDeclarationError("legacy and explicit Scope Unit topology disagree")
                        old = legacy[0]
                        delegated.setdefault(name, []).append(ScopeDelegation(
                            name=old.name, atom_id=old.atom_id, version=old.version, source=old.source,
                            admitted_role_forms=old.admitted_role_forms, pair_receivers=(),
                        ))
                    sources = tuple(delegated.get(name, ()))
                    for delegation in sources:
                        if any(receiver != (declaration.scope_unit_id if field == "ID" else declaration.name)
                               for field, receiver in delegation.pair_receivers):
                            raise ScopeDeclarationError("Scope Delegation pair names another Scope Unit")
                    pairs = tuple(dict.fromkeys((*declaration.admitted_role_forms,
                                               *(pair for item in sources for pair in item.admitted_role_forms))))
                    declaration = replace(declaration, admitted_role_forms=pairs, delegations=sources)
                    rows.append(declaration)
                    pending.append((declaration, _child_authority(authority, declaration)))
        if not rows:
            raise ScopeDeclarationError("no current Scope Unit Declarations found")
        for (directory, is_root), expected in frontier.items():
            if tuple(path for path, _ in _declaration_candidates(reader, directory, root=is_root)) != expected:
                raise ScopeDeclarationError("Scope Unit Declaration source frontier changed during discovery")
        for relative, pin in pins.items():
            if hashlib.sha256(reader.read(root / relative, remember=False)).hexdigest() != pin["sha256"]:
                raise ScopeDeclarationError("Scope Unit Declaration sources changed during discovery")
        return assemble_scope_unit_declarations(
            rows, project_root=root, control_root=control, source_pins=pins, digest=_digest(pins),
        )
    except ScopeDeclarationError:
        raise
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise ScopeDeclarationError("Scope Unit Declaration source discovery is unavailable or unsafe") from error


__all__ = ["DELEGATION_ROLE_FOLDERS", "ScopeDeclarationError", "ScopeUnitDeclarations", "read_scope_unit_declarations"]
