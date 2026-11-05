---
atom_id: CA-E-262
ref_id: CA-E-262
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
tier: 5
relations:
  evaluation_for:
  - CA-M-404
  - CA-M-409
  derived_from:
  - CA-A-053
status: Active
version: 24
updated_at: 2026-10-27 19:59:31 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
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
