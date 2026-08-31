#!/usr/bin/env python3
"""Generate a bounded, non-authoritative view of the live CAPRMEDIO control root."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
import tomllib


SCRIPT = Path(__file__).resolve()
ROOT = next(parent for parent in SCRIPT.parents if (parent / ".git").exists())
CONTROL = ROOT / ".caprmedio_caprmedio"
RUNTIME = ROOT / ".caprmedio_runtime"
TOOLS_ROOT = SCRIPT.parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from framework_installation import InstallationError, installation_status  # noqa: E402


OUTPUT = CONTROL / "project_scope_unit_graph.projection.toml"
SOURCE_MAP = CONTROL / "project_scope_unit_graph_sources.projection.toml"
CANONICAL_GENERATOR_CARRIER = Path(
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/GENERATE_PROJECT_GRAPH_STATE/"
    "generate_project_graph_state.py"
)
CANONICAL_GENERATOR = ROOT / CANONICAL_GENERATOR_CARRIER
CONFIG = (
    ROOT
    / ".caprmedio_framework"
    / "00_APPLICABLE_METHODOLOGY"
    / "000_APPLICABLE_MTHD_sources"
    / "003_LOCAL_CONFIGURATION"
    / "caprmedio_framework_settings.toml"
)
JOURNAL = CONTROL / "work_journal"
INACTIVE_FOLDERS = frozenset({"archive", "drafts", "done", "solved", "handled", "canceled"})
CONTRIBUTION_KEYS = ("project_scope_unit_graph", "project_graph_state")
PROJECT_CONFIGURATION_ATOM_ID = "CAPRMEDIO-I-001"
PROJECT_IDENTITY = "caprmedio"
SCOPE_UNIT_NAME = re.compile(
    r"(?P<numeric_prefix>[0-9]+)_(?P<unit_type>LAYER|FEATURE)_(?:(?P<local_order>[1-9][0-9]*)_)?(?P<name>[A-Z][A-Z0-9_]*)\Z"
)
SCOPE_UNIT_CANDIDATE = re.compile(r"[0-9]+_(?:LAYER|FEATURE)_")
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


def configuration_binding(config_sha: str) -> dict[str, str]:
    """Resolve the one completed receipt for the canonical native carrier."""

    matches: list[dict[str, str]] = []
    configuration_path = project_relative(CONFIG)
    for carrier in sorted(JOURNAL.glob("*.ndjson")):
        for number, line in enumerate(carrier.read_text(encoding="utf-8").splitlines(), 1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            result = record.get("result")
            if (
                record.get("kind") != "governed_project_change"
                or record.get("event") != "completed"
                or record.get("subject_kind") != "file"
                or not isinstance(result, dict)
                or result.get("path") != configuration_path
                or result.get("sha256") != config_sha
                or not isinstance(result.get("version"), int)
            ):
                continue
            updated_at = normalise_timestamp(record.get("occurred_at"))
            if not updated_at:
                continue
            matches.append(
                {
                    "revision": str(result["version"]),
                    "journal_carrier": project_relative(carrier),
                    "journal_line": str(number),
                    "journal_event_id": str(record.get("event_id", "unknown")),
                    "updated_at": updated_at,
                }
            )
    if len(matches) == 1:
        return {"atom_id": PROJECT_CONFIGURATION_ATOM_ID, "status": "resolved", **matches[0]}
    return {
        "atom_id": PROJECT_CONFIGURATION_ATOM_ID,
        "status": "unresolved" if not matches else "ambiguous",
        "revision": "unknown",
        "journal_carrier": "",
        "journal_line": "",
        "journal_event_id": "",
        "updated_at": "",
    }


def configuration() -> dict[str, object]:
    try:
        document = tomllib.loads(CONFIG.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as error:
        raise SystemExit(f"invalid Project Configuration: {error}") from error
    project = document.get("project")
    artifacts = document.get("artifacts")
    identity = artifacts.get("identity") if isinstance(artifacts, dict) else None
    modes = document.get("authority_modes")
    if not isinstance(project, dict) or not isinstance(identity, dict) or not isinstance(modes, dict):
        raise SystemExit("Project Configuration lacks project, artifacts.identity, or authority_modes")
    for key in ("key", "name", "repository_slug"):
        if not isinstance(project.get(key), str) or not project[key]:
            raise SystemExit(f"Project Configuration lacks project.{key}")
    if project["key"] != PROJECT_IDENTITY or project["name"] != PROJECT_IDENTITY:
        raise SystemExit("Project Configuration must identify the Project as lowercase caprmedio")
    if not isinstance(identity.get("project_prefix"), str) or not identity["project_prefix"]:
        raise SystemExit("Project Configuration lacks artifacts.identity.project_prefix")
    for key in ("default", "governance", "metamodel", "project", "semantics"):
        if not isinstance(modes.get(key), str) or not modes[key]:
            raise SystemExit(f"Project Configuration lacks authority_modes.{key}")
    return document


def active_path(path: Path, control: Path) -> bool:
    return not INACTIVE_FOLDERS.intersection(path.relative_to(control).parts)


def parse_scope_unit_name(name: str) -> dict[str, object] | None:
    match = SCOPE_UNIT_NAME.fullmatch(name)
    if match is None:
        if SCOPE_UNIT_CANDIDATE.match(name):
            raise SystemExit(f"invalid Scope Unit Directory Carrier name: {name}")
        return None
    unit_type_name = match["unit_type"]
    local_order = match["local_order"]
    if (unit_type_name == "LAYER") != (local_order is not None):
        raise SystemExit(f"invalid Local Order for Scope Unit Directory Carrier: {name}")
    return {
        "unit_name": match["name"],
        "unit_type_name": unit_type_name,
        # A Scope Unit's Type value is determined by Local Order participation,
        # not by the independent Operator-controlled Unit Type Name.
        "type_value": "Layer" if local_order is not None else "Feature",
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


def scope_units(control: Path, root: Path, modes: dict[str, object]) -> list[dict[str, object]]:
    """Discover active typed Scope Units and link each to its nearest typed parent."""

    default_mode = modes.get("default")
    if not isinstance(default_mode, str) or not default_mode:
        raise SystemExit("Project Configuration lacks authority_modes.default")
    rows: list[dict[str, object]] = []
    for carrier in sorted((path for path in control.rglob("*") if path.is_dir()), key=lambda path: path.as_posix()):
        if not active_path(carrier, control):
            continue
        if EPIC_DIRECTORY.fullmatch(carrier.name):
            continue
        parsed = parse_scope_unit_name(carrier.name)
        if parsed is None:
            continue
        relative_to_control = carrier.relative_to(control).as_posix()
        rows.append(
            {
                "node_id": relative_to_control,
                # name, scope_unit_type, and structural_parent remain compact
                # compatibility aliases for existing consumers. The value-bearing
                # fields below are the governed graph representation.
                "unit_name": parsed["unit_name"],
                "name": parsed["unit_name"],
                "project_boundary_position": "PROJECT",
                "type_value": parsed["type_value"],
                "authority_path": carrier.relative_to(root).as_posix(),
                "authority_materialized": True,
                "numeric_prefix": parsed["numeric_prefix"],
                "unit_type_name": parsed["unit_type_name"],
                "scope_unit_type": parsed["type_value"],
                "authority_mode": default_mode,
                "local_order": parsed["local_order"],
                "parent": PROJECT_IDENTITY,
                "structural_parent": PROJECT_IDENTITY,
            }
        )
    if not rows:
        raise SystemExit("no active typed Scope Unit Directory Carriers found")
    by_path = {control / str(row["node_id"]): row for row in rows}
    for row in rows:
        parent = (control / str(row["node_id"])).parent
        parent_row: dict[str, object] | None = None
        while parent != control:
            parent_row = by_path.get(parent)
            if parent_row is not None:
                row["parent"] = parent_row["node_id"]
                row["structural_parent"] = parent_row["node_id"]
                break
            parent = parent.parent
        row["structural_level"] = 1 if parent_row is None else int(parent_row["structural_level"]) + 1
    structural_level_width = len(str(max(int(row["structural_level"]) for row in rows)))
    for row in rows:
        row["navigational_order_number"] = navigational_order_number(
            str(row["numeric_prefix"]),
            int(row["structural_level"]),
            structural_level_width,
        )
    for row in rows:
        children = [child for child in rows if child["parent"] == row["node_id"]]
        child_types = {str(child["type_value"]) for child in children}
        if not child_types:
            row["child_composition"] = "NONE"
        elif child_types == {"Layer"}:
            row["child_composition"] = "LAYERS"
        elif child_types == {"Feature"}:
            row["child_composition"] = "FEATURES"
        else:
            row["child_composition"] = "MIXED"
    return rows


def current_directory_entries(directory: Path) -> list[dict[str, str]]:
    """Return the exact Git-admitted current file frontier of one Directory Carrier."""

    relative = project_relative(directory)
    completed = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "--cached", "--others", "--exclude-standard", "--", relative],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise SystemExit("cannot resolve the Git-admitted Scope Unit Directory Carrier frontier")
    entries: list[dict[str, str]] = []
    for value in completed.stdout.splitlines():
        path = ROOT / value
        if not path.is_file():
            raise SystemExit(f"Scope Unit Directory Carrier contains an unresolved entry: {value}")
        entries.append({"path": value, "sha256": sha(path)})
    return sorted(entries, key=lambda entry: entry["path"])


def directory_receipt(directory: Path) -> dict[str, str]:
    """Resolve the one completed Work Journal receipt for a current Directory Carrier."""

    relative = project_relative(directory)
    current_entries = current_directory_entries(directory)
    if not current_entries:
        raise SystemExit(f"Scope Unit Directory Carrier is empty: {relative}")
    relative_entries = [
        {"path": Path(entry["path"]).relative_to(relative).as_posix(), "sha256": entry["sha256"]}
        for entry in current_entries
    ]
    expected_digest = canonical_json_digest(relative_entries)
    matches: list[dict[str, str]] = []
    for carrier, number, record in journal_records(JOURNAL):
        result = record.get("result")
        if (
            record.get("kind") != "governed_project_change"
            or record.get("event") != "completed"
            or record.get("subject_kind") != "folder"
            or not isinstance(result, dict)
            or result.get("path") != relative
            or result.get("sha256") != expected_digest
            or not isinstance(result.get("version"), int)
            or result.get("entries") != current_entries
        ):
            continue
        updated_at = normalise_timestamp(record.get("occurred_at"))
        event_id = record.get("event_id")
        if not updated_at or not isinstance(event_id, str) or not event_id:
            continue
        matches.append(
            {
                "carrier": relative,
                "revision": str(result["version"]),
                "sha256": expected_digest,
                "journal_carrier": project_relative(carrier),
                "journal_line": str(number),
                "journal_event_id": event_id,
                "updated_at": updated_at,
            }
        )
    if len(matches) != 1:
        state = "unresolved" if not matches else "ambiguous"
        raise SystemExit(f"{state} exact Work Journal receipt for Scope Unit Directory Carrier: {relative}")
    return matches[0]


def atom_frontmatter(path: Path) -> tuple[str, str]:
    """Return frontmatter and body from one governed Markdown Atom carrier."""

    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SystemExit(f"Delivery Atom lacks frontmatter: {project_relative(path)}")
    boundary = text.find("\n---\n", 4)
    if boundary < 0:
        raise SystemExit(f"Delivery Atom has unterminated frontmatter: {project_relative(path)}")
    return text[4:boundary], text[boundary + len("\n---\n") :]


DELIVERY_BINDING = re.compile(
    r"(?m)^[A-Z][A-Z0-9_]* uses authority path `(?P<authority_path>[^`]+)` "
    r"and Delivery path `(?P<delivery_path>[^`]+)`\.$"
)
DELIVERY_ATOM_ID = re.compile(r"(?P<atom_id>CA-D-[0-9]+)-")


def delivery_atom_binding(directory: Path, receipt: dict[str, str]) -> dict[str, str]:
    """Resolve the sole active Delivery Atom which binds one Scope Unit's places."""

    delivery_directory = directory / "07_delivery"
    if not delivery_directory.is_dir():
        raise SystemExit(f"Scope Unit lacks a Delivery directory: {project_relative(directory)}")
    authority_path = project_relative(directory) + "/"
    candidates: list[dict[str, str]] = []
    receipt_entries = {
        entry["path"]: entry["sha256"] for entry in current_directory_entries(directory)
    }
    for path in sorted(delivery_directory.glob("*.md")):
        frontmatter, body = atom_frontmatter(path)
        matches = list(DELIVERY_BINDING.finditer(body))
        if len(matches) != 1 or matches[0]["authority_path"] != authority_path:
            continue
        versions = re.findall(r"(?m)^version:\s*([1-9][0-9]*)\s*$", frontmatter)
        updated_ats = re.findall(r"(?m)^updated_at:\s*([^\n]+)\s*$", frontmatter)
        atom_id_match = DELIVERY_ATOM_ID.match(path.name)
        updated_at = normalise_timestamp(updated_ats[0]) if len(updated_ats) == 1 else ""
        if len(versions) != 1 or not atom_id_match or not updated_at:
            raise SystemExit(f"Delivery Atom lacks an exact revision: {project_relative(path)}")
        digest = sha(path)
        path_relative = project_relative(path)
        if receipt_entries.get(path_relative) != digest:
            raise SystemExit(
                "Scope Unit Directory Carrier receipt does not bind its active Delivery Atom: "
                f"{path_relative}"
            )
        candidates.append(
            {
                "atom_id": atom_id_match["atom_id"],
                "carrier": path_relative,
                "revision": versions[0],
                "sha256": digest,
                "authority_path": authority_path,
                "delivery_path": matches[0]["delivery_path"],
                "journal_carrier": receipt["journal_carrier"],
                "journal_line": receipt["journal_line"],
                "journal_event_id": receipt["journal_event_id"],
                "updated_at": updated_at,
            }
        )
    if len(candidates) != 1:
        state = "missing" if not candidates else "ambiguous"
        raise SystemExit(
            f"{state} active Delivery Atom binding for Scope Unit Directory Carrier: "
            f"{project_relative(directory)}"
        )
    return candidates[0]


