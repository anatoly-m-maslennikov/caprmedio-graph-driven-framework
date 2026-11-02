---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Domain/Continuant/Atom.Summary
  - Subject/Graph Node/Domain/Continuant/Atom.Author
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Assignee'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Label'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Definition of Done'
  - Subject/Graph Relation
  - Subject/Graph Node/Engineering/Execution Control/Decision Confidence
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan.implementation_retry_limit'
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Carrier/File
version: 24
updated_at: 2026-10-27 06:04:45 +0400
relations:
  depends_on:
  - CA-R-1588
atom_id: CA-M-306@24
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Implementation Method
---
# Summary

Author Plan Atoms

## Scope

Plan Atoms.

## Claim

**to** author a Plan Atom, apply the common Plan authoring rules independently of Label:

1. resolve **`=1`** effective Author.
2. state **`=1`** intended work **or** outcome **in** Objective, supported by own work, directly contained Plans, **or** both under CA-R-1575.
3. resolve its Claim Target Scope Unit under CA-R-1588; keep narrower **or** composite work restrictions **in** Objective, **and** do **not** target an ancestor Scope Unit.
4. **if** it has own work, resolve **`=1`** effective Assignee **and** assign that work **to** that Assignee. retain the leaf-work bound under CA-R-1589.
5. write **`=1`** Definition of Done under CA-M-123, carried inside Details under CA-D-470; include applicable own-work and verification conditions. For a containing Plan whose Status is Done **or** Canceled, require every directly contained Plan to be Done **or** Canceled; mixed terminal statuses are allowed, and containment does **not** force a child Status to match the parent.
6. use a Label **only** for navigation; apply an authoring Subtype **only when** explicitly governed.
7. express required start dependencies with `BLOCKS`; **when** a Plan is contained by another Plan, declare `IS_CONTAINED_BY` on the child and derive `CONTAINS`; do **not** infer execution dependencies from leading numbers **or** folder placement.
8. resolve confidence **and** retry values from their applicable sources; store **only** explicitly selected overrides on this Plan.
9. keep supporting Details within Objective **and** its restrictions **without** another intended outcome. review Objective against the completed Details **and** Definition of Done; explicitly revise Objective **if** needed **and** recheck their agreement.
10. **only after** that review, derive Summary from the finalized Objective under CA-R-1418 **and** CA-R-1465. retain the established Summary across Revisions; **if** it needs changing, replace the Atom identity under CA-R-1464.

## Details
