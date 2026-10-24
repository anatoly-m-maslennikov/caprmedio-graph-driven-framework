---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Source Unit Responsibility
  depends_on: []
version: 16
updated_at: 2026-10-24 01:28:26 +0400
relations:
  evaluation_for:
  - CA-M-419
  - CA-E-539
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-266@16
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eval Case
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

- [CA-M-419 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-419-PROGRAMMATIC-STANDARD-ENG_POLICY--ratchet-hand-authored-python-source-boundaries.md)