def bind_scope_unit_authority(scope_unit_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    """Attach exact current Directory Carrier receipts and Delivery Atom authority."""

    for row in scope_unit_rows:
        directory = ROOT / str(row["authority_path"])
        receipt = directory_receipt(directory)
        delivery = delivery_atom_binding(directory, receipt)
        row["delivery_path"] = delivery["delivery_path"]
        row["directory_receipt"] = receipt
        row["delivery_atom"] = delivery
    return scope_unit_rows


def active_contributions() -> list[dict[str, str]]:
    contributions = []
    for path in sorted(CONTROL.rglob("*.md")):
        if not active_path(path, CONTROL):
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        boundary = text.find("\n---\n", 4)
        if boundary < 0:
            raise SystemExit(f"unterminated Atom frontmatter: {project_relative(path)}")
        frontmatter = text[4:boundary]
        if re.search(r"(?m)^project_settings:\s*$", frontmatter):
            raise SystemExit(f"ordinary Atom supplies retired project_settings: {project_relative(path)}")
        keys = [key for key in CONTRIBUTION_KEYS if re.search(rf"(?m)^{key}:\s*$", frontmatter)]
        if not keys:
            continue
        version = re.findall(r"(?m)^version:\s*([1-9][0-9]*)\s*$", frontmatter)
        updated_at = re.findall(r"(?m)^updated_at:\s*([^\n]+)\s*$", frontmatter)
        if len(version) != 1 or len(updated_at) != 1:
            raise SystemExit(f"contribution lacks one revision: {project_relative(path)}")
        timestamp = normalise_timestamp(updated_at[0])
        if not timestamp:
            raise SystemExit(f"contribution lacks a valid timestamp: {project_relative(path)}")
        for key in keys:
            contributions.append(
                {
                    "key": key,
                    "carrier": project_relative(path),
                    "atom": path.stem,
                    "version": version[0],
                    "updated_at": timestamp,
                    "sha256": sha(path),
                }
            )
    return contributions


def source_updated_at(
    binding: dict[str, str],
    contributions: list[dict[str, str]],
    scope_unit_rows: list[dict[str, object]],
) -> str:
    candidates = [binding["updated_at"], *(item["updated_at"] for item in contributions)]
    for row in scope_unit_rows:
        receipt = row["directory_receipt"]
        delivery = row["delivery_atom"]
        assert isinstance(receipt, dict) and isinstance(delivery, dict)
        candidates.append(str(receipt["updated_at"]))
        candidates.append(str(delivery["updated_at"]))
    valid = [value for value in candidates if TIMESTAMP.fullmatch(value)]
    if not valid:
        raise SystemExit("no valid source revision timestamp")
    return max(valid)


SCOPE_UNIT_GRAPH_FIELDS = (
    "node_id",
    "unit_name",
    "name",
    "project_boundary_position",
    "type_value",
    "child_composition",
    "structural_level",
    "local_order",
    "unit_type_name",
    "navigational_order_number",
    "parent",
    "structural_parent",
    "authority_path",
    "delivery_path",
    "authority_materialized",
    "numeric_prefix",
    "scope_unit_type",
    "authority_mode",
)


def project_scope_unit_graph(
    updated_at: str,
    config: dict[str, object],
    config_sha: str,
    binding: dict[str, str],
    scope_unit_rows: list[dict[str, object]],
    contributions: list[dict[str, str]],
    executed_generator: Path | None = None,
) -> str:
    project = config["project"]
    identity = config["artifacts"]["identity"]
    modes = config["authority_modes"]
    assert isinstance(project, dict) and isinstance(identity, dict) and isinstance(modes, dict)
    generator = generator_metadata(executed_generator)
    lines = [
        "# Generated projection. Delete and regenerate; do not edit directly.",
        "[projection]",
        'schema_version = "3"',
        'kind = "project_scope_unit_graph"',
        "non_authoritative = true",
        'currentness = "exact_source_bound"',
        f"updated_at = {quote(updated_at)}",
        *[f"{key} = {quote(value)}" for key, value in generator.items()],
        "",
        "[configuration]",
        f"atom_id = {quote(binding['atom_id'])}",
        f"revision = {quote(binding['revision'])}",
        f"carrier = {quote(project_relative(CONFIG))}",
        f"sha256 = {quote(config_sha)}",
        f"binding_status = {quote(binding['status'])}",
        f"journal_carrier = {quote(binding['journal_carrier'])}",
        f"journal_line = {quote(binding['journal_line'])}",
        f"journal_event_id = {quote(binding['journal_event_id'])}",
        "",
        "[project]",
        f"key = {quote(project['key'])}",
        f"name = {quote(project['name'])}",
        f"repository_slug = {quote(project['repository_slug'])}",
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
    ]
    for row in scope_unit_rows:
        lines += ["", "[[scope_units]]"]
        for key in SCOPE_UNIT_GRAPH_FIELDS:
            value = row[key]
            if value is None:
                continue
            encoded = str(value).lower() if isinstance(value, bool) else value if isinstance(value, int) else quote(value)
            lines.append(f"{key} = {encoded}")
    for contribution in contributions:
        lines += ["", "[[admitted_contributions]]"] + [f"{key} = {quote(value)}" for key, value in contribution.items()]
    return "\n".join(lines) + "\n"


def project_scope_unit_graph_sources(
    updated_at: str,
    config_sha: str,
    binding: dict[str, str],
    scope_unit_rows: list[dict[str, object]],
    contributions: list[dict[str, str]],
    executed_generator: Path | None = None,
) -> str:
    configuration_revision = f"{binding['atom_id']}@{binding['revision']}"
    generator = generator_metadata(executed_generator)
    lines = [
        "# Generated source bindings. Delete and regenerate; do not edit directly.",
        "[projection]",
        'schema_version = "3"',
        'kind = "project_scope_unit_graph_sources"',
        "non_authoritative = true",
        'currentness = "exact_source_bound"',
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
        journal_binding: dict[str, str],
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
                f"journal_carrier = {quote(journal_binding['journal_carrier'])}",
                f"journal_line = {quote(journal_binding['journal_line'])}",
                f"journal_event_id = {quote(journal_binding['journal_event_id'])}",
            ]
        )

    for output_path in (
        "project.key",
        "project.name",
        "project.repository_slug",
        "artifacts.identity.project_prefix",
        "authority_modes",
    ):
        append_binding(
            output_path,
            "project_configuration",
            project_relative(CONFIG),
            configuration_revision,
            config_sha,
            binding,
        )
    for row in scope_unit_rows:
        node_path = "scope_units." + str(row["node_id"])
        receipt = row["directory_receipt"]
        delivery = row["delivery_atom"]
        assert isinstance(receipt, dict) and isinstance(delivery, dict)
        directory_revision = "Directory Carrier@" + str(receipt["revision"])
        directory_fields = (
            "node_id",
            "unit_name",
            "name",
            "project_boundary_position",
            "type_value",
            "structural_level",
            "local_order",
            "unit_type_name",
            "navigational_order_number",
            "authority_materialized",
            "numeric_prefix",
            "scope_unit_type",
        )
        for field in directory_fields:
            if row[field] is not None:
                append_binding(
                    node_path + "." + field,
                    "scope_unit_directory_carrier",
                    str(receipt["carrier"]),
                    directory_revision,
                    str(receipt["sha256"]),
                    receipt,
                )
        for field in ("authority_path", "delivery_path"):
            append_binding(
                node_path + "." + field,
                "delivery_atom",
                str(delivery["carrier"]),
                str(delivery["atom_id"]) + "@" + str(delivery["revision"]),
                str(delivery["sha256"]),
                delivery,
            )
        append_binding(
            node_path + ".authority_path",
            "scope_unit_directory_carrier",
            str(receipt["carrier"]),
            directory_revision,
            str(receipt["sha256"]),
            receipt,
        )
        parent = str(row["parent"])
        if parent == PROJECT_IDENTITY:
            append_binding(
                node_path + ".parent",
                "project_configuration",
                project_relative(CONFIG),
                configuration_revision,
                config_sha,
                binding,
            )
            append_binding(
                node_path + ".structural_parent",
                "project_configuration",
                project_relative(CONFIG),
                configuration_revision,
                config_sha,
                binding,
            )
        else:
            parent_row = next(candidate for candidate in scope_unit_rows if candidate["node_id"] == parent)
            parent_receipt = parent_row["directory_receipt"]
            assert isinstance(parent_receipt, dict)
            parent_revision = "Directory Carrier@" + str(parent_receipt["revision"])
            for field in ("parent", "structural_parent"):
                append_binding(
                    node_path + "." + field,
                    "scope_unit_directory_carrier",
                    str(parent_receipt["carrier"]),
                    parent_revision,
                    str(parent_receipt["sha256"]),
                    parent_receipt,
                )
        child_rows = [candidate for candidate in scope_unit_rows if candidate["parent"] == row["node_id"]]
        append_binding(
            node_path + ".child_composition",
            "scope_unit_directory_carrier",
            str(receipt["carrier"]),
            directory_revision,
            str(receipt["sha256"]),
            receipt,
        )
        for child in child_rows:
            child_receipt = child["directory_receipt"]
            assert isinstance(child_receipt, dict)
            append_binding(
                node_path + ".child_composition",
                "scope_unit_directory_carrier",
                str(child_receipt["carrier"]),
                "Directory Carrier@" + str(child_receipt["revision"]),
                str(child_receipt["sha256"]),
                child_receipt,
            )
        append_binding(
            node_path + ".authority_mode",
            "project_configuration",
            project_relative(CONFIG),
            configuration_revision,
            config_sha,
            binding,
        )
    for contribution in contributions:
        output_path = "admitted_contributions." + contribution["atom"] + "." + contribution["key"]
        revision = contribution["atom"] + "@" + contribution["version"] + "," + contribution["updated_at"]
        lines += [
            "",
            "[[bindings]]",
            f"output_path = {quote(output_path)}",
            'source_kind = "atom_contribution"',
            f"source_carrier = {quote(contribution['carrier'])}",
            f"source_revision = {quote(revision)}",
            f"source_sha256 = {quote(contribution['sha256'])}",
        ]
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
    temporary_directory = RUNTIME / "state" / "generate_project_graph_state"
    temporary_directory.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=temporary_directory, delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(payload)
    temporary.replace(path)


