---
atom_id: CA-E-365
ref_id: CA-E-365
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Static Analysis
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Static Analysis
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
tier: 6
relations:
  evaluation_for:
  - CA-M-419
  - CA-M-420
  - CA-E-539
  derived_from:
  - CA-A-053
status: Active
version: 23
updated_at: 2026-10-27 19:59:33 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Reject unchecked cyclomatic complexity

## Claim checked

**every** new **or** materially changed executable unit has a result from the admitted
cyclomatic-complexity lint **and** stays within its Evaluation-owned maximum **or** one
accepted bounded exception.

## Test case

evaluate one materially changed function for which no current complexity-lint
result exists.

## Acceptance criteria

pass **only** **when** conformance is rejected **until** **all** of the following hold:

- the admitted lint reports a value for the changed unit.
- that value satisfies the Evaluation-owned maximum **or** an accepted bounded exception covers that value.

## Failure disposition

block the changed unit from claiming source-boundary conformance.

## Sources

- [CA-M-419 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-419-PROGRAMMATIC-ENG_POLICY--ratchet-hand-authored-python-source-boundaries.md)
- [CA-M-420 — Ratchet typing and automation adoption](../05_method/CA-M-420-PROGRAMMATIC-ENG_POLICY--ratchet-typing-and-automation-adoption.md)
