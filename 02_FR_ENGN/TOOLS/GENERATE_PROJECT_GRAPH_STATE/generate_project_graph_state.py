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


def units() -> list[dict[str, object]]:
    rows = []
    directories = [CONTROL, *sorted(path for path in CONTROL.rglob("*") if path.is_dir())]
    for directory in directories:
        children = [
            child
            for child in directory.iterdir()
            if child.name != ".DS_Store" and child != OUTPUT
        ]
        child_dirs = [child for child in children if child.is_dir()]
        child_files = [child for child in children if child.is_file()]
        kind = "mixed" if child_dirs and child_files else "area" if child_dirs else "feature" if child_files else "empty"
        relative = directory.relative_to(CONTROL)
        rows.append(
            {
                "path": directory.relative_to(ROOT).as_posix(),
                "parent": "" if directory == CONTROL else directory.parent.relative_to(ROOT).as_posix(),
                "depth": len(relative.parts),
                "as_is_kind": kind,
                "archived": "archive" in relative.parts,
                "direct_directory_count": len(child_dirs),
                "direct_file_count": len(child_files),
            }
        )
    return rows


def project_graph_state(
    generated_at: str,
    config_sha: str,
    binding: dict[str, str],
    source_rows: list[dict[str, str]],
    frontier_sha: str,
    contribution_rows: list[dict[str, str]],
    unit_rows: list[dict[str, object]],
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
        f"filesystem_unit_count = {len(unit_rows)}",
        f"graph_contribution_count = {len(contribution_rows)}",
    ]
    for row in unit_rows:
        lines += ["", "[[filesystem_units]]"] + [
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
    unit_rows = units()
    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")
    temporary_output = SCRIPT.parent / "project_graph_state.toml.tmp"
    temporary_output.write_text(
        project_graph_state(generated_at, config_sha, binding, source_rows, frontier_sha, contribution_rows, unit_rows),
        encoding="utf-8",
    )
    temporary_output.replace(OUTPUT)


if __name__ == "__main__":
    main()
