#!/usr/bin/env python3
# CA-D-253@30
# CA-D-306@30
# CA-D-326@27
# CA-D-359@30
# CA-D-561@25

"""Compile an Applicable Methodology projection for local release."""

from __future__ import annotations



import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from artifact_metadata import SETTINGS_PATH, atom_identifier
from carrier_aliases import carrier_status_folder
from header_yaml import header_scalar
from project_selection import ProjectSelectionError, active_selection
from settings_carrier import read_settings_carrier


DEFAULT_CONTROL_ROOT = SETTINGS_PATH.parent
FRAMEWORK_APPLICABLE_RELATIVE = Path("000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY")
OUTPUT_RELATIVE = DEFAULT_CONTROL_ROOT / FRAMEWORK_APPLICABLE_RELATIVE
SOURCE_RELATIVE = OUTPUT_RELATIVE / "000_APPLICABLE_MTHD_sources"
LAYERS = (
    ("CORE_META_MODEL", 0, True),
    ("INSTALLED_EXTENSIONS", 1, True),
    ("PROJECT_CONFIGURATION", 2, True),
)
ROLES = (
    ("REQUIREMENT", "04_requirement"),
    ("METHOD", "05_method"),
    ("EVALUATION", "06_evaluation"),
    ("DELIVERY", "07_delivery"),
    ("OPERATIONS", "09_operations"),
)
ROLE_BY_DIRECTORY = {directory: role for role, directory in ROLES}
ROLE_ORDER = {directory: index for index, (_, directory) in enumerate(ROLES)}
IGNORED_INSTALLED_EXTENSION_FILES = {".gitkeep"}
RELATION_KINDS = {
    "replacement": {"replacement_of", "replaces"},
    "incompatible": {"incompatible_with", "incompatibility_with"},
}
DEFAULT_SETTINGS_NAME = "caprmedio_framework_default_settings.toml"
INSTANCE_SETTINGS_RELATIVE = Path("000_CAPRMEDIO_framework/caprmedio_framework_settings.toml")


@dataclass(frozen=True)
class MethodologyPaths:
    source: Path = SOURCE_RELATIVE
    output: Path = OUTPUT_RELATIVE
    declaration_digest: str | None = None
    control_root: Path = DEFAULT_CONTROL_ROOT

def configured_control_root(root: Path) -> Path:
    """Resolve the one Project-local control root from Project Settings."""
    settings_path = root / SETTINGS_PATH
    if not settings_path.is_file() or settings_path.is_symlink():
        raise CompileError("project-settings-missing", "Project Settings Carrier is required", path=SETTINGS_PATH.as_posix())
    try:
        settings = read_settings_carrier(settings_path)
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise CompileError("project-settings-invalid", "Project Settings Carrier must be valid UTF-8 TOML", path=SETTINGS_PATH.as_posix()) from error
    value = settings.get("paths", {}).get("control_root") if isinstance(settings.get("paths"), dict) else None
    if not isinstance(value, str) or not value:
        raise CompileError("project-control-root-missing", "Project Settings requires paths.control_root")
    control = Path(value)
    if control.is_absolute() or ".." in control.parts or control == Path(".") or not (root / control).resolve().is_relative_to(root.resolve()):
        raise CompileError("project-control-root-invalid", "paths.control_root must be a safe repository-relative path", value=value)
    return control


def methodology_paths(root: Path) -> MethodologyPaths:
    """Resolve source and delivery places from current Scope Unit Declarations.

    Applicable Methodology is the Projection-location exception: its default
    lives in the Project's Framework folder, not the general ``_projection``
    directory.  An explicit source-unit delivery binding remains authoritative.
    """
    control = configured_control_root(root)
    try:
        selection = active_selection(root)
    except ProjectSelectionError as error:
        raise CompileError("scope-declarations-invalid", "Cannot resolve methodology places from Scope Unit Declarations") from error
    if selection.control_relative != control:
        raise CompileError("project-control-root-invalid", "Project Settings disagree with selected Scope Unit Declarations")
    declared = selection.structure.get("scope_units")
    if isinstance(declared, Mapping):
        units = [declared.get("METHODOLOGY_SOURCES")]
    elif isinstance(declared, (list, tuple)):
        units = [row for row in declared if isinstance(row, Mapping) and row.get("scope_unit_name") == "METHODOLOGY_SOURCES"]
    else:
        raise CompileError("scope-declarations-invalid", "Scope Unit Declarations must derive Scope Unit rows")
    if len(units) != 1:
        raise CompileError("source-unit-cardinality", "Scope Unit Declarations must declare exactly one METHODOLOGY_SOURCES unit")
    unit = units[0]
    if not isinstance(unit, Mapping):
        raise CompileError("source-unit-cardinality", "Scope Unit Declarations must declare exactly one METHODOLOGY_SOURCES unit")
    value = unit.get("authority_path")
    if not isinstance(value, str) or not value:
        raise CompileError("source-unit-place-missing", "Methodology source unit has no declared authority place", property="authority_path")
    source = Path(value)
    if source.is_absolute() or ".." in source.parts or source == Path("."):
        raise CompileError("source-unit-place-invalid", "Methodology source place must be repository-relative", property="authority_path")
    output_value = unit.get("delivery_path")
    if not isinstance(output_value, str) or not output_value:
        raise CompileError("output-unit-place-invalid", "Methodology delivery place must be a non-empty repository-relative path", property="delivery_path")
    output = Path(output_value)
    if output.is_absolute() or ".." in output.parts or output == Path("."):
        raise CompileError("output-unit-place-invalid", "Methodology delivery place must be repository-relative", property="delivery_path")
    source_place = (root / source).resolve()
    output_place = (root / output).resolve()
    if not source_place.is_relative_to(root.resolve()):
        raise CompileError("source-unit-place-invalid", "Methodology source place resolves outside the Project", property="authority_path")
    if not output_place.is_relative_to(root.resolve()):
        raise CompileError("output-unit-place-invalid", "Methodology delivery place resolves outside the Project", property="delivery_path")
    if output_place.is_relative_to(source_place) or any(
        source_place.is_relative_to((output_place / role_directory).resolve())
        for _, role_directory in ROLES
    ):
        raise CompileError("source-output-overlap", "Generated output cannot replace the authoritative source place")
    digest = getattr(selection, "declaration_digest", None)
    if not isinstance(digest, str) or not digest:
        raise CompileError("scope-declarations-invalid", "Scope Unit Declaration frontier has no digest")
    return MethodologyPaths(source, output, digest, control)


