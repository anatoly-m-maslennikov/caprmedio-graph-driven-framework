---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role:=Operations)/Workflow
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role:=Operations)/Action
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - 'CAPRMEDIO <+ STRUCTURE <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action//Assess Atom Update Identity'
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ Atom.Content.Summary
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/Operator
version: 25
updated_at: 2026-11-02 08:06:47 +0400
relations:
  evaluation_for:
  - CA-O-067
  - CA-M-303
  - CA-R-1432
  - CA-R-1464
  - CA-R-1520
atom_id: CA-E-491
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/06_evaluation/CA-E-491-PROJECT_CONFIGURATION-EVAL_CASE--validate-update-to-replacement-routing.md
  source_atom_id: CA-E-491
  source_atom_revision: 25
  source_sha256: 79eae8d7af7293434902e3eaef8661ebbb36646dcce563c21124b17a6c3a369b
  original_relations_sha256: 6e6d3a471477ab476cf4857eae5daac93e2ec1d8486362a6e4215397d13154e7
---
## Summary

Validate update-to-replacement routing

## Claim scope

an update Workflow's routing of CA-O-067 assessment results.

## Claim

the Evaluation **must** check that an update Workflow owns the routing of CA-O-067 assessment results under CA-M-303.

## Details

- call the assessment Action **without** a continuation binding: require a read-only classification result, **not** a selected next Step, ended Workflow Run, **or** dispatched successor.
- supply a valid identity-preserving proposal: the caller follows its declared update path **and** remaining checks rather than treating assessment as completed persistence.
- change the proposed Summary: require a replacement-required assessment **and** the caller's terminal handoff under CA-R-1520; no intermediate update is persisted.
- change a previously assessed proposal **or** its evidence **before** persistence: require reassessment **and** routing using the new result.
- leave the assessment unresolved: require the caller's declared evidence **or** escalation path rather than presumed approval.
- omit the caller's continuation binding **or** performed-effect account needed for handoff: block continuation **without** making the assessment Action invent either value.
- the ending update Run does **not** call, wait for, **or** claim completion of replacement; the executor receives the caller's complete terminal result.

check the declared graph with read-only Action fixtures. this Evaluation does **not** require execution of the replacement effect.
