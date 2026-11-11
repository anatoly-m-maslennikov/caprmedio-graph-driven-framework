---
atom_id: CA-R-1702
ref_id: CA-R-1702
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
  - CAPRMEDIO_MODEL <+ Package/Project Package
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Operations)/Action
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Operations)/Workflow
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Workflow) >{1+} Atom/(.Header.Context.Role :=
    Operations)/(.Header.Context.Form := Step)
  - CAPRMEDIO_MODEL <+ Actor
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
relations:
  child_of:
  - CA-M-539
status: Active
version: 51
updated_at: "2026-11-11 18:46:16 +0400"
carrier_destination:
  file:
    name: CA-R-1702-CORE_META_MODEL-RULE--preserve-content-role-boundaries-through-caprmedio-loop.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Preserve content role boundaries through CAPRMEDIO loop

## Claim

### Prose Claim


transitions through the CAPRMEDIO loop across Content Roles.


**every** transition through Concern, Analysis & Advisory, Plan, Requirement, Method, Evaluation, Delivery, Implementation, **and** Operations produces **or** updates the meaning owned by the receiving Content Role **without** converting the source meaning into that role **or** implying completion of a later role.

**in** particular:

- Analysis & Advisory owns findings, alternatives, explanation, **and** rationale;
- Plan states intended work **without** realizing it; decomposition relates independent Plan Atoms **without** merging their Claims;
- Requirement establishes model definitions, required properties, outcomes, **or** boundaries **without** selecting their Method;
- Method provides authorship, construction, **and** Implementation conventions, Evaluation checks correctness, **and** Delivery specifies Carrier contents **and** boundaries;
- Implementation materially realizes accepted Spec Claims **and** **may** contain procedural code, but does **not** prove Evaluation **or** operational success; **and**
- Operations owns specific reusable Action behavior, Workflow graph, **and** Step invocation binding; Actor participation **and** authorization remain Requirement rules. actual executions **and** their Journal Records carrying execution evidence **and** state changes are distinct from those definitions **and** from RMED Spec.

Relations carry meaning between roles while **every** related Artifact retains its own identity, authority, lifecycle, **and** owning role.
