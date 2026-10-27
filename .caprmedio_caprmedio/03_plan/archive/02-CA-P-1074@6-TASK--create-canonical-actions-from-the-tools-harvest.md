---
atom_id: CA-P-1074@6
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Content
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Subject/Domain/Node/Continuant/Atom.Subjects
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Atom.Tier
  - Subject/Graph/Relation
  - Subject/Domain/Node/Continuant/Actor
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Autonomous Confidence Threshold'
version: 6
updated_at: 2026-10-24 19:39:48 +0400
relations:
  depends_on:
  - CA-P-1073
status: Archived
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Create canonical Actions from the TOOLS harvest

the Assignee **must** realize the reusable atomic Action definitions missing from existing O authority.

## Scope

(the approved Action candidates from the full TOOLS inventory **and** their admitted canonical O owner); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((an approved Action candidate has neither reused nor new canonical authority) **or** (an Action has a useful independent subdivision that is hidden) **or** (a Tool-specific implementation detail becomes a generic procedural rule) **or** (the same Action has duplicate authoritative definitions)).

## Details

reuse existing O definitions extracted **in** earlier phases; create **only** genuinely missing Action Claims **in** the canonical owner established **in** sub-Epic 1. preserve source traceability **and** meaningful preconditions, results, **and** Actor boundaries. unresolved definitions, ownership, **or** new behavior below 99% confidence require an Operator answer.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
