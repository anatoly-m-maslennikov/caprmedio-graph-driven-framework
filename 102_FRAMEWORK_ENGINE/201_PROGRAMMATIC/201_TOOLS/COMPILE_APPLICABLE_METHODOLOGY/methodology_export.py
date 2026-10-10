"""Seal and export one frozen active-Methodology source frontier."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import re
import shutil
import sys
import tempfile
import tomllib
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Mapping, Sequence


_ROOT = Path(__file__).resolve().parent
_SPEC = importlib.util.spec_from_file_location("caprmedio_methodology_export_compiler", _ROOT / "compile_applicable_methodology.py")
assert _SPEC and _SPEC.loader
compiler = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = compiler
_SPEC.loader.exec_module(compiler)

SCHEMA = "caprmedio.methodology_export.v3"
LEGACY_EXPORT_SCHEMA = "caprmedio.methodology_export.v2"
FROZEN_SCHEMA = "caprmedio.methodology_export.frozen.v3"
LEGACY_FROZEN_SCHEMA = "caprmedio.methodology_export.frozen.v1"
LEGACY_PROJECT_FROZEN_SCHEMA = "caprmedio.methodology_export.frozen.v2"
SEAL_SCHEMA = "caprmedio.methodology_export.seal.v1"
INVENTORY_NAME = "methodology-export-inventory.json"
SEAL_NAME = "methodology-export-seal.json"
UNSEALED_NAME = "methodology-export-unsealed.json"
LOCK_NAME = ".methodology-export.lock"


class MethodologyExportError(Exception):
    def __init__(self, code: str, message: str, **details: object) -> None:
        super().__init__(message)
        self.code, self.message, self.details = code, message, details


@dataclass(frozen=True)
class SourcePin:
    path: str
    sha256: str


@dataclass(frozen=True)
class Atom:
    source_path: str
    atom_id: str
    version: int
    sha256: str

    def record(self) -> dict[str, object]:
        return {"atom_id": self.atom_id, "sha256": self.sha256, "source_path": self.source_path, "version": self.version}


@dataclass(frozen=True)
class BindingAtom:
    """One non-authoritative Active Delivery source with a package Tool binding."""

    source_path: str
    atom_id: str
    version: int
    sha256: str

    def record(self) -> dict[str, object]:
        return {"atom_id": self.atom_id, "sha256": self.sha256, "source_path": self.source_path, "version": self.version}


@dataclass(frozen=True)
class FrozenManifest:
    payload: dict[str, object]
    sha256: str
    selected: tuple[Atom, ...]
    supports: tuple[SourcePin, ...]
    catalogs: tuple[SourcePin, ...]
    bindings: tuple[BindingAtom, ...]
    framework_engine_inventory_sha256: str | None


@dataclass(frozen=True)
class MethodologyExport:
    output_root: Path
    inventory_path: Path
    inventory: dict[str, object]
    inventory_digest: str
    atom_count: int
    support_count: int
    frozen_manifest_sha256: str


def _json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _valid_digest(value: object) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(char in "0123456789abcdef" for char in value)


def _checksum(value: Mapping[str, object]) -> str:
    unsigned = dict(value)
    unsigned.pop("sha256", None)
    return _digest(_json(unsigned))


def _relative(value: object, field: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value:
        raise MethodologyExportError("export-path-invalid", f"{field} must be a slash-separated relative path")
    path = Path(value)
    if path.is_absolute() or path.as_posix() != value or any(part in {"", ".", ".."} for part in path.parts):
        raise MethodologyExportError("export-path-unsafe", f"{field} is unsafe", path=value)
    return value


def _protected_basename(name: str) -> bool:
    return name.startswith(".env") or name.endswith(".env")


def _guard_source_metadata(root: Path) -> None:
    """Reject protected names using directory metadata before any payload read.

    This runs before compiler discovery as well as before every source-tree or
    pinned-source payload read.  It deliberately uses ``scandir`` metadata,
    never ``Path.rglob``/``read_bytes`` on an entry that may be protected.
    """
    for ancestor in (root, *root.parents):
        if _protected_basename(ancestor.name):
            raise MethodologyExportError("protected-source-path", "source_root has a protected .env ancestor", path=ancestor.as_posix())
        if ancestor.is_symlink():
            raise MethodologyExportError("source-symlink-forbidden", "source_root has a symlinked ancestor", path=ancestor.as_posix())

    def walk(directory: Path) -> None:
        with os.scandir(directory) as entries:
            for entry in entries:
                if _protected_basename(entry.name):
                    raise MethodologyExportError("protected-source-path", "source tree contains a protected .env path", path=(directory / entry.name).as_posix())
                if entry.is_symlink():
                    raise MethodologyExportError("source-symlink-forbidden", "source tree contains a symlink", path=(directory / entry.name).as_posix())
                if entry.is_dir(follow_symlinks=False):
                    walk(directory / entry.name)
                elif not entry.is_file(follow_symlinks=False):
                    raise MethodologyExportError("source-entry-invalid", "source tree contains a non-regular entry", path=(directory / entry.name).as_posix())

    walk(root)


def _source_root(value: Path | str) -> Path:
    root = Path(value)
    if not root.is_absolute() or ".." in root.parts:
        raise MethodologyExportError("source-root-unsafe", "source_root must be an absolute path without traversal")
    if not root.is_dir():
        raise MethodologyExportError("source-root-invalid", "source_root must be a regular directory")
    root = root.resolve(strict=True)
    _guard_source_metadata(root)
    return root


def _source_tree_digest(root: Path) -> str:
    _guard_source_metadata(root)
    rows = [
        {"path": path.relative_to(root).as_posix(), "sha256": _digest(path.read_bytes())}
        for path in sorted(root.rglob("*"))
        if path.is_file() and path.name != ".DS_Store"
    ]
    return _digest(_json(rows))


def _pins(value: object, field: str) -> tuple[SourcePin, ...]:
    if not isinstance(value, list):
        raise MethodologyExportError("source-pins-invalid", f"{field} must be a list")
    rows: list[SourcePin] = []
    for item in value:
        if not isinstance(item, Mapping) or set(item) != {"path", "sha256"}:
            raise MethodologyExportError("source-pins-invalid", f"{field} entries require path and sha256")
        path, digest = _relative(item["path"], f"{field}.path"), item["sha256"]
        if not _valid_digest(digest):
            raise MethodologyExportError("source-pins-invalid", f"{field} sha256 is invalid", path=path)
        if path != ".DS_Store" and Path(path).name != ".DS_Store":
            rows.append(SourcePin(path, digest))
    if len({pin.path for pin in rows}) != len(rows):
        raise MethodologyExportError("source-pins-duplicate", f"{field} repeats a source path")
    return tuple(sorted(rows, key=lambda pin: pin.path))


def _pin_bytes(root: Path, pin: SourcePin, kind: str) -> bytes:
    _guard_source_metadata(root)
    path = root / pin.path
    if path.is_symlink() or not path.is_file():
        raise MethodologyExportError(f"{kind}-pin-missing", f"{kind} pin is not a regular source file", path=pin.path)
    if _digest(path.read_bytes()) != pin.sha256:
        raise MethodologyExportError(f"{kind}-pin-stale", f"{kind} pin digest does not match source bytes", path=pin.path)
    return path.read_bytes()


def _project_binding(project_root: Path | str | None, source_root: Path) -> dict[str, object] | None:
    """Bind a Project export to its resolved places and raw control carriers."""
    if project_root is None:
        return None
    project = Path(project_root)
    if not project.is_absolute() or ".." in project.parts or project.is_symlink() or not project.is_dir():
        raise MethodologyExportError("project-root-invalid", "project_root must be an absolute regular Project directory")
    project = project.resolve(strict=True)
    try:
        places = compiler.methodology_paths(project)
    except compiler.CompileError as error:
        raise MethodologyExportError(error.code, error.message, **error.details) from error
    declared_source = project / places.source
    if declared_source.is_symlink() or not declared_source.is_dir() or declared_source.resolve(strict=True) != source_root:
        raise MethodologyExportError("project-source-root-mismatch", "source_root is not the Project Structure declared Methodology source root")
    project_settings = project / compiler.SETTINGS_PATH
    structure = project / places.control_root / "project_structure.toml"
    for path, label in ((project_settings, "Project Settings"), (structure, "Project Structure")):
        if path.is_symlink() or not path.is_file():
            raise MethodologyExportError("project-binding-invalid", f"{label} must be a regular file", path=path.as_posix())
    instance = project / places.control_root / compiler.INSTANCE_SETTINGS_RELATIVE
    try:
        instance_present = compiler.safe_framework_settings_carrier(project, instance)
    except compiler.CompileError as error:
        raise MethodologyExportError(error.code, error.message, **error.details) from error
    return {
        "project_root": project.as_posix(),
        "control_root": (project / places.control_root).resolve(strict=True).as_posix(),
        "source_root": source_root.as_posix(),
        "project_settings_path": project_settings.as_posix(),
        "project_settings_sha256": _digest(project_settings.read_bytes()),
        "project_structure_path": structure.as_posix(),
        "project_structure_sha256": _digest(structure.read_bytes()),
        "instance_settings_path": instance.as_posix(),
        "instance_settings_sha256": _digest(instance.read_bytes()) if instance_present else None,
    }


def reopen_project_export_binding(project_root: Path | str, source_root: Path | str) -> Mapping[str, object]:
    """Reopen the current immutable Project export binding for a declared source root."""
    binding = _project_binding(project_root, _source_root(source_root))
    if binding is None:
        raise MethodologyExportError("project-root-invalid", "project_root is required for a Project export binding")
    return binding


def _active(root: Path, project_binding: Mapping[str, object] | None = None) -> tuple[Atom, ...]:
    _guard_source_metadata(root)
    if project_binding is None:
        if any(
            path.is_file()
            for layer in ("002_INSTALLED_EXTENSIONS", "003_PROJECT_CONFIGURATION")
            for path in (root / layer).rglob("*.md")
        ):
            raise MethodologyExportError("project-binding-required", "detached export accepts Core Meta-model sources only")
        discovery_root = root
        places = compiler.MethodologyPaths(source=Path("."), output=Path(".export-output"), control_root=Path("."))
    else:
        discovery_root = Path(str(project_binding["project_root"]))
        try:
            places = compiler.methodology_paths(discovery_root)
        except compiler.CompileError as error:
            raise MethodologyExportError(error.code, error.message, **error.details) from error
    try:
        candidates, diagnostics, _ = compiler.discover_candidates(discovery_root, places)
    except compiler.CompileError as error:
        raise MethodologyExportError(error.code, error.message, **error.details) from error
    blocked = [item for item in diagnostics if item.get("code") not in {"source-excluded", "empty-source-frontier"}]
    if blocked:
        item = blocked[0]
        raise MethodologyExportError(str(item["code"]), str(item.get("message", "active frontier invalid")))
    if project_binding is None and any(item.layer != "CORE_META_MODEL" for item in candidates):
        raise MethodologyExportError("project-binding-required", "detached export accepts Core Meta-model sources only")
    atoms = tuple(sorted((Atom(
        (discovery_root / item.source_path).relative_to(root).as_posix(), item.atom_id, item.version, item.source_sha256
    ) for item in candidates), key=lambda atom: atom.source_path))
    if not atoms:
        raise MethodologyExportError("empty-source-frontier", "no eligible current active Methodology source revisions were found")
    return atoms


def _stable_active(root: Path, project_binding: Mapping[str, object] | None = None) -> tuple[tuple[Atom, ...], str]:
    """Bind discovery to an unchanged metadata-guarded source-tree snapshot."""
    before = _source_tree_digest(root)
    active = _active(root, project_binding)
    after = _source_tree_digest(root)
    if after != before:
        raise MethodologyExportError("source-tree-changed-during-discovery", "source tree changed while active frontier was discovered")
    return active, after


def _frontier_digest(atoms: Sequence[Atom]) -> str:
    return _digest(_json([atom.record() for atom in sorted(atoms, key=lambda atom: atom.source_path)]))


def _atom_records(value: object, field: str) -> tuple[Atom, ...]:
    if not isinstance(value, list) or not value:
        raise MethodologyExportError("frozen-manifest-invalid", f"{field} must be non-empty")
    atoms: list[Atom] = []
    for item in value:
        if not isinstance(item, Mapping) or set(item) != {"atom_id", "sha256", "source_path", "version"}:
            raise MethodologyExportError("frozen-manifest-invalid", f"{field} record is invalid")
        path, atom_id, version, digest = _relative(item["source_path"], f"{field}.source_path"), item["atom_id"], item["version"], item["sha256"]
        if not isinstance(atom_id, str) or not atom_id or type(version) is not int or version < 1 or not _valid_digest(digest):
            raise MethodologyExportError("frozen-manifest-invalid", f"{field} record is invalid", path=path)
        atoms.append(Atom(path, atom_id, version, digest))
    ordered = tuple(sorted(atoms, key=lambda atom: atom.source_path))
    if len({atom.source_path for atom in ordered}) != len(ordered) or [atom.record() for atom in ordered] != value:
        raise MethodologyExportError("frozen-manifest-invalid", f"{field} must be unique and canonical")
    return ordered


def _binding_records(value: object, field: str) -> tuple[BindingAtom, ...]:
    if not isinstance(value, list):
        raise MethodologyExportError("frozen-manifest-invalid", f"{field} must be a list")
    bindings: list[BindingAtom] = []
    for item in value:
        if not isinstance(item, Mapping) or set(item) != {"atom_id", "sha256", "source_path", "version"}:
            raise MethodologyExportError("frozen-manifest-invalid", f"{field} record is invalid")
        path, atom_id, version, digest = _relative(item["source_path"], f"{field}.source_path"), item["atom_id"], item["version"], item["sha256"]
        if not isinstance(atom_id, str) or not atom_id or type(version) is not int or version < 1 or not _valid_digest(digest):
            raise MethodologyExportError("frozen-manifest-invalid", f"{field} record is invalid", path=path)
        bindings.append(BindingAtom(path, atom_id, version, digest))
    ordered = tuple(sorted(bindings, key=lambda binding: binding.source_path))
    if len({binding.source_path for binding in ordered}) != len(ordered) or [binding.record() for binding in ordered] != value:
        raise MethodologyExportError("frozen-manifest-invalid", f"{field} must be unique and canonical")
    return ordered


def _project_regular(root: Path, relative: str, *, code: str) -> Path:
    path = root
    for component in Path(relative).parts:
        path = path / component
        try:
            observed = path.lstat()
        except OSError as error:
            raise MethodologyExportError(code, "binding entrypoint is absent from the Framework Engine inventory", path=relative) from error
        if path.is_symlink() or not (path.is_dir() or path.is_file()):
            raise MethodologyExportError(code, "binding entrypoint has an unsafe Framework Engine ancestor", path=relative)
    if not path.is_file():
        raise MethodologyExportError(code, "binding entrypoint is not a regular Framework Engine member", path=relative)
    return path


def _tool_entrypoint(data: bytes, source_path: str) -> str | None:
    """Read one closed TOML tool-binding declaration from an Active Delivery Atom."""
    if b"[tool_binding]" not in data:
        return None
    blocks = re.findall(rb"(?ms)^```toml\n(.*?)^```\s*$", data)
    declarations: list[str] = []
    for block in blocks:
        try:
            value = tomllib.loads(block.decode("utf-8"))
        except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
            raise MethodologyExportError("binding-declaration-invalid", "Tool binding TOML is invalid", path=source_path) from error
        binding = value.get("tool_binding") if isinstance(value, Mapping) else None
        if binding is None:
            continue
        if not isinstance(binding, Mapping):
            raise MethodologyExportError("binding-declaration-invalid", "Tool binding declaration must be a TOML table", path=source_path)
        entrypoint = binding.get("entrypoint")
        declarations.append(_relative(entrypoint, "tool_binding.entrypoint"))
    if len(declarations) != 1:
        raise MethodologyExportError("binding-declaration-invalid", "Active Delivery Atom must have exactly one closed Tool binding declaration", path=source_path)
    return declarations[0]


_BINDING_PRUNED_DIRECTORIES = frozenset({"archive", "draft", "drafts", "journal", "projection", "_journal", "_projection", "_release_materialized"})


def _project_directory(root: Path, relative: str, *, code: str) -> Path:
    """Reopen a project-relative directory without following an alias."""
    path = root
    for component in Path(relative).parts:
        path = path / component
        try:
            observed = path.lstat()
        except OSError as error:
            raise MethodologyExportError(code, "declared Framework Engine path is absent", path=relative) from error
        if path.is_symlink() or not path.is_dir():
            raise MethodologyExportError(code, "declared Framework Engine path is unsafe", path=relative)
    return path


def _framework_engine_scope(project_binding: Mapping[str, object] | None) -> tuple[Path, Path, str] | None:
    """Open the one Framework Engine authority child explicitly bound by Structure."""
    if project_binding is None:
        return None
    project = Path(str(project_binding["project_root"]))
    control_root = Path(str(project_binding["control_root"]))
    structure = Path(str(project_binding["project_structure_path"]))
    if (
        not project.is_absolute()
        or not control_root.is_absolute()
        or not structure.is_absolute()
        or project.is_symlink()
        or control_root.is_symlink()
        or structure.is_symlink()
        or not project.is_dir()
        or not control_root.is_dir()
        or not structure.is_file()
        or _digest(structure.read_bytes()) != project_binding.get("project_structure_sha256")
    ):
        raise MethodologyExportError("project-binding-invalid", "bound Project Structure carrier is not current")
    try:
        document = tomllib.loads(structure.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise MethodologyExportError("framework-engine-scope-invalid", "Project Structure is not valid UTF-8 TOML") from error
    units = document.get("scope_units") if isinstance(document, Mapping) else None
    matches = [unit for unit in units if isinstance(unit, Mapping) and unit.get("scope_unit_name") == "FRAMEWORK_ENGINE"] if isinstance(units, list) else []
    if len(matches) != 1:
        raise MethodologyExportError("framework-engine-scope-invalid", "Project Structure must declare exactly one FRAMEWORK_ENGINE scope")
    authority = _relative(matches[0].get("authority_path"), "FRAMEWORK_ENGINE.authority_path")
    delivery = _relative(matches[0].get("delivery_path"), "FRAMEWORK_ENGINE.delivery_path")
    authority_root = _project_directory(project, authority, code="framework-engine-scope-invalid")
    try:
        authority_root.relative_to(control_root)
    except ValueError as error:
        raise MethodologyExportError("framework-engine-scope-invalid", "Framework Engine authority must be inside the bound control child", path=authority) from error
    return project, authority_root, delivery


def _binding_frontier(project_binding: Mapping[str, object] | None) -> tuple[BindingAtom, ...]:
    """Discover every eligible Active Delivery binding in the exact bound control tree."""
    scope = _framework_engine_scope(project_binding)
    if scope is None:
        return ()
    project, _engine_authority, delivery_root = scope
    control_root = Path(str(project_binding["control_root"]))
    _guard_source_metadata(control_root)
    bindings: list[BindingAtom] = []
    for path in sorted(control_root.rglob("*.md")):
        relative_from_control = path.relative_to(control_root)
        if _BINDING_PRUNED_DIRECTORIES.intersection(relative_from_control.parts):
            continue
        if path.name == ".DS_Store" or path.is_symlink() or not path.is_file():
            continue
        source_path = path.relative_to(project).as_posix()
        data = path.read_bytes()
        if not data.startswith(b"---\n"):
            continue
        try:
            frontmatter, _ = compiler.split_frontmatter(data, source_path)
            if compiler.top_scalar(frontmatter, "content_role") != "Delivery":
                continue
            if re.search(r"(?m)^projection:\s*(?:$|\{)", frontmatter):
                continue
            if compiler.top_scalar(frontmatter, "status") != "Active":
                continue
            version_raw = compiler.top_scalar(frontmatter, "version")
            if version_raw is None or not re.fullmatch(r"[1-9][0-9]*", version_raw):
                raise MethodologyExportError("binding-source-version-invalid", "Active Delivery binding requires a positive integer version", path=source_path)
            if not compiler.top_scalar(frontmatter, "atom_id"):
                raise MethodologyExportError("binding-source-identity-invalid", "Active Delivery binding requires an explicit Atom ID", path=source_path)
            atom_id = compiler.derive_atom_id(path, frontmatter)
        except compiler.CompileError as error:
            raise MethodologyExportError(error.code, error.message, **error.details) from error
        entrypoint = _tool_entrypoint(data, source_path)
        if entrypoint is None:
            continue
        entrypoint_path = Path(entrypoint)
        delivery_path = Path(delivery_root)
        if entrypoint_path.parts[: len(delivery_path.parts)] != delivery_path.parts:
            raise MethodologyExportError("binding-entrypoint-invalid", "Tool binding entrypoint must be a Framework Engine inventory member", path=entrypoint)
        _project_regular(project, entrypoint, code="binding-entrypoint-invalid")
        bindings.append(BindingAtom(source_path, atom_id, int(version_raw), _digest(data)))
    ordered = tuple(sorted(bindings, key=lambda binding: binding.source_path))
    if len({binding.source_path for binding in ordered}) != len(ordered) or len({(binding.atom_id, binding.version) for binding in ordered}) != len(ordered):
        raise MethodologyExportError("binding-frontier-duplicate", "binding frontier has duplicate source identities")
    return ordered


def _binding_control_tree_digest(control_root: Path) -> str:
    """Hash only the controls eligible for binding discovery, never archived payloads."""
    _guard_source_metadata(control_root)
    rows = []
    for path in sorted(control_root.rglob("*")):
        relative = path.relative_to(control_root)
        if _BINDING_PRUNED_DIRECTORIES.intersection(relative.parts):
            continue
        if not path.is_file() or path.name == ".DS_Store":
            continue
        rows.append({"path": relative.as_posix(), "sha256": _digest(path.read_bytes())})
    return _digest(_json(rows))


def _framework_engine_inventory_digest(project_binding: Mapping[str, object] | None) -> str | None:
    """Bind discovery to the full regular Framework Engine inventory, not one path."""
    scope = _framework_engine_scope(project_binding)
    if scope is None:
        return None
    project, _authority_root, delivery_root = scope
    engine = project / delivery_root
    if not engine.exists():
        return _digest(_json([]))
    if engine.is_symlink() or not engine.is_dir():
        raise MethodologyExportError("framework-engine-inventory-invalid", "Framework Engine inventory root is unsafe", path=engine.as_posix())
    return _source_tree_digest(engine)


def _stable_binding_frontier(project_binding: Mapping[str, object] | None) -> tuple[tuple[BindingAtom, ...], str | None]:
    scope = _framework_engine_scope(project_binding)
    if scope is None:
        return (), None
    _project, _engine_authority, _delivery_root = scope
    control_root = Path(str(project_binding["control_root"]))
    before_source = _binding_control_tree_digest(control_root)
    before_inventory = _framework_engine_inventory_digest(project_binding)
    bindings = _binding_frontier(project_binding)
    after_inventory = _framework_engine_inventory_digest(project_binding)
    after_source = _binding_control_tree_digest(control_root)
    if after_inventory != before_inventory:
        raise MethodologyExportError("framework-engine-changed-during-discovery", "Framework Engine inventory changed while binding frontier was discovered")
    if after_source != before_source:
        raise MethodologyExportError("binding-source-changed-during-discovery", "Framework Engine source controls changed while binding frontier was discovered")
    return bindings, after_inventory


def _binding_candidate(binding: BindingAtom, source: bytes) -> Any:
    try:
        frontmatter, _ = compiler.split_frontmatter(source, binding.source_path)
        relations = compiler.relations_digest(frontmatter)
    except compiler.CompileError as error:
        raise MethodologyExportError(error.code, error.message, **error.details) from error
    return compiler.Candidate(
        layer="BINDING", layer_order=0, role="delivery", role_directory="07_delivery",
        atom_id=binding.atom_id, version=binding.version, source_path=binding.source_path,
        source_sha256=binding.sha256, basename=Path(binding.source_path).name,
        priority=None, priority_group=None, replacements=(), incompatibilities=(),
        definition_term=None, definition_subject_path=None, original_relations_sha256=relations,
    )


def binding_projection_bytes(source: bytes, binding: BindingAtom) -> bytes:
    """Render the canonical non-authoritative projection for one frozen binding pin."""
    return compiler.projection_bytes(source, binding.source_path, _binding_candidate(binding, source))


def validate_binding_projection_source_preservation(source: bytes, projected: bytes, binding: BindingAtom) -> None:
    """Verify canonical metadata insertion and exact inverse source preservation."""
    try:
        compiler.validate_projection_source_preservation(source, projected, binding.source_path, _binding_candidate(binding, source))
    except compiler.CompileError as error:
        raise MethodologyExportError(error.code, error.message, **error.details) from error


def _support_is_atom(pin: SourcePin, data: bytes) -> None:
    if Path(pin.path).suffix != ".md" or not data.startswith(b"---\n"):
        return
    try:
        frontmatter, _ = compiler.split_frontmatter(data, pin.path)
    except compiler.CompileError:
        return
    if compiler.top_scalar(frontmatter, "atom_id") is not None:
        raise MethodologyExportError("support-atom-forbidden", "Atom carriers must be in the frozen selected frontier", path=pin.path)


def freeze_methodology_manifest(*, source_root: Path | str, selected_atoms: Sequence[Mapping[str, object]], support_inventory: Sequence[Mapping[str, object]], catalog_pins: Sequence[Mapping[str, object]], project_root: Path | str | None = None) -> dict[str, object]:
    """Create data for a separate freeze authority; it performs no output write."""
    root = _source_root(source_root)
    project_binding = _project_binding(project_root, root)
    active, source_tree = _stable_active(root, project_binding)
    if not isinstance(selected_atoms, Sequence) or isinstance(selected_atoms, (str, bytes)) or not selected_atoms:
        raise MethodologyExportError("selected-atoms-invalid", "selected_atoms must be non-empty")
    index: dict[tuple[str, int], list[Atom]] = {}
    for atom in active:
        index.setdefault((atom.atom_id, atom.version), []).append(atom)
    selected: list[Atom] = []
    for request in selected_atoms:
        if not isinstance(request, Mapping) or set(request) != {"atom_id", "version"}:
            raise MethodologyExportError("selected-atoms-invalid", "freeze selection requires exactly atom_id and version")
        atom_id, version = request["atom_id"], request["version"]
        matches = index.get((atom_id, version), []) if isinstance(atom_id, str) and type(version) is int else []
        if len(matches) == 0:
            raise MethodologyExportError("selected-source-revision-missing", "freeze selection is not active", atom_id=atom_id, version=version)
        if len(matches) != 1:
            raise MethodologyExportError("selected-source-ambiguous", "freeze selection has multiple active carriers", atom_id=atom_id, version=version)
        selected.append(matches[0])
    selected = sorted(selected, key=lambda atom: atom.source_path)
    if len({(atom.atom_id, atom.version) for atom in selected}) != len(selected):
        raise MethodologyExportError("selected-atoms-duplicate", "freeze selection repeats an Atom revision")
    supports, catalogs = _pins(list(support_inventory), "support_inventory"), _pins(list(catalog_pins), "catalog_pins")
    if {atom.source_path for atom in selected}.intersection(pin.path for pin in supports):
        raise MethodologyExportError("support-overlaps-selected-atom", "support inventory duplicates a selected Atom")
    for pin in supports:
        _support_is_atom(pin, _pin_bytes(root, pin, "support"))
    for pin in catalogs:
        _pin_bytes(root, pin, "catalog")
    bindings, engine_inventory = _stable_binding_frontier(project_binding)
    payload: dict[str, object] = {
        "active_frontier": [atom.record() for atom in active],
        "active_frontier_sha256": _frontier_digest(active),
        "binding_atoms": [binding.record() for binding in bindings],
        "catalog_pins": [{"path": pin.path, "sha256": pin.sha256} for pin in catalogs],
        "schema": FROZEN_SCHEMA,
        "project_binding": project_binding,
        "framework_engine_inventory_sha256": engine_inventory,
        "selected_atoms": [atom.record() for atom in selected],
        "source_root": root.as_posix(),
        "source_tree_sha256": source_tree,
        "support_inventory": [{"path": pin.path, "sha256": pin.sha256} for pin in supports],
    }
    payload["sha256"] = _checksum(payload)
    return payload


def frozen_manifest_bytes(manifest: Mapping[str, object]) -> bytes:
    value = dict(manifest)
    if value.get("schema") not in {FROZEN_SCHEMA, LEGACY_PROJECT_FROZEN_SCHEMA, LEGACY_FROZEN_SCHEMA} or not _valid_digest(value.get("sha256")) or value["sha256"] != _checksum(value):
        raise MethodologyExportError("frozen-manifest-invalid", "frozen manifest checksum is invalid")
    return _json(value) + b"\n"


def _frozen(root: Path, value: Path | str, project_root: Path | str | None = None) -> FrozenManifest:
    path = Path(value)
    if not path.is_absolute() or ".." in path.parts or path.is_symlink() or not path.is_file():
        raise MethodologyExportError("frozen-manifest-missing", "frozen_manifest_path must be an absolute regular file")
    try:
        raw, payload = path.read_bytes(), json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise MethodologyExportError("frozen-manifest-invalid", "frozen manifest must be valid JSON") from error
    legacy_required = {"active_frontier", "active_frontier_sha256", "catalog_pins", "schema", "selected_atoms", "sha256", "source_root", "source_tree_sha256", "support_inventory"}
    project_required = legacy_required | {"project_binding"}
    required = project_required | {"binding_atoms", "framework_engine_inventory_sha256"}
    schema = payload.get("schema") if isinstance(payload, dict) else None
    expected_fields = legacy_required if schema == LEGACY_FROZEN_SCHEMA else project_required if schema == LEGACY_PROJECT_FROZEN_SCHEMA else required
    if not isinstance(payload, dict) or set(payload) != expected_fields or raw != _json(payload) + b"\n" or schema not in {FROZEN_SCHEMA, LEGACY_PROJECT_FROZEN_SCHEMA, LEGACY_FROZEN_SCHEMA} or not _valid_digest(payload.get("sha256")) or payload["sha256"] != _checksum(payload):
        raise MethodologyExportError("frozen-manifest-invalid", "frozen manifest bytes or fields are invalid")
    if payload["source_root"] != root.as_posix() or not _valid_digest(payload.get("source_tree_sha256")) or not _valid_digest(payload.get("active_frontier_sha256")):
        raise MethodologyExportError("frozen-manifest-root-mismatch", "frozen manifest does not bind source_root")
    active, selected = _atom_records(payload["active_frontier"], "active_frontier"), _atom_records(payload["selected_atoms"], "selected_atoms")
    if payload["active_frontier_sha256"] != _frontier_digest(active) or not set(selected).issubset(set(active)):
        raise MethodologyExportError("frozen-manifest-invalid", "frozen selected frontier is not complete")
    supports, catalogs = _pins(payload["support_inventory"], "support_inventory"), _pins(payload["catalog_pins"], "catalog_pins")
    bindings: tuple[BindingAtom, ...] = ()
    if schema == LEGACY_FROZEN_SCHEMA:
        if project_root is not None:
            raise MethodologyExportError("frozen-manifest-legacy-read-only", "historical frozen.v1 manifests cannot become Project-bound exports")
        project_binding = None
    else:
        project_binding = _project_binding(project_root, root)
        if payload["project_binding"] != project_binding:
            raise MethodologyExportError("frozen-manifest-project-binding-stale", "frozen manifest Project binding is no longer current")
    current_active, current_tree = _stable_active(root, project_binding)
    if current_active != active or current_tree != payload["source_tree_sha256"]:
        raise MethodologyExportError("frozen-frontier-stale", "current authoring frontier differs from frozen manifest")
    engine_inventory: str | None = None
    if schema == FROZEN_SCHEMA:
        bindings = _binding_records(payload["binding_atoms"], "binding_atoms")
        expected_inventory = _framework_engine_inventory_digest(project_binding)
        if payload["framework_engine_inventory_sha256"] != expected_inventory or (expected_inventory is not None and not _valid_digest(expected_inventory)):
            raise MethodologyExportError("framework-engine-inventory-stale", "Framework Engine inventory differs from frozen manifest")
        current_bindings, engine_inventory = _stable_binding_frontier(project_binding)
        if current_bindings != bindings:
            raise MethodologyExportError("binding-frontier-stale", "current Tool binding frontier differs from frozen manifest")
    for pin in supports:
        _support_is_atom(pin, _pin_bytes(root, pin, "support"))
    for pin in catalogs:
        _pin_bytes(root, pin, "catalog")
    return FrozenManifest(payload, payload["sha256"], selected, supports, catalogs, bindings, engine_inventory)


def _candidate_atom_bytes(root: Path, atom: Atom) -> bytes:
    data = _pin_bytes(root, SourcePin(atom.source_path, atom.sha256), "selected-source")
    try:
        frontmatter, _ = compiler.split_frontmatter(data, atom.source_path)
        valid = compiler.derive_atom_id(Path(atom.source_path), frontmatter) == atom.atom_id and compiler.top_scalar(frontmatter, "status") == "Active" and compiler.top_scalar(frontmatter, "version") == str(atom.version)
    except compiler.CompileError:
        valid = False
    if not valid:
        raise MethodologyExportError("selected-source-tampered", "selected source metadata changed", path=atom.source_path)
    return data


def _candidate_root(value: Path | str) -> Path:
    root = Path(value)
    if not root.is_absolute() or ".." in root.parts or not any(index + 2 == len(root.parts) - 1 and root.parts[index + 1] == "release_candidates" and root.parts[index + 2] for index, part in enumerate(root.parts) if part == ".caprmedio_tmp"):
        raise MethodologyExportError("candidate-root-unsafe", "release_candidate_root must end in .caprmedio_tmp/release_candidates/<run_id>")
    return root


def _prepare_candidate(root: Path, source: Path) -> None:
    if root == source or root.is_relative_to(source):
        raise MethodologyExportError("candidate-root-unsafe", "release candidate cannot be inside source_root")
    for ancestor in (root, *root.parents):
        if ancestor.is_symlink():
            raise MethodologyExportError("candidate-root-unsafe", "release candidate has a symlinked ancestor", path=ancestor.as_posix())
    root.mkdir(parents=True, exist_ok=True)


def _lock(root: Path) -> int:
    try:
        descriptor = os.open(root / LOCK_NAME, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        os.write(descriptor, str(os.getpid()).encode("ascii"))
        return descriptor
    except FileExistsError as error:
        raise MethodologyExportError("export-run-locked", "candidate already has an export writer", path=(root / LOCK_NAME).as_posix()) from error


def _unlock(root: Path, descriptor: int) -> None:
    os.close(descriptor)
    (root / LOCK_NAME).unlink(missing_ok=True)


def _files(root: Path) -> dict[str, bytes]:
    if not root.exists():
        return {}
    if root.is_symlink() or not root.is_dir():
        raise MethodologyExportError("export-output-unsafe", "output is not a regular directory", path=root.as_posix())
    result: dict[str, bytes] = {}
    for path in root.rglob("*"):
        if path.is_symlink() or not (path.is_file() or path.is_dir()):
            raise MethodologyExportError("export-output-unsafe", "output has an unsafe entry", path=path.as_posix())
        if path.is_file():
            result[path.relative_to(root).as_posix()] = path.read_bytes()
    return result


def _tree(root: Path) -> str:
    return _digest(_json([{"path": path, "sha256": _digest(data)} for path, data in sorted(_files(root).items())]))


def _write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.next")
    if temporary.exists() or temporary.is_symlink():
        raise MethodologyExportError("export-output-busy", "export temporary file exists", path=temporary.as_posix())
    try:
        temporary.write_bytes(data)
        if temporary.read_bytes() != data:
            raise MethodologyExportError("export-write-mismatch", "temporary bytes differ", path=path.as_posix())
        os.replace(temporary, path)
    finally:
        if temporary.exists() or temporary.is_symlink():
            temporary.unlink(missing_ok=True)


def _replace(staged: Path, output: Path) -> None:
    prior_exists, prior, expected = output.exists(), _files(output), _files(staged)
    try:
        output.mkdir(parents=True, exist_ok=True)
        for path, data in expected.items():
            _write(output / path, data)
        for path in sorted(set(prior).difference(expected), reverse=True):
            (output / path).unlink()
    except Exception as error:
        uncertain = False
        try:
            current = _files(output)
            for path in sorted(set(current).difference(prior), reverse=True):
                (output / path).unlink()
            for path, data in prior.items():
                _write(output / path, data)
            if not prior_exists:
                shutil.rmtree(output)
        except Exception:
            uncertain = True
        raise MethodologyExportError("export-replacement-uncertain" if uncertain else "export-replacement-failed", "output replacement failed", path=output.as_posix()) from error


def _read_json(path: Path, code: str) -> dict[str, object]:
    if path.is_symlink() or not path.is_file():
        raise MethodologyExportError(code, "required JSON file is missing", path=path.as_posix())
    try:
        raw, value = path.read_bytes(), json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise MethodologyExportError(code, "required JSON file is invalid", path=path.as_posix()) from error
    if not isinstance(value, dict) or raw != _json(value) + b"\n":
        raise MethodologyExportError(code, "required JSON file is not canonical", path=path.as_posix())
    return value


def _sealed(root: Path) -> MethodologyExport:
    if (root / UNSEALED_NAME).exists() or (root / UNSEALED_NAME).is_symlink():
        raise MethodologyExportError("export-unsealed", "candidate contains an explicitly unsealed export")
    output, seal_path = root / "methodology", root / SEAL_NAME
    if not output.exists() or not seal_path.exists():
        raise MethodologyExportError("export-seal-missing", "candidate has no sealed Methodology export")
    seal = _read_json(seal_path, "export-seal-invalid")
    if set(seal) != {"frozen_manifest_sha256", "inventory_sha256", "output_tree_sha256", "schema", "sha256"} or seal.get("schema") != SEAL_SCHEMA or not _valid_digest(seal.get("sha256")) or seal["sha256"] != _checksum(seal):
        raise MethodologyExportError("export-seal-invalid", "export seal is invalid")
    inventory_path = output / INVENTORY_NAME
    inventory = _read_json(inventory_path, "export-inventory-invalid")
    legacy_fields = {"atoms", "atom_count", "catalog_pins", "catalog_pin_count", "frozen_manifest", "frozen_manifest_sha256", "inventory_sha256", "logical_delivery_root", "schema", "support", "support_count"}
    expected_fields = legacy_fields | {"bindings", "binding_count"}
    inventory_schema = inventory.get("schema")
    if set(inventory) != (expected_fields if inventory_schema == SCHEMA else legacy_fields) or inventory_schema not in {SCHEMA, LEGACY_EXPORT_SCHEMA} or inventory.get("logical_delivery_root") != "methodology":
        raise MethodologyExportError("export-inventory-invalid", "export inventory has an invalid shape")
    unsigned = dict(inventory)
    digest = unsigned.pop("inventory_sha256", None)
    if not _valid_digest(digest) or digest != _digest(_json(unsigned)) or seal["inventory_sha256"] != digest or seal["frozen_manifest_sha256"] != inventory["frozen_manifest_sha256"] or seal["output_tree_sha256"] != _tree(output):
        raise MethodologyExportError("export-seal-invalid", "export seal does not match inventory and output")
    frozen = inventory["frozen_manifest"]
    if not isinstance(frozen, Mapping) or inventory["frozen_manifest_sha256"] != frozen.get("sha256"):
        raise MethodologyExportError("export-inventory-invalid", "inventory lacks its bound frozen manifest")
    frozen_manifest_bytes(frozen)
    if not isinstance(inventory["atoms"], list):
        raise MethodologyExportError("export-inventory-invalid", "inventory atoms are invalid")
    atom_source_records: list[dict[str, object]] = []
    for row in inventory["atoms"]:
        if not isinstance(row, Mapping) or set(row) != {"atom_id", "destination_path", "digest", "sha256", "source_path", "version"} or row.get("destination_path") != row.get("source_path") or row.get("digest") != row.get("sha256"):
            raise MethodologyExportError("export-inventory-invalid", "inventory Atom row is invalid")
        atom_source_records.append({key: row[key] for key in ("atom_id", "sha256", "source_path", "version")})
    atoms = _atom_records(atom_source_records, "inventory.atoms")
    supports = _pins(inventory["support"], "inventory.support")
    binding_source_records: list[dict[str, object]] = []
    binding_destinations: list[str] = []
    binding_inventory = inventory.get("bindings", [])
    if not isinstance(binding_inventory, list):
        raise MethodologyExportError("export-inventory-invalid", "inventory bindings are invalid")
    for row in binding_inventory:
        if not isinstance(row, Mapping) or set(row) != {"atom_id", "destination_path", "digest", "sha256", "source_path", "version"} or not _valid_digest(row.get("digest")):
            raise MethodologyExportError("export-inventory-invalid", "inventory binding row is invalid")
        destination = row.get("destination_path")
        if not isinstance(destination, str) or not destination.startswith("bindings/") or _relative(destination, "inventory.bindings.destination_path") != destination:
            raise MethodologyExportError("export-inventory-invalid", "inventory binding destination is invalid")
        binding_source_records.append({key: row[key] for key in ("atom_id", "sha256", "source_path", "version")})
        binding_destinations.append(destination)
    bindings = _binding_records(binding_source_records, "inventory.bindings")
    if len(set(binding_destinations)) != len(binding_destinations) or inventory["atom_count"] != len(atoms) or inventory["support_count"] != len(supports) or inventory.get("binding_count", 0) != len(bindings) or not isinstance(inventory["catalog_pins"], list) or inventory["catalog_pin_count"] != len(inventory["catalog_pins"]):
        raise MethodologyExportError("export-inventory-invalid", "inventory counts are invalid")
    expected = {INVENTORY_NAME}
    for atom in atoms:
        expected.add(atom.source_path)
        if (output / atom.source_path).is_symlink() or not (output / atom.source_path).is_file() or _digest((output / atom.source_path).read_bytes()) != atom.sha256:
            raise MethodologyExportError("export-inventory-invalid", "Atom output differs from inventory", path=atom.source_path)
    for pin in supports:
        expected.add(pin.path)
        if (output / pin.path).is_symlink() or not (output / pin.path).is_file() or _digest((output / pin.path).read_bytes()) != pin.sha256:
            raise MethodologyExportError("export-inventory-invalid", "support output differs from inventory", path=pin.path)
    binding_rows = {str(row["destination_path"]): row for row in binding_inventory}
    for binding, destination in zip(bindings, binding_destinations, strict=True):
        expected.add(destination)
        member = output / destination
        # Binding projections have their own digest; the ``sha256`` field is
        # deliberately the frozen raw authority pin rather than output bytes.
        row = binding_rows[destination]
        if member.is_symlink() or not member.is_file() or _digest(member.read_bytes()) != row["digest"]:
            raise MethodologyExportError("export-inventory-invalid", "binding projection differs from inventory", path=destination)
    if set(_files(output)) != expected:
        raise MethodologyExportError("export-inventory-invalid", "output contains unsealed files")
    return MethodologyExport(output, inventory_path, inventory, digest, len(atoms), len(supports), str(inventory["frozen_manifest_sha256"]))


def read_sealed_export(*, release_candidate_root: Path | str) -> MethodologyExport:
    root = _candidate_root(release_candidate_root)
    if (root / LOCK_NAME).exists() or (root / LOCK_NAME).is_symlink():
        raise MethodologyExportError("export-run-locked", "candidate export has an active writer")
    return _sealed(root)


def export_selected_methodology(*, source_root: Path | str, frozen_manifest_path: Path | str, release_candidate_root: Path | str, project_root: Path | str | None = None) -> MethodologyExport:
    """Write and seal only the physically frozen active source declaration."""
    source = _source_root(source_root)
    frozen = _frozen(source, frozen_manifest_path, project_root)
    if frozen.payload.get("schema") != FROZEN_SCHEMA:
        raise MethodologyExportError("frozen-manifest-legacy-read-only", "historical frozen manifests cannot create a new export")
    candidate = _candidate_root(release_candidate_root)
    _prepare_candidate(candidate, source)
    descriptor = _lock(candidate)
    try:
        output = candidate / "methodology"
        if output.exists() or (candidate / SEAL_NAME).exists() or (candidate / UNSEALED_NAME).exists():
            sealed = _sealed(candidate)
            if sealed.frozen_manifest_sha256 != frozen.sha256:
                raise MethodologyExportError("export-run-already-sealed", "candidate already has a different sealed export")
            return sealed
        _write(candidate / UNSEALED_NAME, _json({"frozen_manifest_sha256": frozen.sha256, "schema": SCHEMA, "state": "writing"}) + b"\n")
        payloads = {atom.source_path: _candidate_atom_bytes(source, atom) for atom in frozen.selected}
        payloads.update({pin.path: _pin_bytes(source, pin, "support") for pin in frozen.supports})
        binding_rows: list[dict[str, object]] = []
        binding_root = Path(str(frozen.payload["project_binding"]["project_root"])) if isinstance(frozen.payload.get("project_binding"), Mapping) else None
        if binding_root is None:
            raise MethodologyExportError("frozen-manifest-project-binding-stale", "binding projections require a Project binding")
        for binding in frozen.bindings:
            source_bytes = _project_regular(binding_root, binding.source_path, code="binding-source-invalid").read_bytes()
            if _digest(source_bytes) != binding.sha256:
                raise MethodologyExportError("binding-source-stale", "binding source differs from its frozen pin", path=binding.source_path)
            projected = binding_projection_bytes(source_bytes, binding)
            validate_binding_projection_source_preservation(source_bytes, projected, binding)
            destination = f"bindings/{binding.source_path}"
            payloads[destination] = projected
            binding_rows.append({**binding.record(), "destination_path": destination, "digest": _digest(projected)})
        reread = _frozen(source, frozen_manifest_path, project_root)
        if reread != frozen or any(_candidate_atom_bytes(source, atom) != payloads[atom.source_path] for atom in frozen.selected) or any(_pin_bytes(source, pin, "support") != payloads[pin.path] for pin in frozen.supports):
            raise MethodologyExportError("frozen-manifest-stale", "frozen inputs changed during export")
        atom_rows = [{**atom.record(), "destination_path": atom.source_path, "digest": atom.sha256} for atom in frozen.selected]
        support_rows = [{"path": pin.path, "sha256": pin.sha256} for pin in frozen.supports]
        unsigned: dict[str, object] = {"atoms": atom_rows, "atom_count": len(atom_rows), "bindings": binding_rows, "binding_count": len(binding_rows), "catalog_pins": [{"path": pin.path, "sha256": pin.sha256} for pin in frozen.catalogs], "catalog_pin_count": len(frozen.catalogs), "frozen_manifest": frozen.payload, "frozen_manifest_sha256": frozen.sha256, "logical_delivery_root": "methodology", "schema": SCHEMA, "support": support_rows, "support_count": len(support_rows)}
        inventory = {**unsigned, "inventory_sha256": _digest(_json(unsigned))}
        staging = Path(tempfile.mkdtemp(prefix=".methodology-export-", dir=candidate))
        try:
            staged = staging / "methodology"
            for path, data in sorted(payloads.items()):
                _write(staged / path, data)
            _write(staged / INVENTORY_NAME, _json(inventory) + b"\n")
            _replace(staged, output)
            seal: dict[str, object] = {"frozen_manifest_sha256": frozen.sha256, "inventory_sha256": inventory["inventory_sha256"], "output_tree_sha256": _tree(output), "schema": SEAL_SCHEMA}
            seal["sha256"] = _checksum(seal)
            _write(candidate / SEAL_NAME, _json(seal) + b"\n")
            (candidate / UNSEALED_NAME).unlink()
        finally:
            shutil.rmtree(staging, ignore_errors=True)
        # This is the final operation: re-open and validate the seal/inventory
        # after all output bytes and the seal were written.  The public reader
        # additionally refuses while a writer lock exists.
        return _sealed(candidate)
    finally:
        _unlock(candidate, descriptor)
