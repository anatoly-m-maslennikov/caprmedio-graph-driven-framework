---
atom_id: CA-P-1075
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
  - CA-P-1074
status: Active
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Compose canonical Processes from the TOOLS harvest

the Assignee **must** realize the missing reusable Process definitions as Action sequences.

## Scope

(the approved Process candidates **and** canonical Action definitions from the TOOLS harvest); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((a Process **contains** undefined **or** duplicated Action definitions) **or** (ordering **or** required authorization/recovery behavior is lost) **or** (an execution instance **or** its log is confused with the reusable Process) **or** (unapproved control-flow behavior is introduced)).

## Details

compose by reference **to** canonical Actions **and** already existing Processes **only** **where** the admitted model permits it. preserve the actual source workflow intent **and** identify missing steps **without** inventing approval. ensure the Process can govern  persisted **and** session-**only** Tasks **and** does **not** depend on a particular Tool being the sole source of its procedure.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
