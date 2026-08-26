"""Shared implementation for CAPRMEDIO Markdown Atom operations."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import tomllib
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

SCHEMA_VERSION = 1
CONTROL_ROOT = ".caprmedio"
ROLE_DIRECTORY = re.compile(r"^(0[1-9])_[a-z0-9_]+$")
CURRENT_FILENAME = re.compile(
    r"^CA-(?:C|A|P|R|M|E|D|O|I)-(?:[0-9]{3,})?-[A-Z][A-Z0-9_]*(?:-[A-Z][A-Z0-9_]*)*--[a-z0-9][a-z0-9_-]*\.md$"
)
ATOM_ID = re.compile(r"^(CA-[A-Z]+-[0-9]{3,})(?:-|$)")


class ToolError(RuntimeError):
    def __init__(self, code: str, message: str, details: Mapping[str, Any] | None = None) -> None:
        self.code = code
        self.message = message
        self.details = dict(details or {})
        super().__init__(message)


@dataclass(frozen=True)
class Atom:
    path: Path
    relative: str
    filename: str
    atom_id: str | None
    lifecycle: str
    role_directory: str
    frontmatter: str
    content: str


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def resolve_repository(value: str | Path) -> Path:
    candidate = Path(value).expanduser().resolve()
    for root in (candidate, *candidate.parents):
        if (root / ".git").exists():
            return root
    raise ToolError("repository-not-found", f"cannot resolve Git repository from {candidate}")


def _inside(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def safe_path(root: Path, value: str, *, must_exist: bool = False) -> Path:
    root = root.resolve()
    if not value or "\x00" in value:
        raise ToolError("path-invalid", "path must be a non-empty string")
    candidate = Path(value).expanduser()
    path = candidate.resolve() if candidate.is_absolute() else (root / candidate).resolve()
    control = (root / CONTROL_ROOT).resolve()
    if not _inside(path, control):
        raise ToolError("outside-control-root", f"path is outside {CONTROL_ROOT}: {value}")
    if must_exist and not path.exists():
        raise ToolError("path-not-found", f"path does not exist: {value}")
    return path


def split_frontmatter(text: str) -> tuple[str, str]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if not normalized.startswith("---\n"):
        raise ToolError("atom-frontmatter-missing", "Markdown Atom must begin with YAML frontmatter")
    end = normalized.find("\n---\n", 4)
    if end < 0:
        raise ToolError("atom-frontmatter-invalid", "Markdown Atom frontmatter is not closed")
    return normalized[4:end], normalized[end + 5 :]


def _role_directory(path: Path, control: Path) -> str | None:
    relative = path.relative_to(control)
    for part in reversed(relative.parts[:-1]):
        if ROLE_DIRECTORY.fullmatch(part):
            return part
    return None


def _lifecycle(path: Path, control: Path) -> str:
    parts = {part.lower() for part in path.relative_to(control).parts}
    if "archive" in parts:
        return "archived"
    if "drafts" in parts:
        return "draft"
    return "active"


def atom_from_path(root: Path, path: Path) -> Atom:
    root = root.resolve()
    control = (root / CONTROL_ROOT).resolve()
    path = path.resolve()
    if not _inside(path, control) or path.suffix.lower() != ".md" or not path.is_file():
        raise ToolError("not-markdown-atom", f"not a CAPRMEDIO Markdown Atom carrier: {path}")
    role = _role_directory(path, control)
    if role is None and path != control / "CA-INTENT.md":
        raise ToolError("not-markdown-atom", f"carrier is not placed in a CAPRMEDIO content-role directory: {path}")
    frontmatter, content = split_frontmatter(path.read_text(encoding="utf-8"))
    lifecycle = _lifecycle(path, control)
    match = ATOM_ID.match(path.name)
    atom_id = "CA-INTENT" if path.name == "CA-INTENT.md" else match.group(1) if match and lifecycle != "draft" else None
    return Atom(path, path.relative_to(root).as_posix(), path.name, atom_id,
                lifecycle, role or "control-root", frontmatter, content)


def scan_atoms(root: Path, *, under: str | None = None, lifecycle: str = "all") -> list[Atom]:
    root = root.resolve()
    base = safe_path(root, under, must_exist=True) if under else (root / CONTROL_ROOT).resolve()
    candidates = [base] if base.is_file() else sorted(base.rglob("*.md"), key=lambda p: p.as_posix())
    atoms: list[Atom] = []
    for path in candidates:
        try:
            atom = atom_from_path(root, path)
        except (ToolError, UnicodeDecodeError, OSError):
            continue
        if lifecycle == "all" or atom.lifecycle == lifecycle:
            atoms.append(atom)
    return sorted(atoms, key=lambda atom: atom.relative)


def resolve_selector(root: Path, selector: str, atoms: Sequence[Atom] | None = None) -> Atom:
    root = root.resolve()
    if "/" in selector or (selector.endswith(".md") and Path(selector).is_absolute()):
        try:
            return atom_from_path(root, safe_path(root, selector, must_exist=True))
        except ToolError as error:
            if error.code not in {"path-not-found", "not-markdown-atom"}:
                raise
    pool = list(atoms) if atoms is not None else scan_atoms(root)
    normalized = Path(selector).name
    matches = [atom for atom in pool if selector == atom.relative or normalized == atom.filename
               or normalized == Path(atom.filename).stem or selector == atom.atom_id]
    unique = {atom.relative: atom for atom in matches}
    if not unique:
        raise ToolError("atom-not-found", f"no CAPRMEDIO Markdown Atom matches selector: {selector}")
    if len(unique) != 1:
        raise ToolError("atom-selector-ambiguous", f"selector matches more than one Atom: {selector}",
                        {"matches": sorted(unique)})
    return next(iter(unique.values()))


def resolve_selectors(root: Path, selectors: Sequence[str]) -> list[Atom]:
    root = root.resolve()
    if not selectors:
        raise ToolError("atom-selector-required", "at least one Atom selector is required")
    pool = scan_atoms(root)
    resolved = [resolve_selector(root, selector, pool) for selector in selectors]
    paths = [atom.relative for atom in resolved]
    duplicates = sorted({path for path in paths if paths.count(path) > 1})
    if duplicates:
        raise ToolError("duplicate-target", "the same Atom was selected more than once", {"paths": duplicates})
    return resolved


def metadata(atom: Atom) -> dict[str, Any]:
    return {"atom_id": atom.atom_id, "path": atom.relative, "filename": atom.filename,
            "lifecycle": atom.lifecycle, "content_role_directory": atom.role_directory,
            "frontmatter": atom.frontmatter}


def present(atom: Atom, view: str) -> dict[str, Any]:
    result: dict[str, Any] = {}
    if view in {"metadata", "both"}:
        result["metadata"] = metadata(atom)
    if view in {"content", "both"}:
        result["content"] = atom.content
    return result


def _load_payload(path: str) -> dict[str, Any]:
    try:
        text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
        value = json.loads(text)
    except (OSError, json.JSONDecodeError) as error:
        raise ToolError("input-invalid", f"cannot read JSON input: {error}") from error
    if not isinstance(value, dict):
        raise ToolError("input-invalid", "JSON input root must be an object")
    return value


def _items(payload: Mapping[str, Any]) -> list[dict[str, Any]]:
    raw = payload.get("atoms")
    if not isinstance(raw, list) or not raw or any(not isinstance(item, dict) for item in raw):
        raise ToolError("input-invalid", "input must contain a non-empty atoms array of objects")
    return [dict(item) for item in raw]


def _normalize_frontmatter(value: Any) -> str:
    if not isinstance(value, str):
        raise ToolError("input-invalid", "frontmatter must be a YAML string without delimiters")
    normalized = value.replace("\r\n", "\n").replace("\r", "\n").strip("\n")
    if normalized.startswith("---") or "\n---" in normalized:
        raise ToolError("input-invalid", "frontmatter must not include YAML delimiters")
    return normalized


def _revision(frontmatter: str, *, creating: bool) -> str:
    lines = frontmatter.splitlines()
    index = next((i for i, line in enumerate(lines) if re.fullmatch(r"version:\s*[0-9]+\s*", line)), None)
    current = int(lines[index].split(":", 1)[1]) if index is not None else 0
    line = f"version: {1 if creating else current + 1}"
    if index is None:
        lines.append(line)
    else:
        lines[index] = line
    stamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")
    index = next((i for i, line in enumerate(lines) if line.startswith("updated_at:")), None)
    line = f"updated_at: {stamp}"
    if index is None:
        lines.append(line)
    else:
        lines[index] = line
    return "\n".join(lines)


def render(frontmatter: str, content: str) -> bytes:
    if not isinstance(content, str):
        raise ToolError("input-invalid", "content must be a string")
    return ("---\n" + frontmatter.rstrip("\n") + "\n---\n" + content).encode("utf-8")


def _validate_destination(root: Path, path: Path, *, filename_required: bool) -> None:
    control = (root / CONTROL_ROOT).resolve()
    if not _inside(path, control):
        raise ToolError("outside-control-root", f"destination is outside {CONTROL_ROOT}: {path}")
    probe = path.parent if filename_required else path
    if not any(ROLE_DIRECTORY.fullmatch(part) for part in probe.relative_to(control).parts):
        raise ToolError("destination-not-atom-place", f"destination has no CAPRMEDIO content-role directory: {path}")


def _atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def _restore(snapshots: Mapping[Path, bytes | None]) -> None:
    for path, previous in reversed(list(snapshots.items())):
        if previous is None:
            path.unlink(missing_ok=True)
        else:
            _atomic_write(path, previous)


def run_search(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    atoms = scan_atoms(root, under=args.under, lifecycle=args.lifecycle)
    if args.atom:
        selected = {atom.relative for atom in resolve_selectors(root, args.atom)}
        atoms = [atom for atom in atoms if atom.relative in selected]
    for query in args.query or []:
        needle = query.casefold()
        atoms = [atom for atom in atoms if needle in "\n".join((atom.relative, atom.frontmatter, atom.content)).casefold()]
    if args.limit is not None:
        atoms = atoms[:args.limit]
    return {"count": len(atoms), "atoms": [present(atom, args.view) for atom in atoms]}


def run_read(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    atoms = resolve_selectors(root, args.atom)
    return {"count": len(atoms), "atoms": [present(atom, args.view) for atom in atoms]}


def run_create(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    plans: list[tuple[Path, bytes]] = []
    existing_ids = {atom.atom_id for atom in scan_atoms(root) if atom.atom_id}
    planned_ids: set[str] = set()
    for item in _items(_load_payload(args.input)):
        if "path" in item:
            if "directory" in item or "filename" in item:
                raise ToolError("input-invalid", "create item uses path or directory plus filename, not both")
            path = safe_path(root, str(item["path"]))
        else:
            directory = safe_path(root, str(item.get("directory", "")))
            filename = item.get("filename")
            if not isinstance(filename, str):
                raise ToolError("input-invalid", "create item requires filename")
            path = (directory / filename).resolve()
        _validate_destination(root, path, filename_required=True)
        if not CURRENT_FILENAME.fullmatch(path.name):
            raise ToolError("filename-invalid", f"new Atom filename does not follow current grammar: {path.name}")
        if path.exists() or any(existing == path for existing, _ in plans):
            raise ToolError("destination-collision", f"Atom destination already exists: {path.relative_to(root)}")
        match = ATOM_ID.match(path.name)
        atom_id = match.group(1) if match else None
        destination_lifecycle = _lifecycle(path, (root / CONTROL_ROOT).resolve())
        if destination_lifecycle == "draft" and atom_id is not None:
            raise ToolError("draft-has-stable-id", f"draft filename must not contain a stable Atom ID: {path.name}")
        if destination_lifecycle != "draft" and atom_id is None:
            raise ToolError("atom-id-required", f"non-draft Atom filename must contain a stable Atom ID: {path.name}")
        if atom_id and (atom_id in existing_ids or atom_id in planned_ids):
            raise ToolError("atom-id-collision", f"Atom ID already exists: {atom_id}")
        if atom_id:
            planned_ids.add(atom_id)
        frontmatter = _revision(_normalize_frontmatter(item.get("frontmatter", "")), creating=True)
        plans.append((path, render(frontmatter, item.get("content", ""))))
    result = {"count": len(plans), "changes": [{"operation": "create", "path": p.relative_to(root).as_posix()} for p, _ in plans]}
    if not args.apply:
        return result
    snapshots = {path: None for path, _ in plans}
    try:
        for path, data in plans:
            _atomic_write(path, data)
    except BaseException:
        _restore(snapshots)
        raise
    return result


def run_update(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    raw_items = _items(_load_payload(args.input))
    selectors = [item.get("selector") for item in raw_items]
    if any(not isinstance(selector, str) for selector in selectors):
        raise ToolError("input-invalid", "every update item requires selector")
    atoms = resolve_selectors(root, selectors)
    plans: list[tuple[Atom, bytes]] = []
    for item, atom in zip(raw_items, atoms, strict=True):
        if "frontmatter" not in item and "content" not in item:
            raise ToolError("input-invalid", "update item must provide frontmatter or content")
        frontmatter = _normalize_frontmatter(item["frontmatter"]) if "frontmatter" in item else atom.frontmatter
        content = item["content"] if "content" in item else atom.content
        plans.append((atom, render(_revision(frontmatter, creating=False), content)))
    result = {"count": len(plans), "changes": [{"operation": "update", "path": atom.relative} for atom, _ in plans]}
    if not args.apply:
        return result
    snapshots = {atom.path: atom.path.read_bytes() for atom, _ in plans}
    try:
        for atom, data in plans:
            _atomic_write(atom.path, data)
    except BaseException:
        _restore(snapshots)
        raise
    return result


def _execute_move_plans(
    root: Path,
    plans: Sequence[tuple[Atom, Path]],
    *,
    operation: str,
    apply: bool,
) -> dict[str, Any]:
    targets = [target for _, target in plans]
    if len(set(targets)) != len(targets):
        raise ToolError("destination-collision", "more than one selected Atom resolves to the same destination")
    selected_sources = {atom.path for atom, _ in plans}
    for atom, target in plans:
        if target.exists() and target not in selected_sources:
            raise ToolError("destination-collision", f"destination already exists: {target.relative_to(root)}")
        if target == atom.path:
            raise ToolError(f"{operation}-noop", f"destination equals source: {atom.relative}")
    result = {"count": len(plans), "changes": [{"operation": operation, "from": atom.relative,
               "to": target.relative_to(root).as_posix()} for atom, target in plans]}
    if not apply:
        return result
    snapshots: dict[Path, bytes | None] = {}
    for atom, target in plans:
        snapshots.setdefault(atom.path, atom.path.read_bytes())
        snapshots.setdefault(target, target.read_bytes() if target.exists() else None)
    try:
        payloads = [(atom, target, atom.path.read_bytes()) for atom, target in plans]
        for _, target, data in payloads:
            _atomic_write(target, data)
        for atom, target, _ in payloads:
            if atom.path != target:
                atom.path.unlink()
    except BaseException:
        _restore(snapshots)
        raise
    return result


def run_move(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    atoms = resolve_selectors(root, args.atom) if args.atom else []
    source: Path | None = None
    if args.from_path:
        source = safe_path(root, args.from_path, must_exist=True)
        known = {atom.relative for atom in atoms}
        atoms.extend(atom for atom in scan_atoms(root, under=args.from_path) if atom.relative not in known)
    if not atoms:
        raise ToolError("atom-selector-required", "move requires --atom or --from")
    destination = safe_path(root, args.to)
    _validate_destination(root, destination, filename_required=False)
    plans: list[tuple[Atom, Path]] = []
    for atom in atoms:
        target = destination / atom.filename
        if source is not None and _inside(atom.path, source) and not args.flatten:
            target = destination / atom.path.relative_to(source)
        target = target.resolve()
        _validate_destination(root, target, filename_required=True)
        target_lifecycle = _lifecycle(target, (root / CONTROL_ROOT).resolve())
        if target_lifecycle == "draft" and atom.atom_id is not None:
            raise ToolError("draft-has-stable-id", f"move would place a stable Atom ID in drafts: {atom.relative}")
        if target_lifecycle != "draft" and atom.atom_id is None:
            raise ToolError("atom-id-required", f"move would place an identity-less draft outside drafts: {atom.relative}")
        plans.append((atom, target))
    return _execute_move_plans(root, plans, operation="move", apply=args.apply)


def run_archive(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    atoms = resolve_selectors(root, args.atom)
    control = (root / CONTROL_ROOT).resolve()
    plans: list[tuple[Atom, Path]] = []
    for atom in atoms:
        if atom.lifecycle != "active" or atom.atom_id is None:
            raise ToolError("atom-not-active", f"only active Atoms with stable identity can be archived: {atom.relative}")
        role_name = _role_directory(atom.path, control)
        if role_name is None:
            raise ToolError("archive-location-missing", f"Atom has no content-role archive location: {atom.relative}")
        role = next(parent for parent in atom.path.parents if role_name == parent.name)
        target = (role / "archive" / atom.filename).resolve()
        plans.append((atom, target))
    return _execute_move_plans(root, plans, operation="archive", apply=args.apply)


def run_promote(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    raw_items = _items(_load_payload(args.input))
    selectors = [item.get("selector") for item in raw_items]
    if any(not isinstance(selector, str) for selector in selectors):
        raise ToolError("input-invalid", "every promote item requires selector")
    atoms = resolve_selectors(root, selectors)
    existing_ids = {atom.atom_id for atom in scan_atoms(root) if atom.atom_id}
    planned_ids: set[str] = set()
    control = (root / CONTROL_ROOT).resolve()
    plans: list[tuple[Atom, Path]] = []
    for item, atom in zip(raw_items, atoms, strict=True):
        if atom.lifecycle != "draft" or atom.atom_id is not None:
            raise ToolError("atom-not-draft", f"only identity-less drafts can be promoted: {atom.relative}")
        requested = item.get("atom_id")
        if not isinstance(requested, str) or re.fullmatch(r"CA-[A-Z]+-[0-9]{3,}", requested) is None:
            raise ToolError("atom-id-invalid", "promote item requires an Atom ID such as CA-R-343")
        draft_prefix = re.match(r"^(CA-[A-Z]+)--(.+)$", atom.filename)
        if draft_prefix is None or not requested.startswith(draft_prefix.group(1) + "-"):
            raise ToolError("atom-id-role-mismatch", f"Atom ID does not match the draft content role: {requested}")
        if requested in existing_ids or requested in planned_ids:
            raise ToolError("atom-id-collision", f"Atom ID already exists: {requested}")
        planned_ids.add(requested)
        filename = requested + "-" + draft_prefix.group(2)
        if not CURRENT_FILENAME.fullmatch(filename):
            raise ToolError("filename-invalid", f"promoted Atom filename does not follow current grammar: {filename}")
        parent_parts = atom.path.parent.relative_to(control).parts
        draft_indexes = [index for index, part in enumerate(parent_parts) if part.lower() == "drafts"]
        if not draft_indexes:
            raise ToolError("atom-not-draft", f"draft carrier has no drafts location: {atom.relative}")
        index = draft_indexes[-1]
        active_parent = control.joinpath(*parent_parts[:index], *parent_parts[index + 1:])
        target = (active_parent / filename).resolve()
        _validate_destination(root, target, filename_required=True)
        plans.append((atom, target))
    return _execute_move_plans(root, plans, operation="promote", apply=args.apply)


def _frontmatter_tier(frontmatter: str) -> str:
    matches = re.findall(r"(?m)^tier:\s*(core|standard)\s*$", frontmatter)
    if len(matches) != 1:
        raise ToolError("current-tier-unresolved", "active Atom must declare exactly one tier: core or standard")
    return matches[0]


def _replace_tier(frontmatter: str, target_tier: str) -> str:
    if target_tier not in {"core", "standard"}:
        raise ToolError("target-tier-invalid", "target tier must be core or standard")
    _frontmatter_tier(frontmatter)
    return re.sub(r"(?m)^tier:\s*(?:core|standard)\s*$", f"tier: {target_tier}", frontmatter)


def _scope_graph(root: Path) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    carrier = root / CONTROL_ROOT / "project_scope_unit_graph.projection.toml"
    try:
        document = tomllib.loads(carrier.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise ToolError("scope-projection-unavailable", f"cannot read current Scope Unit projection: {error}") from error
    raw_rows = document.get("scope_units")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise ToolError("scope-projection-invalid", "Scope Unit projection contains no scope_units")
    rows: dict[str, dict[str, Any]] = {}
    selectors: dict[str, str] = {}
    for raw in raw_rows:
        if not isinstance(raw, dict):
            raise ToolError("scope-projection-invalid", "Scope Unit row must be a table")
        name, prefix, parent, authority = (raw.get(field) for field in ("name", "prefix", "structural_parent", "authority_path"))
        if not all(isinstance(value, str) for value in (name, prefix, parent, authority)):
            raise ToolError("scope-projection-invalid", "Scope Unit identity and authority fields must be strings")
        key = name
        if key in rows:
            raise ToolError("scope-projection-invalid", f"duplicate Scope Unit key: {key}")
        rows[key] = {**raw, "key": key}
        for selector in {key, name, prefix}:
            normalized = selector.casefold()
            if normalized in selectors and selectors[normalized] != key:
                raise ToolError("scope-projection-invalid", f"ambiguous Scope Unit selector: {selector}")
            selectors[normalized] = key

    resolving: set[str] = set()

    def full_path(key: str) -> Path:
        row = rows[key]
        cached = row.get("full_authority_path")
        if isinstance(cached, Path):
            return cached
        if key in resolving:
            raise ToolError("scope-projection-invalid", "Scope Unit authority hierarchy contains a cycle")
        resolving.add(key)
        parent = str(row["structural_parent"])
        relative = Path(str(row["authority_path"]))
        if parent:
            if parent not in rows:
                raise ToolError("scope-projection-invalid", f"unknown Scope Unit parent: {parent}")
            value = (full_path(parent) / relative).resolve()
        else:
            value = (root / relative).resolve()
        resolving.remove(key)
        row["full_authority_path"] = value
        return value

    for key in rows:
        full_path(key)
    return rows, selectors


def _scope_for_atom(atom: Atom, rows: Mapping[str, Mapping[str, Any]], control: Path) -> str:
    role_name = _role_directory(atom.path, control)
    scope_path = control if role_name is None else next(parent.parent for parent in atom.path.parents if parent.name == role_name)
    matches = [key for key, row in rows.items() if row["full_authority_path"] == scope_path]
    if len(matches) != 1:
        raise ToolError("atom-scope-unresolved", f"cannot resolve exactly one Scope Unit for Atom: {atom.relative}")
    return matches[0]


def _is_same_or_ancestor(rows: Mapping[str, Mapping[str, Any]], current: str, target: str) -> bool:
    cursor = current
    while True:
        if cursor == target:
            return True
        parent = str(rows[cursor]["structural_parent"])
        if not parent:
            return False
        cursor = parent


def _upgrade_filename(filename: str, target_prefix: str) -> str:
    head, separator, summary = filename.partition("--")
    if not separator or "-" not in head:
        raise ToolError("filename-invalid", f"cannot derive upgraded filename: {filename}")
    segments = head.split("-")
    segments[-1] = target_prefix
    upgraded = "-".join(segments) + "--" + summary
    if not CURRENT_FILENAME.fullmatch(upgraded):
        raise ToolError("filename-invalid", f"upgraded Atom filename does not follow current grammar: {upgraded}")
    return upgraded


def run_upgrade(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    raw_items = _items(_load_payload(args.input))
    selectors_raw = [item.get("selector") for item in raw_items]
    if any(not isinstance(selector, str) for selector in selectors_raw):
        raise ToolError("input-invalid", "every upgrade item requires selector")
    atoms = resolve_selectors(root, selectors_raw)
    rows, scope_selectors = _scope_graph(root)
    control = (root / CONTROL_ROOT).resolve()
    plans: list[tuple[Atom, Path, bytes, str, str, str, str]] = []
    for item, atom in zip(raw_items, atoms, strict=True):
        if atom.lifecycle != "active" or atom.atom_id is None:
            raise ToolError("atom-not-active", f"only active Atoms with stable identity can be upgraded: {atom.relative}")
        target_tier = item.get("tier")
        if not isinstance(target_tier, str) or target_tier not in {"core", "standard"}:
            raise ToolError("target-tier-invalid", "every upgrade item requires explicit tier: core or standard")
        current_tier = _frontmatter_tier(atom.frontmatter)
        current_scope = _scope_for_atom(atom, rows, control)
        requested_scope = item.get("to_scope")
        if requested_scope is None:
            target_scope = current_scope
        elif isinstance(requested_scope, str) and requested_scope.casefold() in scope_selectors:
            target_scope = scope_selectors[requested_scope.casefold()]
        else:
            raise ToolError("target-scope-unresolved", f"unknown target Scope Unit: {requested_scope}")
        if not _is_same_or_ancestor(rows, current_scope, target_scope):
            raise ToolError("target-scope-not-upper", "target Scope Unit must be the current Scope Unit or one of its ancestors")
        if target_scope == current_scope and not (current_tier == "standard" and target_tier == "core"):
            raise ToolError("target-tier-not-higher", f"target tier is not higher than current tier: {current_tier} -> {target_tier}")
        frontmatter = _revision(_replace_tier(atom.frontmatter, target_tier), creating=False)
        if target_scope == current_scope:
            target = atom.path
        else:
            role_name = _role_directory(atom.path, control)
            if role_name is None:
                raise ToolError("upgrade-location-missing", f"Atom has no content-role location: {atom.relative}")
            filename = _upgrade_filename(atom.filename, str(rows[target_scope]["prefix"]))
            target = (rows[target_scope]["full_authority_path"] / role_name / filename).resolve()
            _validate_destination(root, target, filename_required=True)
        plans.append((atom, target, render(frontmatter, atom.content), current_tier, target_tier, current_scope, target_scope))

    targets = [target for _, target, *_ in plans]
    if len(set(targets)) != len(targets):
        raise ToolError("destination-collision", "more than one upgraded Atom resolves to the same destination")
    selected_sources = {atom.path for atom, *_ in plans}
    for atom, target, *_ in plans:
        if target != atom.path and target.exists() and target not in selected_sources:
            raise ToolError("destination-collision", f"upgrade destination already exists: {target.relative_to(root)}")
    result = {"count": len(plans), "changes": [
        {"operation": "upgrade", "atom_id": atom.atom_id, "from": atom.relative,
         "to": target.relative_to(root).as_posix(), "from_tier": current_tier,
         "to_tier": target_tier, "from_scope": current_scope, "to_scope": target_scope}
        for atom, target, _, current_tier, target_tier, current_scope, target_scope in plans
    ]}
    if not args.apply:
        return result
    snapshots: dict[Path, bytes | None] = {}
    for atom, target, *_ in plans:
        snapshots.setdefault(atom.path, atom.path.read_bytes())
        snapshots.setdefault(target, target.read_bytes() if target.exists() else None)
    try:
        for _, target, data, *_ in plans:
            _atomic_write(target, data)
        for atom, target, *_ in plans:
            if atom.path != target:
                atom.path.unlink()
    except BaseException:
        _restore(snapshots)
        raise
    return result


def describe(tool_id: str) -> dict[str, Any]:
    kinds = {"ATOM_SEARCH": "finder", "ATOM_READ": "finder", "ATOM_CREATE": "doer",
             "ATOM_UPDATE": "doer", "ATOM_MOVE": "doer", "ATOM_ARCHIVE": "doer",
             "ATOM_PROMOTE": "doer", "ATOM_UPGRADE": "doer"}
    return {"capability_id": tool_id, "kind": kinds[tool_id],
            "scope": "CAPRMEDIO Markdown Atom carriers under .caprmedio", "singular_and_bulk": True,
            "mutation_default": "dry-run" if kinds[tool_id] == "doer" else "read-only",
            "selector_forms": ["repository-relative path", "full filename", "filename stem", "Atom ID"]}


def parser(tool_id: str) -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(prog=tool_id.lower().replace("_", "-"))
    result.add_argument("--repository", default=".")
    sub = result.add_subparsers(dest="command", required=True)
    sub.add_parser("describe")
    run = sub.add_parser("run")
    if tool_id == "ATOM_SEARCH":
        run.add_argument("--query", action="append")
        run.add_argument("--atom", action="append")
        run.add_argument("--under")
        run.add_argument("--lifecycle", choices=("all", "active", "draft", "archived"), default="all")
        run.add_argument("--limit", type=int)
        run.add_argument("--view", choices=("metadata", "content", "both"), default="metadata")
    elif tool_id == "ATOM_READ":
        run.add_argument("--atom", action="append", required=True)
        run.add_argument("--view", choices=("metadata", "content", "both"), default="both")
    elif tool_id in {"ATOM_CREATE", "ATOM_UPDATE", "ATOM_PROMOTE", "ATOM_UPGRADE"}:
        run.add_argument("--input", required=True)
        run.add_argument("--apply", action="store_true")
    elif tool_id == "ATOM_ARCHIVE":
        run.add_argument("--atom", action="append", required=True)
        run.add_argument("--apply", action="store_true")
    else:
        run.add_argument("--atom", action="append")
        run.add_argument("--from", dest="from_path")
        run.add_argument("--to", required=True)
        run.add_argument("--flatten", action="store_true")
        run.add_argument("--apply", action="store_true")
    return result


def cli(tool_id: str) -> int:
    args = parser(tool_id).parse_args()
    kind = "finder" if tool_id in {"ATOM_SEARCH", "ATOM_READ"} else "doer"
    mode = "describe" if args.command == "describe" else "apply" if getattr(args, "apply", False) else "read-only" if kind == "finder" else "dry-run"
    try:
        root = resolve_repository(args.repository)
        if args.command == "describe":
            operation = describe(tool_id)
        else:
            runners = {"ATOM_SEARCH": run_search, "ATOM_READ": run_read, "ATOM_CREATE": run_create,
                       "ATOM_UPDATE": run_update, "ATOM_MOVE": run_move, "ATOM_ARCHIVE": run_archive,
                       "ATOM_PROMOTE": run_promote, "ATOM_UPGRADE": run_upgrade}
            operation = runners[tool_id](root, args)
        envelope = {"schema_version": SCHEMA_VERSION, "tool": {"capability_id": tool_id, "kind": kind},
                    "ok": True, "mode": mode, "diagnostics": [], "result": operation}
        print(canonical_json(envelope))
        return 0
    except (ToolError, OSError, UnicodeError) as error:
        diagnostic: dict[str, Any] = {"code": getattr(error, "code", "operation-failed"),
                                      "message": getattr(error, "message", str(error))}
        if getattr(error, "details", None):
            diagnostic["details"] = error.details
        envelope = {"schema_version": SCHEMA_VERSION, "tool": {"capability_id": tool_id, "kind": kind},
                    "ok": False, "mode": mode, "diagnostics": [diagnostic], "result": {}}
        print(canonical_json(envelope))
        return 2
