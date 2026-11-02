---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: framework-engine-mcp
  depends_on: []
version: 6
updated_at: 2026-10-23 03:17:34 +0400
relations:
  evaluation_for:
  - CA-M-171
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-277@6
status: Archived
---
# Remove one disabled Tool projection

## Claim checked

Registry reconciliation removes a projection whose source Tool is disabled.

## Test case

Disable one previously exposed current Tool **and** regenerate the registry.

## Acceptance criteria

the resulting complete registry excludes that Tool **and** retains **every** other eligible current source.

## Failure disposition

Stop **when** a stale **or** independently allowlisted projection remains.
