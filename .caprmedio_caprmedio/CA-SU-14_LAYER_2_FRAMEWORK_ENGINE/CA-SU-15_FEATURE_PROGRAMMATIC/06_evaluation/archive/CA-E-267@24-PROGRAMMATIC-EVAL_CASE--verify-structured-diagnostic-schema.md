---
atom_id: CA-E-267
ref_id: CA-E-267@24
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
tier: 5
relations:
  evaluation_for:
  - CA-M-414
  derived_from:
  - CA-A-053
status: Archived
version: 24
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: CA-E-267@24-PROGRAMMATIC-EVAL_CASE--verify-structured-diagnostic-schema.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
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

evaluate one emitted diagnostic record for a declared component event.

#### Acceptance criteria

pass **only** **when** the record uses ERROR, WARNING, INFO, **or** DEBUG, includes its
declared actionable contextual fields, **and** does **not** repurpose Journal history
as an operational diagnostic.

#### Failure disposition

reject the diagnostic path **until** its schema **and** severity are corrected.

#### Sources

- [CA-M-414 — Emit structured operational diagnostics](../05_method/CA-M-414-PROGRAMMATIC-ENG_POLICY--emit-structured-operational-diagnostics.md)
