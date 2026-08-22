---
subject_scopes:
  - python-engineering
version: 3
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Provide small adapters around a deterministic core

Deliver one deterministic, I/O-free manager that owns all semantic logic and decisions and returns a typed result or execution graph from explicit typed inputs. Surround it with atomic non-deciding workers and adapters that own host callbacks, filesystem access, process execution, clocks, environment access, logging exporters, scheduling, or persistence engines.

Expose worker contracts structurally where that reduces coupling. Workers return observations or completion events and never choose targets, sequence, retry, fallback, or acceptance. A direct worker call or queued readiness event may identify only the fixed downstream transition in the manager-produced graph. Keep technical lifecycle state inside the worker, Scheduler, or independently supervised service that owns it and avoid inheritance hierarchies that are not required by substitutable behavior.

Candidate alignment: CA-D-001, CA-D-002, CA-M-002, CA-M-005.

## Sources

- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
- [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html)
- [Python documentation: dataclasses](https://docs.python.org/3.14/library/dataclasses.html)
