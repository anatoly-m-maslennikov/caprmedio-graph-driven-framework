---
cce_version: cce_1
cce_form: evaluation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
version: 24
updated_at: 2026-11-02 19:44:26 +0400
relations:
  evaluation_for:
  - CA-M-409
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-265
ref_id: CA-E-265
role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Active
author: Anatoly Maslennikov
tier: 5
form: Eval Case
container:
  scope_unit: CA-SU-15
---
# Surface one subprocess timeout

## Claim checked

one PROGRAMMATIC subprocess boundary observes **and** returns timeout completion
instead of waiting indefinitely **or** reporting a successful result.

## Applicable conditions

apply **only** **when** a component invokes a subprocess with a declared timeout.
components **without** a subprocess boundary are **not** applicable.

## Test case

invoke one declared subprocess that exceeds its declared timeout.

## Acceptance criteria

pass **only** **when** the boundary returns a typed timeout outcome with the declared
input context **and** no false success.

## Failure disposition

stop the affected operation **and** return timeout recovery **to** its owner.

## Sources

- [CA-M-409 — Bound file and subprocess effects](../05_method/CA-M-409-PROGRAMMATIC-ENG_POLICY--bound-file-and-subprocess-effects.md)
