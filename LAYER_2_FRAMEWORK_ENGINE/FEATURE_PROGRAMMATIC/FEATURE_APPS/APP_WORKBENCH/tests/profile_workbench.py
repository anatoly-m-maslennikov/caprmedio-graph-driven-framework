# CA-R-2998@1
# CA-M-503@1
# CA-D-703@1
# CA-E-795@1

"""Opt-in, isolated Workbench profiler; it is never a latency or throughput gate."""

from __future__ import annotations

import argparse
import cProfile
import hashlib
from importlib import metadata
import json
import os
from pathlib import Path
import resource
import shutil
import sys
import time
import tracemalloc
import uuid
from typing import Any


REBUILD_CYCLES = 3
TRACE_FRAMES = 5
OWNER = "workbench-profile"
IMPLEMENTATION_ROOT = Path(__file__).resolve().parents[5]
APPS_ROOT = IMPLEMENTATION_ROOT / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS"
TOOLS_ROOT = IMPLEMENTATION_ROOT / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS"
BACKEND_ROOT = APPS_ROOT / "APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND"
CODE_FILES = (
    "query_store.py", "source_reader.py", "source_rows.py", "markdown_content.py",
    "content_schema.py", "incremental_relations.py", "projection_delta.py", "relations.py",
)


def _imports() -> None:
    for path in (str(TOOLS_ROOT), str(APPS_ROOT)):
        if path not in sys.path:
            sys.path.insert(0, path)


def _temporary_root(project_root: Path) -> Path:
    _imports()
    from project_selection import resolve_project

    selection = resolve_project(project_root)
    temporary = selection.settings.get("paths", {}).get("temporary_root")
    if not isinstance(temporary, str) or not temporary:
        raise ValueError("Project settings must define paths.temporary_root")
    return (selection.root / temporary).resolve()


def output_directory(project_root: Path, requested: Path | None) -> Path:
    temporary = _temporary_root(project_root)
    candidate = (requested if requested is not None else temporary / OWNER / uuid.uuid4().hex).resolve()
    if not candidate.is_relative_to(temporary):
        raise ValueError("--output must stay beneath the selected Project temporary root")
    candidate.mkdir(parents=True, exist_ok=False)
    return candidate


def _code_hashes() -> dict[str, str]:
    return {name: hashlib.sha256((BACKEND_ROOT / name).read_bytes()).hexdigest() for name in CODE_FILES}


def _source_digest(project_root: Path, atom_rows: list[dict[str, Any]], scope_rows: list[dict[str, Any]]) -> dict[str, Any]:
    paths = {
        str(row[path_key])
        for row in [*atom_rows, *scope_rows]
        for path_key in ("source_path", "declaration_source_path")
        if isinstance(row.get(path_key), str)
    }
    digest = hashlib.sha256()
    for relative in sorted(paths):
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(hashlib.sha256((project_root / relative).read_bytes()).digest())
    return {"count": len(paths), "digest": digest.hexdigest()}


def _peak_rss_bytes() -> int:
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return raw if sys.platform == "darwin" else raw * 1024


def _native_memory(connection: Any) -> dict[str, Any]:
    try:
        rows = connection.execute("SELECT tag, memory_usage_bytes FROM duckdb_memory()").fetchall()
    except Exception as error:
        return {"available": False, "reason": str(error)}
    return {
        "available": True,
        "managed_bytes": sum(int(row[1]) for row in rows),
        "tags": {str(row[0]): int(row[1]) for row in rows if int(row[1])},
    }


def _allocation_traces(snapshot: tracemalloc.Snapshot) -> list[dict[str, Any]]:
    return [
        {
            "size_bytes": statistic.size,
            "count": statistic.count,
            "traceback": [str(frame) for frame in statistic.traceback],
        }
        for statistic in snapshot.statistics("lineno")[:20]
    ]


