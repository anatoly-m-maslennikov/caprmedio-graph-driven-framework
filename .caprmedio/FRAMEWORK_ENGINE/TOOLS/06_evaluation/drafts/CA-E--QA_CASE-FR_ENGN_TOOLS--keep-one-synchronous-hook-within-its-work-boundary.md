---
subject_scopes:
  - hooks
  - performance
version: 2
updated_at: 2026-08-22 02:30:28
relations: {}
---
# Keep one synchronous Hook within its work boundary

Given one Git Hook invocation containing one required fail-closed gate and one unrelated broad scan, execute the synchronous path under its admitted latency threshold. Verify only the gate completes before host continuation, the scan is absent from the Hook process and deferred to changed-target or background execution, and timeout or failure returns the declared Git outcome and diagnostic.

This case does not evaluate Codex event intake; that Hook is asynchronous and has its own QA case.

Candidate alignment: CA-E-001, CA-E-002, CA-M-005, CA-R-815, CA-R-861.

## Sources

- [Git documentation: githooks](https://git-scm.com/docs/githooks)
- [Python documentation: subprocess timeouts](https://docs.python.org/3.14/library/subprocess.html#subprocess.run)
