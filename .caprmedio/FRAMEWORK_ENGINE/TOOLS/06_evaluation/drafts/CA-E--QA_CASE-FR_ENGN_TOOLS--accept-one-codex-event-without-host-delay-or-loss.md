---
subject_scopes:
  - commit-automation
  - hooks
version: 1
updated_at: 2026-08-22 02:30:28
relations: {}
---
# Accept one Codex event without host delay or loss

Given one asynchronous Codex `PostToolUse` event and a stopped commit-automation service, invoke the installed Hook, terminate its process immediately after the atomic inbox rename, and run a no-op host command. Verify the Hook returns inside its admitted enqueue threshold, the host command does not wait for repository analysis, exactly one schema-valid immutable event remains in the Runtime inbox, and a later service start processes that same event identity.

The case fails on repository or graph scanning in the Hook process, direct pipeline-worker spawn, missing or duplicate event, acknowledgement before durable acceptance, or host latency outside the declared threshold.

Candidate alignment: CA-E-001, CA-E-002, CA-M-003, CA-M-005, CA-R-815, CA-R-861.

## Sources

- [Codex hooks documentation](https://learn.chatgpt.com/docs/hooks)
- [Python documentation: os.replace](https://docs.python.org/3.14/library/os.html#os.replace)
