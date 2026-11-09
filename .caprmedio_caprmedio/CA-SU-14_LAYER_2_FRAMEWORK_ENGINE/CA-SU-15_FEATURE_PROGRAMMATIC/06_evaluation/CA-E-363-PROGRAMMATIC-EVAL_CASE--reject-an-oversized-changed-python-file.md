---
atom_id: CA-E-363
ref_id: CA-E-363
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Static Analysis/Python Code"
tier: 6
relations:
  evaluation_for:
  - CA-M-419
  - CA-E-539
  derived_from:
  - CA-A-053
status: Active
version: 22
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
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

- [CA-M-419 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-419-PROGRAMMATIC-ENG_POLICY--ratchet-hand-authored-python-source-boundaries.md)
