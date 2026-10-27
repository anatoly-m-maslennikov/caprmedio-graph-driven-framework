---
atom_id: CA-P-981
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
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
version: 8
updated_at: 2026-10-25 17:32:27 +0400
relations:
  depends_on:
  - CA-P-980
status: Active
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Define operational Actor authority

the Assignee **must** establish Actor participation **and** permission policies under Operations.

## Scope

(selected RMEDO Actor-policy **and** O-classification authority **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((operational authorization depends on a persisted Plan existing) **or** (human Operators **and** AI Agents are conflated) **or** (AI Agents obtain original **or** self-expanded authority) **or** (foundational Actor definitions are indiscriminately moved with operational policies)).

## Details

the current project policies CA-P-032 **and** CA-P-033 remain Principle **and** CA-P-034 remains Core **when** their role is later migrated. this Task defines the model boundary; the actual three project exceptions are changed **in** the project-content **and** carrier phases. their inclusion does **not** admit other P Atoms. retain the distinction between a framework Actor model definition **and** an operational participation policy.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
