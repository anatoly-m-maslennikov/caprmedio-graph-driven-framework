#!/usr/bin/env python3
"""Generate a bounded, non-authoritative view of the live CAPRMEDIO control root."""

from __future__ import annotations



import argparse
import copy
import hashlib
import json
import os
import re
import sys
from pathlib import Path
import tomllib


SCRIPT = Path(__file__).resolve()
TOOLS_ROOT = SCRIPT.parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from framework_installation import InstallationError, installation_status  # noqa: E402
from artifact_metadata import SETTINGS_PATH, atom_identifier, project_identity  # noqa: E402
from project_runtime import atomic_tempfile, repository_root  # noqa: E402
from project_selection import ProjectSelectionError, active_selection  # noqa: E402
from scope_unit_declarations import read_scope_unit_declarations  # noqa: E402


ROOT = repository_root(SCRIPT)
CONTROL = ROOT / ".caprmedio_caprmedio"


OUTPUT = CONTROL / "_projection" / "project_scope_unit_graph.projection.toml"
SOURCE_MAP = CONTROL / "_projection" / "project_scope_unit_graph_sources.projection.toml"
CANONICAL_GENERATOR_CARRIER = Path(
    "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/GENERATE_PROJECT_GRAPH_STATE/"
    "generate_project_graph_state.py"
)
CANONICAL_GENERATOR = ROOT / CANONICAL_GENERATOR_CARRIER
CONFIG = (
    CONTROL
    / "000_CAPRMEDIO_framework"
    / "caprmedio_framework_settings.toml"
)
# Source scope Units remain under the declared applicable-Methodology source
# tree.  They are independent from the D359 instance Settings carrier.
METHODOLOGY_SOURCE_SCOPE_UNITS = (
    "CORE_META_MODEL",
    "INSTALLED_EXTENSIONS",
    "PROJECT_CONFIGURATION",
)
JOURNAL = CONTROL / "_journal"
INACTIVE_FOLDERS = frozenset({"archive", "drafts", "done", "solved", "handled", "canceled", "cancelled"})
SCOPE_UNIT_NAME = re.compile(
    r"(?P<numeric_prefix>[0-9]+)_(?P<unit_type>LAYER|FEATURE)_(?:(?P<local_order>[1-9][0-9]*)_)?(?P<name>[A-Z][A-Z0-9_]*)\Z"
)
SCOPE_UNIT_CANDIDATE = re.compile(r"CA-SU-[1-9][0-9]*_")
EPIC_DIRECTORY = re.compile(
    r"[0-9]+-CA-Epic-[0-9]+-[A-Z][A-Z0-9_]*-[a-z0-9][a-z0-9-]*\Z"
)
TIMESTAMP = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\Z")
TIMESTAMP_WITH_OFFSET = re.compile(
    r"([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2})(?: [+-][0-9]{4})\Z"
)
ISO_TIMESTAMP = re.compile(r"([0-9]{4}-[0-9]{2}-[0-9]{2})T([0-9]{2}:[0-9]{2}:[0-9]{2})(?:Z|[+-][0-9]{2}:[0-9]{2})\Z")


