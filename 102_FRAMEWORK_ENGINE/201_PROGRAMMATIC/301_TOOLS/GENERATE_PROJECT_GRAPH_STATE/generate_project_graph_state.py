#!/usr/bin/env python3
"""Generate a bounded, non-authoritative view of the live CAPRMEDIO control root."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
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
CANONICAL_GENERATOR = SCRIPT
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
    match = ISO_TIMESTAMP.fullmatch(value)
    return f"{match.group(1)} {match.group(2)}" if match else ""


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
    unit_type = match["unit_type"]
    local_order = match["local_order"]
    if (unit_type == "LAYER") != (local_order is not None):
        raise SystemExit(f"invalid Local Order for Scope Unit Directory Carrier: {name}")
    return {
        "name": match["name"],
        "scope_unit_type": unit_type.title(),
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
                "name": parsed["name"],
                "authority_path": carrier.relative_to(root).as_posix(),
                "authority_materialized": True,
                "numeric_prefix": parsed["numeric_prefix"],
                "scope_unit_type": parsed["scope_unit_type"],
                "authority_mode": default_mode,
                "local_order": parsed["local_order"],
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
    return rows


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


def source_updated_at(binding: dict[str, str], contributions: list[dict[str, str]]) -> str:
    candidates = [binding["updated_at"], *(item["updated_at"] for item in contributions)]
    valid = [value for value in candidates if TIMESTAMP.fullmatch(value)]
    if not valid:
        raise SystemExit("no valid source revision timestamp")
    return max(valid)


def project_scope_unit_graph(
    updated_at: str,
    config: dict[str, object],
    config_sha: str,
    binding: dict[str, str],
    scope_unit_rows: list[dict[str, object]],
    contributions: list[dict[str, str]],
) -> str:
    project = config["project"]
    identity = config["artifacts"]["identity"]
    modes = config["authority_modes"]
    assert isinstance(project, dict) and isinstance(identity, dict) and isinstance(modes, dict)
    lines = [
        "# Generated projection. Delete and regenerate; do not edit directly.",
        "[projection]",
        'schema_version = "2"',
        'kind = "project_scope_unit_graph"',
        "non_authoritative = true",
        'currentness = "working_tree_snapshot"',
        f"updated_at = {quote(updated_at)}",
        f"canonical_generator = {quote(project_relative(CANONICAL_GENERATOR))}",
        f"canonical_generator_sha256 = {quote(sha(CANONICAL_GENERATOR))}",
        f"executed_generator = {quote(project_relative(SCRIPT))}",
        f"executed_generator_sha256 = {quote(sha(SCRIPT))}",
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
        for key, value in row.items():
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
) -> str:
    configuration_revision = f"{binding['atom_id']}@{binding['revision']}"
    lines = [
        "# Generated source bindings. Delete and regenerate; do not edit directly.",
        "[projection]",
        'schema_version = "2"',
        'kind = "project_scope_unit_graph_sources"',
        "non_authoritative = true",
        f"updated_at = {quote(updated_at)}",
        f"graph_projection = {quote(project_relative(OUTPUT))}",
    ]
    for output_path in (
        "project.key",
        "project.name",
        "project.repository_slug",
        "artifacts.identity.project_prefix",
        "authority_modes",
    ):
        lines += [
            "",
            "[[bindings]]",
            f"output_path = {quote(output_path)}",
            'source_kind = "project_configuration"',
            f"source_carrier = {quote(project_relative(CONFIG))}",
            f"source_revision = {quote(configuration_revision)}",
            f"source_sha256 = {quote(config_sha)}",
            f"journal_event_id = {quote(binding['journal_event_id'])}",
        ]
    for row in scope_unit_rows:
        lines += [
            "",
            "[[bindings]]",
            f"output_path = {quote('scope_units.' + str(row['node_id']))}",
            'source_kind = "scope_unit_directory_carrier"',
            f"source_carrier = {quote(str(row['authority_path']))}",
            'source_revision = "working_tree_snapshot"',
        ]
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
    rows = scope_units(CONTROL, ROOT, modes)
    updated_at = source_updated_at(binding, contributions)
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
