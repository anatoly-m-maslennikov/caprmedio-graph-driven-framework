# CA-E-677@18
# CA-E-795@1
# CA-E-780@7
"""Shared reporting and hard limits for Workbench performance acceptance."""

from __future__ import annotations

import json
import sys
import tracemalloc
import time
import unittest

LATENCY_BUDGET_SECONDS = 1.5
BATCH_BUDGET_SECONDS = 15.0
MOVE_BUDGET_SECONDS = 30.0
STRUCTURAL_BUDGET_SECONDS = 60.0
REBUILD_BUDGET_SECONDS = 45.0


def record_performance(
    case: unittest.TestCase,
    *,
    operation: str,
    measurement: str,
    started_at: float,
    budget_seconds: float,
    items: int = 1,
    fixture_atom_count: int = 5_000,
) -> dict[str, object]:
    elapsed = time.monotonic() - started_at
    metric: dict[str, object] = {
        "measurement": measurement,
        "operation": operation,
        "elapsed_seconds": round(elapsed, 6),
        "limit_seconds": budget_seconds,
        "items": items,
        "fixture_atom_count": fixture_atom_count,
        "runtime_image": getattr(case, "image", None),
        "context": "controlled_fixture",
        "clock": "operation_start_to_verified_query_visibility",
        "includes_request_and_polling": True,
    }
    if items > 1:
        metric["atoms_per_second"] = round(items / elapsed, 3)
        metric["minimum_atoms_per_second"] = round(items / budget_seconds, 3)
    print("WORKBENCH_PERFORMANCE " + json.dumps(metric, sort_keys=True), flush=True)
    case.assertFalse(
        tracemalloc.is_tracing(), "Allocation profiling must be disabled for performance gates"
    )
    case.assertIsNone(sys.getprofile(), "CPU profiling must be disabled for performance gates")
    case.assertLessEqual(
        elapsed,
        budget_seconds,
        f"{operation}: {items} item(s) took {elapsed:.6f}s; budget {budget_seconds:.3f}s",
    )
    return metric
