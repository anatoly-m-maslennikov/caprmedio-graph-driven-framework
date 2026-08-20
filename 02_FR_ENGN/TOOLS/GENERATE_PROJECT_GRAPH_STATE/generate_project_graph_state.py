#!/usr/bin/env python3
"""Generate a bounded, non-authoritative view of the live CAPRMEDIO control root."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path

SCRIPT = Path(__file__).resolve()
ROOT = next(parent for parent in SCRIPT.parents if (parent / ".git").exists())
CONTROL = ROOT / ".caprmedio"
RUNTIME = ROOT / ".caprmedio_runtime"
OUTPUT = CONTROL / "project_graph_state.toml"
CANONICAL_GENERATOR = (
    ROOT
    / "02_FR_ENGN"
    / "TOOLS"
    / "GENERATE_PROJECT_GRAPH_STATE"
    / "generate_project_graph_state.py"
)
CONFIG = ROOT / "caprmedio_framework_settings.toml"
JOURNAL = CONTROL / "work_journal"

PROJECT_ROOT_FOLDERS = (
    ("FRAMEWORK_METHODOLOGY", "100_LAYER_1_FRAMEWORK_METHODOLOGY", "CAPRMEDIO-GOV-REQU-774--register-project-layer-directory-labels.md"),
    ("FRAMEWORK_ENGINE", "200_LAYER_2_FRAMEWORK_ENGINE", "CAPRMEDIO-GOV-REQU-774--register-project-layer-directory-labels.md"),
    ("DOCUMENTATION", "300_LAYER_3_DOCUMENTATION", "CAPRMEDIO-GOV-REQU-774--register-project-layer-directory-labels.md"),
    ("RELEASES", "400_LAYER_4_RELEASES", "CAPRMEDIO-GOV-REQU-774--register-project-layer-directory-labels.md"),
    ("FIELD", "FIELD", "CAPRMEDIO-GOV-REQU-776--register-field-directory-label.md"),
)

SCOPE_UNITS = (
    ("METAMODEL", "METAMODEL", "_01_BSEED_LAYER_1_METAMODEL", "ordered_unit", -1, "-1/1", "", 1, "", "CAPRMEDIO-REQU-706--define-caprmedio-structural-topology.md"),
    ("SEMANTICS", "SEMANTICS", "_02_BSEED_LAYER_2_SEMANTICS", "ordered_unit", -1, "-1/2", "", 2, "METAMODEL", "CAPRMEDIO-REQU-706--define-caprmedio-structural-topology.md"),
    ("GOVERNANCE", "GOVERNANCE", "_03_BSEED_LAYER_3_GOVERNANCE", "ordered_unit", -1, "-1/3", "", 3, "SEMANTICS", "CAPRMEDIO-REQU-706--define-caprmedio-structural-topology.md"),
    ("PROJECT", "PROJECT", ".", "project_root", 0, "0", "", None, None, "CAPRMEDIO-REQU-706--define-caprmedio-structural-topology.md"),
    ("FRAMEWORK_METHODOLOGY", "PROJECT/FRAMEWORK_METHODOLOGY", "100_LAYER_1_FRAMEWORK_METHODOLOGY", "ordered_unit", 1, "1/1", "PROJECT", 1, "", "CAPRMEDIO-REQU-707--order-project-layers.md"),
    ("FRAMEWORK_ENGINE", "PROJECT/FRAMEWORK_ENGINE", "200_LAYER_2_FRAMEWORK_ENGINE", "ordered_unit", 1, "1/2", "PROJECT", 2, "FRAMEWORK_METHODOLOGY", "CAPRMEDIO-REQU-707--order-project-layers.md"),
    ("DOCUMENTATION", "PROJECT/DOCUMENTATION", "300_LAYER_3_DOCUMENTATION", "ordered_unit", 1, "1/3", "PROJECT", 3, "FRAMEWORK_ENGINE", "CAPRMEDIO-REQU-707--order-project-layers.md"),
    ("RELEASES", "PROJECT/RELEASES", "400_LAYER_4_RELEASES", "ordered_unit", 1, "1/4", "PROJECT", 4, "DOCUMENTATION", "CAPRMEDIO-REQU-707--order-project-layers.md"),
    ("FIELD", "PROJECT/FIELD", "FIELD", "unordered_unit", 1, "1", "PROJECT", None, None, "CAPRMEDIO-REQU-775--define-field-as-unordered-project-child.md"),
    ("APP", "PROJECT/FRAMEWORK_ENGINE/APP", "200_LAYER_2_FRAMEWORK_ENGINE/APP", "unordered_unit", 2, "2", "FRAMEWORK_ENGINE", None, None, "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-700--define-framework-engine-feature-topology.md"),
    ("SKILLS", "PROJECT/FRAMEWORK_ENGINE/SKILLS", "200_LAYER_2_FRAMEWORK_ENGINE/SKILLS", "unordered_unit", 2, "2", "FRAMEWORK_ENGINE", None, None, "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-700--define-framework-engine-feature-topology.md"),
    ("TOOLS", "PROJECT/FRAMEWORK_ENGINE/TOOLS", "200_LAYER_2_FRAMEWORK_ENGINE/TOOLS", "unordered_unit", 2, "2", "FRAMEWORK_ENGINE", None, None, "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-700--define-framework-engine-feature-topology.md"),
    ("TARGET_SET", "PROJECT/FRAMEWORK_ENGINE/TOOLS/TARGET_SET", "200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/TARGET_SET", "unordered_unit", 3, "3", "TOOLS", None, None, "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-704--define-target-set-tool-unit.md"),
    ("GRAPH_CHECK", "PROJECT/FRAMEWORK_ENGINE/TOOLS/GRAPH_CHECK", "200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/GRAPH_CHECK", "unordered_unit", 3, "3", "TOOLS", None, None, "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-705--define-graph-check-tool-unit.md"),
    ("BULK_CHANGE", "PROJECT/FRAMEWORK_ENGINE/TOOLS/BULK_CHANGE", "200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/BULK_CHANGE", "unordered_unit", 3, "3", "TOOLS", None, None, "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-706--define-bulk-change-tool-unit.md"),
    ("PROJECTION_REBUILD", "PROJECT/FRAMEWORK_ENGINE/TOOLS/PROJECTION_REBUILD", "200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/PROJECTION_REBUILD", "unordered_unit", 3, "3", "TOOLS", None, None, "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-707--define-projection-rebuild-tool-unit.md"),
    ("IMPLEMENTATION_INVENTORY", "PROJECT/FRAMEWORK_ENGINE/TOOLS/IMPLEMENTATION_INVENTORY", "200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/IMPLEMENTATION_INVENTORY", "unordered_unit", 3, "3", "TOOLS", None, None, "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-708--define-implementation-inventory-tool-unit.md"),
    ("ADOPT_RECONCILE", "PROJECT/FRAMEWORK_ENGINE/TOOLS/ADOPT_RECONCILE", "200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/ADOPT_RECONCILE", "unordered_unit", 3, "3", "TOOLS", None, None, "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-709--define-adopt-reconcile-tool-unit.md"),
    ("COMMIT_TRIGGER", "PROJECT/FRAMEWORK_ENGINE/TOOLS/COMMIT_TRIGGER", "200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/COMMIT_TRIGGER", "unordered_unit", 3, "3", "TOOLS", None, None, "CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-flat-auto-commit-tool-topology.md"),
    ("COMMIT_CONTEXT", "PROJECT/FRAMEWORK_ENGINE/TOOLS/COMMIT_CONTEXT", "200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/COMMIT_CONTEXT", "unordered_unit", 3, "3", "TOOLS", None, None, "CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-flat-auto-commit-tool-topology.md"),
    ("APPEND_CHANGE_RECORDS", "PROJECT/FRAMEWORK_ENGINE/TOOLS/APPEND_CHANGE_RECORDS", "200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/APPEND_CHANGE_RECORDS", "unordered_unit", 3, "3", "TOOLS", None, None, "CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-flat-auto-commit-tool-topology.md"),
    ("COMMIT_CHANGE_SET", "PROJECT/FRAMEWORK_ENGINE/TOOLS/COMMIT_CHANGE_SET", "200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/COMMIT_CHANGE_SET", "unordered_unit", 3, "3", "TOOLS", None, None, "CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-flat-auto-commit-tool-topology.md"),
)


def sha(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def quote(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def files() -> list[Path]:
    return sorted(
        path
        for path in CONTROL.rglob("*")
        if path.is_file()
        and path.name != ".DS_Store"
        and path != OUTPUT
    )


def frontier(paths: list[Path]) -> tuple[list[dict[str, str]], str]:
    rows = [
        {"path": path.relative_to(ROOT).as_posix(), "sha256": sha(path)}
        for path in paths
    ]
    packed = "".join(f"{row['path']}\0{row['sha256']}\n" for row in rows)
    return rows, hashlib.sha256(packed.encode()).hexdigest()


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


def frontmatter(text: str, key: str) -> str | None:
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return None
    prefix = f"{key}:"
    for line in text[4 : text.find("\n---\n", 4)].splitlines():
        if line.startswith(prefix):
            return line[len(prefix) :].strip().strip('"\'')
    return None


def contributions(paths: list[Path]) -> list[dict[str, str]]:
    rows = []
    for path in paths:
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        if "\nproject_graph_state:\n" not in text:
            continue
        rows.append(
            {
                "atom_id": frontmatter(text, "atom_id") or path.stem.split("--", 1)[0],
                "carrier": path.relative_to(ROOT).as_posix(),
                "version": frontmatter(text, "version") or "unknown",
                "sha256": sha(path),
            }
        )
    return rows


def atom_by_filename(paths: list[Path]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for path in paths:
        if path.suffix != ".md" or "archive" in path.relative_to(CONTROL).parts:
            continue
        if path.name in result:
            raise SystemExit(f"ambiguous active Atom carrier filename: {path.name}")
        result[path.name] = path
    return result


def source_binding(index: dict[str, Path], filename: str) -> dict[str, str]:
    try:
        source = index[filename]
    except KeyError as error:
        raise SystemExit(f"missing active Scope Unit source Atom: {filename}") from error
    text = source.read_text(encoding="utf-8")
    return {
        "source_atom_id": frontmatter(text, "atom_id") or source.stem.split("--", 1)[0],
        "source_carrier": source.relative_to(ROOT).as_posix(),
        "source_version": frontmatter(text, "version") or "unknown",
    }


def project_root_folders(index: dict[str, Path]) -> list[dict[str, object]]:
    rows = []
    for scope_unit, folder, source_filename in PROJECT_ROOT_FOLDERS:
        path = CONTROL / folder
        rows.append(
            {
                "scope_unit": scope_unit,
                "path": path.relative_to(ROOT).as_posix(),
                "materialized": path.is_dir(),
                **source_binding(index, source_filename),
            }
        )
    return rows


def scope_units(index: dict[str, Path]) -> list[dict[str, object]]:
    rows = []
    for identity, scope_path, folder, kind, level, coordinate, parent, local_order, upstream, source_filename in SCOPE_UNITS:
        carrier = CONTROL if folder == "." else CONTROL / folder
        row: dict[str, object] = {
            "identity": identity,
            "scope_path": scope_path,
            "carrier_folder": carrier.relative_to(ROOT).as_posix() if carrier.is_dir() else "",
            "carrier_materialized": carrier.is_dir(),
            "structural_kind": kind,
            "structural_level": level,
            "structural_coordinate": coordinate,
            "structural_parent": parent,
        }
        if kind == "ordered_unit":
            row["local_order"] = local_order
            row["upstream_unit"] = upstream
        row.update(source_binding(index, source_filename))
        rows.append(row)
    return rows


def project_graph_state(
    generated_at: str,
    config_sha: str,
    binding: dict[str, str],
    source_rows: list[dict[str, str]],
    frontier_sha: str,
    contribution_rows: list[dict[str, str]],
    root_folder_rows: list[dict[str, object]],
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
        f"canonical_generator_sha256 = {quote(sha(CANONICAL_GENERATOR))}",
        f"executed_generator = {quote(SCRIPT.relative_to(ROOT).as_posix())}",
        f"executed_generator_sha256 = {quote(sha(SCRIPT))}",
        f"source_frontier_sha256 = {quote(frontier_sha)}",
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
        f"governed_file_count = {len(source_rows)}",
        f"project_root_scope_unit_folder_count = {len(root_folder_rows)}",
        f"scope_unit_count = {len(scope_unit_rows)}",
        f"graph_contribution_count = {len(contribution_rows)}",
    ]
    for row in root_folder_rows:
        lines += ["", "[[project_root_scope_unit_folders]]"] + [
            f"{key} = {str(value).lower() if isinstance(value, bool) else value if isinstance(value, int) else quote(value)}"
            for key, value in row.items()
        ]
    for row in scope_unit_rows:
        lines += ["", "[[scope_units]]"] + [
            f"{key} = {str(value).lower() if isinstance(value, bool) else value if isinstance(value, int) else quote(value)}"
            for key, value in row.items()
        ]
    for row in contribution_rows:
        lines += ["", "[[graph_contributions]]"] + [
            f"{key} = {quote(value)}" for key, value in row.items()
        ]
    for row in source_rows:
        lines += ["", "[[source_frontier]]"] + [
            f"{key} = {quote(value)}" for key, value in row.items()
        ]
    return "\n".join(lines) + "\n"


def main() -> None:
    if RUNTIME not in SCRIPT.parents:
        raise SystemExit(
            "copy the canonical generator under .caprmedio_runtime and run that copy"
        )
    if not CONTROL.is_dir() or not CONFIG.is_file() or not CANONICAL_GENERATOR.is_file():
        raise SystemExit("required control root, configuration, or canonical generator is missing")
    if sha(SCRIPT) != sha(CANONICAL_GENERATOR):
        raise SystemExit("runtime generator copy differs from the canonical Tool carrier")
    governed = files()
    source_rows, frontier_sha = frontier(governed)
    config_sha = sha(CONFIG)
    binding = configuration_binding(config_sha)
    contribution_rows = contributions(governed)
    atom_index = atom_by_filename(governed)
    root_folder_rows = project_root_folders(atom_index)
    scope_unit_rows = scope_units(atom_index)
    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")
    temporary_output = SCRIPT.parent / "project_graph_state.toml.tmp"
    temporary_output.write_text(
        project_graph_state(generated_at, config_sha, binding, source_rows, frontier_sha, contribution_rows, root_folder_rows, scope_unit_rows),
        encoding="utf-8",
    )
    temporary_output.replace(OUTPUT)


if __name__ == "__main__":
    main()
