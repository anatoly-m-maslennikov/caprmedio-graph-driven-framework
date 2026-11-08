# CA-M-508@5
# CA-E-799@3
# CA-E-800@3
"""Private, profiler-free resource observations for Workbench acceptance tests."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
from pathlib import Path
import sys
import threading
import time
from typing import Any, Mapping


@dataclass(frozen=True)
class CgroupSnapshot:
    cpu_seconds: float
    memory_current: int
    memory_peak: int
    oom_kill: int


def assert_profiler_off() -> None:
    if sys.getprofile() is not None:
        raise AssertionError("CPU profiling must be disabled for resource gates")
    import tracemalloc
    if tracemalloc.is_tracing():
        raise AssertionError("Allocation profiling must be disabled for resource gates")


def _fields(path: str) -> dict[str, int]:
    try:
        lines = Path(path).read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise AssertionError(f"Workbench fixture requires cgroup v2 {path}") from error
    values: dict[str, int] = {}
    for line in lines:
        key, _, raw = line.partition(" ")
        try:
            values[key] = int(raw.strip())
        except ValueError as error:
            raise AssertionError(f"invalid cgroup counter {key!r}") from error
    return values


def cgroup_snapshot() -> CgroupSnapshot:
    """Read cgroup-v2 metrics inside the isolated Docker fixture."""
    cpu = _fields("/sys/fs/cgroup/cpu.stat")
    memory = _fields("/sys/fs/cgroup/memory.events")
    try:
        current = int(Path("/sys/fs/cgroup/memory.current").read_text().strip())
        peak = int(Path("/sys/fs/cgroup/memory.peak").read_text().strip())
    except (OSError, ValueError) as error:
        raise AssertionError("Workbench fixture requires cgroup-v2 memory counters") from error
    if "usage_usec" not in cpu or "oom_kill" not in memory or current < 0 or peak < current:
        raise AssertionError("invalid cgroup-v2 resource counters")
    return CgroupSnapshot(cpu["usage_usec"] / 1_000_000, current, peak, memory["oom_kill"])


def interval(before: CgroupSnapshot, after: CgroupSnapshot) -> dict[str, float | int]:
    if after.cpu_seconds < before.cpu_seconds or after.oom_kill < before.oom_kill:
        raise AssertionError("cgroup counters moved backwards")
    return {"cpu_seconds": round(after.cpu_seconds - before.cpu_seconds, 6),
            "memory_current": after.memory_current, "memory_peak": after.memory_peak,
            "oom_kill": after.oom_kill - before.oom_kill}


def plateau(samples: list[CgroupSnapshot], maximum_growth_bytes: int) -> dict[str, int]:
    """Test quiescent current-memory samples without forcing garbage collection."""
    if len(samples) < 2 or maximum_growth_bytes < 0:
        raise ValueError("plateau needs two samples and a non-negative limit")
    values = [sample.memory_current for sample in samples]
    growth = max(0, max(values) - values[0])
    if growth > maximum_growth_bytes:
        raise AssertionError(f"memory plateau grew {growth} bytes; limit {maximum_growth_bytes}")
    return {"minimum_memory_current": min(values), "maximum_memory_current": max(values),
            "growth_bytes": growth, "spread_bytes": max(values) - min(values)}


def _open_view_results(service: Any) -> set[str]:
    result_ids: set[str] = set()
    for item in service._workspaces.list()["items"]:
        for view in service._workspaces.get(item["workspace_id"])["views"]:
            result = view.get("result")
            if isinstance(result, dict) and isinstance(result.get("query_id"), str):
                result_ids.add(result["query_id"])
    return result_ids


def _keys_digest(values: Any) -> str:
    return hashlib.sha256("\n".join(sorted(map(str, values))).encode()).hexdigest()


def owner_inventory(service: Any) -> dict[str, Any]:
    """Snapshot private Workbench owners. It deliberately is not a product API."""
    with service._refresh_lock:
        store = service._store
        if store is None:
            raise AssertionError("Workbench store is not running")
        with store._lock:
            tables = {row[0] for row in store._connection.execute(
                "SELECT table_name FROM information_schema.tables WHERE table_schema = 'workbench_results'"
            ).fetchall()}
            results = set(store._results)
            pinned = {key for key, value in store._results.items() if value.pinned}
            managed = store._connection.execute("SELECT sum(memory_usage_bytes) FROM duckdb_memory()").fetchone()[0]
        state, reader = service._relation_state, service._reader
        outgoing = {} if state is None else state.outgoing
        if not set(reader._cached) <= reader._source_paths or not set(reader._failed) <= reader._source_paths:
            raise AssertionError("reader retains a removed source path")
        return {
            "result_tables": sorted(tables), "result_ids": sorted(results),
            "pinned_result_ids": sorted(pinned), "open_view_result_ids": sorted(_open_view_results(service)),
            "source_cache": {"cached": len(reader._cached), "failed": len(reader._failed),
                             "source_paths": len(reader._source_paths), "content_invalid": len(reader._content_invalid),
                             "reference_keys": len(reader._references.paths),
                             "reference_paths": sum(map(len, reader._references.paths.values())),
                             "accepted_references": len(reader._references.accepted),
                             "cached_paths_digest": _keys_digest(reader._cached),
                             "source_paths_digest": _keys_digest(reader._source_paths),
                             "reference_keys_digest": _keys_digest(reader._references.paths)},
            "relation_state": {"raw_by_path": 0 if state is None else len(state.raw_by_path),
                               "refs": 0 if state is None else len(state.refs),
                               "direct_facts": 0 if state is None else len(state.direct_facts),
                               "outgoing": len(outgoing),
                               "outgoing_keys_digest": _keys_digest(outgoing),
                               "empty_outgoing_keys": sorted(f"{kind}:{key}" for (kind, key), edges in outgoing.items() if not edges),
                               "atom_rows": 0 if state is None else len(state.atom_rows),
                               "atom_order": 0 if state is None else len(state.atom_order),
                               "scope_rows": 0 if state is None else len(state.scope_rows),
                               "registry_contributions": 0 if state is None else len(state.registry_contributions)},
            "watcher_pending": 0 if service._watcher is None else service._watcher._changes.qsize(),
            "duckdb_managed_bytes": managed,
            "process": {"threads": threading.active_count(), "file_descriptors": len(list(Path("/proc/self/fd").iterdir()))},
        }


def assert_inventory(actual: Mapping[str, Any], baseline: Mapping[str, Any] | None = None) -> None:
    ids, tables = set(actual["result_ids"]), set(actual["result_tables"])
    if tables != {f"query_{query_id}" for query_id in ids}:
        raise AssertionError("result tables do not exactly match QueryStore ownership")
    if set(actual["pinned_result_ids"]) != set(actual["open_view_result_ids"]):
        raise AssertionError("result pins do not exactly match open View ownership")
    if actual["relation_state"]["empty_outgoing_keys"]:
        raise AssertionError("relation state retains empty outgoing keys")
    if baseline is not None:
        current = actual["source_cache"] | actual["relation_state"]
        for key, expected in baseline.items():
            if current.get(key) != expected:
                raise AssertionError(f"owner inventory {key} is {current.get(key)!r}; expected {expected!r}")


def settle(service: Any, *, polls: int = 3, poll_seconds: float = 0.05) -> None:
    """Drain FIFO query logging and observe three quiescent indexer polls."""
    if polls < 1 or poll_seconds < 0:
        raise ValueError("invalid settle interval")
    service._query_log._writer.submit(lambda: None).result(timeout=10)
    deadline, quiet = time.monotonic() + 45, 0
    while quiet < polls:
        if time.monotonic() >= deadline:
            raise AssertionError("Workbench did not drain its watcher/log work")
        pending = service._watcher is not None and service._watcher._changes.qsize()
        busy = pending or service.sync_status()["syncing"] or service._query_log._writer._work_queue.qsize()
        quiet = 0 if busy else quiet + 1
        time.sleep(poll_seconds)


def emit_metrics(payload: Mapping[str, Any]) -> dict[str, Any]:
    value = dict(payload)
    print("WORKBENCH_RESOURCE " + json.dumps(value, sort_keys=True), flush=True)
    return value


def snapshot_json(snapshot: CgroupSnapshot) -> dict[str, float | int]:
    return asdict(snapshot)
