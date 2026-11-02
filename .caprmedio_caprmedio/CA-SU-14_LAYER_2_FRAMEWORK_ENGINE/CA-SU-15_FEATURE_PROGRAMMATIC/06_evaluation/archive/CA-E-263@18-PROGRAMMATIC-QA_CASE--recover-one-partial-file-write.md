---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/External Effect Boundary
  depends_on: []
version: 18
updated_at: 2026-10-24 10:48:25 +0400
relations:
  evaluation_for:
  - CA-M-409
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-263@18
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
tier: 5
type: Eval Case
---
# Recover one partial file write

## Claim checked

one interrupted PROGRAMMATIC file replacement preserves **or** explicitly reports
its declared recovery boundary **without** guessing at a completed result.

## Applicable conditions

apply **when** a component writes replacement content through a temporary carrier
**or** **otherwise** has a declared partial-write recovery boundary.

## Test case

interrupt one replacement **after** its temporary carrier is prepared but **before**
the declared replacement completes.

## Acceptance criteria

pass **only** **when** the original target **or** a declared recoverable result remains
identifiable, no false completion is reported, **and** the partial state is
diagnosable from the returned context.

## Failure disposition

stop the mutation path **until** its weaker recovery boundary is explicit **or** its
atomic replacement guarantee is restored.

## Sources

- [CA-M-409 — Bound file and subprocess effects](../05_method/CA-M-409-PROGRAMMATIC-ENG_POLICY--bound-file-and-subprocess-effects.md)
