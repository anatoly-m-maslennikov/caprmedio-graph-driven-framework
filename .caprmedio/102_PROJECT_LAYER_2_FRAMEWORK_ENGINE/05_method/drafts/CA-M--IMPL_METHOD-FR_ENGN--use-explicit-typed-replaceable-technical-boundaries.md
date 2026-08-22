---
subject_scopes:
  - framework-engine-software
version: 2
updated_at: 2026-08-22 01:50:50
relations: {}
---
# Use explicit typed replaceable technical boundaries

Represent a replaceable technical boundary with an explicit interface and explicit input and output data. Use structural Protocols when consumers need a capability contract without requiring implementations to inherit from a framework base class.

Keep substrate-specific behavior in small adapters. Make the deterministic semantic core depend on the boundary contract rather than on a concrete filesystem, hook host, process runner, telemetry exporter, or persistence engine.

Candidate alignment: CA-M-002, CA-M-005, CA-M-006, CA-D-001.

## Sources

- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
- [Python documentation: typing.Protocol](https://docs.python.org/3.14/library/typing.html#typing.Protocol)