def main() -> None:
    args = parse_args()
    if args.describe:
        print(json.dumps({"kind": "project_scope_unit_graph", "outputs": [project_relative(OUTPUT), project_relative(SOURCE_MAP)], "writes_only_with_apply": True}, sort_keys=True))
        return
    if not CONTROL.is_dir() or not CONFIG.is_file():
        raise SystemExit("required control root or Project Configuration is missing")
    config = configuration()
    config_sha = sha(CONFIG)
    binding = configuration_binding(config_sha)
    if binding["status"] != "resolved":
        raise SystemExit("Project Configuration current revision binding is unresolved or ambiguous")
    contributions = active_contributions()
    modes = config["authority_modes"]
    assert isinstance(modes, dict)
    rows = bind_scope_unit_authority(scope_units(CONTROL, ROOT, modes))
    updated_at = source_updated_at(binding, contributions, rows)
    graph_payload = project_scope_unit_graph(updated_at, config, config_sha, binding, rows, contributions)
    sources_payload = project_scope_unit_graph_sources(updated_at, config_sha, binding, rows, contributions)
    changed = (not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != graph_payload) or (
        not SOURCE_MAP.is_file() or SOURCE_MAP.read_text(encoding="utf-8") != sources_payload
    )
    print(json.dumps({"apply": args.apply, "changed": changed, "contributions": len(contributions), "outputs": [project_relative(OUTPUT), project_relative(SOURCE_MAP)], "scope_units": len(rows)}, sort_keys=True))
    if not args.apply:
        return
    installed_generator()
    write_output(OUTPUT, graph_payload)
    write_output(SOURCE_MAP, sources_payload)


if __name__ == "__main__":
    main()
