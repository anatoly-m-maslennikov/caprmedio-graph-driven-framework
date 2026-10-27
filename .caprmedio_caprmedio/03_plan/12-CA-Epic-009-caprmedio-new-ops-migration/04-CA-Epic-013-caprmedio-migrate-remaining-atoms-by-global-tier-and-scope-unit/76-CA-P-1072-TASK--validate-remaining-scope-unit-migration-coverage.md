---
atom_id: CA-P-1072
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Domain/Continuant/Atom/Content Role
  - Subject/Graph Node/Domain/Continuant/Atom.Subjects
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Atom.Tier
  - Subject/Graph Relation
  - Subject/Graph Node/Domain/Continuant/Actor
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Autonomous Confidence Threshold'
version: 7
updated_at: 2026-10-25 17:32:27 +0400
relations:
  depends_on:
  - CA-P-1071
status: Active
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Validate remaining Scope Unit migration coverage

the Assignee **must** verify complete ordered coverage of the remaining selected authority.

## Scope

(the completed per-tier **and** per-Scope-Unit RMEDO migration batches **in** sub-Epic 4); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((an admitted source **or** resulting successor is unaccounted for) **or** (**any** batch is incomplete **or** skipped) **or** (a tier **or** unit ordering constraint was violated) **or** (an unintended CAP, I, history, Settings, runtime, **or** generated-source edit occurred)).

## Details

reconcile the initial inventory, approved queue changes, **and** final source mappings. verify no mandatory temporal axis survives **in** selected content **or** metadata, required relations resolve, **and** operational definitions have one authority source. preserve the TOOLS harvest source/result map; do **not** treat model migration as completed harvest.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