def sha(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def quote(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def project_relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def normalise_timestamp(value: object) -> str:
    if not isinstance(value, str):
        return ""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '\"'}:
        value = value[1:-1]
    if TIMESTAMP.fullmatch(value):
        return value
    local_match = TIMESTAMP_WITH_OFFSET.fullmatch(value)
    if local_match:
        return local_match.group(1)
    match = ISO_TIMESTAMP.fullmatch(value)
    return f"{match.group(1)} {match.group(2)}" if match else ""


def canonical_json_digest(value: object) -> str:
    """Return the Work Journal canonical digest for one JSON-compatible value."""

    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def generator_metadata(executed_generator: Path | None = None) -> dict[str, str]:
    """Describe canonical source authority separately from this execution carrier."""

    if not CANONICAL_GENERATOR.is_file():
        raise SystemExit("canonical Project Scope Unit Graph Generator source is missing")
    executed_path = SCRIPT if executed_generator is None else executed_generator.resolve()
    try:
        executed = project_relative(executed_path)
    except ValueError as error:
        raise SystemExit("executed Project Scope Unit Graph Generator is outside the repository") from error
    return {
        "canonical_generator": CANONICAL_GENERATOR_CARRIER.as_posix(),
        "canonical_generator_sha256": sha(CANONICAL_GENERATOR),
        "executed_generator": executed,
        "executed_generator_sha256": sha(executed_path),
    }


def canonical_projection_bytes(payload: str) -> bytes:
    """Return the execution-independent canonical bytes of one graph Projection."""

    return "\n".join(
        line
        for line in payload.splitlines()
        if not line.startswith("executed_generator")
    ).encode("utf-8") + b"\n"


def journal_records(journal: Path) -> list[tuple[Path, int, dict[str, object]]]:
    """Return parseable Work Journal records in canonical carrier and line order."""

    records: list[tuple[Path, int, dict[str, object]]] = []
    for carrier in sorted(journal.glob("*.ndjson")):
        with carrier.open(encoding="utf-8") as source:
            for number, line in enumerate(source, 1):
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(record, dict):
                    records.append((carrier, number, record))
    return records


def configuration_binding(config_sha: str, carrier: Path | None = None) -> dict[str, str]:
    """Observe optional log metadata matching the current Settings bytes."""

    matches: list[dict[str, str]] = []
    carrier = CONFIG if carrier is None else carrier
    configuration_path = project_relative(carrier)
    try:
        current_sha = sha(carrier)
    except OSError:
        current_sha = ""
    if current_sha and config_sha == current_sha:
        try:
            history = journal_records(JOURNAL)
        except (OSError, UnicodeDecodeError):
            history = []
        for journal_carrier, number, record in history:
            result = record.get("result")
            if (
                not isinstance(result, dict)
                or result.get("path") != configuration_path
                or result.get("sha256") != config_sha
            ):
                continue
            matches.append(
                {
                    "revision": str(result.get("version", "unknown")),
                    "journal_carrier": project_relative(journal_carrier),
                    "journal_line": str(number),
                    "journal_event_id": str(record.get("event_id", "unknown")),
                    "updated_at": normalise_timestamp(record.get("occurred_at")),
                }
            )
    if len(matches) == 1:
        return {"identifier": carrier.stem, "status": "resolved", **matches[0]}
    return {
        "identifier": carrier.stem,
        "status": "unresolved" if not matches else "ambiguous",
        "revision": "unknown",
        "journal_carrier": "",
        "journal_line": "",
        "journal_event_id": "",
        "updated_at": "",
    }


def settings_bindings() -> dict[str, dict[str, str]]:
    """Bind both authoritative Settings Carriers independently."""
    bindings = {}
    for kind, carrier in (("project_settings", ROOT / SETTINGS_PATH), ("framework_settings", CONFIG)):
        digest = sha(carrier)
        bindings[kind] = {
            **configuration_binding(digest, carrier),
            "carrier": project_relative(carrier),
            "sha256": digest,
        }
    return bindings


def configuration() -> dict[str, object]:
    try:
        identity = project_identity(ROOT)
        if not CONFIG.is_file() or CONFIG.is_symlink():
            raise ValueError("Framework Instance Settings Carrier is missing or invalid")
        framework = tomllib.loads(CONFIG.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError) as error:
        raise SystemExit(str(error)) from error
    artifacts = framework.get("artifacts")
    if "project" in framework or (isinstance(artifacts, dict) and "identity" in artifacts):
        raise SystemExit("Project identity belongs only in Project Settings, not Framework Instance Settings")
    modes = framework.get("authority_modes")
    if not isinstance(modes, dict):
        raise SystemExit("Framework Instance Settings lacks authority_modes")
    for key in ("default", "governance", "metamodel", "project", "semantics"):
        if not isinstance(modes.get(key), str) or not modes[key]:
            raise SystemExit(f"Framework Instance Settings lacks authority_modes.{key}")
    return {
        "project": identity["project"],
        "artifacts": {"identity": identity["identity"]},
        "authority_modes": modes,
    }


def active_path(path: Path, control: Path) -> bool:
    return not INACTIVE_FOLDERS.intersection(path.relative_to(control).parts)


def parse_scope_unit_name(name: str) -> dict[str, object] | None:
    match = SCOPE_UNIT_NAME.fullmatch(name)
    if match is None:
        if SCOPE_UNIT_CANDIDATE.match(name):
            raise SystemExit(f"invalid Scope Unit Directory Carrier name: {name}")
        return None
    scope_unit_label = match["unit_type"]
    local_order = match["local_order"]
    if (scope_unit_label == "LAYER") != (local_order is not None):
        raise SystemExit(f"invalid Local Order for Scope Unit Directory Carrier: {name}")
    return {
        "scope_unit_name": match["name"],
        "scope_unit_label": scope_unit_label,
        # A Scope Unit's Type value is determined by Local Order participation,
        # not by the independent Operator-controlled Label.
        "scope_unit_type": "Ordered" if local_order is not None else "Unordered",
        "numeric_prefix": match["numeric_prefix"],
        "local_order": int(local_order) if local_order is not None else None,
    }


def navigational_order_number(
    numeric_prefix: str, structural_level: int, structural_level_width: int
) -> int:
    """Validate the dynamic prefix allocation and return its Navigational Order Number."""

    if structural_level < 1 or structural_level_width < 1:
        raise SystemExit("invalid derived Scope Unit Structural Level")
    if len(numeric_prefix) <= structural_level_width:
        raise SystemExit(f"numeric prefix lacks Navigational Order Number: {numeric_prefix}")
    level_digits = numeric_prefix[:structural_level_width]
    navigational_order_digits = numeric_prefix[structural_level_width:]
    if int(level_digits) != structural_level:
        raise SystemExit(
            "numeric prefix Structural Level does not match typed Scope Unit ancestry: "
            f"{numeric_prefix}"
        )
    navigational_order = int(navigational_order_digits)
    if navigational_order < 1:
        raise SystemExit(f"numeric prefix has invalid Navigational Order Number: {numeric_prefix}")
    return navigational_order


class _DeclarationRows(list):
    """Keep non-serialized Current Declaration evidence with projected rows."""

    def __init__(self, values, root: Path, control: Path, digest: str, row_digest: str | None = None):
        super().__init__(values)
        self._root = root
        self._control = control
        self._declaration_digest = digest
        self._row_digest = row_digest

    def __deepcopy__(self, memo):
        return _DeclarationRows(copy.deepcopy(list(self), memo), self._root, self._control,
                                self._declaration_digest, self._row_digest)

    def seal(self) -> None:
        self._row_digest = canonical_json_digest(list(self))


def _revalidate_scope_boundary(rows: list[dict[str, object]]) -> None:
    if not isinstance(rows, _DeclarationRows):
        raise SystemExit("Scope rows lack their captured Scope Unit Declaration evidence")
    try:
        if rows._row_digest != canonical_json_digest(list(rows)):
            raise ProjectSelectionError("Scope rows changed after Current Declarations were captured")
        current = read_scope_unit_declarations(rows._root, rows._control)
        if current.digest != rows._declaration_digest:
            raise ProjectSelectionError("Scope Unit Declaration sources changed after Scope rows were captured")
    except (OSError, ValueError, ProjectSelectionError) as error:
        raise SystemExit(str(error)) from error


def scope_units(control: Path, root: Path, modes: dict[str, object]) -> list[dict[str, object]]:
    """Project complete accepted declarations, independently of folder naming."""

    try:
        project_name = project_identity(root)["project"]["name"]
    except ValueError as error:
        raise SystemExit(str(error)) from error
    default_mode = modes.get("default")
    if default_mode not in {"strict", "casual"}:
        raise SystemExit("Project Configuration lacks authority_modes.default")
    try:
        selection = active_selection(root)
        if selection.control_root != control:
            raise ProjectSelectionError("Graph control differs from the selected Project")
        declaration_set = read_scope_unit_declarations(root, control)
        structure = declaration_set.as_structure()
    except (OSError, ValueError, ProjectSelectionError) as error:
        raise SystemExit(str(error)) from error
    declarations = structure.get("scope_units")
    if not isinstance(declarations, list):
        raise SystemExit("Scope Unit Declarations did not derive scope_units")
    nodes: dict[str, str] = {}
    for declaration in declarations:
        if not isinstance(declaration, dict):
            raise SystemExit("Scope Unit Declarations contain an invalid row")
        name, authority = declaration.get("scope_unit_name"), declaration.get("authority_path")
        if not isinstance(name, str) or not isinstance(authority, str):
            raise SystemExit("Scope Unit Declarations lack a name or authority path")
        if name == project_name:
            continue
        path = root / authority
        try:
            node = path.relative_to(control).as_posix()
        except ValueError:
            node = path.relative_to(root).as_posix()
        if node in nodes.values():
            raise SystemExit(f"duplicate projected Scope Unit node ID: {node}")
        nodes[name] = node
    rows: list[dict[str, object]] = _DeclarationRows([], root, control, declaration_set.digest)
    for declaration in sorted(declarations, key=lambda item: str(item.get("scope_unit_name", ""))):
        if not isinstance(declaration, dict):
            raise SystemExit("Scope Unit Declarations contain an invalid row")
        name = str(declaration["scope_unit_name"])
        if name == project_name:
            continue
        authority = str(declaration["authority_path"])
        carrier = root / authority
        parent_name = str(declaration["parent"])
        parent = project_name if parent_name in {"PROJECT", project_name} else nodes[parent_name]
        prefix = re.match(r"([0-9]+)_", carrier.name)
        source = declaration_set.by_name.get(name)
        if source is None:
            raise SystemExit(f"Scope Unit Declaration source is missing: {name}")
        source_path = source.source.relative_to(root).as_posix()
        source_pin = declaration_set.source_pins.get(source_path)
        if source_pin is None:
            raise SystemExit(f"Scope Unit Declaration source pin is missing: {name}")
        rows.append(
            {
                **declaration,
                "node_id": nodes[name],
                "project_boundary_position": "PROJECT",
                "authority_materialized": carrier.is_dir(),
                "numeric_prefix": prefix.group(1) if prefix else None,
                "authority_mode": declaration.get("authority_mode", default_mode),
                "authority_mode_inherited": "authority_mode" not in declaration,
                "local_order": declaration.get("local_order"),
                "parent": parent,
                "structural_parent": parent,
                "declaration_source_path": source_path,
                "declaration_source_pin": dict(source_pin),
                "declaration_digest": declaration_set.digest,
            }
        )
    for row in rows:
        children = [child for child in rows if child["parent"] == row["node_id"]]
        child_types = {str(child["scope_unit_type"]) for child in children}
        if not child_types:
            row["child_composition"] = "NONE"
        elif child_types == {"Ordered"}:
            row["child_composition"] = "ORDERED"
        elif child_types == {"Unordered"}:
            row["child_composition"] = "UNORDERED"
        else:
            row["child_composition"] = "MIXED"
    rows.seal()
    _revalidate_scope_boundary(rows)
    return rows


def directory_observations(
    control: Path, root: Path, scope_unit_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    """Report physical carriers without accepting their naming or topology as declarations."""
    declared = {root / str(row["authority_path"]).removesuffix("/"): row for row in scope_unit_rows}
    paths = set(declared)
    paths.update(path for path in control.rglob("*")
                 if path.is_dir() and not path.is_symlink() and active_path(path, control)
                 and SCOPE_UNIT_CANDIDATE.match(path.name))
    nodes = {path: str(row["node_id"]) for path, row in declared.items()}
    for path in paths - declared.keys():
        nodes[path] = path.relative_to(control).as_posix()
    materialized = {path for path in paths if path.is_dir()}
    levels = {path: 1 + sum(parent in materialized for parent in path.parents) for path in materialized}
    width = len(str(max(levels.values(), default=1)))
    project_name = project_identity(root)["project"]["name"]
    observations = []
    for path in sorted(paths):
        row = declared.get(path)
        observation: dict[str, object] = {
            "kind": "declared" if row is not None else "undeclared",
            "node_id": nodes[path], "authority_path": path.relative_to(root).as_posix(),
            "authority_materialized": path in materialized, "mismatches": [],
        }
        if path in materialized:
            parent = next((ancestor for ancestor in path.parents if ancestor in materialized), None)
            observation.update({"observed_parent": nodes[parent] if parent is not None else project_name,
                                "observed_structural_level": levels[path]})
            parsed = SCOPE_UNIT_NAME.fullmatch(path.name)
            if parsed is not None:
                local_order = parsed["local_order"]
                observation.update({
                    "observed_scope_unit_name": parsed["name"],
                    "observed_scope_unit_type": "Ordered" if local_order is not None else "Unordered",
                    "observed_scope_unit_label": parsed["unit_type"],
                    "observed_numeric_prefix": parsed["numeric_prefix"],
                    "observed_local_order": int(local_order) if local_order is not None else None,
                })
                prefix = parsed["numeric_prefix"]
                if len(prefix) > width:
                    observation["observed_prefix_structural_level"] = int(prefix[:width])
                    observation["observed_navigational_order_number"] = int(prefix[width:])
            if row is not None:
                observation["mismatches"] = [field for field in (
                    "scope_unit_name", "scope_unit_type", "scope_unit_label", "parent", "local_order",
                ) if "observed_" + field in observation and observation["observed_" + field] != row[field]]
        observations.append(observation)
    return observations


def bind_scope_unit_structure(scope_unit_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    """Recheck Current Declarations before exposing their already-derived paths."""
    _revalidate_scope_boundary(scope_unit_rows)
    return scope_unit_rows


def active_source_atoms() -> list[dict[str, str]]:
    """Return the deterministic active Atom frontier of every configured source Scope Unit."""

    try:
        declarations = read_scope_unit_declarations(ROOT, CONTROL)
    except (OSError, ValueError) as error:
        raise SystemExit(str(error)) from error
    structure = {
        row["scope_unit_name"]: row
        for row in declarations.as_structure()["scope_units"]
        if isinstance(row, dict) and isinstance(row.get("scope_unit_name"), str)
    }
    atoms: list[dict[str, str]] = []
    atom_ids: set[str] = set()
    for source_scope_unit in METHODOLOGY_SOURCE_SCOPE_UNITS:
        declaration = declarations.by_name.get(source_scope_unit)
        if declaration is None:
            raise SystemExit(f"configured Methodology Source Scope Unit is undeclared: {source_scope_unit}")
        row = structure.get(source_scope_unit)
        if not isinstance(row, dict):
            raise SystemExit(f"configured Methodology Source Scope Unit is invalid: {source_scope_unit}")
        directory = ROOT / str(row["authority_path"])
        if not directory.is_dir():
            raise SystemExit(f"configured Methodology Source Scope Unit is missing: {project_relative(directory)}")
        for path in sorted(directory.rglob("*.md")):
            relative = path.relative_to(directory)
            if INACTIVE_FOLDERS.intersection(relative.parts):
                continue
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---\n"):
                continue
            boundary = text.find("\n---\n", 4)
            if boundary < 0:
                raise SystemExit(f"unterminated source Atom frontmatter: {project_relative(path)}")
            frontmatter = text[4:boundary]
            declared_atom_id = re.findall(r"(?m)^atom_id:\s*([^\n]+)\s*$", frontmatter)
            version = re.findall(r"(?m)^version:\s*([1-9][0-9]*)\s*$", frontmatter)
            updated_at = re.findall(r"(?m)^updated_at:\s*([^\n]+)\s*$", frontmatter)
            filename_atom_id = path.stem.partition("--")[0]
            if len(declared_atom_id) > 1 or not filename_atom_id or len(version) != 1 or len(updated_at) != 1:
                raise SystemExit(f"source Atom lacks one identity and revision: {project_relative(path)}")
            atom_id = atom_identifier(path.name, declared_atom_id[0] if declared_atom_id else None)
            if atom_id in atom_ids:
                raise SystemExit(f"duplicate active source Atom identity: {atom_id}")
            timestamp = normalise_timestamp(updated_at[0])
            if not timestamp:
                raise SystemExit(f"source Atom lacks a valid timestamp: {project_relative(path)}")
            atom_ids.add(atom_id)
            atoms.append(
                {
                    "source_scope_unit": source_scope_unit,
                    "carrier": project_relative(path),
                    "atom_id": atom_id,
                    "atom_id_source": "frontmatter" if declared_atom_id else "filename",
                    "version": version[0],
                    "updated_at": timestamp,
                    "sha256": sha(path),
                }
            )
    if not atoms:
        raise SystemExit("configured Methodology Source Scope Units contain no active Atoms")
    return atoms


def source_updated_at(
    bindings: dict[str, dict[str, str]],
    source_atoms: list[dict[str, str]],
) -> str:
    candidates = [*(item["updated_at"] for item in bindings.values()), *(item["updated_at"] for item in source_atoms)]
    valid = [value for value in candidates if TIMESTAMP.fullmatch(value)]
    if not valid:
        raise SystemExit("no valid source revision timestamp")
    return max(valid)


SCOPE_UNIT_GRAPH_FIELDS = (
    "node_id",
    "scope_unit_name",
    "scope_unit_id",
    "project_boundary_position",
    "scope_unit_type",
    "scope_unit_label",
    "child_composition",
    "local_order",
    "parent",
    "structural_parent",
    "authority_path",
    "delivery_path",
    "authority_materialized",
    "numeric_prefix",
    "authority_mode",
)


def settings_binding_lines(bindings: dict[str, dict[str, str]]) -> list[str]:
    lines = []
    for kind, binding in bindings.items():
        lines += [f"[settings.{kind}]"]
        lines += [f"{key} = {quote(value)}" for key, value in binding.items()]
        lines.append("")
    return lines


def project_scope_unit_graph(
    updated_at: str,
    config: dict[str, object],
    bindings: dict[str, dict[str, str]],
    scope_unit_rows: list[dict[str, object]],
    source_atoms: list[dict[str, str]],
    executed_generator: Path | None = None,
    *, observations: list[dict[str, object]] | None = None,
) -> str:
    _revalidate_scope_boundary(scope_unit_rows)
    project = config["project"]
    identity = config["artifacts"]["identity"]
    modes = config["authority_modes"]
    assert isinstance(project, dict) and isinstance(identity, dict) and isinstance(modes, dict)
    generator = generator_metadata(executed_generator)
    lines = [
        "# Generated projection. Delete and regenerate; do not edit directly.",
        "[projection]",
        'schema_version = "4"',
        'kind = "project_scope_unit_graph"',
        "non_authoritative = true",
        f"currentness = {quote('exact_source_bound' if all(item['status'] == 'resolved' for item in bindings.values()) else 'unknown')}",
        f"updated_at = {quote(updated_at)}",
        *[f"{key} = {quote(value)}" for key, value in generator.items()],
        "",
        *settings_binding_lines(bindings),
        "[project]",
        f"key = {quote(project['key'])}",
        f"name = {quote(project['name'])}",
        f"repository_slug = {quote(project['repository_slug'])}",
        f"obsolete_names = {quote(project['obsolete_names'])}",
        "",
        "[artifacts.identity]",
        f"project_prefix = {quote(identity['project_prefix'])}",
        "",
        "[authority_modes]",
        *[f"{key} = {quote(modes[key])}" for key in sorted(modes)],
        "",
        "[repository]",
        f"control_root = {quote(project_relative(CONTROL))}",
        f"scope_unit_count = {len(scope_unit_rows)}",
        "",
        "[methodology_source_frontier]",
        f"source_scope_unit_count = {len(METHODOLOGY_SOURCE_SCOPE_UNITS)}",
        f"atom_count = {len(source_atoms)}",
        f"digest = {quote(canonical_json_digest(source_atoms))}",
    ]
    for row in scope_unit_rows:
        lines += ["", "[[scope_units]]"]
        for key in SCOPE_UNIT_GRAPH_FIELDS:
            value = row[key]
            if value is None:
                continue
            encoded = str(value).lower() if isinstance(value, bool) else value if isinstance(value, int) else quote(value)
            lines.append(f"{key} = {encoded}")
    for source_atom in source_atoms:
        lines += ["", "[[methodology_source_atoms]]"] + [
            f"{key} = {quote(value)}" for key, value in source_atom.items()
        ]
    for observation in observations or []:
        lines += ["", "[[directory_observations]]"]
        for key, value in observation.items():
            if value is None:
                continue
            encoded = str(value).lower() if isinstance(value, bool) else value if isinstance(value, int) else quote(value)
            lines.append(f"{key} = {encoded}")
    return "\n".join(lines) + "\n"


def project_scope_unit_graph_sources(
    updated_at: str,
    bindings: dict[str, dict[str, str]],
    scope_unit_rows: list[dict[str, object]],
    source_atoms: list[dict[str, str]],
    executed_generator: Path | None = None,
    *, observations: list[dict[str, object]] | None = None,
) -> str:
    _revalidate_scope_boundary(scope_unit_rows)
    generator = generator_metadata(executed_generator)
    lines = [
        "# Generated source bindings. Delete and regenerate; do not edit directly.",
        "[projection]",
        'schema_version = "4"',
        'kind = "project_scope_unit_graph_sources"',
        "non_authoritative = true",
        f"currentness = {quote('exact_source_bound' if all(item['status'] == 'resolved' for item in bindings.values()) else 'unknown')}",
        f"updated_at = {quote(updated_at)}",
        f"graph_projection = {quote(project_relative(OUTPUT))}",
        *[f"{key} = {quote(value)}" for key, value in generator.items()],
    ]

    def append_binding(
        output_path: str,
        source_kind: str,
        source_carrier: str,
        source_revision: str,
        source_sha256: str,
        journal_binding: dict[str, str] | None = None,
    ) -> None:
        lines.extend(
            [
                "",
                "[[bindings]]",
                f"output_path = {quote(output_path)}",
                f"source_kind = {quote(source_kind)}",
                f"source_carrier = {quote(source_carrier)}",
                f"source_revision = {quote(source_revision)}",
                f"source_sha256 = {quote(source_sha256)}",
            ]
        )
        if journal_binding is not None:
            lines.extend(
                [
                    f"journal_carrier = {quote(journal_binding['journal_carrier'])}",
                    f"journal_line = {quote(journal_binding['journal_line'])}",
                    f"journal_event_id = {quote(journal_binding['journal_event_id'])}",
                ]
            )

    for output_path in (
        "project.key", "project.name", "project.repository_slug", "project.obsolete_names",
        "artifacts.identity.project_prefix", "authority_modes",
    ):
        kind = "framework_settings" if output_path == "authority_modes" else "project_settings"
        binding = bindings[kind]
        append_binding(
            output_path, kind, binding["carrier"],
            f"{binding['identifier']}@{binding['revision']}", binding["sha256"], binding,
        )
    for row in scope_unit_rows:
        node_path = "scope_units." + str(row["node_id"])
        for field in SCOPE_UNIT_GRAPH_FIELDS:
            if row[field] is None:
                continue
            if field in {"authority_materialized", "numeric_prefix"}:
                observed = {key: row[key] for key in ("authority_path", "authority_materialized", "numeric_prefix")}
                append_binding(
                    node_path + "." + field, "directory_observation", str(row["authority_path"]),
                    "observed_directory", canonical_json_digest(observed),
                )
                continue
            if field == "authority_mode" and row.get("authority_mode_inherited", True):
                binding = bindings["framework_settings"]
                append_binding(
                    node_path + "." + field, "framework_settings", binding["carrier"],
                    f"{binding['identifier']}@{binding['revision']}", binding["sha256"], binding,
                )
                continue
            source_pin = row.get("declaration_source_pin")
            source_path = row.get("declaration_source_path")
            if not isinstance(source_pin, dict) or not isinstance(source_path, str):
                raise SystemExit("Scope Unit Declaration source pin is unavailable")
            atom_id, version, digest = source_pin.get("atom_id"), source_pin.get("version"), source_pin.get("sha256")
            if not isinstance(atom_id, str) or type(version) is not int or not isinstance(digest, str):
                raise SystemExit("Scope Unit Declaration source pin is invalid")
            append_binding(
                node_path + "." + field, "scope_unit_declaration",
                source_path, atom_id + "@" + str(version), digest,
            )
    for observation in observations or []:
        for field, value in observation.items():
            if value is not None:
                append_binding(
                    "directory_observations." + str(observation["authority_path"]) + "." + field,
                    "directory_observation", str(observation["authority_path"]), "observed_directory",
                    canonical_json_digest(observation),
                )
    for source_atom in source_atoms:
        revision = source_atom["atom_id"] + "@" + source_atom["version"] + "," + source_atom["updated_at"]
        append_binding(
            "methodology_source_atoms." + source_atom["atom_id"],
            "methodology_source_atom",
            source_atom["carrier"],
            revision,
            source_atom["sha256"],
        )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write both generated Projections")
    parser.add_argument("--describe", action="store_true", help="describe the Tool without reading sources")
    return parser.parse_args()


def installed_generator() -> None:
    try:
        installed = installation_status(ROOT)
    except InstallationError as error:
        raise SystemExit(f"{error.code}: {error.message}") from error
    expected = ROOT / str(installed["package_root"]) / "GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py"
    if SCRIPT != expected.resolve():
        raise SystemExit("run the selected installed GENERATE_PROJECT_GRAPH_STATE Tool")


def write_output(path: Path, payload: str) -> None:
    descriptor, temporary_name = atomic_tempfile(path, "generate_project_graph_state")
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        temporary.replace(path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def main() -> None:
    args = parse_args()
    if args.describe:
        print(json.dumps({"kind": "project_scope_unit_graph", "outputs": [project_relative(OUTPUT), project_relative(SOURCE_MAP)], "writes_only_with_apply": True}, sort_keys=True))
        return
    if not CONTROL.is_dir() or not CONFIG.is_file():
        raise SystemExit("required control root or Project Configuration is missing")
    config = configuration()
    bindings = settings_bindings()
    source_atoms = active_source_atoms()
    modes = config["authority_modes"]
    assert isinstance(modes, dict)
    rows = scope_units(CONTROL, ROOT, modes)
    observations = directory_observations(CONTROL, ROOT, rows)
    updated_at = source_updated_at(bindings, source_atoms)
    graph_payload = project_scope_unit_graph(updated_at, config, bindings, rows, source_atoms, observations=observations)
    sources_payload = project_scope_unit_graph_sources(updated_at, bindings, rows, source_atoms, observations=observations)
    changed = (not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != graph_payload) or (
        not SOURCE_MAP.is_file() or SOURCE_MAP.read_text(encoding="utf-8") != sources_payload
    )
    _revalidate_scope_boundary(rows)
    print(json.dumps({"apply": args.apply, "changed": changed, "methodology_source_atoms": len(source_atoms), "outputs": [project_relative(OUTPUT), project_relative(SOURCE_MAP)], "scope_units": len(rows)}, sort_keys=True))
    if not args.apply:
        return
    installed_generator()
    _revalidate_scope_boundary(rows)
    write_output(OUTPUT, graph_payload)
    _revalidate_scope_boundary(rows)
    write_output(SOURCE_MAP, sources_payload)


def _image_main():
    return main()


if __name__ == "__main__":
    # Direct script execution needs the shared process boundary available from the tools root.
    import sys
    from pathlib import Path
    _TOOLS_ROOT = next(p for p in Path(__file__).resolve().parents if p.name in {"FEATURE_TOOLS", "TOOLS"})
    if str(_TOOLS_ROOT) not in sys.path:
        sys.path.insert(0, str(_TOOLS_ROOT))
    from runtime_process_boundary import run_process
    raise SystemExit(run_process(_image_main, operation="GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state"))
