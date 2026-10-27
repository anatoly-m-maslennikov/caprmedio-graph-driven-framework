---
atom_id: CA-P-996
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
  - CA-P-995
status: Active
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Validate source Carrier migration closure

the Assignee **must** verify lossless source-level model application.

## Scope

(the selected source carriers covered by sub-Epics 1 through 3); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((an input lacks a retained, replaced, split, moved, **or** archived-successor disposition) **or** (an active duplicate authority **or** dangling **in**-scope reference remains) **or** (source content **and** metadata disagree) **or** (a deliberately deferred generated output is presented as current **or** validated)).

## Details

check source identities, versions, Carrier paths, Subjects, Relations, Type registrations, **and** scoped schema validation. **if** a validator **or** compiler cannot handle the new model, record the exact unsupported capability **and** request separate implementation authority; do **not** change I under this RMEDO Epic. historical **and** generated carriers are **not** rewritten. no installed Tool **or** runtime conformance claim follows from source validation.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
