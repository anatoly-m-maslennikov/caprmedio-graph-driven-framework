---
atom_id: CA-E-357
ref_id: CA-E-357@22
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
tier: 5
relations:
  evaluation_for:
  - CA-M-408
  derived_from:
  - CA-A-053
status: Archived
version: 22
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
    name: CA-E-357@22-PROGRAMMATIC-EVAL_CASE--reject-an-object-without-persistent-ownership.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
---
## Summary

Reject an object without persistent ownership

## Claim

### Prose Claim

#### Claim checked

one PROGRAMMATIC object is admitted **only** **when** it requires identity across calls
**and** owns state, an invariant, a resource, a lifecycle, **or** a replaceable
adapter.

#### Test case

evaluate one changed object that **only** wraps a bounded one-shot effect **and** owns
no responsibility across calls.

#### Acceptance criteria

pass **only** **when** the object is rejected **and** the effect is allocated **to** a
specifically named bounded function.

#### Failure disposition

reject the object **until** persistent ownership is demonstrated **or** the wrapper is
replaced by a function.

#### Sources

- [CA-M-408 — Allocate owned state and lifecycle to objects](../05_method/CA-M-408-PROGRAMMATIC-ENG_POLICY--allocate-owned-state-and-lifecycle-to-objects.md)
