---
atom_id: CA-E-364
ref_id: CA-E-364@23
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Static
    Analysis/Python Code
tier: 6
relations:
  evaluation_for:
  - CA-M-419
  - CA-E-539
  derived_from:
  - CA-A-053
status: Archived
version: 23
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
    name: CA-E-364@23-PROGRAMMATIC-EVAL_CASE--reject-a-medium-unit-with-multiple-jobs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
---
## Summary

Reject a medium unit with multiple jobs

## Claim

### Prose Claim

#### Claim checked

one changed executable unit between 26 **and** 40 logical lines performs **=1** coherent job.

#### Test case

evaluate one 30-line changed function whose accurate name **and** branches reveal
two independently reusable responsibilities.

#### Acceptance criteria

pass **only** **when** the unit is rejected **until** the two responsibilities are split.

#### Failure disposition

block the unit from claiming the 26-to-40-line allowance.

#### Sources

- [CA-M-419 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-419-PROGRAMMATIC-ENG_POLICY--ratchet-hand-authored-python-source-boundaries.md)
