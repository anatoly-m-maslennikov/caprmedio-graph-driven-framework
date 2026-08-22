---
subject_scopes:
  - framework-engine-software
  - performance
version: 2
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Benchmark execution surfaces separately

Benchmark interactive Hooks, bounded batch Tools, MCP calls, App interactions, and background services as separate surfaces with separate workloads and thresholds. Preserve the command, input fixture, supported runtime, platform metadata, warm-up and calibration behavior, sample distribution, baseline, and comparison result.

Treat unstable results as insufficient evidence. Reopen a performance policy when the workload, environment, or Operator priority that justified its threshold changes.

Candidate alignment: CA-R-815, CA-E-002, CA-R-861, CA-O-003.

## Sources

- [Python documentation: cProfile and profile](https://docs.python.org/3.14/library/profile.html)
- [pyperf documentation](https://pyperf.readthedocs.io/en/latest/)
