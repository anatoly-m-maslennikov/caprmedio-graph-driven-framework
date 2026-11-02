---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Engineering/External Effect Boundary
  depends_on:
  - Subject/Graph Node/Engineering/Effect Authorization
version: 21
updated_at: 2026-10-25 17:32:27 +0400
relations:
  evaluation_for:
  - CA-M-404
  - CA-M-409
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-262@21
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
tier: 5
type: Eval Case
---
# Reject file mutation with unmet precondition

## Claim checked

one PROGRAMMATIC file mutation stops **before** writing, replacing, **or** removing a
file **when** its declared target **or** precondition is invalid.

## Applicable conditions

apply **when** a component writes, replaces, **or** removes a file.

## Test case

request one file mutation with a declared precondition that does **not** hold.

## Acceptance criteria

pass **only** **when** the operation returns the precondition failure **and** leaves the
target bytes unchanged.

## Failure disposition

reject the mutation **and** preserve the existing target for diagnosis.

## Sources

- [CA-M-409 — Bound file and subprocess effects](../05_method/CA-M-409-PROGRAMMATIC-ENG_POLICY--bound-file-and-subprocess-effects.md)
