---
atom_id: CA-O-draft
role: Operations
form: Action
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Action'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---
## Summary

Set one Current Atom Status

## Claim scope

This Action applies to one exact selected non-container Current Atom under its applicable model and one exact requested Status in that model's Current group. The group includes model-admitted statuses beyond Active when present and excludes Draft and Archived; no container, descendant, cascade, scope or tier target is admitted.

## Claim

Set One Current Atom Status **means** the reusable Action that validates the selected source, target Status and status-dependent placement before applying one status-only result:

- A target Status must be exactly model-admitted as Current. The Action does not invent a transition matrix, infer Active, perform promotion, or handle Draft or Archived targets.
- If the target equals the selected Current Status, return a truthful no-op with the same identity, content, Version and Updated At; create no archive or successor.
- For an actual change, preserve identity, Summary, Role and content; archive the exact selected predecessor as canonical `ID@N` with status Archived, preserving Version N and its prior Updated At; then publish canonical `ID@N+1` with the actual Updated At and the target Status in its admitted Current placement.
- Resolve and validate the exact source and destinations, avoid overwriting another Atom, and return attributable diagnostics for invalid inputs or artifacts. Preserve completed effects and their evidence on partial work; do not automatically retry or roll back. Journal only records actual business events and is not permission, completeness proof or a success gate.

This Action owns the status effect and its validation boundary only. It owns no Workflow graph or Step binding and claims no implementation or provider selection.
