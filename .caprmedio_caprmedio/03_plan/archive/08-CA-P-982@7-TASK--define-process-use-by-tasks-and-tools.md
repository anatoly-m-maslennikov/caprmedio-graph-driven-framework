---
atom_id: CA-P-982@7
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
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
version: 7
updated_at: 2026-10-24 19:39:48 +0400
relations:
  depends_on:
  - CA-P-981
status: Archived
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Define process use by Tasks and Tools

the Assignee **must** establish uniform Process use by persisted **or** ephemeral Tasks **and** their executors.

## Scope

(selected RMEDO authority for Operation use **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((a session-**only** Task bypasses the applicable Process **or** authorization) **or** (a Tool is made an independent source of procedure authority) **or** (P intended work, O procedure, **and** Tool Implementation are conflated) **or** (Method conventions **and** operational Action sequences have no usable boundary)).

## Details

Tasks can exist **only** **in** an Operator session; this does **not** require a persistent P Atom for **every** Task. Tools, AI Agents, **and** Operators execute **or** support the same governed Processes. TOOLS RMED specifies Implementation capabilities, interfaces, applicable Methods, Evaluations, **and** Carrier boundaries; operational procedures are defined elsewhere under O **and** referenced, **not** copied. procedural implementation code is **not** prohibited. resolve the canonical owning Scope Unit for reusable O definitions **before** extraction Tasks write them; do **not** invent a new Scope Unit **or** target folder **without** sufficient authority.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
