---
atom_id: CA-M-303
ref_id: CA-M-303
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
  dependencies:
  - CAPRMEDIO_MODEL <+ Actor
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Action
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - 'CAPRMEDIO_STRUCTURE <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)//Assess Atom Update Identity'
tier: 3
status: Active
version: 26
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-M-303-CORE_META_MODEL-IMPLEMENTATION_METHOD--declare-update-routing-in-the-calling-workflow.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-303-CORE_META_MODEL-IMPLEMENTATION_METHOD--declare-update-routing-in-the-calling-workflow.md
  source_atom_id: CA-M-303
  source_atom_revision: 26
  source_sha256: 0a40372f43b6ae62265ab81b89dd2f1c58af911421cb1d1a553f61a17d904cd1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare update routing **in** the calling Workflow

## Claim

### Prose Claim


Atom update routing for a calling Workflow.


**to** author an Atom update Workflow, declare its response **to** identity assessment **in** the Workflow graph rather than **in** the assessment Action **or** executor code.

- reference CA-O-067-CORE_META_MODEL-ACTION--assess-atom-update-identity for the assessment; bind the target Revision, proposed result, applicable authority, **and** evidence **to** that Step. the Action returns its assessment **without** selecting the caller's next Step **or** continuation Workflow.
- map identity-preserving results **to** the caller's declared update path **and** remaining authorization **and** checks; the assessment alone does **not** perform the update.
- map replacement-required results **to** a terminal handoff under CA-R-1520-CORE_META_MODEL-RULE--return-workflow-handoffs-through-terminal-results. keep the admitted replacement-continuation binding **in** the Workflow definition, **not** as an assessment Action input. the ending Run does **not** call **or** wait for replacement **or** persist an intermediate update merely **to** replace it.
- map unresolved results **to** the caller's declared evidence-gathering **or** escalation path; an unresolved result **must not** be treated as approval.
- include reassessment **when** the proposal changes **or** its evidence becomes stale **before** persistence. a changed Summary remains a replacement under CA-R-1464-CORE_META_MODEL-REQUIREMENT--keep-summary-fixed-for-atom-identity even **when** the request began as an update.

this Method constrains how an Author expresses the caller's graph. it is **not** another Workflow, executable routing service, **or** requirement **to** build the executor through a particular Workflow.
