#!/usr/bin/env python3
"""Generate a bounded, non-authoritative view of the live CAPRMEDIO control root."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
import tempfile
import tomllib

SCRIPT = Path(__file__).resolve()
ROOT = next(parent for parent in SCRIPT.parents if (parent / ".git").exists())
CONTROL = ROOT / ".caprmedio"
RUNTIME = ROOT / ".caprmedio_runtime"
INSTALL = ROOT / ".caprmedio_install"
for parent in SCRIPT.parents:
    if parent.name == ".caprmedio_install":
        sys.pycache_prefix = str(RUNTIME / "cache/python")
        break
TOOLS_ROOT = SCRIPT.parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from framework_installation import InstallationError, installation_status  # noqa: E402

OUTPUT = CONTROL / "project_scope_unit_graph.projection.toml"
SOURCE_MAP = CONTROL / "project_scope_unit_graph_sources.projection.toml"
CANONICAL_GENERATOR = (
    ROOT
    / "002_FRAMEWORK_ENGINE"
    / "PROGRAMMATIC"
    / "TOOLS"
    / "GENERATE_PROJECT_GRAPH_STATE"
    / "generate_project_graph_state.py"
)
CONFIG = ROOT / "caprmedio_framework_settings.toml"
JOURNAL = CONTROL / "work_journal"
INACTIVE_FOLDERS = {"archive", "drafts", "done", "solved", "handled"}
CONTRIBUTION_KEYS = ("project_scope_unit_graph", "project_graph_state")

SCOPE_UNITS = (
    ("META_METHODOLOGY", "META_MTHD", "META_METHODOLOGY", "-100_BSEED_SUPERLAYER_META_METHODOLOGY", "", "tbd", ".", "ordered_unit", -2, "-2/1", "", 1, ""),
    ("METAMODEL", "MMODEL", "META_METHODOLOGY/METAMODEL", "-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL", ".caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METAMODEL", "resolved", "", "ordered_unit", -1, "-1/1", "META_METHODOLOGY", 1, ""),
    ("SEMANTICS", "SEMNTC", "META_METHODOLOGY/SEMANTICS", "-100_BSEED_SUPERLAYER_META_METHODOLOGY/-102_BSEED_LAYER_2_SEMANTICS", "", "tbd", ".caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY", "ordered_unit", -1, "-1/2", "META_METHODOLOGY", 2, "METAMODEL"),
    ("GOVERNANCE", "GOVERN", "META_METHODOLOGY/GOVERNANCE", "-100_BSEED_SUPERLAYER_META_METHODOLOGY/-103_BSEED_LAYER_3_GOVERNANCE", "", "tbd", ".caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY", "ordered_unit", -1, "-1/3", "META_METHODOLOGY", 3, "SEMANTICS"),
    ("CAPRMEDIO", "CA", "CAPRMEDIO", ".", ".", "resolved", "", "project_root", 0, "0", "", None, None),
    ("FRAMEWORK_METHODOLOGY", "FR_MTHD", "CAPRMEDIO/FRAMEWORK_METHODOLOGY", "101_LAYER_1_FRAMEWORK_METHODOLOGY", "001_FRAMEWORK_METHODOLOGY", "resolved", "", "ordered_unit", 1, "1/1", "CAPRMEDIO", 1, ""),
    ("FRAMEWORK_ENGINE", "FR_ENGN", "CAPRMEDIO/FRAMEWORK_ENGINE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE", "002_FRAMEWORK_ENGINE", "resolved", "", "ordered_unit", 1, "1/2", "CAPRMEDIO", 2, "FRAMEWORK_METHODOLOGY"),
    ("OPERATOR_DOCUMENTATION", "OPER_DOC", "CAPRMEDIO/OPERATOR_DOCUMENTATION", "103_PROJECT_LAYER_3_OPERATOR_DOCUMENTATION", "003_OPERATOR_DOCUMENTATION", "resolved", "", "ordered_unit", 1, "1/3", "CAPRMEDIO", 3, "FRAMEWORK_ENGINE"),
    ("CORE_EXTENSIONS", "CORE_EXTENSIONS", "CAPRMEDIO/CORE_EXTENSIONS", "104_PROJECT_LAYER_4_CORE_EXTENSIONS", "004_CORE_EXTENSIONS", "resolved", "", "ordered_unit", 1, "1/4", "CAPRMEDIO", 4, "OPERATOR_DOCUMENTATION"),
    ("RELEASES", "RELSS", "CAPRMEDIO/RELEASES", "105_PROJECT_LAYER_5_RELEASES", "005_RELEASES", "resolved", "", "ordered_unit", 1, "1/5", "CAPRMEDIO", 5, "CORE_EXTENSIONS"),
    ("COMMUNITY_EXTENSIONS", "COMMUNITY_EXTENSIONS", "CAPRMEDIO/COMMUNITY_EXTENSIONS", "110_PROJECT_FEATURE_COMMUNITY_EXTENSIONS", "010_COMMUNITY_EXTENSIONS", "resolved", "", "unordered_unit", 1, "1", "CAPRMEDIO", None, None),
    ("FIELD", "FIELD", "CAPRMEDIO/FIELD", "110_PROJECT_FEATURE_FIELD", "010_FIELD", "resolved", "", "unordered_unit", 1, "1", "CAPRMEDIO", None, None),
    ("PROGRAMMATIC", "PROGRAMMATIC", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC", "002_FRAMEWORK_ENGINE/PROGRAMMATIC", "resolved", "", "unordered_unit", 2, "2", "FRAMEWORK_ENGINE", None, None),
    ("AGENTIC", "AGENTIC", "CAPRMEDIO/FRAMEWORK_ENGINE/AGENTIC", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/AGENTIC", "002_FRAMEWORK_ENGINE/AGENTIC", "resolved", "", "unordered_unit", 2, "2", "FRAMEWORK_ENGINE", None, None),
    ("APPS", "APPS", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/APPS", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS", "resolved", "", "unordered_unit", 3, "3", "PROGRAMMATIC", None, None),
    ("MCP", "MCP", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/MCP", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/MCP", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/MCP", "resolved", "", "unordered_unit", 3, "3", "PROGRAMMATIC", None, None),
    ("TOOLS", "TOOLS", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS", "resolved", "", "unordered_unit", 3, "3", "PROGRAMMATIC", None, None),
    ("SKILLS", "SKILLS", "CAPRMEDIO/FRAMEWORK_ENGINE/AGENTIC/SKILLS", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/AGENTIC/SKILLS", "002_FRAMEWORK_ENGINE/AGENTIC/SKILLS", "resolved", "", "unordered_unit", 3, "3", "AGENTIC", None, None),
    ("GRAPH_APP", "GRAPH_APP", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/GRAPH_APP", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/GRAPH_APP", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/GRAPH_APP", "resolved", "", "unordered_unit", 4, "4", "APPS", None, None),
    ("AGENT_HOST_PLUGINS", "AGENT_HOST_PLUGINS", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS", "resolved", "", "unordered_unit", 4, "4", "APPS", None, None),
    ("CODEX_PLUGIN", "CODEX_PLUGIN", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN", "resolved", "", "unordered_unit", 5, "5", "AGENT_HOST_PLUGINS", None, None),
    ("TARGET_SET", "TARGET_SET", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/TARGET_SET", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/TARGET_SET", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/TARGET_SET", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("GRAPH_CHECK", "GRAPH_CHECK", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/GRAPH_CHECK", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/GRAPH_CHECK", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/GRAPH_CHECK", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("BULK_CHANGE", "BULK_CHANGE", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/BULK_CHANGE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/BULK_CHANGE", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/BULK_CHANGE", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("PROJECTION_REBUILD", "PROJECTION_REBUILD", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/PROJECTION_REBUILD", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/PROJECTION_REBUILD", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/PROJECTION_REBUILD", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("IMPLEMENTATION_INVENTORY", "IMPLEMENTATION_INVENTORY", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/IMPLEMENTATION_INVENTORY", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/IMPLEMENTATION_INVENTORY", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/IMPLEMENTATION_INVENTORY", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("ADOPT_RECONCILE", "ADOPT_RECONCILE", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ADOPT_RECONCILE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ADOPT_RECONCILE", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ADOPT_RECONCILE", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("GENERATE_PROJECT_GRAPH_STATE", "GENERATE_PROJECT_GRAPH_STATE", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/GENERATE_PROJECT_GRAPH_STATE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/GENERATE_PROJECT_GRAPH_STATE", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/GENERATE_PROJECT_GRAPH_STATE", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("COMMIT_TRIGGER", "COMMIT_TRIGGER", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_TRIGGER", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_TRIGGER", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_TRIGGER", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("COMMIT_CONTEXT", "COMMIT_CONTEXT", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("APPEND_CHANGE_RECORDS", "APPEND_CHANGE_RECORDS", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/APPEND_CHANGE_RECORDS", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/APPEND_CHANGE_RECORDS", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/APPEND_CHANGE_RECORDS", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("COMMIT_CHANGE_SET", "COMMIT_CHANGE_SET", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("INSTALL_TOOLS", "INSTALL_TOOLS", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/INSTALL_TOOLS", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/INSTALL_TOOLS", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/INSTALL_TOOLS", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("START_BACKGROUND_SERVICES", "START_BACKGROUND_SERVICES", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/START_BACKGROUND_SERVICES", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/START_BACKGROUND_SERVICES", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/START_BACKGROUND_SERVICES", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("ATOM_SEARCH", "ATOM_SEARCH", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_SEARCH", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_SEARCH", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_SEARCH", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("ATOM_READ", "ATOM_READ", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_READ", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_READ", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_READ", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("ATOM_CREATE", "ATOM_CREATE", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_CREATE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_CREATE", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_CREATE", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("ATOM_UPDATE", "ATOM_UPDATE", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_UPDATE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_UPDATE", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_UPDATE", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("ATOM_MOVE", "ATOM_MOVE", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_MOVE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_MOVE", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_MOVE", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("ATOM_ARCHIVE", "ATOM_ARCHIVE", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_ARCHIVE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_ARCHIVE", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_ARCHIVE", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("ATOM_PROMOTE", "ATOM_PROMOTE", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_PROMOTE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_PROMOTE", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_PROMOTE", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("ATOM_UPGRADE", "ATOM_UPGRADE", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_UPGRADE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_UPGRADE", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/ATOM_UPGRADE", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("CLOSE_ATOM", "CLOSE_ATOM", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/CLOSE_ATOM", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/CLOSE_ATOM", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/CLOSE_ATOM", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("MIGRATE_ATOM_IDENTITY", "MIGRATE_ATOM_IDENTITY", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/MIGRATE_ATOM_IDENTITY", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/MIGRATE_ATOM_IDENTITY", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/MIGRATE_ATOM_IDENTITY", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("REBIND_ATOM_RELATIONS", "REBIND_ATOM_RELATIONS", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/REBIND_ATOM_RELATIONS", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/REBIND_ATOM_RELATIONS", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/REBIND_ATOM_RELATIONS", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
    ("REPLACE_ATOM", "REPLACE_ATOM", "CAPRMEDIO/FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/REPLACE_ATOM", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/REPLACE_ATOM", "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/REPLACE_ATOM", "resolved", "", "unordered_unit", 4, "4", "TOOLS", None, None),
)


def sha(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def quote(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def configuration_binding(config_sha: str) -> dict[str, str]:
    matches = []
    for carrier in sorted(JOURNAL.glob("*.ndjson")):
        for number, line in enumerate(carrier.read_text(encoding="utf-8").splitlines(), 1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            details = record.get("details", {})
            if (
                record.get("kind") == "artifact_revision"
                and details.get("sha256") == config_sha
                and "CAPRMEDIO-FRAMEWORK-SETTINGS" in record.get("governed_subjects", [])
            ):
                matches.append(
                    {
                        "revision": str(details.get("version", "unknown")),
                        "journal_carrier": carrier.relative_to(ROOT).as_posix(),
                        "journal_line": str(number),
                        "journal_event_id": str(record.get("event_id", "unknown")),
                        "updated_at": str(details.get("updated_at", "")),
                    }
                )
    if len(matches) == 1:
        return {"atom_id": "CAPRMEDIO-I-001", "status": "resolved", **matches[0]}
    return {
        "atom_id": "CAPRMEDIO-I-001",
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
    if not isinstance(identity.get("project_prefix"), str) or not identity["project_prefix"]:
        raise SystemExit("Project Configuration lacks artifacts.identity.project_prefix")
    for key in ("default", "governance", "metamodel", "project", "semantics"):
        if not isinstance(modes.get(key), str) or not modes[key]:
            raise SystemExit(f"Project Configuration lacks authority_modes.{key}")
    return document


def authority_mode(name: str, modes: dict[str, object]) -> str:
    mode_key = {
        "META_METHODOLOGY": "metamodel",
        "METAMODEL": "metamodel",
        "SEMANTICS": "semantics",
        "GOVERNANCE": "governance",
        "CAPRMEDIO": "project",
    }.get(name, "default")
    value = modes[mode_key]
    assert isinstance(value, str)
    return value


def scope_units(config: dict[str, object]) -> list[dict[str, object]]:
    rows = []
    authority_places: dict[str, Path] = {}
    delivery_places: dict[str, Path] = {}
    modes = config["authority_modes"]
    assert isinstance(modes, dict)
    for name, prefix, scope_path, authority_folder, delivery_path, delivery_status, delivery_boundary, kind, level, coordinate, parent, local_order, upstream in SCOPE_UNITS:
        if not prefix:
            raise SystemExit(f"missing stable prefix for Scope Unit: {name}")
        authority = CONTROL if authority_folder == "." else CONTROL / authority_folder
        delivery = ROOT / delivery_path if delivery_path else None
        scope_segment = scope_path.rsplit("/", 1)[-1]
        authority_parent = parent
        delivery_parent = "FRAMEWORK_METHODOLOGY" if level == -1 else parent
        delivery_parent_place = "authority" if level == -1 else "delivery" if parent else ""
        if authority_parent:
            if authority_parent not in authority_places:
                raise SystemExit(f"unknown authority parent for Scope Unit: {name}")
            projected_authority_path = authority.relative_to(authority_places[authority_parent]).as_posix()
        else:
            projected_authority_path = authority.relative_to(ROOT).as_posix()
        if delivery is not None and delivery_parent:
            if delivery_parent_place == "authority" and delivery_parent == "FRAMEWORK_METHODOLOGY":
                parent_place = CONTROL / "101_LAYER_1_FRAMEWORK_METHODOLOGY"
            else:
                parent_places = authority_places if delivery_parent_place == "authority" else delivery_places
                if delivery_parent not in parent_places:
                    raise SystemExit(f"unknown Delivery parent for Scope Unit: {name}")
                parent_place = parent_places[delivery_parent]
            projected_delivery_path = Path(os.path.relpath(delivery, parent_place)).as_posix()
        elif delivery is not None:
            projected_delivery_path = delivery.relative_to(ROOT).as_posix()
        else:
            projected_delivery_path = ""
        projected_delivery_boundary = "." if delivery_status == "tbd" else delivery_boundary
        if delivery_status == "resolved" and (delivery is None or authority.resolve() == delivery.resolve()):
            raise SystemExit(f"invalid resolved Delivery place for Scope Unit: {name}")
        if delivery_status == "tbd" and (delivery is not None or not delivery_boundary):
            raise SystemExit(f"invalid unresolved Delivery boundary for Scope Unit: {name}")
        row: dict[str, object] = {
            "name": name,
            "prefix": prefix,
            "authority_path": projected_authority_path,
            "authority_materialized": authority.is_dir(),
            "delivery_path": projected_delivery_path,
            "delivery_status": delivery_status,
            "delivery_materialized": delivery.is_dir() if delivery is not None else False,
            "delivery_boundary": projected_delivery_boundary,
            "structural_kind": kind,
            "structural_level": level,
            "structural_coordinate": coordinate,
            "structural_parent": parent,
            "authority_mode": authority_mode(name, modes),
        }
        if kind == "ordered_unit":
            row["local_order"] = local_order
            row["upstream_unit"] = upstream
        rows.append(row)
        authority_places[scope_segment] = authority
        if delivery is not None:
            delivery_places[scope_segment] = delivery
    return rows


def active_contributions() -> list[dict[str, str]]:
    contributions = []
    for path in sorted(CONTROL.rglob("*.md")):
        if INACTIVE_FOLDERS.intersection(path.relative_to(CONTROL).parts):
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        boundary = text.find("\n---\n", 4)
        if boundary < 0:
            raise SystemExit(f"unterminated Atom frontmatter: {path.relative_to(ROOT)}")
        frontmatter = text[4:boundary]
        if re.search(r"(?m)^project_settings:\s*$", frontmatter):
            raise SystemExit(f"ordinary Atom supplies retired project_settings: {path.relative_to(ROOT)}")
        keys = [key for key in CONTRIBUTION_KEYS if re.search(rf"(?m)^{key}:\s*$", frontmatter)]
        if not keys:
            continue
        version = re.findall(r"(?m)^version:\s*([1-9][0-9]*)\s*$", frontmatter)
        updated_at = re.findall(r"(?m)^updated_at:\s*([^\n]+)\s*$", frontmatter)
        if len(version) != 1 or len(updated_at) != 1:
            raise SystemExit(f"contribution lacks one revision: {path.relative_to(ROOT)}")
        for key in keys:
            contributions.append(
                {
                    "key": key,
                    "carrier": path.relative_to(ROOT).as_posix(),
                    "atom": path.stem,
                    "version": version[0],
                    "updated_at": updated_at[0],
                    "sha256": sha(path),
                }
            )
    return contributions


def source_updated_at(binding: dict[str, str], contributions: list[dict[str, str]]) -> str:
    candidates = [binding["updated_at"], *(item["updated_at"] for item in contributions)]
    valid = [value for value in candidates if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}", value)]
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
        'schema_version = "1"',
        'kind = "project_scope_unit_graph"',
        "non_authoritative = true",
        'currentness = "working_tree_snapshot"',
        f"updated_at = {quote(updated_at)}",
        f"canonical_generator = {quote(CANONICAL_GENERATOR.relative_to(ROOT).as_posix())}",
        f"canonical_generator_sha256 = {quote(sha(CANONICAL_GENERATOR))}",
        f"executed_generator = {quote(SCRIPT.relative_to(ROOT).as_posix())}",
        f"executed_generator_sha256 = {quote(sha(SCRIPT))}",
        "",
        "[configuration]",
        f"atom_id = {quote(binding['atom_id'])}",
        f"revision = {quote(binding['revision'])}",
        f"carrier = {quote(CONFIG.relative_to(ROOT).as_posix())}",
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
        f"control_root = {quote(CONTROL.relative_to(ROOT).as_posix())}",
        f"scope_unit_count = {len(scope_unit_rows)}",
    ]
    for row in scope_unit_rows:
        lines += ["", "[[scope_units]]"] + [
            f"{key} = {str(value).lower() if isinstance(value, bool) else value if isinstance(value, int) else quote(value)}"
            for key, value in row.items()
        ]
    for contribution in contributions:
        lines += ["", "[[admitted_contributions]]"] + [
            f"{key} = {quote(value)}" for key, value in contribution.items()
        ]
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
        'schema_version = "1"',
        'kind = "project_scope_unit_graph_sources"',
        "non_authoritative = true",
        f"updated_at = {quote(updated_at)}",
        f"graph_projection = {quote(OUTPUT.relative_to(ROOT).as_posix())}",
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
            f"source_carrier = {quote(CONFIG.relative_to(ROOT).as_posix())}",
            f"source_revision = {quote(configuration_revision)}",
            f"source_sha256 = {quote(config_sha)}",
            f"journal_event_id = {quote(binding['journal_event_id'])}",
    ]
    for row in scope_unit_rows:
        row_name = str(row["name"])
        lines += [
            "",
            "[[bindings]]",
            f"output_path = {quote('scope_units.' + row_name)}",
            'source_kind = "current_graph_structure"',
            f"source_carrier = {quote(str(row['authority_path']))}",
            f"source_revision = {quote('working_tree_snapshot')}",
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
        print(json.dumps({"kind": "project_scope_unit_graph", "outputs": [str(OUTPUT.relative_to(ROOT)), str(SOURCE_MAP.relative_to(ROOT))], "writes_only_with_apply": True}, sort_keys=True))
        return
    if not CONTROL.is_dir() or not CONFIG.is_file():
        raise SystemExit("required control root or configuration is missing")
    config = configuration()
    config_sha = sha(CONFIG)
    binding = configuration_binding(config_sha)
    if binding["status"] != "resolved":
        raise SystemExit("Project Configuration current revision binding is unresolved or ambiguous")
    contributions = active_contributions()
    rows = scope_units(config)
    updated_at = source_updated_at(binding, contributions)
    graph_payload = project_scope_unit_graph(updated_at, config, config_sha, binding, rows, contributions)
    sources_payload = project_scope_unit_graph_sources(updated_at, config_sha, binding, rows, contributions)
    changed = (not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != graph_payload) or (
        not SOURCE_MAP.is_file() or SOURCE_MAP.read_text(encoding="utf-8") != sources_payload
    )
    print(json.dumps({"apply": args.apply, "changed": changed, "contributions": len(contributions), "outputs": [str(OUTPUT.relative_to(ROOT)), str(SOURCE_MAP.relative_to(ROOT))]}, sort_keys=True))
    if not args.apply:
        return
    installed_generator()
    write_output(OUTPUT, graph_payload)
    write_output(SOURCE_MAP, sources_payload)


if __name__ == "__main__":
    main()