def declaration_source_pins(root: Path, places: MethodologyPaths) -> dict[str, str]:
    """Return the current declaration-Atom frontier as path-to-byte-digest pins."""
    if configured_control_root(root) != places.control_root:
        raise CompileError("source-frontier-changed", "Project control root changed after declaration discovery")
    try:
        selection = active_selection(root)
    except ProjectSelectionError as error:
        raise CompileError("scope-declarations-invalid", "Cannot read Scope Unit Declaration frontier") from error
    if selection.control_relative != places.control_root:
        raise CompileError("source-frontier-changed", "Project control root changed after declaration discovery")
    digest = getattr(selection, "declaration_digest", None)
    raw_pins = getattr(selection, "declaration_source_pins", None)
    if digest != places.declaration_digest or not isinstance(raw_pins, Mapping):
        raise CompileError("source-frontier-changed", "Scope Unit Declaration frontier changed after discovery")
    pins: dict[str, str] = {}
    for path, pin in raw_pins.items():
        if not isinstance(path, str) or not isinstance(pin, Mapping):
            raise CompileError("scope-declarations-invalid", "Scope Unit Declaration frontier pins are invalid")
        sha256 = pin.get("sha256")
        if not isinstance(sha256, str) or not re.fullmatch(r"[0-9a-f]{64}", sha256):
            raise CompileError("scope-declarations-invalid", "Scope Unit Declaration frontier pins are invalid", path=path)
        pins[path] = sha256
    return dict(sorted(pins.items()))


def source_layer_paths(root: Path, places: MethodologyPaths) -> dict[str, Path]:
    """Resolve the three physical source-layer roots from current declarations."""
    if configured_control_root(root) != places.control_root:
        raise CompileError("source-frontier-changed", "Project control root changed after declaration discovery")
    try:
        selection = active_selection(root)
    except ProjectSelectionError as error:
        raise CompileError("scope-declarations-invalid", "Cannot read Source Layer declarations") from error
    if selection.control_relative != places.control_root:
        raise CompileError("source-frontier-changed", "Project control root changed after declaration discovery")
    if selection.declaration_digest != places.declaration_digest:
        raise CompileError("source-frontier-changed", "Scope Unit Declaration frontier changed after discovery")
    rows = selection.structure.get("scope_units")
    if not isinstance(rows, (list, tuple)):
        raise CompileError("scope-declarations-invalid", "Scope Unit Declarations must derive source-layer rows")
    by_name = {
        row.get("scope_unit_name"): row
        for row in rows
        if isinstance(row, Mapping) and isinstance(row.get("scope_unit_name"), str)
    }
    names = [name for name, _, _ in LAYERS]
    if any(name not in by_name for name in names):
        raise CompileError("source-layer-declaration-missing", "Scope Unit Declarations must declare every Methodology Source Layer")
    paths: dict[str, Path] = {}
    for name in names:
        row = by_name[name]
        value = row.get("authority_path")
        path = Path(value) if isinstance(value, str) else None
        if path is None or path.is_absolute() or ".." in path.parts or path == Path("."):
            raise CompileError("source-layer-authority-invalid", "Source Layer authority path is unsafe", scope_unit_name=name)
        if path.parent != places.source:
            raise CompileError(
                "source-layer-authority-invalid",
                "Source Layer authority must be an immediate child of METHODOLOGY_SOURCES",
                scope_unit_name=name,
                authority_path=path.as_posix(),
            )
        paths[name] = path
    if len({path.name for path in paths.values()}) != len(paths):
        raise CompileError("source-layer-authority-invalid", "Source Layer authorities must have distinct physical paths")
    return paths


