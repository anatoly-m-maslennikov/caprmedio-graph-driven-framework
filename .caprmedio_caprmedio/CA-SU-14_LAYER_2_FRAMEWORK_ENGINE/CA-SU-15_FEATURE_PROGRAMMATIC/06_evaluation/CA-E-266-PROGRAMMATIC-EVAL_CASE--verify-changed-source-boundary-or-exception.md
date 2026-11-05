---
atom_id: CA-E-266
ref_id: CA-E-266
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Static Analysis/Python
    Code
tier: 6
relations:
  evaluation_for:
  - CA-M-419
  - CA-E-539
  derived_from:
  - CA-A-053
status: Active
version: 24
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Verify changed source boundary or exception

## Claim checked

one changed hand-authored PROGRAMMATIC Python executable unit above 40 logical
lines has one specific bounded exception that preserves a single
responsibility.

## Applicable conditions

apply **to** a new **or** materially changed hand-authored Python file. generated
Runtime **and** Delivery outputs are **not** applicable.

## Test case

evaluate one changed executable unit exceeding 40 logical lines **without** a
documented exception.

## Acceptance criteria

pass **only** **when** the unit is rejected **until** it is split, reduced, **or** supplied
with one exception recording its measured size, reason, bounded scope, single
responsibility, **and** condition for reconsideration.

## Failure disposition

block the changed source from claiming source-boundary conformance.

## Sources

- [CA-M-419 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-419-PROGRAMMATIC-ENG_POLICY--ratchet-hand-authored-python-source-boundaries.md)
