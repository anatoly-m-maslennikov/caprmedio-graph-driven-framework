---
atom_id: CA-E-436
ref_id: CA-E-436@33-draft
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Traceability"
  - CAPRMEDIO_MODEL <+ Scope Unit
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Component Structure"
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)
tier: 3
relations:
  child_of:
  - CA-E-001
status: Draft
version: 33
updated_at: "2026-11-11 18:12:55 +0400"
carrier_destination:
  file:
    name: CA-E-436@33-draft-CORE_META_MODEL-EVAL_POLICY--evaluate-graph-of-graphs-connectivity.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/000_draft
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: CORE_META_MODEL
---
## Summary
Evaluate graph-of-graphs connectivity

## Claim

### Prose Claim

Check connectivity **only** for a graph and scope where active authority requires a specific connection. Report a missing required path when no permitted path connects its endpoints. Separate graph components **must not** fail this check by themselves.