class CompileError(Exception):
    """A stable compilation validation failure."""

    def __init__(self, code: str, message: str, **details: object) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details

    def record(self) -> dict[str, object]:
        result: dict[str, object] = {"code": self.code, "message": self.message}
        if self.details:
            result["details"] = self.details
        return result


@dataclass(frozen=True)
class Candidate:
    layer: str
    layer_order: int
    role: str
    role_directory: str
    atom_id: str
    version: int
    source_path: str
    source_sha256: str
    basename: str
    priority: str | None
    priority_group: str | None
    replacements: tuple[str, ...]
    incompatibilities: tuple[str, ...]
    definition_term: str | None
    definition_subject_path: str | None
    output_relative: str = OUTPUT_RELATIVE.as_posix()
    extension_id: str | None = None
    extension_revision: str | None = None
    original_relations_sha256: str = ""

    def frontier_record(self) -> dict[str, object]:
        return {
            "source_layer": self.layer,
            "atom_id": self.atom_id,
            "source_atom_id": self.atom_id,
            "atom_revision": self.version,
            "source_atom_revision": self.version,
            "source_carrier_path": self.source_path,
            "source_carrier_sha256": self.source_sha256,
            "original_relations_sha256": self.original_relations_sha256,
            **({"extension_id": self.extension_id, "extension_revision": self.extension_revision}
               if self.extension_id is not None else {}),
        }

    def report_record(self) -> dict[str, object]:
        record = {
            **self.frontier_record(),
            "content_role": self.role,
            "output_path": f"{self.output_relative}/{self.role_directory}/{self.basename}",
        }
        if self.definition_term is not None:
            record["definition_term"] = self.definition_term
            record["definition_subject_path"] = self.definition_subject_path
        return record


def relations_digest(frontmatter: str) -> str:
    """Digest authored Relations without normalizing or rewriting them."""
    return sha256_bytes("\n".join(top_block(frontmatter, "relations")).encode("utf-8"))


def parse_toml(path: Path, code: str) -> dict[str, object]:
    try:
        value = read_settings_carrier(path)
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise CompileError(code, "Framework Settings must be valid UTF-8 TOML", path=path.as_posix()) from error
    if not isinstance(value, dict):
        raise CompileError(code, "Framework Settings must decode to a table", path=path.as_posix())
    return value


def framework_settings_carriers(root: Path, places: MethodologyPaths) -> tuple[Path, Path]:
    """Return the default and one D359-authoritative instance Settings Carriers."""
    layers = source_layer_paths(root, places)
    return (
        root / layers["CORE_META_MODEL"] / DEFAULT_SETTINGS_NAME,
        root / places.control_root / INSTANCE_SETTINGS_RELATIVE,
    )


def safe_framework_settings_carrier(root: Path, path: Path) -> bool:
    """Return whether an optional carrier is present, refusing symlink escapes."""
    try:
        relative = path.relative_to(root)
    except ValueError as error:
        raise CompileError("framework-settings-invalid", "Framework Settings Carrier escapes the Project", path=path.as_posix()) from error
    ancestor = root
    for part in relative.parts:
        ancestor /= part
        if ancestor.is_symlink():
            raise CompileError("framework-settings-invalid", "Framework Settings Carrier cannot be a symlink or have a symlink ancestor", path=repo_relative(root, path))
    if not path.exists():
        return False
    if not path.is_file():
        raise CompileError("framework-settings-invalid", "Framework Settings Carrier must be a regular file", path=repo_relative(root, path))
    return True


def framework_settings(root: Path, places: MethodologyPaths) -> tuple[dict[str, object], dict[str, str]]:
    """Read only governed settings Carriers, retaining their byte bindings."""
    merged: dict[str, object] = {}
    bindings: dict[str, str] = {}
    for path in framework_settings_carriers(root, places):
        if not safe_framework_settings_carrier(root, path):
            continue
        raw = path.read_bytes()
        parsed = parse_toml(path, "framework-settings-invalid")
        merged.update(parsed)
        bindings[repo_relative(root, path)] = sha256_bytes(raw)
    return merged, bindings


def extension_selections(settings: Mapping[str, object]) -> dict[str, str]:
    """Return explicit enabled Extension identity/revision selections.

    The source authority only fixes the semantics (enabled plus revision).  The
    small reader accepts the two TOML table forms needed by instance settings;
    it never infers activation from installation or retained configuration.
    """
    selections: dict[str, str] = {}
    raw_sections = [settings.get(name) for name in ("extensions", "installed_extensions", "extension_selections")]
    for section in raw_sections:
        records: list[tuple[str | None, Mapping[str, object]]] = []
        if isinstance(section, Mapping):
            for identity, value in section.items():
                if isinstance(value, Mapping):
                    records.append((str(identity), value))
        elif isinstance(section, list):
            for value in section:
                if isinstance(value, Mapping):
                    identity = value.get("id", value.get("extension_id", value.get("name")))
                    records.append((identity if isinstance(identity, str) else None, value))
        for fallback_identity, record in records:
            enabled = record.get("enabled", record.get("active"))
            identity = record.get("id", record.get("extension_id", fallback_identity))
            revision = record.get("revision", record.get("selected_revision"))
            if enabled is not True:
                continue
            if not isinstance(identity, str) or not identity or not isinstance(revision, (str, int)) or not str(revision):
                raise CompileError("extension-selection-invalid", "Enabled Extension requires an identity and selected revision")
            rendered_revision = str(revision)
            if identity in selections and selections[identity] != rendered_revision:
                raise CompileError("extension-selection-ambiguous", "Extension has more than one active selected revision", extension_id=identity)
            selections[identity] = rendered_revision
    return dict(sorted(selections.items()))


