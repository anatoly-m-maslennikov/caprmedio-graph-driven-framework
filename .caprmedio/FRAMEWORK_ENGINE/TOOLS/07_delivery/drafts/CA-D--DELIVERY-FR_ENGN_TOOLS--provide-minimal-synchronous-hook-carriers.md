---
subject_scopes:
  - hooks
version: 2
updated_at: 2026-08-22 02:30:28
relations: {}
---
# Provide minimal synchronous Hook carriers

Deliver each synchronous Git Hook as a small adapter that performs only its required fail-closed gate or post-action observation. Give it an explicit latency and timeout boundary, stable exit semantics, structured diagnostics, and a handoff to changed-target or background execution for non-gating work.

Deliver Codex automatic-commit intake separately as an asynchronous Hook carrier whose only effect is one atomic Runtime-inbox append. Do not embed broad repository or graph scans, context gathering, Journal append, Git mutation, retry, control logic, or per-event worker spawning in either carrier.

Candidate alignment: CA-D-001, CA-D-002, CA-M-005, CA-R-815, CA-R-861.

## Sources

- [Git documentation: githooks](https://git-scm.com/docs/githooks)
- [Python documentation: subprocess timeouts](https://docs.python.org/3.14/library/subprocess.html#subprocess.run)
- [Codex hooks documentation](https://learn.chatgpt.com/docs/hooks)
