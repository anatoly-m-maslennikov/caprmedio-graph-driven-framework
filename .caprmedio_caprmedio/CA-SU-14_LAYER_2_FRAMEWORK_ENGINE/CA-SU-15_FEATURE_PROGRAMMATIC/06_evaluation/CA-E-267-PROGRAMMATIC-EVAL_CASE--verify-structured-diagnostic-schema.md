---
atom_id: CA-E-267
ref_id: CA-E-267
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
tier: 5
relations:
  evaluation_for:
  - CA-M-414
  - CA-R-1095
  DERIVED_FROM:
  - CA-A-053
status: Active
version: 25
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
    name: CA-E-267-PROGRAMMATIC-EVAL_CASE--verify-structured-diagnostic-schema.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Verify structured diagnostic schema

## Claim



### Prose Claim
#### Claim checked

one PROGRAMMATIC operational diagnostic uses an admitted severity **and** provides
the actionable contextual fields required by its declared schema.

#### Applicable conditions

apply **when** a component emits a diagnostic for normal operation, degraded
operation, failure, recovery, **or** diagnostic detail.

#### Test case

evaluate one emitted diagnostic record for a declared component event. Also run a bounded scan that isolates a schema-invalid Atom and continues with a warning.

#### Acceptance criteria

pass **only** **when** the record uses ERROR, WARNING, INFO, **or** DEBUG, includes its
declared actionable contextual fields, **and** does **not** repurpose Journal history
as an operational diagnostic. For the bounded scan, require a structured warning with the validated Project prefix, repository-relative path and reason, and an operation response with `complete: false`; verify that no business action, Run or Journal record is fabricated and no historical Journal carrier is rewritten.

#### Failure disposition

reject the diagnostic path **until** its schema **and** severity are corrected.

#### Sources

- [CA-M-414 — Emit structured operational diagnostics](../05_method/CA-M-414-PROGRAMMATIC-ENG_POLICY--emit-structured-operational-diagnostics.md)
