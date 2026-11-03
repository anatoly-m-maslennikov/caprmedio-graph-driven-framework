---
subjects:
  active: Atom.Role
  passive:
  - Atom.Role
  - Package/Implementation
  - Atom/(.Role:=Operations)/Action
  - Atom/(.Role:=Operations)/Workflow
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type:
    Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type:
    Step'
  - Actor
  - Entity/Object/Continuant/History/Journal > Event Record
  - CFEL <+ Relation
version: 49
updated_at: 2026-11-02 15:49:28 +0400
relations:
  child_of:
  - CA-M-447
atom_id: CA-R-1702
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1702-CORE_META_MODEL-RULE--preserve-content-role-boundaries-through-caprmedio-loop.md
  source_atom_id: CA-R-1702
  source_atom_revision: 49
  source_sha256: e8c98e31652d9c10bcaaac0d70bc50916209481820ea4fdfef2845f71efb9041
  original_relations_sha256: cda81380ab057c4da428dab72b93f65bb72092983ee69756870fff6e5dc9bea9
---
## Summary

Preserve content role boundaries through CAPRMEDIO loop

## Claim scope

transitions through the CAPRMEDIO loop across Content Roles.

## Claim

**every** transition through Concern, Analysis & Advisory, Plan, Requirement, Method, Evaluation, Delivery, Implementation, **and** Operations produces **or** updates the meaning owned by the receiving Content Role **without** converting the source meaning into that role **or** implying completion of a later role.

**in** particular:

- Analysis & Advisory owns findings, alternatives, explanation, **and** rationale;
- Plan states intended work **without** realizing it; decomposition relates independent Plan Atoms **without** merging their Claims;
- Requirement establishes model definitions, required properties, outcomes, **or** boundaries **without** selecting their Method;
- Method provides authorship, construction, **and** Implementation conventions, Evaluation checks correctness, **and** Delivery specifies Carrier contents **and** boundaries;
- Implementation materially realizes accepted Spec Claims **and** **may** contain procedural code, but does **not** prove Evaluation **or** operational success; **and**
- Operations owns specific reusable Action behavior, Workflow graph, **and** Step invocation binding; Actor participation **and** authorization remain Requirement rules. actual executions **and** their Journal Records carrying execution evidence **and** state changes are distinct from those definitions **and** from RMED Spec.

Relations carry meaning between roles while **every** related Artifact retains its own identity, authority, lifecycle, **and** owning role.
