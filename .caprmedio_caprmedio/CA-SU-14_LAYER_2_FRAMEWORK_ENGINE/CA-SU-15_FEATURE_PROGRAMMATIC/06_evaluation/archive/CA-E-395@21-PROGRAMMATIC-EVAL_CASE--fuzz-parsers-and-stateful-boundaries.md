---
atom_id: CA-E-395
ref_id: CA-E-395@21
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Dynamic
    Testing
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
tier: 1
relations:
  evaluation_for:
  - CA-M-285
  derived_from:
  - CA-A-053
status: Archived
version: 21
updated_at: 2026-10-27 19:59:34 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
carrier_destination:
  file:
    name: CA-E-395@21-PROGRAMMATIC-EVAL_CASE--fuzz-parsers-and-stateful-boundaries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
---
## Summary

Fuzz parsers and stateful boundaries

## Claim

### Prose Claim

#### Claim checked

broad input **or** transition spaces preserve accepted invariants under generated
valid, invalid, **and** ordered cases.

#### Test case

run a bounded property **or** state-machine campaign against one parser **or**
lifecycle **and** inject an invariant-breaking generated sequence.

#### Acceptance criteria

pass **only** **when** the minimal failing input **or** sequence **and** seed are preserved,
the defect is accepted **or** rejected explicitly, **and** an accepted defect gains a
deterministic regression case.

#### Failure disposition

reject unreplayable generated evidence **and** keep expensive campaigns outside
synchronous Hooks.

#### Sources

- [Hypothesis stateful testing](https://hypothesis.readthedocs.io/en/latest/stateful.html)
- [CA-M-285 — Select software Evaluation techniques by failure mode](../05_method/CA-M-285-PROGRAMMATIC--select-software-evaluation-techniques-by-failure-mode.md)
