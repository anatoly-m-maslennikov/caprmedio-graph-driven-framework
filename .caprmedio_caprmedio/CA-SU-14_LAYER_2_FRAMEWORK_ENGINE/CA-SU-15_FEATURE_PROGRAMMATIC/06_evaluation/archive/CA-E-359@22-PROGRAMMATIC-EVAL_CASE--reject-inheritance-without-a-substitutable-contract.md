---
atom_id: CA-E-359
ref_id: CA-E-359@22
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Code
    Authoring
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
    name: CA-E-359@22-PROGRAMMATIC-EVAL_CASE--reject-inheritance-without-a-substitutable-contract.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
---
## Summary

Reject inheritance without a substitutable contract

## Claim

### Prose Claim

#### Claim checked

one PROGRAMMATIC inheritance relationship exists **only** for a stable
substitutable subtype contract.

#### Test case

evaluate one changed subclass that inherits behavior for code reuse but cannot
replace its base under the base contract.

#### Acceptance criteria

pass **only** **when** the inheritance is rejected **and** the behavior is expressed by a
function, module, **or** composed collaborator.

#### Failure disposition

reject the subtype boundary **until** substitutability is demonstrated **or**
inheritance is removed.

#### Sources

- [CA-M-408 — Allocate owned state and lifecycle to objects](../05_method/CA-M-408-PROGRAMMATIC-ENG_POLICY--allocate-owned-state-and-lifecycle-to-objects.md)
