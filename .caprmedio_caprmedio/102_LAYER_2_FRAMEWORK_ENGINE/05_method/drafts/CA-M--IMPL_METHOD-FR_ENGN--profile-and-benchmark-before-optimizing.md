---
subject_scopes:
  - framework-engine-software
  - performance
version: 2
updated_at: 2026-08-22 01:50:50
relations: {}
---
# Profile and benchmark before optimizing

Use a profiler to locate measured bottlenecks before changing code for speed. Evaluate a proposed optimization with a reproducible benchmark that records inputs, environment metadata, baseline distribution, changed distribution, and the accepted regression threshold.

Keep separate measurements for interactive Hooks, batch Tools, MCP calls, App interactions, and background services because their latency and throughput needs differ. Prefer the simpler implementation when the measured benefit does not justify its added operating cost.

Candidate alignment: CA-R-815, CA-R-861, CA-M-005, CA-E-002, CA-O-003.

## Sources

- [Python documentation: profilers](https://docs.python.org/3.14/library/profile.html)
- [pyperf documentation](https://pyperf.readthedocs.io/en/latest/)
