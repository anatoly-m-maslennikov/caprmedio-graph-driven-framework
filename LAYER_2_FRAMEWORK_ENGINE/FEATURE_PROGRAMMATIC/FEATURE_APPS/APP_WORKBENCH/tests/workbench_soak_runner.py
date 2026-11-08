# CA-M-508@5
# CA-E-799@3
# CA-E-800@3
"""In-container short resource guard and opt-in 30-minute same-owner soak."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import platform
import sys
import tempfile
import time
from typing import Any

APP_ROOT = Path(__file__).resolve().parents[1]
PROGRAMMATIC = APP_ROOT.parents[1]
for location in (PROGRAMMATIC / "FEATURE_MCP", PROGRAMMATIC / "FEATURE_TOOLS", APP_ROOT.parent, APP_ROOT / "tests"):
    sys.path.insert(0, str(location))

from workbench_performance_fixture import FIXTURE_ATOM_COUNT, prepare_fixture  # noqa: E402
from workbench_soak_metrics import (  # noqa: E402
    assert_inventory, assert_profiler_off, cgroup_snapshot, emit_metrics, interval,
    owner_inventory, plateau, settle, snapshot_json,
)
from workbench_soak_workload import Workload  # noqa: E402
from workbench_tools import WorkbenchTools  # noqa: E402

# Calibrated against the fixed fixture; never derive limits from an acceptance run.
CPU_LIMIT_SECONDS = 25.0
CURRENT_MEMORY_LIMIT_BYTES = 576 * 1024**2
PEAK_MEMORY_LIMIT_BYTES = 640 * 1024**2
IDLE_CPU_LIMIT_SECONDS = 0.75
PLATEAU_GROWTH_LIMIT_BYTES = 64 * 1024**2


def record(payload: dict[str, Any], output: Path | None) -> None:
    emit_metrics(payload)
    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(payload, sort_keys=True) + "\n")


def resource_phase(tools: Any, name: str, operation: str, calibrate: bool) -> dict[str, Any]:
    before, started = cgroup_snapshot(), time.monotonic()
    tools._call(operation, {})
    after = cgroup_snapshot()
    values = interval(before, after) | {"wall_seconds": time.monotonic() - started}
    if values["wall_seconds"] > 45:
        raise AssertionError(f"{name} exceeded unchanged 45-second rebuild budget: {values}")
    if not calibrate and (
        values["cpu_seconds"] > CPU_LIMIT_SECONDS
        or after.memory_current > CURRENT_MEMORY_LIMIT_BYTES or after.memory_peak > PEAK_MEMORY_LIMIT_BYTES
    ):
        raise AssertionError(f"{name} resource regression: {values}")
    if values["oom_kill"]:
        raise AssertionError(f"{name} OOM: {values}")
    return values


def checkpoint(workload: Workload, baseline: dict[str, Any], identity: tuple[int, int]) -> dict[str, Any]:
    if (os.getpid(), id(workload.owner)) != identity:
        raise AssertionError("soak owner was replaced before the final leak check")
    settle(workload.owner)
    actual = owner_inventory(workload.owner)
    assert_inventory(actual, baseline["source_cache"] | baseline["relation_state"])
    return actual


def run(seconds: int, *, calibrate: bool, output: Path | None) -> dict[str, Any]:  # noqa: C901
    if seconds < 0 or 0 < seconds < 1800:
        raise ValueError("use zero for the short guard, or at least 1800 real seconds")
    assert_profiler_off()
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="workbench-soak-") as temporary:
        fixture = prepare_fixture(Path(temporary))
        settings = fixture.root / ".caprmedio_runtime" / "caprmedio_runtime_settings.toml"
        settings.parent.mkdir(parents=True)
        settings.write_text("[workbench]\nresult_ttl_seconds = 1\n", encoding="utf-8")
        tools = WorkbenchTools(fixture.root)
        try:
            cold = resource_phase(tools, "cold", "query_schema", calibrate)
            reread = resource_phase(tools, "warm_full_reread", "workbench_reread", calibrate)
            workload = Workload(tools, fixture)
            workload.warm()
            workload.cycle(999_999)
            settle(workload.owner)
            time.sleep(15)
            baseline = owner_inventory(workload.owner)
            assert_inventory(baseline)
            identity = (os.getpid(), id(workload.owner))
            samples = [cgroup_snapshot()]
            record({"status": "started", "cold": cold, "warm_full_reread": reread,
                    "pid": identity[0], "owner": identity[1], "baseline": baseline,
                    "resources": snapshot_json(samples[0])}, output)
            cycles, continuous_start = 0, time.monotonic()
            deadline = continuous_start + seconds
            next_schema = next_report = continuous_start
            while cycles < 2 or time.monotonic() < deadline:
                now = time.monotonic()
                schema = seconds > 0 and now >= next_schema + 300
                workload.cycle(cycles, schema=schema)
                if schema:
                    next_schema = now
                cycles += 1
                actual = checkpoint(workload, baseline, identity)
                samples.append(cgroup_snapshot())
                if samples[-1].oom_kill:
                    raise AssertionError("OOM during resource workload")
                if not calibrate and (
                    samples[-1].memory_current > CURRENT_MEMORY_LIMIT_BYTES
                    or samples[-1].memory_peak > PEAK_MEMORY_LIMIT_BYTES
                ):
                    raise AssertionError("resource workload exceeded frozen current/peak memory budgets")
                if time.monotonic() >= next_report + 60:
                    record({"status": "progress", "cycles": cycles,
                            "continuous_seconds": time.monotonic() - continuous_start,
                            "pid": identity[0], "owner": identity[1], "inventory": actual,
                            "resources": snapshot_json(samples[-1])}, output)
                    next_report = time.monotonic()
                if seconds:
                    time.sleep(max(0, min(deadline - time.monotonic(), 10 - (time.monotonic() - now))))
            continuous_seconds = time.monotonic() - continuous_start
            if continuous_seconds < seconds:
                raise AssertionError("soak finished before its real-time duration")
            idle_before = cgroup_snapshot()
            time.sleep(15)  # No in-container polling or profiling during the idle measurement.
            idle_after = cgroup_snapshot()
            idle = interval(idle_before, idle_after)
            if not calibrate and (
                idle_after.memory_current > CURRENT_MEMORY_LIMIT_BYTES
                or idle_after.memory_peak > PEAK_MEMORY_LIMIT_BYTES or idle_after.oom_kill
            ):
                raise AssertionError(f"idle memory/OOM exceeded frozen budgets: {idle}")
            inventory = checkpoint(workload, baseline, identity)
            samples.append(idle_after)
            if not calibrate:
                if idle["cpu_seconds"] > IDLE_CPU_LIMIT_SECONDS:
                    raise AssertionError(f"idle CPU exceeded frozen budget: {idle}")
                plateau_values = plateau(samples, PLATEAU_GROWTH_LIMIT_BYTES)
            else:
                plateau_values = {"observed_growth_bytes": max(x.memory_current for x in samples) - min(x.memory_current for x in samples)}
            final_reread = resource_phase(tools, "final_full_reread", "workbench_reread", calibrate)
            settle(workload.owner)
            final = owner_inventory(workload.owner)
            assert_inventory(final, baseline["source_cache"] | baseline["relation_state"])
            if final["result_ids"]:
                raise AssertionError("full reread retained process-local query results")
            result = {
                "status": "passed", "calibration_only": calibrate, "requested_seconds": seconds,
                "continuous_seconds": continuous_seconds, "cycles": cycles, "pid": identity[0],
                "owner": identity[1], "elapsed_seconds": time.monotonic() - started,
                "fixture_atoms": FIXTURE_ATOM_COUNT, "runtime_image": os.environ.get("CAPRMEDIO_IMAGE"),
                "platform": platform.platform(), "cpu_cap": 1, "memory_cap_bytes": 1536 * 1024**2,
                "cold": cold, "warm_full_reread": reread, "final_full_reread": final_reread,
                "idle_15_seconds": idle, "plateau": plateau_values,
                "settled_samples": [snapshot_json(sample) for sample in samples],
                "baseline_inventory": baseline, "pre_reset_inventory": inventory, "final_inventory": final,
                "limits": {"rebuild_wall_seconds": 45, "rebuild_cpu_seconds": CPU_LIMIT_SECONDS,
                           "current_memory_bytes": CURRENT_MEMORY_LIMIT_BYTES,
                           "peak_memory_bytes": PEAK_MEMORY_LIMIT_BYTES, "idle_cpu_seconds": IDLE_CPU_LIMIT_SECONDS,
                           "plateau_growth_bytes": PLATEAU_GROWTH_LIMIT_BYTES},
            }
            record(result, output)
            return result
        finally:
            if tools._service is not None:
                tools._service.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=0)
    parser.add_argument("--calibrate", action="store_true")
    parser.add_argument("--output", type=Path)
    options = parser.parse_args()
    try:
        run(options.seconds, calibrate=options.calibrate, output=options.output)
    except Exception as error:
        record({"status": "failed", "error": str(error)}, options.output)
        raise


if __name__ == "__main__":
    main()
