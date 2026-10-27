---
atom_id: CA-P-997
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
  - CA-P-996
status: Active
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Confirm the tier and Scope Unit execution queue

the Assignee **must** confirm an exhaustive ordered queue of one Global Tier **and** one current Scope Unit per migration Task.

## Scope

(the remaining selected project RMEDO Atoms outside the completed project-root **and** Methodology Sources batches); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((an admitted batch has no Task) **or** (Tasks are ordered by navigation number instead of resolved Global Tier) **or** (two Tasks own the same batch **or** a Task spans multiple current Scope Units) **or** (an earlier incomplete tier is bypassed)).

## Details

recompute from current sources at execution time, using active model authority rather than counts captured during plan creation. queue tiers ascending; within a tier use stable current-Scope-Unit order. inventory  directly owned **and** relational Atoms by their owning Carrier exactly once; Claim targets are preserved, **not** used **to** duplicate the work. Core Meta-Model, Project Configuration, Methodology Sources parent, **and** project root are excluded because prior phases own them. installed Extension sources are empty at planning time; **if** newly admitted authority exists, insert its own scoped Tasks **before** proceeding. detect untyped/ambiguous source locations **and** ask rather than dropping them.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
