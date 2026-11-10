---
atom_id: CA-E-270
ref_id: CA-E-270
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
    <+ Verification <+ Static Analysis
  dependencies:
  - MODEL//CAPRMEDIO <+ Event Record
tier: 6
relations:
  evaluation_for:
  - CA-M-420
  - CA-E-539
  - CA-E-540
  DERIVED_FROM:
  - CA-A-053
status: Active
version: 27
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
destination:
  file:
    name: CA-E-270-PROGRAMMATIC-EVAL_CASE--verify-changed-code-adoption-ratchet.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Verify changed-code adoption ratchet

## Claim



### Prose Claim
#### Claim checked

one changed **or** new PROGRAMMATIC target within an admitted automation **or** typing
capability does **not** regress below its current passing boundary.

#### Applicable conditions

apply **when** a component changes source within an admitted typing, formatting,
linting, **or** behavioral-check capability. unadmitted capability selection is
**not** applicable.

#### Test case

evaluate one changed target against its current admitted passing boundary.

#### Acceptance criteria

pass **only** **when** the target meets the current Method-owned boundary **or** has one
accepted Method-owned bounded exception. Configuration **and** Implementation **must**
materialize that selection, Delivery **must** govern its carrier, **and** Journal Records
**must** carry evidence of the actual result **without** becoming another selection authority.

#### Failure disposition

reject the ratchet claim **and** return the target **to** its change owner.

#### Sources

- [CA-M-420 — Ratchet typing and automation adoption](../05_method/CA-M-420-PROGRAMMATIC-ENG_POLICY--ratchet-typing-and-automation-adoption.md)
