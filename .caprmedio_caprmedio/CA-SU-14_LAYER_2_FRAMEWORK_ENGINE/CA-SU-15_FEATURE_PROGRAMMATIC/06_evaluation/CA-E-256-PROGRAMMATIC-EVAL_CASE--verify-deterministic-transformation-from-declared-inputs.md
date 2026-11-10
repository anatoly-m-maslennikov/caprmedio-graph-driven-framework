---
atom_id: CA-E-256
ref_id: CA-E-256
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Authoring <+ Code Authoring
tier: 5
relations:
  evaluation_for:
  - CA-M-407
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
    name: CA-E-256-PROGRAMMATIC-EVAL_CASE--verify-deterministic-transformation-from-declared-inputs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Verify deterministic transformation from declared inputs

## Claim



### Prose Claim
#### Claim checked

one declared deterministic PROGRAMMATIC transformation produces its result **and**
failure values from explicit declared inputs **without** an implicit host
observation **or** external effect.

#### Applicable conditions

apply **when** a component parses, classifies, validates, plans, projects,
formats, **or** **otherwise** transforms explicit input into a result.

#### Test case

evaluate one transformation twice with the same declared input while varying
an **otherwise** irrelevant host observation.

#### Acceptance criteria

pass **only** **when** both results **and** failure values are equivalent **and** the
transformation reports no filesystem, process, clock, environment, network,
persistence, **or** logging-export effect.

#### Failure disposition

stop treating the unit as deterministic **and** assign its missing observation **or**
effect boundary **to** the appropriate owner.

#### Sources

- [CA-M-407 — Allocate deterministic transformations to functions](../05_method/CA-M-407-PROGRAMMATIC-ENG_POLICY--allocate-deterministic-transformations-to-functions.md)
