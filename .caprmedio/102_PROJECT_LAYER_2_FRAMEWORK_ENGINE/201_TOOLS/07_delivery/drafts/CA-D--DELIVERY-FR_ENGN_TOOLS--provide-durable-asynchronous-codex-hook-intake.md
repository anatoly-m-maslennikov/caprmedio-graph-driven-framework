---
subject_scopes:
  - commit-automation
  - hooks
version: 1
updated_at: 2026-08-22 02:30:28
relations: {}
---
# Provide durable asynchronous Codex Hook intake

Deliver one asynchronous Codex `PostToolUse` carrier that normalizes the host payload into an immutable schema-versioned event, writes it through a temporary carrier and atomic rename to `.caprmedio_runtime/state/commit_automation/inbox/<event_id>.json`, and exits successfully after that durable acceptance boundary. The event identifies its source, repository, session, turn, Tool use, Hook event, stable event identity, and observation time.

The carrier contains no repository scan, graph traversal, commit-context gathering, Journal append, Git mutation, retry, lifecycle control, or direct pipeline-worker spawn. Concurrent or out-of-order callbacks may create independent inbox events without starting parallel Git work. A cancelled Hook cannot erase an event whose atomic inbox write completed.

Treat the inbox envelope as a transient operational copy required to survive Hook and service failure. After the Journal accepts the corresponding canonical provenance, compact Runtime state to Journal-resolvable identities and receipts; do not retain another session-provenance authority in Runtime, Atoms, or Projections.

Candidate alignment: CA-R-004, CA-R-827, CA-R-861, CA-M-003, CA-M-005, CA-D-001, CA-E-002.

## Sources

- [Codex hooks documentation](https://learn.chatgpt.com/docs/hooks)
- [Python documentation: tempfile](https://docs.python.org/3.14/library/tempfile.html)
- [Python documentation: os.replace](https://docs.python.org/3.14/library/os.html#os.replace)
