---
atom_id: CA-E-268
ref_id: CA-E-268
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
    name: CA-E-268-PROGRAMMATIC-EVAL_CASE--verify-diagnostic-secret-redaction.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Verify diagnostic secret redaction

## Claim



### Prose Claim
#### Claim checked

one PROGRAMMATIC diagnostic path sanitizes a sensitive input **before** its record
is exposed **to** the declared sink.

#### Applicable conditions

apply **when** a diagnostic path could receive sensitive **or** secret-bearing input.
paths whose declared inputs contain no such value are **not** applicable.

#### Test case

Supply one secret-bearing input **to** one declared diagnostic path.

#### Acceptance criteria

pass **only** **when** the exposed record retains the diagnostic context while omitting
**or** irreversibly redacting the secret-bearing value.

#### Failure disposition

stop the diagnostic path **and** correct its sanitization boundary **before** release.

#### Sources

- [CA-M-414 — Emit structured operational diagnostics](../05_method/CA-M-414-PROGRAMMATIC-ENG_POLICY--emit-structured-operational-diagnostics.md)
