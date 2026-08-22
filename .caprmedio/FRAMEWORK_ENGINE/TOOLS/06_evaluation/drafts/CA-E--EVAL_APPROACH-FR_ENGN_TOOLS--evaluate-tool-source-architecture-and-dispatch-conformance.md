---
subject_scopes:
  - tool-orchestration
  - framework-engine-python
version: 2
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Evaluate Tool source architecture and dispatch conformance

Evaluate every changed Tool source tree for the declared file and executable-unit limits, one pure manager, atomic non-deciding workers, an acyclic manager-defined execution graph, mechanical scheduling or direct dispatch, canonical manager/worker/asset placement, and externalized large static mappings. Reject a generated-output exception because generated files are not part of the Tools source distribution.

Inject worker observations and require the manager to make every semantic and lifecycle decision without I/O. Require direct worker handoffs and queued completion events to follow only manager-declared transitions; the dispatcher or scheduler may advance state but may not change the graph.

Report each failed constraint independently with the exact file, object, dependency, transition, or effect boundary.

Candidate alignment: CA-E-001, CA-E-002, CA-M-002, CA-M-005, CA-D-001, CA-D-002.

## Sources

- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [Python FAQ: testing programs and components](https://docs.python.org/3/faq/library.html#how-do-i-test-a-python-program-or-component)
- [Python documentation: `unittest.mock`](https://docs.python.org/3/library/unittest.mock.html)
- [Python documentation: queues](https://docs.python.org/3.14/library/asyncio-queue.html)
