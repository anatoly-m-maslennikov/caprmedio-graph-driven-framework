---
atom_id: CA-E-437
ref_id: CA-E-437@28-draft
container:
  scope_unit: CA-SU-14
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/Type: Applicable Methodology'
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Package
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
tier: 5
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-R-1424
status: Draft
version: 28
updated_at: "2026-11-11 18:12:55 +0400"
carrier_destination:
  file:
    name: CA-E-437@28-draft-FRAMEWORK_ENGINE-POLICY--evaluate-methodology-alignment-support.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/06_evaluation/000_draft
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: FRAMEWORK_ENGINE
---
## Summary
Evaluate methodology alignment support

## Claim

### Prose Claim


the methodology alignment support Evaluation **must** return `fail` **if** the available Tools cannot assess the governed instance against the current Applicable Methodology, omit known nonconformance, cannot support an authorized repair, **or** mutate authority **without** Operator permission; a targeted check **may** use a bounded affected Scope **and** its dependencies. an unresolved finding **or** Operator-created orphan **must not** by itself establish failure of the required support capability **or** be reported as conformance.