def source_state_snapshot(root: Path, places: MethodologyPaths | None = None) -> dict[str, str]:
    """Capture every governed source/settings byte so new input also invalidates staging."""
    places = places or methodology_paths(root)
    source_root = root / places.source
    if not source_root.is_dir():
        raise CompileError("source-root-missing", "Applicable Methodology source root is missing", path=places.source.as_posix())
    snapshot: dict[str, str] = {}
    for path in sorted(source_root.rglob("*")):
        if path.name == ".DS_Store" and path.is_file() and not path.is_symlink():
            continue
        if path.is_file() and not path.is_symlink():
            snapshot[repo_relative(root, path)] = sha256_bytes(path.read_bytes())
    snapshot.update(declaration_source_pins(root, places))
    project_settings = root / places.control_root / "caprmedio_project_settings.toml"
    if project_settings.is_file() and not project_settings.is_symlink():
        snapshot[repo_relative(root, project_settings)] = sha256_bytes(project_settings.read_bytes())
    for settings_carrier in framework_settings_carriers(root, places):
        if safe_framework_settings_carrier(root, settings_carrier):
            snapshot[repo_relative(root, settings_carrier)] = sha256_bytes(settings_carrier.read_bytes())
    return snapshot


def canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def scalar_value(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value


def split_frontmatter(data: bytes, path: str) -> tuple[str, bytes]:
    if not data.startswith(b"---\n"):
        raise CompileError("source-frontmatter-missing", "Source Carrier requires YAML frontmatter", path=path)
    boundary = data.find(b"\n---\n", 4)
    if boundary < 0:
        raise CompileError("source-frontmatter-unterminated", "Source Carrier frontmatter is unterminated", path=path)
    try:
        frontmatter = data[4:boundary].decode("utf-8")
        data.decode("utf-8")
    except UnicodeDecodeError as error:
        raise CompileError("source-not-utf8", "Source Carrier must be UTF-8", path=path) from error
    return frontmatter, data[boundary + 5 :]


def top_scalar(frontmatter: str, key: str) -> str | None:
    try:
        return header_scalar(frontmatter, key)
    except ValueError as error:
        raise CompileError("source-frontmatter-invalid", "Source Carrier has invalid or conflicting Header properties", key=key) from error


def top_block(frontmatter: str, key: str) -> list[str]:
    lines = frontmatter.splitlines()
    start = next((index for index, line in enumerate(lines) if re.fullmatch(rf"{re.escape(key)}:\s*", line)), None)
    if start is None:
        return []
    block: list[str] = []
    for line in lines[start + 1 :]:
        if line and not line[0].isspace():
            break
        block.append(line)
    return block


def relation_targets(frontmatter: str, kinds: set[str]) -> tuple[str, ...]:
    block = top_block(frontmatter, "relations")
    if not block:
        return ()
    found: set[str] = set()
    current_mapping_kind: str | None = None
    current_list_kind: str | None = None
    collecting_list_targets = False
    for line in block:
        mapping = re.fullmatch(r"  ([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)", line)
        if mapping:
            key, raw = mapping.groups()
            current_mapping_kind = key if key in kinds else None
            current_list_kind = None
            collecting_list_targets = False
            if current_mapping_kind and raw and raw != "[]":
                found.add(scalar_value(raw))
            continue
        list_type = re.fullmatch(r"  -\s*type:\s*(.+?)\s*", line)
        if list_type:
            kind = scalar_value(list_type.group(1))
            current_list_kind = kind if kind in kinds else None
            current_mapping_kind = None
            collecting_list_targets = False
            continue
        list_target_key = re.fullmatch(r"    (?:target|targets):\s*(.*?)\s*", line)
        if list_target_key and current_list_kind:
            raw = list_target_key.group(1)
            collecting_list_targets = not raw
            if raw and raw != "[]":
                found.add(scalar_value(raw))
            continue
        mapping_item = re.fullmatch(r"    -\s*(.+?)\s*", line)
        if mapping_item and current_mapping_kind:
            found.add(scalar_value(mapping_item.group(1)))
            continue
        list_item = re.fullmatch(r"      -\s*(.+?)\s*", line)
        if list_item and current_list_kind and collecting_list_targets:
            found.add(scalar_value(list_item.group(1)))
    return tuple(sorted(value for value in found if value))


def derive_atom_id(path: Path, frontmatter: str) -> str:
    explicit = top_scalar(frontmatter, "atom_id")
    identity = atom_identifier(path.name, explicit)
    if not identity:
        raise CompileError("source-atom-identity-missing", "Cannot derive Source Atom identity", path=path.as_posix())
    return identity


def terminal_term(subject_path: str) -> str:
    parts = re.split(r"\s*[/:]\s*", subject_path.strip())
    if not parts or any(not part for part in parts):
        raise CompileError("source-subject-path-invalid", "Definition Subject Path is invalid", subject_path=subject_path)
    return parts[-1]


def definition_subject(frontmatter: str, path: str) -> tuple[str | None, str | None]:
    if (top_scalar(frontmatter, "cce_form") or "").lower() != "definition":
        return None, None
    block = top_block(frontmatter, "subjects")
    current_kind: str | None = None
    governed: list[str] = []
    for line in block:
        kind = re.fullmatch(r"  ([a-z_]+):\s*(.*?)\s*", line)
        if kind:
            current_kind = kind.group(1)
            raw = kind.group(2)
            if raw and current_kind in {"governs", "declared"}:
                governed.append(scalar_value(raw))
            continue
        item = re.fullmatch(r"(?:    |      )-\s*(.+?)\s*", line)
        if item and current_kind in {"governs", "declared"}:
            governed.append(scalar_value(item.group(1)))
    if len(governed) != 1:
        raise CompileError(
            "definition-term-cardinality",
            "A Definition Atom must identify exactly one Term through GOVERNS",
            path=path,
            governs_count=len(governed),
        )
    return terminal_term(governed[0]), governed[0]


def candidate_sort_key(candidate: Candidate) -> tuple[object, ...]:
    return (candidate.layer_order, candidate.atom_id, candidate.version, candidate.source_path)


def selected_sort_key(candidate: Candidate) -> tuple[object, ...]:
    return (ROLE_ORDER[candidate.role_directory], candidate.atom_id, candidate.source_path)


def proposal_sort_key(candidate: Candidate) -> tuple[object, ...]:
    priority_rank = priority_value(candidate.priority)
    return (-candidate.version, -priority_rank, candidate.layer_order, candidate.source_path)


def priority_value(value: str | None) -> int:
    if value is None:
        return 0
    labels = {"low": 10, "medium": 20, "high": 30, "critical": 40}
    if value.lower() in labels:
        return labels[value.lower()]
    try:
        return int(value)
    except ValueError:
        return 0


def repo_relative(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as error:
        raise CompileError("path-outside-project", "Carrier is outside the Project root", path=path.as_posix()) from error


def discover_candidates(root: Path, places: MethodologyPaths | None = None) -> tuple[list[Candidate], list[dict[str, object]], dict[str, str]]:
    """Read the complete governed frontier without deriving activation from files."""
    places = places or methodology_paths(root)
    source_root = root / places.source
    diagnostics: list[dict[str, object]] = []
    if not source_root.is_dir():
        raise CompileError("source-root-missing", "Applicable Methodology source root is missing", path=places.source.as_posix())
    layers = source_layer_paths(root, places)
    root_role_directories = {directory for _, directory in ROLES}
    observed_layers = sorted(path.name for path in source_root.iterdir() if path.is_dir() and path.name not in root_role_directories)
    expected_layers = sorted(path.name for path in layers.values())
    if observed_layers != expected_layers:
        raise CompileError("source-layer-topology-mismatch", "Structural Source Layers differ from the governed topology", expected=expected_layers, observed=observed_layers)

    settings, _ = framework_settings(root, places)
    selected_extensions = extension_selections(settings)
    candidates: list[Candidate] = []
    snapshot = source_state_snapshot(root, places)

    def exclude(path: Path, reason: str, **details: object) -> None:
        diagnostics.append({"code": "source-excluded", "source_carrier_path": repo_relative(root, path), "reason": reason, **details})

    def collect(layer: str, order: int, role_root: Path, extension_id: str | None = None, extension_revision: str | None = None) -> None:
        if not role_root.exists():
            return
        if not role_root.is_dir() or role_root.is_symlink():
            raise CompileError("source-role-not-directory", "Source role Carrier must be a directory", path=repo_relative(root, role_root))
        for path in sorted(role_root.rglob("*.md")):
            relative_within_role = path.relative_to(role_root)
            relative = repo_relative(root, path)
            if {"archived", "draft", "done", "canceled"}.intersection(
                carrier_status_folder(part) for part in relative_within_role.parts[:-1]
            ):
                exclude(path, "inactive-location")
                continue
            if not path.is_file() or path.is_symlink():
                exclude(path, "not-regular")
                continue
            try:
                data = path.read_bytes()
                frontmatter, _ = split_frontmatter(data, relative)
                if re.search(r"(?m)^projection:\s*(?:$|\{)", frontmatter):
                    raise CompileError("source-projection-metadata-present", "Authoritative Source Carrier cannot contain projection metadata", path=relative)
                status = top_scalar(frontmatter, "status")
                if status not in {"Active", "active"}:
                    exclude(path, "inactive" if status else "status-missing", status=status)
                    continue
                version_raw = top_scalar(frontmatter, "version")
                if version_raw is None or not re.fullmatch(r"[1-9][0-9]*", version_raw):
                    raise CompileError("source-version-invalid", "Selected Source Atom revision requires a positive integer version", path=relative)
                defined_term, definition_subject_path = definition_subject(frontmatter, relative)
                candidates.append(Candidate(
                    layer=layer, layer_order=order, role=ROLE_BY_DIRECTORY[role_root.name], role_directory=role_root.name,
                    atom_id=derive_atom_id(path, frontmatter), version=int(version_raw), source_path=relative,
                    source_sha256=sha256_bytes(data), basename=path.name, priority=top_scalar(frontmatter, "priority"),
                    priority_group=top_scalar(frontmatter, "applicable_methodology_priority_group"),
                    replacements=relation_targets(frontmatter, RELATION_KINDS["replacement"]),
                    incompatibilities=relation_targets(frontmatter, RELATION_KINDS["incompatible"]),
                    definition_term=defined_term, definition_subject_path=definition_subject_path,
                    output_relative=places.output.as_posix(), extension_id=extension_id, extension_revision=extension_revision,
                    original_relations_sha256=relations_digest(frontmatter),
                ))
            except CompileError as error:
                diagnostics.append({**error.record(), "path": relative})

    for layer, order, _ in (LAYERS[0], LAYERS[2]):
        for _, role_directory in ROLES:
            collect(layer, order, root / layers[layer] / role_directory)

    installed = root / layers["INSTALLED_EXTENSIONS"]
    observed_revisions: set[tuple[str, str]] = set()
    for extension_root in sorted(path for path in installed.iterdir() if path.is_dir() and not path.is_symlink()):
        extension_id = extension_root.name
        for revision_root in sorted(path for path in extension_root.iterdir() if path.is_dir() and not path.is_symlink()):
            revision = revision_root.name
            observed_revisions.add((extension_id, revision))
            selected_revision = selected_extensions.get(extension_id)
            for _, role_directory in ROLES:
                role_root = revision_root / role_directory
                if selected_revision != revision:
                    for path in sorted(role_root.rglob("*.md")) if role_root.is_dir() else []:
                        exclude(path, "extension-revision-unselected", extension_id=extension_id, extension_revision=revision)
                    continue
                collect("INSTALLED_EXTENSIONS", 1, role_root, extension_id, revision)
    for extension_id, revision in selected_extensions.items():
        if (extension_id, revision) not in observed_revisions:
            diagnostics.append({"code": "activated-extension-revision-missing", "extension_id": extension_id, "extension_revision": revision})
        elif not any(candidate.extension_id == extension_id and candidate.extension_revision == revision for candidate in candidates):
            diagnostics.append({"code": "activated-extension-has-no-current-carriers", "extension_id": extension_id, "extension_revision": revision})

    candidates.sort(key=candidate_sort_key)
    if not candidates:
        diagnostics.append({"code": "empty-source-frontier", "message": "No eligible current active RMEDO Source Atom revisions were found"})
    return candidates, diagnostics, snapshot


def frontier_digest(candidates: Iterable[Candidate]) -> str:
    records = [candidate.frontier_record() for candidate in sorted(candidates, key=candidate_sort_key)]
    return sha256_bytes(canonical_json(records))


def conflict_record(kind: str, candidates: Iterable[Candidate], proposal: Candidate, **details: object) -> dict[str, object]:
    ordered = sorted(set(candidates), key=candidate_sort_key)
    identity = {
        "type": kind,
        "candidate_source_carrier_paths": [candidate.source_path for candidate in ordered],
        "details": details,
    }
    return {
        "conflict_id": sha256_bytes(canonical_json(identity)),
        "type": kind,
        "candidate_source_carrier_paths": identity["candidate_source_carrier_paths"],
        "details": details,
        "proposed_resolution": {"selected_source_carrier_path": proposal.source_path},
    }


def candidate_aliases(candidate: Candidate) -> set[str]:
    stem = Path(candidate.basename).stem
    return {candidate.atom_id, stem, stem.split("--", 1)[0]}


def detect_conflicts(candidates: list[Candidate]) -> list[dict[str, object]]:
    conflicts: list[dict[str, object]] = []
    by_identity: dict[str, list[Candidate]] = {}
    alias_index: dict[str, list[Candidate]] = {}
    by_output: dict[tuple[str, str], list[Candidate]] = {}
    by_priority_group: dict[str, list[Candidate]] = {}
    by_definition_term: dict[str, list[Candidate]] = {}
    for candidate in candidates:
        by_identity.setdefault(candidate.atom_id, []).append(candidate)
        by_output.setdefault((candidate.role_directory, candidate.basename), []).append(candidate)
        if candidate.priority_group:
            by_priority_group.setdefault(candidate.priority_group, []).append(candidate)
        if candidate.definition_term:
            by_definition_term.setdefault(candidate.definition_term, []).append(candidate)
        for alias in candidate_aliases(candidate):
            alias_index.setdefault(alias, []).append(candidate)

    replacement_pairs: set[tuple[str, str]] = set()
    incompatibility_pairs: set[tuple[str, str]] = set()
    for candidate in candidates:
        for target in candidate.replacements:
            for replaced in alias_index.get(target, []):
                if replaced.source_path != candidate.source_path:
                    replacement_pairs.add((candidate.source_path, replaced.source_path))
        for target in candidate.incompatibilities:
            for incompatible in alias_index.get(target, []):
                if incompatible.source_path != candidate.source_path:
                    incompatibility_pairs.add(tuple(sorted((candidate.source_path, incompatible.source_path))))

    lookup = {candidate.source_path: candidate for candidate in candidates}
    involved_pairs = {frozenset(pair) for pair in replacement_pairs}.union(frozenset(pair) for pair in incompatibility_pairs)
    involved_priority = {candidate.source_path for group in by_priority_group.values() if len(group) > 1 for candidate in group}

    for atom_id, group in sorted(by_identity.items()):
        if len(group) <= 1:
            continue
        group_paths = {candidate.source_path for candidate in group}
        if any(pair.issubset(group_paths) for pair in involved_pairs) or group_paths.intersection(involved_priority):
            continue
        proposal = sorted(group, key=proposal_sort_key)[0]
        conflicts.append(conflict_record("duplicate_selected_atom_identity", group, proposal, atom_id=atom_id))

    for term, group in sorted(by_definition_term.items()):
        if len(group) <= 1:
            continue
        group_paths = {candidate.source_path for candidate in group}
        if any(pair.issubset(group_paths) for pair in involved_pairs) or group_paths.intersection(involved_priority):
            continue
        proposal = sorted(group, key=proposal_sort_key)[0]
        conflicts.append(
            conflict_record(
                "duplicate_governed_term_definition",
                group,
                proposal,
                term=term,
                definition_subject_paths={
                    candidate.source_path: candidate.definition_subject_path
                    for candidate in sorted(group, key=candidate_sort_key)
                },
            )
        )

    for replacer_path, replaced_path in sorted(replacement_pairs):
        replacer = lookup[replacer_path]
        replaced = lookup[replaced_path]
        conflicts.append(
            conflict_record(
                "unresolved_replacement",
                (replacer, replaced),
                replacer,
                replacer_source_carrier_path=replacer_path,
                replaced_source_carrier_path=replaced_path,
            )
        )

    for first_path, second_path in sorted(incompatibility_pairs):
        group = (lookup[first_path], lookup[second_path])
        proposal = sorted(group, key=proposal_sort_key)[0]
        conflicts.append(conflict_record("incompatible_retained_candidates", group, proposal))

    for group_name, group in sorted(by_priority_group.items()):
        if len(group) <= 1:
            continue
        proposal = sorted(group, key=proposal_sort_key)[0]
        conflicts.append(
            conflict_record(
                "unresolved_priority",
                group,
                proposal,
                priority_group=group_name,
                observed_priorities={candidate.source_path: candidate.priority for candidate in sorted(group, key=candidate_sort_key)},
            )
        )

    for (role_directory, basename), group in sorted(by_output.items()):
        if len(group) <= 1:
            continue
        proposal = sorted(group, key=proposal_sort_key)[0]
        conflicts.append(
            conflict_record(
                "output_path_collision",
                group,
                proposal,
                output_path=f"{group[0].output_relative}/{role_directory}/{basename}",
            )
        )

    conflicts.sort(key=lambda item: (str(item["type"]), str(item["conflict_id"])))
    return conflicts


def output_plan(candidates: list[Candidate]) -> list[dict[str, object]]:
    return [candidate.report_record() for candidate in sorted(candidates, key=selected_sort_key)]


def projection_metadata_bytes(source_relative_from_output: str, candidate: Candidate) -> bytes:
    """Render the one canonical projection metadata insertion verbatim."""
    return (
        "\nprojection:\n"
        f"  source_carrier_path: {source_relative_from_output}\n"
        f"  source_atom_id: {candidate.atom_id}\n"
        f"  source_atom_revision: {candidate.version}\n"
        f"  source_sha256: {candidate.source_sha256}\n"
        f"  original_relations_sha256: {candidate.original_relations_sha256}"
    ).encode("utf-8")


def projection_bytes(source: bytes, source_relative_from_output: str, candidate: Candidate) -> bytes:
    path = candidate.source_path
    frontmatter, _ = split_frontmatter(source, path)
    if re.search(r"(?m)^projection:\s*(?:$|\{)", frontmatter):
        raise CompileError("source-projection-metadata-present", "Authoritative Source Carrier cannot contain projection metadata", path=path)
    boundary = source.find(b"\n---\n", 4)
    return source[:boundary] + projection_metadata_bytes(source_relative_from_output, candidate) + source[boundary:]


def validate_projection_source_preservation(
    source: bytes,
    projected: bytes,
    source_relative_from_output: str,
    candidate: Candidate,
) -> None:
    """Require a projection to preserve its source bytes apart from canonical metadata."""
    path = candidate.source_path
    frontmatter, _ = split_frontmatter(source, path)
    if re.search(r"(?m)^projection:\s*(?:$|\{)", frontmatter):
        raise CompileError("source-projection-metadata-present", "Authoritative Source Carrier cannot contain projection metadata", path=path)
    boundary = source.find(b"\n---\n", 4)
    metadata = projection_metadata_bytes(source_relative_from_output, candidate)
    prefix = source[:boundary]
    suffix = source[boundary:]
    if not projected.startswith(prefix + metadata) or projected[len(prefix + metadata):] != suffix:
        raise CompileError(
            "projection-source-preservation-invalid",
            "Projected Carrier must preserve source bytes except for canonical projection metadata",
            path=path,
        )


def stage_outputs(root: Path, candidates: list[Candidate], source_snapshot: dict[str, str], places: MethodologyPaths | None = None) -> Path:
    output_root = root / (places or methodology_paths(root)).output
    temporary_staging = root / ".caprmedio_runtime/compile_applicable_methodology"
    temporary_staging.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix="transaction-", dir=temporary_staging))
    new_root = staging / "new"
    for _, role_directory in ROLES:
        (new_root / role_directory).mkdir(parents=True)
    try:
        for candidate in candidates:
            source_path = root / candidate.source_path
            target_parent = output_root / candidate.role_directory
            relative_source = Path(os.path.relpath(source_path, start=target_parent)).as_posix()
            projected = projection_bytes(source_path.read_bytes(), relative_source, candidate)
            target = new_root / candidate.role_directory / candidate.basename
            target.write_bytes(projected)
        _, current_diagnostics, current_snapshot = discover_candidates(root, places)
        if any(item.get("code") not in {"source-excluded"} for item in current_diagnostics) or current_snapshot != source_snapshot:
            raise CompileError("source-frontier-changed", "Source frontier changed while outputs were staged")
        return staging
    except Exception:
        shutil.rmtree(staging, ignore_errors=True)
        raise


