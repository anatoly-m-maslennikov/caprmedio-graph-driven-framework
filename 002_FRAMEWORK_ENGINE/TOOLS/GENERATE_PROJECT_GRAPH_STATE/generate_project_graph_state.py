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
    / "002_FRAMEWORK_ENGINE"
    / "TOOLS"
    / "GENERATE_PROJECT_GRAPH_STATE"
    / "generate_project_graph_state.py"
)
CONFIG = ROOT / "caprmedio_framework_settings.toml"
JOURNAL = CONTROL / "work_journal"

SCOPE_UNITS = (
    ("META_METHODOLOGY", "META_MTHD", "META_METHODOLOGY", "000_BSEED_SUPERLAYER_META_METHODOLOGY", "", "tbd", ".", "ordered_unit", -2, "-2/1", "", 1, ""),
    ("METAMODEL", "MMODEL", "META_METHODOLOGY/METAMODEL", "000_BSEED_SUPERLAYER_META_METHODOLOGY/01_BSEED_LAYER_1_METAMODEL", ".caprmedio/101_PROJECT_LAYER_1_FRAMEWORK_METHODOLOGY/METAMODEL", "resolved", "", "ordered_unit", -1, "-1/1", "META_METHODOLOGY", 1, ""),
    ("SEMANTICS", "SEMNTC", "META_METHODOLOGY/SEMANTICS", "000_BSEED_SUPERLAYER_META_METHODOLOGY/02_BSEED_LAYER_2_SEMANTICS", "", "tbd", ".caprmedio/101_PROJECT_LAYER_1_FRAMEWORK_METHODOLOGY", "ordered_unit", -1, "-1/2", "META_METHODOLOGY", 2, "METAMODEL"),
    ("GOVERNANCE", "GOVERN", "META_METHODOLOGY/GOVERNANCE", "000_BSEED_SUPERLAYER_META_METHODOLOGY/03_BSEED_LAYER_3_GOVERNANCE", "", "tbd", ".caprmedio/101_PROJECT_LAYER_1_FRAMEWORK_METHODOLOGY", "ordered_unit", -1, "-1/3", "META_METHODOLOGY", 3, "SEMANTICS"),
    ("CAPRMEDIO", "CA", "CAPRMEDIO", ".", ".", "resolved", "", "project_root", 0, "0", "", None, None),
    ("FRAMEWORK_METHODOLOGY", "FR_MTHD", "CAPRMEDIO/FRAMEWORK_METHODOLOGY", "101_PROJECT_LAYER_1_FRAMEWORK_METHODOLOGY", "001_FRAMEWORK_METHODOLOGY", "resolved", "", "ordered_unit", 1, "1/1", "CAPRMEDIO", 1, ""),
    ("FRAMEWORK_ENGINE", "FR_ENGN", "CAPRMEDIO/FRAMEWORK_ENGINE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE", "002_FRAMEWORK_ENGINE", "resolved", "", "ordered_unit", 1, "1/2", "CAPRMEDIO", 2, "FRAMEWORK_METHODOLOGY"),
    ("OPERATOR_DOCUMENTATION", "OPER_DOC", "CAPRMEDIO/OPERATOR_DOCUMENTATION", "103_PROJECT_LAYER_3_OPERATOR_DOCUMENTATION", "003_OPERATOR_DOCUMENTATION", "resolved", "", "ordered_unit", 1, "1/3", "CAPRMEDIO", 3, "FRAMEWORK_ENGINE"),
    ("CORE_EXTENSIONS", "CORE_EXTENSIONS", "CAPRMEDIO/CORE_EXTENSIONS", "104_PROJECT_LAYER_4_CORE_EXTENSIONS", "004_CORE_EXTENSIONS", "resolved", "", "ordered_unit", 1, "1/4", "CAPRMEDIO", 4, "OPERATOR_DOCUMENTATION"),
    ("RELEASES", "RELSS", "CAPRMEDIO/RELEASES", "105_PROJECT_LAYER_5_RELEASES", "005_RELEASES", "resolved", "", "ordered_unit", 1, "1/5", "CAPRMEDIO", 5, "CORE_EXTENSIONS"),
    ("COMMUNITY_EXTENSIONS", "COMMUNITY_EXTENSIONS", "CAPRMEDIO/COMMUNITY_EXTENSIONS", "110_PROJECT_FEATURE_COMMUNITY_EXTENSIONS", "010_COMMUNITY_EXTENSIONS", "resolved", "", "unordered_unit", 1, "1", "CAPRMEDIO", None, None),
    ("FIELD", "FIELD", "CAPRMEDIO/FIELD", "110_PROJECT_FEATURE_FIELD", "010_FIELD", "resolved", "", "unordered_unit", 1, "1", "CAPRMEDIO", None, None),
    ("APPS", "APPS", "CAPRMEDIO/FRAMEWORK_ENGINE/APPS", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/202_APPS", "002_FRAMEWORK_ENGINE/APPS", "resolved", "", "unordered_unit", 2, "2", "FRAMEWORK_ENGINE", None, None),
    ("SKILLS", "SKILLS", "CAPRMEDIO/FRAMEWORK_ENGINE/SKILLS", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/203_SKILLS", "002_FRAMEWORK_ENGINE/SKILLS", "resolved", "", "unordered_unit", 2, "2", "FRAMEWORK_ENGINE", None, None),
    ("TOOLS", "TOOLS", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS", "002_FRAMEWORK_ENGINE/TOOLS", "resolved", "", "unordered_unit", 2, "2", "FRAMEWORK_ENGINE", None, None),
    ("GRAPH_APP", "GRAPH_APP", "CAPRMEDIO/FRAMEWORK_ENGINE/APPS/GRAPH_APP", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/202_APPS/GRAPH_APP", "002_FRAMEWORK_ENGINE/APPS/GRAPH_APP", "resolved", "", "unordered_unit", 3, "3", "APPS", None, None),
    ("MCP", "MCP", "CAPRMEDIO/FRAMEWORK_ENGINE/APPS/MCP", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/202_APPS/MCP", "", "tbd", "002_FRAMEWORK_ENGINE/APPS", "unordered_unit", 3, "3", "APPS", None, None),
    ("AGENT_HOST_PLUGINS", "AGENT_HOST_PLUGINS", "CAPRMEDIO/FRAMEWORK_ENGINE/APPS/AGENT_HOST_PLUGINS", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/202_APPS/AGENT_HOST_PLUGINS", "002_FRAMEWORK_ENGINE/APPS/AGENT_HOST_PLUGINS", "resolved", "", "unordered_unit", 3, "3", "APPS", None, None),
    ("CODEX_PLUGIN", "CODEX_PLUGIN", "CAPRMEDIO/FRAMEWORK_ENGINE/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/202_APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN", "002_FRAMEWORK_ENGINE/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN", "resolved", "", "unordered_unit", 4, "4", "AGENT_HOST_PLUGINS", None, None),
    ("TARGET_SET", "TARGET_SET", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/TARGET_SET", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/TARGET_SET", "002_FRAMEWORK_ENGINE/TOOLS/TARGET_SET", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("GRAPH_CHECK", "GRAPH_CHECK", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/GRAPH_CHECK", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/GRAPH_CHECK", "002_FRAMEWORK_ENGINE/TOOLS/GRAPH_CHECK", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("BULK_CHANGE", "BULK_CHANGE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/BULK_CHANGE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/BULK_CHANGE", "002_FRAMEWORK_ENGINE/TOOLS/BULK_CHANGE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("PROJECTION_REBUILD", "PROJECTION_REBUILD", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/PROJECTION_REBUILD", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/PROJECTION_REBUILD", "002_FRAMEWORK_ENGINE/TOOLS/PROJECTION_REBUILD", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("IMPLEMENTATION_INVENTORY", "IMPLEMENTATION_INVENTORY", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/IMPLEMENTATION_INVENTORY", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/IMPLEMENTATION_INVENTORY", "002_FRAMEWORK_ENGINE/TOOLS/IMPLEMENTATION_INVENTORY", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ADOPT_RECONCILE", "ADOPT_RECONCILE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ADOPT_RECONCILE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/ADOPT_RECONCILE", "002_FRAMEWORK_ENGINE/TOOLS/ADOPT_RECONCILE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("COMMIT_TRIGGER", "COMMIT_TRIGGER", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/COMMIT_TRIGGER", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/COMMIT_TRIGGER", "002_FRAMEWORK_ENGINE/TOOLS/COMMIT_TRIGGER", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("COMMIT_CONTEXT", "COMMIT_CONTEXT", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/COMMIT_CONTEXT", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/COMMIT_CONTEXT", "002_FRAMEWORK_ENGINE/TOOLS/COMMIT_CONTEXT", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("APPEND_CHANGE_RECORDS", "APPEND_CHANGE_RECORDS", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/APPEND_CHANGE_RECORDS", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/APPEND_CHANGE_RECORDS", "002_FRAMEWORK_ENGINE/TOOLS/APPEND_CHANGE_RECORDS", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("COMMIT_CHANGE_SET", "COMMIT_CHANGE_SET", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/COMMIT_CHANGE_SET", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/COMMIT_CHANGE_SET", "002_FRAMEWORK_ENGINE/TOOLS/COMMIT_CHANGE_SET", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("INSTALL_TOOLS", "INSTALL_TOOLS", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/INSTALL_TOOLS", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/INSTALL_TOOLS", "002_FRAMEWORK_ENGINE/TOOLS/INSTALL_TOOLS", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("START_BACKGROUND_SERVICES", "START_BACKGROUND_SERVICES", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/START_BACKGROUND_SERVICES", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/START_BACKGROUND_SERVICES", "002_FRAMEWORK_ENGINE/TOOLS/START_BACKGROUND_SERVICES", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_SEARCH", "ATOM_SEARCH", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_SEARCH", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/ATOM_SEARCH", "002_FRAMEWORK_ENGINE/TOOLS/ATOM_SEARCH", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_READ", "ATOM_READ", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_READ", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/ATOM_READ", "002_FRAMEWORK_ENGINE/TOOLS/ATOM_READ", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_CREATE", "ATOM_CREATE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_CREATE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/ATOM_CREATE", "002_FRAMEWORK_ENGINE/TOOLS/ATOM_CREATE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_UPDATE", "ATOM_UPDATE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_UPDATE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/ATOM_UPDATE", "002_FRAMEWORK_ENGINE/TOOLS/ATOM_UPDATE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_MOVE", "ATOM_MOVE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_MOVE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/ATOM_MOVE", "002_FRAMEWORK_ENGINE/TOOLS/ATOM_MOVE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_ARCHIVE", "ATOM_ARCHIVE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_ARCHIVE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/ATOM_ARCHIVE", "002_FRAMEWORK_ENGINE/TOOLS/ATOM_ARCHIVE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_PROMOTE", "ATOM_PROMOTE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_PROMOTE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/ATOM_PROMOTE", "002_FRAMEWORK_ENGINE/TOOLS/ATOM_PROMOTE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
    ("ATOM_UPGRADE", "ATOM_UPGRADE", "CAPRMEDIO/FRAMEWORK_ENGINE/TOOLS/ATOM_UPGRADE", "102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/ATOM_UPGRADE", "002_FRAMEWORK_ENGINE/TOOLS/ATOM_UPGRADE", "resolved", "", "unordered_unit", 3, "3", "TOOLS", None, None),
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
                parent_place = CONTROL / "101_PROJECT_LAYER_1_FRAMEWORK_METHODOLOGY"
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
