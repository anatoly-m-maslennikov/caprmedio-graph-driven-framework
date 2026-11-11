---
atom_id: CA-E-501
ref_id: CA-E-501
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)/(.Header.Context.Form := Plan)'
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)/(.Header.Context.Form := Plan)'
  - CAPRMEDIO_MODEL <+ Atom.Content
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Assignee'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Content.Definition of Done'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Content.Details'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.Context.Label'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.State.Status'
  - CAPRMEDIO_MODEL <+ Scope Unit
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Decision Confidence"
tier: 4
relations:
  evaluation_for:
  - CA-R-1574@21
  - CA-R-1575
  - CA-R-1576@21
  - CA-R-1577
  - CA-R-1581@23
  - CA-R-1599
  - CA-R-1583@26
  - CA-R-1584
  - CA-R-1587
  - CA-R-1588
  - CA-R-1589
  - CA-M-306
  - CA-D-470
status: Active
version: 30
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-E-501-CORE_META_MODEL-EVAL_CASE--validate-common-plan-authoring.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Validate common Plan authoring

## Claim

### Prose Claim


Plan authoring under the common model.


the Plan authoring Evaluation **must** reject **any** Plan that violates the common model.

## Details

### cases

- accept a standalone file-backed Plan, a file-backed Hub with contained work **and** an optional directory, **and** a Plan with both own work **and** contained children. reject a folder-only Plan.
- reject a Summary-only Plan with no own work **and** no contained Plan; do **not** treat an empty containment set as completion.
- require **`=1`** intended work **or** outcome Claim **in** Objective **and** **=1** effective Author; require **`=1`** effective Assignee for own work, but **not** for a Plan with no own work and contained children.
- require **`=1`** observable, decidable Definition of Done under `### Definition of Done` inside Details **in** **every** Plan Markdown file, including a Plan with contained children. reject its absence.
- accept an atomic **or** explicitly grouped composite falsification expression; reject ambiguity **or** Details that introduce independent work **or** another completion claim.
- for a containing Plan Atom, admit Status Done **or** Canceled only **when** every directly contained Plan is Done **or** Canceled; mixed terminal statuses are allowed, and a child Status need not match the parent. Preserve the separate own-work and Definition-of-Done conditions for Done; do **not** treat Archived contained Plan work as a valid terminal child.
- change **only** the Label among Version, Objective, Epic, Task, **and** Subtask: authoring admission **and** completion **must** remain unchanged. reject treating those Labels as authoring Subtypes.
- select the owning Scope Unit as the default Claim Target Scope Unit during authoring regardless of Plan containment, **and** require the resolved value inside the Atom; preserve a permitted different target **and** narrower Claim restrictions. reject an ancestor target **or** **any** Hub substituted as a Scope Unit target.
- accept inherited confidence values **without** copied overrides; reject an unresolved effective value **before** autonomous execution.

report the exact Plan identity **and** failed rule; a Label **must not** waive the failure.
