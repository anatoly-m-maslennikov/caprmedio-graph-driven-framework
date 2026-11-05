---
atom_id: CA-E-370
ref_id: CA-E-370
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - Subject/CAPRMEDIO/Carrier
tier: 5
relations:
  evaluation_for:
  - CA-M-414
  derived_from:
  - CA-A-053
status: Active
version: 22
updated_at: 2026-10-27 19:59:33 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Verify logging lifecycle materialization

## Claim checked

one production-relevant PROGRAMMATIC component materializes the active Logging
Policy's sink, retention, access, sampling, rotation, size, back-pressure,
unavailable-sink, **and** disk-pressure boundaries.

## Test case

evaluate one production-relevant component whose logging materialization omits
its unavailable-sink behavior.

## Acceptance criteria

pass **only** **when** deployment is rejected **until** the missing behavior is declared
**without** configuration, Implementation, **or** Delivery claiming policy authority.

## Failure disposition

block the production logging path **until** its lifecycle materialization is
complete.

## Sources

- [CA-M-414 — Emit structured operational diagnostics](../05_method/CA-M-414-PROGRAMMATIC-ENG_POLICY--emit-structured-operational-diagnostics.md)
