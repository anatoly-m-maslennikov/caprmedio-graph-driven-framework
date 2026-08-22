---
subject_scopes:
  - hooks
version: 2
updated_at: 2026-08-22 02:30:28
relations: {}
---
# Keep synchronous Hook work minimal

Run only the smallest deterministic gate that must complete before a synchronous host action continues. A required Git pre-action invariant may fail closed, but broad repository scans, graph traversal, indexing, enrichment, and non-gating tests belong in changed-target evaluation, cached execution, background services, or an explicit later gate.

Use an asynchronous Codex `PostToolUse` Hook for automatic commit intake. It may normalize the host event, atomically persist one immutable event in the Runtime inbox, and return; it must not scan the repository, gather commit context, append the Journal, stage files, create a commit, retry the pipeline, or spawn one pipeline worker per Hook event. Treat the durable inbox write as acceptance and let the independently supervised repository service process it.

Keep Git `pre-commit` and `commit-msg` Hooks synchronous only for the narrow fail-closed Evaluations they own. Keep `post-commit` observational. Measure synchronous gate latency and asynchronous enqueue latency as separate execution surfaces.

Candidate alignment: CA-R-815, CA-R-819, CA-R-861, CA-M-003, CA-M-005, CA-O-003.

## Sources

- [Git documentation: githooks](https://git-scm.com/docs/githooks)
- [Python documentation: subprocess timeouts](https://docs.python.org/3.14/library/subprocess.html#subprocess.run)
- [Codex hooks documentation](https://learn.chatgpt.com/docs/hooks)