def profile(project_root: Path, output: Path) -> dict[str, Any]:
    """Profile one initial index plus exactly three isolated full rebuilds."""
    _imports()
    from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.incremental_relations import materialize_delta
    from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store import QueryStore
    from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_reader import SourceReader

    report: dict[str, Any] = {
        "instrumented": True,
        "not_performance_acceptance_timing": True,
        "rebuild_cycles": REBUILD_CYCLES,
        "trace_frames": TRACE_FRAMES,
        "source_root": str(project_root),
        "runtime": {
            "python_version": sys.version,
            "platform": sys.platform,
            "duckdb_package_version": metadata.version("duckdb"),
        },
        "code_hashes_before": _code_hashes(),
        "measurements": [],
    }
    database_directory = output / "disposable-database"
    error: BaseException | None = None
    started = time.perf_counter()
    profiler = cProfile.Profile()
    tracemalloc.start(TRACE_FRAMES)
    profiler.enable()
    try:
        initial_started = time.perf_counter()
        reader = SourceReader(project_root)
        raw_atoms, raw_scopes = reader.capture()
        report["source_hashes_before"] = _source_digest(project_root, raw_atoms, raw_scopes)
        atom_rows, scope_rows, relation_types, _inverse, _state, _delta = materialize_delta(raw_atoms, raw_scopes)
        extension = os.environ.get("CAPRMEDIO_DUCKPGQ_EXTENSION_DIRECTORY")
        store = QueryStore(
            extension_directory=Path(extension) if extension else None,
            database_path=database_directory / "projection.duckdb",
        )
        try:
            store.replace(atom_rows, scope_rows, relation_types=relation_types, content_schema=reader.content_schema)
            current_bytes, peak_bytes = tracemalloc.get_traced_memory()
            report["measurements"].append({
                "label": "initial_index",
                "instrumented_elapsed_seconds": round(time.perf_counter() - initial_started, 6),
                "includes_source_capture_and_materialization": True,
                "python_current_bytes": current_bytes,
                "python_peak_bytes": peak_bytes,
                "process_high_water_rss_bytes": _peak_rss_bytes(),
                "process_high_water_rss_is_current_memory": False,
                "duckdb_managed_memory": _native_memory(store._connection),
            })
            for number in range(1, REBUILD_CYCLES + 1):
                phase_started = time.perf_counter()
                store.replace(atom_rows, scope_rows, relation_types=relation_types, content_schema=reader.content_schema)
                current_bytes, peak_bytes = tracemalloc.get_traced_memory()
                report["measurements"].append({
                    "label": f"full_rebuild_{number}",
                    "instrumented_elapsed_seconds": round(time.perf_counter() - phase_started, 6),
                    "includes_source_capture_and_materialization": False,
                    "input": "same captured source projection",
                    "python_current_bytes": current_bytes,
                    "python_peak_bytes": peak_bytes,
                    "process_high_water_rss_bytes": _peak_rss_bytes(),
                    "process_high_water_rss_is_current_memory": False,
                    "duckdb_managed_memory": _native_memory(store._connection),
                })
        finally:
            store.close()
        report["dataset"] = {"atom_count": len(raw_atoms), "scope_unit_count": len(raw_scopes)}
        report["source_hashes_after"] = _source_digest(project_root, raw_atoms, raw_scopes)
    except BaseException as caught:
        error = caught
        report["error"] = {"type": type(caught).__name__, "message": str(caught)}
    finally:
        profiler.disable()
        current_bytes, peak_bytes = tracemalloc.get_traced_memory()
        report["python_allocations"] = {
            "current_bytes": current_bytes,
            "peak_bytes": peak_bytes,
            "top": _allocation_traces(tracemalloc.take_snapshot()),
        }
        tracemalloc.stop()
        report["total_instrumented_elapsed_seconds"] = round(time.perf_counter() - started, 6)
        report["code_hashes_after"] = _code_hashes()
        profiler.dump_stats(str(output / "cpu.pstats"))
        try:
            if database_directory.exists():
                shutil.rmtree(database_directory)
            report["disposable_database_cleanup"] = {"succeeded": True}
        except OSError as cleanup_error:
            report["disposable_database_cleanup"] = {
                "succeeded": False, "retained_path": str(database_directory), "error": str(cleanup_error),
            }
        (output / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if error is not None:
        raise error
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, type=Path, help="CAPRMEDIO Project whose sources are read")
    parser.add_argument("--output", type=Path, help="Optional output under the selected Project temporary root")
    args = parser.parse_args()
    project_root = args.project_root.resolve()
    output = output_directory(project_root, args.output)
    report = profile(project_root, output)
    print(json.dumps({"output": str(output), "dataset": report["dataset"], "rebuild_cycles": REBUILD_CYCLES}))


if __name__ == "__main__":
    main()