def replace_outputs_atomically(root: Path, staging: Path, places: MethodologyPaths | None = None) -> None:
    output_root = root / (places or methodology_paths(root)).output
    new_root = staging / "new"
    output_root.mkdir(parents=True, exist_ok=True)
    existing: dict[Path, bytes] = {}
    expected: set[Path] = set()
    for _, role_directory in ROLES:
        target_directory = output_root / role_directory
        target_directory.mkdir(parents=True, exist_ok=True)
        existing.update({path: path.read_bytes() for path in target_directory.rglob("*.md") if path.is_file()})
        expected.update(target_directory / path.name for path in (new_root / role_directory).iterdir() if path.is_file())
    installed: list[Path] = []
    try:
        for _, role_directory in ROLES:
            target_directory = output_root / role_directory
            for replacement in sorted((new_root / role_directory).iterdir()):
                target = target_directory / replacement.name
                os.replace(replacement, target)
                installed.append(target)
        for stale in sorted(set(existing).difference(expected)):
            stale.unlink()
    except Exception as error:
        rollback_failed = False
        for target in reversed(installed):
            if target.exists() and target not in existing:
                try:
                    target.unlink()
                except OSError:
                    rollback_failed = True
        for target, data in existing.items():
            temporary = target.with_name(f".{target.name}.rollback.tmp")
            try:
                temporary.write_bytes(data)
                os.replace(temporary, target)
            except OSError:
                rollback_failed = True
                temporary.unlink(missing_ok=True)
        for target in set(expected).difference(existing):
            if target.exists():
                try:
                    target.unlink()
                except OSError:
                    rollback_failed = True
        raise CompileError(
            "atomic-replacement-uncertain" if rollback_failed else "atomic-replacement-failed",
            "Generated RMEDO output replacement has an uncertain recovery state" if rollback_failed else "Generated RMEDO output replacement rolled back",
            error=type(error).__name__,
        ) from error
    finally:
        shutil.rmtree(staging, ignore_errors=True)


def compile_report(root: Path, places: MethodologyPaths | None = None) -> tuple[dict[str, object], list[Candidate], dict[str, str]]:
    places = places or methodology_paths(root)
    candidates, diagnostics, source_snapshot = discover_candidates(root, places)
    digest = frontier_digest(candidates)
    conflicts = detect_conflicts(candidates)
    selected = sorted(candidates, key=selected_sort_key)
    report: dict[str, object] = {
        "structural_source_layers": [name for name, _, _ in LAYERS],
        "contributing_source_layers": ["CORE_META_MODEL", "INSTALLED_EXTENSIONS", "PROJECT_CONFIGURATION"],
        "source_frontier_digest": digest,
        "eligible_candidate_count": len(candidates),
        "conflict_count": len(conflicts),
        "unresolved_conflict_count": len(conflicts),
        "conflicts": conflicts,
        "diagnostics": diagnostics,
        "excluded_candidates": [item for item in diagnostics if item.get("code") == "source-excluded"],
        "selected_candidate_count": len(selected),
        "output_plan": output_plan(selected),
        "can_apply": not any(
            item.get("code") not in {"source-excluded"} for item in diagnostics
        ) and not conflicts,
    }
    return report, selected, source_snapshot
