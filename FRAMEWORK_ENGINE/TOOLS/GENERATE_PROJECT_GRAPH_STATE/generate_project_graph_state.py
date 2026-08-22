#!/usr/bin/env python3
"""Generate a bounded, non-authoritative view of the live CAPRMEDIO control root."""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path

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

OUTPUT = CONTROL / "project_graph_state.toml"
CANONICAL_GENERATOR = (
    ROOT
    / "FRAMEWORK_ENGINE"
    / "TOOLS"
    / "GENERATE_PROJECT_GRAPH_STATE"
    / "generate_project_graph_state.py"
)
CONFIG = ROOT / "caprmedio_framework_settings.toml"
JOURNAL = CONTROL / "work_journal"

SCOPE_UNITS = (
    ("METAMODEL", "META", "METAMODEL", "METAMODEL", ".caprmedio/FRAMEWORK_METHODOLOGY/METAMODEL", "resolved", "", "ordered_unit", -1, "-1/1", "", 1, ""),
    ("SEMANTICS", "SMNTC", "SEMANTICS", "SEMANTICS", "", "tbd", ".caprmedio/FRAMEWORK_METHODOLOGY", "ordered_unit", -1, "-1/2", "", 2, "METAMODEL"),
    ("GOVERNANCE", "GOV", "GOVERNANCE", "GOVERNANCE", "", "tbd", ".caprmedio/FRAMEWORK_METHODOLOGY", "ordered_unit", -1, "-1/3", "", 3, "SEMANTICS"),
    ("CAPRMEDIO", "CA", "CAPRMEDIO", ".", ".", "resolved", "", "project_root", 0, "0", "", None, None),
    ("FRAMEWORK_METHODOLOGY", "FR_MTHD", "CAPRMEDIO/FRAMEWORK_METHODOLOGY", "FRAMEWORK_METHODOLOGY", "FRAMEWORK_METHODOLOGY", "resolved", "", "ordered_unit", 1, "1/1", "CAPRMEDIO", 1, ""),
    ("FRAMEWORK_ENGINE", "FR_ENGN", "CAPRMEDIO/FRAMEWORK_ENGINE", "FRAMEWORK_ENGINE", "FRAMEWORK_ENGINE", "resolved", "", "ordered_unit", 1, "1/2", "CAPRMEDIO", 2, "FRAMEWORK_METHODOLOGY"),
    ("OPERATOR_DOCUMENTATION", "OPER_DOC", "CAPRMEDIO/OPERATOR_DOCUMENTATION", "OPERATOR_DOCUMENTATION", "OPERATOR_DOCUMENTATION", "resolved", "", "ordered_unit", 1, "1/3", "CAPRMEDIO", 3, "FRAMEWORK_ENGINE"),
    ("EXTENSIONS", "EXTNS", "CAPRMEDIO/EXTENSIONS", "EXTENSIONS", "EXTENSIONS", "resolved", "", "unordered_unit", 1, "1", "CAPRMEDIO", None, None),
    ("RELEASES", "RELSS", "CAPRMEDIO/RELEASES", "RELEASES", "RELEASES", "resolved", "", "unordered_unit", 1, "1", "CAPRMEDIO", None, None),
    ("FIELD", "FIELD", "CAPRMEDIO/FIELD", "FIELD", "FIELD", "resolved", "", "unordered_unit", 1, "1", "CAPRMEDIO", None, None),
    ("APPS", "APPS", "CAPRMEDIO/FRAMEWORK_ENGINE/APPS", "FRAMEWORK_ENGINE/APPS", "FRAMEWORK_ENGINE/APPS", "resolved", "", "unordered_unit", 2, "2", "FRAMEWORK_ENGINE", None, None),
    ("SKILLS", "SKILLS", "CAPRMEDIO/FRAMEWORK_ENGINE/SKILLS", "FRAMEWORK_ENGINE/SKILLS", "FRAMEWORK_ENGINE/SKILLS", "resolved", "", "unordered_unit", 2, "2", "FRAMEWORK_ENGINE", None, None),
    ("TOOLS", "TOOLS", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS", "FRAMEWORK_ENGINE/TOOLS", "FRAMEWORK_ENGINE/TOOLS", "resolved", "", "unordered_unit", 2, "2", "FRAMEWORK_ENGINE", None, None),
    ("GRAPH_APP", "GRAPH_APP", "CAPRMEDIO/FRAMEWORK_ENGINE/APPS/GRAPH_APP", "FRAMEWORK_ENGINE/APPS/GRAPH_APP", "FRAMEWORK_ENGINE/APPS/GRAPH_APP", "resolved", "", "unordered_unit", 3, "3", "APPS", None, None),
    ("MCP", "MCP", "CAPRMEDIO/FRAMEWORK_ENGINE/APPS/MCP", "FRAMEWORK_ENGINE/APPS/MCP", "", "tbd", "FRAMEWORK_ENGINE/APPS", "unordered_unit", 3, "3", "APPS", None, None),
    ("AGENT_HOST_PLUGINS", "AGENT_HOST_PLUGINS", "CAPRMEDIO/FRAMEWORK_ENGINE/APPS/AGENT_HOST_PLUGINS", "FRAMEWORK_ENGINE/APPS/AGENT_HOST_PLUGINS", "FRAMEWORK_ENGINE/APPS/AGENT_HOST_PLUGINS", "resolved", "", "unordered_unit", 3, "3", "APPS", None, None),
    ("CODEX_PLUGIN", "CODEX_PLUGIN", "CAPRMEDIO/FRAMEWORK_ENGINE/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN", "FRAMEWORK_ENGINE/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN", "FRAMEWORK_ENGINE/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN", "resolved", "", "unordered_unit", 4, "4", "AGENT_HOST_PLUGINS", None, None),
    ("TARGET_SET", "TARGET_SET", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/TARGET_SET", "FRAMEWORK_ENGINE/TOOLS/TARGET_SET", "FRAMEWORK_ENGINE/TOOLS/TARGET_SET", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("GRAPH_CHECK", "GRAPH_CHECK", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/GRAPH_CHECK", "FRAMEWORK_ENGINE/TOOLS/GRAPH_CHECK", "FRAMEWORK_ENGINE/TOOLS/GRAPH_CHECK", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("BULK_CHANGE", "BULK_CHANGE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/BULK_CHANGE", "FRAMEWORK_ENGINE/TOOLS/BULK_CHANGE", "FRAMEWORK_ENGINE/TOOLS/BULK_CHANGE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("PROJECTION_REBUILD", "PROJECTION_REBUILD", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/PROJECTION_REBUILD", "FRAMEWORK_ENGINE/TOOLS/PROJECTION_REBUILD", "FRAMEWORK_ENGINE/TOOLS/PROJECTION_REBUILD", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("IMPLEMENTATION_INVENTORY", "IMPLEMENTATION_INVENTORY", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/IMPLEMENTATION_INVENTORY", "FRAMEWORK_ENGINE/TOOLS/IMPLEMENTATION_INVENTORY", "FRAMEWORK_ENGINE/TOOLS/IMPLEMENTATION_INVENTORY", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ADOPT_RECONCILE", "ADOPT_RECONCILE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ADOPT_RECONCILE", "FRAMEWORK_ENGINE/TOOLS/ADOPT_RECONCILE", "FRAMEWORK_ENGINE/TOOLS/ADOPT_RECONCILE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("COMMIT_TRIGGER", "COMMIT_TRIGGER", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/COMMIT_TRIGGER", "FRAMEWORK_ENGINE/TOOLS/COMMIT_TRIGGER", "FRAMEWORK_ENGINE/TOOLS/COMMIT_TRIGGER", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("COMMIT_CONTEXT", "COMMIT_CONTEXT", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/COMMIT_CONTEXT", "FRAMEWORK_ENGINE/TOOLS/COMMIT_CONTEXT", "FRAMEWORK_ENGINE/TOOLS/COMMIT_CONTEXT", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("APPEND_CHANGE_RECORDS", "APPEND_CHANGE_RECORDS", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/APPEND_CHANGE_RECORDS", "FRAMEWORK_ENGINE/TOOLS/APPEND_CHANGE_RECORDS", "FRAMEWORK_ENGINE/TOOLS/APPEND_CHANGE_RECORDS", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("COMMIT_CHANGE_SET", "COMMIT_CHANGE_SET", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/COMMIT_CHANGE_SET", "FRAMEWORK_ENGINE/TOOLS/COMMIT_CHANGE_SET", "FRAMEWORK_ENGINE/TOOLS/COMMIT_CHANGE_SET", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("INSTALL_TOOLS", "INSTALL_TOOLS", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/INSTALL_TOOLS", "FRAMEWORK_ENGINE/TOOLS/INSTALL_TOOLS", "FRAMEWORK_ENGINE/TOOLS/INSTALL_TOOLS", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("START_BACKGROUND_SERVICES", "START_BACKGROUND_SERVICES", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/START_BACKGROUND_SERVICES", "FRAMEWORK_ENGINE/TOOLS/START_BACKGROUND_SERVICES", "FRAMEWORK_ENGINE/TOOLS/START_BACKGROUND_SERVICES", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_SEARCH", "ATOM_SEARCH", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_SEARCH", "FRAMEWORK_ENGINE/TOOLS/ATOM_SEARCH", "FRAMEWORK_ENGINE/TOOLS/ATOM_SEARCH", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_READ", "ATOM_READ", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_READ", "FRAMEWORK_ENGINE/TOOLS/ATOM_READ", "FRAMEWORK_ENGINE/TOOLS/ATOM_READ", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_CREATE", "ATOM_CREATE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_CREATE", "FRAMEWORK_ENGINE/TOOLS/ATOM_CREATE", "FRAMEWORK_ENGINE/TOOLS/ATOM_CREATE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_UPDATE", "ATOM_UPDATE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_UPDATE", "FRAMEWORK_ENGINE/TOOLS/ATOM_UPDATE", "FRAMEWORK_ENGINE/TOOLS/ATOM_UPDATE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_MOVE", "ATOM_MOVE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_MOVE", "FRAMEWORK_ENGINE/TOOLS/ATOM_MOVE", "FRAMEWORK_ENGINE/TOOLS/ATOM_MOVE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_ARCHIVE", "ATOM_ARCHIVE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_ARCHIVE", "FRAMEWORK_ENGINE/TOOLS/ATOM_ARCHIVE", "FRAMEWORK_ENGINE/TOOLS/ATOM_ARCHIVE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_PROMOTE", "ATOM_PROMOTE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_PROMOTE", "FRAMEWORK_ENGINE/TOOLS/ATOM_PROMOTE", "FRAMEWORK_ENGINE/TOOLS/ATOM_PROMOTE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_UPGRADE", "ATOM_UPGRADE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_UPGRADE", "FRAMEWORK_ENGINE/TOOLS/ATOM_UPGRADE", "FRAMEWORK_ENGINE/TOOLS/ATOM_UPGRADE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
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
    }


def scope_units() -> list[dict[str, object]]:
    rows = []
    authority_places: dict[str, Path] = {}
    delivery_places: dict[str, Path] = {}
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
                parent_place = CONTROL / "FRAMEWORK_METHODOLOGY"
            else:
                parent_places = authority_places if delivery_parent_place == "authority" else delivery_places
                if delivery_parent not in parent_places:
                    raise SystemExit(f"unknown Delivery parent for Scope Unit: {name}")
                parent_place = parent_places[delivery_parent]
            projected_delivery_path = delivery.relative_to(parent_place).as_posix()
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
        }
        if kind == "ordered_unit":
            row["local_order"] = local_order
            row["upstream_unit"] = upstream
        rows.append(row)
        authority_places[scope_segment] = authority
        if delivery is not None:
            delivery_places[scope_segment] = delivery
    return rows


def project_graph_state(
    generated_at: str,
    config_sha: str,
    binding: dict[str, str],
    scope_unit_rows: list[dict[str, object]],
) -> str:
    lines = [
        "# Generated runtime view. Delete and regenerate at any time.",
        "[projection]",
        'schema_version = "0.1"',
        'kind = "project_graph_state"',
        "non_authoritative = true",
        'currentness = "working_tree_snapshot"',
        f"generated_at = {quote(generated_at)}",
        f"canonical_generator = {quote(CANONICAL_GENERATOR.relative_to(ROOT).as_posix())}",
        f"canonical_generator_sha256 = {quote(sha(SCRIPT))}",
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
        "[repository]",
        f"control_root = {quote(CONTROL.relative_to(ROOT).as_posix())}",
        f"scope_unit_count = {len(scope_unit_rows)}",
    ]
    for row in scope_unit_rows:
        lines += ["", "[[scope_units]]"] + [
            f"{key} = {str(value).lower() if isinstance(value, bool) else value if isinstance(value, int) else quote(value)}"
            for key, value in row.items()
        ]
    return "\n".join(lines) + "\n"


def main() -> None:
    try:
        installed = installation_status(ROOT)
    except InstallationError as error:
        raise SystemExit(f"{error.code}: {error.message}") from error
    expected = ROOT / str(installed["package_root"]) / "GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py"
    if SCRIPT != expected.resolve():
        raise SystemExit("run the selected installed GENERATE_PROJECT_GRAPH_STATE Tool")
    if not CONTROL.is_dir() or not CONFIG.is_file():
        raise SystemExit("required control root or configuration is missing")
    config_sha = sha(CONFIG)
    binding = configuration_binding(config_sha)
    scope_unit_rows = scope_units()
    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")
    temporary_output = RUNTIME / "state/generate_project_graph_state/project_graph_state.toml.tmp"
    temporary_output.parent.mkdir(parents=True, exist_ok=True)
    temporary_output.write_text(
        project_graph_state(generated_at, config_sha, binding, scope_unit_rows),
        encoding="utf-8",
    )
    temporary_output.replace(OUTPUT)


if __name__ == "__main__":
    main()
