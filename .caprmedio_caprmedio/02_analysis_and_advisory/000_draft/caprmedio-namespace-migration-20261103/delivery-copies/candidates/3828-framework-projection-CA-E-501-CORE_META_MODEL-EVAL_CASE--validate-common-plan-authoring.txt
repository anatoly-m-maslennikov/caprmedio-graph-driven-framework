---
subjects:
  active: 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  passive:
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Assignee'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Content.Definition of Done'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Content.Details'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Label'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Status'
  - CAPRMEDIO <+ MODEL <+ Scope Unit
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
version: 30
updated_at: 2026-11-02 18:35:20 +0400
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
atom_id: CA-E-501
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-501-CORE_META_MODEL-EVAL_CASE--validate-common-plan-authoring.md
  source_atom_id: CA-E-501
  source_atom_revision: 30
  source_sha256: fdf3a1d22f7e33834fff8a6112bef08e9f816b24f263ba1eb1e54a2538f78921
  original_relations_sha256: d74d6c67905f8978e335a96c2236f190cf7fc40fe29f88dee7d98b4bad6b5140
---
## Summary

Validate common Plan authoring

## Claim scope

Plan authoring under the common model.

## Claim

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
