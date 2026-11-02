---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Method/Python Style Checks
  depends_on:
  - Method/Isolated Python Execution
  - Method/Source Unit Responsibility
version: 12
updated_at: "2026-10-22 12:45:09 +0400"
relations:
  evaluation_for:
    - CA-M-419
    - CA-M-420
    - CA-E-539
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-365@12
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Archived
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

- [CA-M-419 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-419-PROGRAMMATIC-STANDARD-IMPLEMENTATION_METHOD--ratchet-hand-authored-python-source-boundaries.md)
- [CA-M-420 — Ratchet typing and automation adoption](../05_method/CA-M-420-PROGRAMMATIC-STANDARD-IMPLEMENTATION_METHOD--ratchet-typing-and-automation-adoption.md)
