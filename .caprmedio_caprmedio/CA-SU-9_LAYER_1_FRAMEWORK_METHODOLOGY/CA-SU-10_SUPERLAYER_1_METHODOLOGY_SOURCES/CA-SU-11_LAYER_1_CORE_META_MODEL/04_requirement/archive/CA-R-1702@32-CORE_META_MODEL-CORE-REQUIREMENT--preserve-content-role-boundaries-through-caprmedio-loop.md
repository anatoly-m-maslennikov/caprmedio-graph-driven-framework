---
subjects:
  governs: semantics
  depends_on:
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Implementation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Actor
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Subject/Graph/Relation
version: 32
updated_at: 2026-10-24 00:38:25 +0400
relations:
  child_of:
  - CA-M-001
atom_id: CA-R-1702@32
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary

Preserve content role boundaries through CAPRMEDIO loop

## Scope

transitions through the CAPRMEDIO loop across Content Roles.

## Claim

**every** transition through Concern, Analysis, Plan, Requirement, Method, Evaluation, Delivery, Implementation, **and** Operations produces **or** updates the meaning owned by the receiving Content Role **without** converting the source meaning into that role **or** implying completion of a later role.

**in** particular:

- Analysis owns findings, alternatives, explanation, **and** rationale;
- Plan states intended work **without** realizing it; decomposition relates independent Plan Atoms **without** merging their Claims;
- Requirement establishes model definitions, required properties, outcomes, **or** boundaries **without** selecting their Method;
- Method provides authorship, construction, **and** Implementation conventions, Evaluation checks correctness, **and** Delivery specifies Carrier contents **and** boundaries;
- Implementation materially realizes accepted Spec Claims **and** **may** contain procedural code, but does **not** prove Evaluation **or** operational success; **and**
- Operations owns specific reusable Action, Workflow, **and** Actor participation/authorization behavior under CA-R-1530; actual executions **and** their Journal Records carrying execution evidence **and** state changes are distinct from those definitions **and** from RMED Spec.

Relations carry meaning between roles while **every** related Artifact retains its own identity, authority, lifecycle, **and** owning role.

## Details
