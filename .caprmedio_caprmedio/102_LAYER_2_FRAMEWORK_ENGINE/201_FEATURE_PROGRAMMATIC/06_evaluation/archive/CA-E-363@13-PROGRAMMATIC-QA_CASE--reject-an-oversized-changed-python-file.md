---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Source Unit Responsibility
  depends_on: []
version: 13
updated_at: 2026-10-24 00:38:25 +0400
relations:
  evaluation_for:
  - CA-M-419
  - CA-E-539
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-363@13
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Reject an oversized changed Python file

## Claim checked

one new **or** materially changed hand-authored PROGRAMMATIC Python file remains at
**or** below 200 physical lines **or** has a specific bounded exception.

## Test case

evaluate one changed 201-line hand-authored Python file with no file-size
exception.

## Acceptance criteria

pass **only** **when** conformance is rejected **until** the file is reduced, split by
responsibility, **or** supplied with one accepted bounded exception.

## Failure disposition

block the changed file from claiming source-boundary conformance.

## Sources

- [CA-M-419 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-419-PROGRAMMATIC-STANDARD-ENG_POLICY--ratchet-hand-authored-python-source-boundaries.md)
