---
artifact_subtype: defect
subject_scopes:
  - lifecycle
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---

# Defect — Lifecycle transitions are not enforced

The lifecycle validator accepts a later `accepted` event after a terminal
state and silently overwrites multiple absorption successors for one atom.
The append-only ledger can therefore reactivate retired authority or derive an
ambiguous successor while still passing validation.

## Rationale

This is a current governance defect because immutable authority requires legal,
deterministic lifecycle transitions rather than append-only storage alone.
