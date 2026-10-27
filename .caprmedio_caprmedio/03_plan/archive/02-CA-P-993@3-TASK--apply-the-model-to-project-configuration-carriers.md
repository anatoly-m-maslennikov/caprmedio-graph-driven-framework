---
atom_id: CA-P-993@3
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on:
  - Atom/Claim
  - Atom/Content Role
  - Atom/Subjects
  - Subject/Domain/Node/Continuant/Scope Unit
  - Atom/Local Tier
  - Atom/Global Tier
  - Subject/Graph/Relation
  - Subject/Domain/Node/Continuant/Actor
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Atom/Content Role: Plan/Type: Task'
  - Autonomous Confidence Threshold
version: 3
updated_at: 2026-10-24 06:12:06 +0400
relations:
  depends_on:
  - CA-P-992
status: Archived
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Apply the model to Project Configuration carriers

the Assignee **must** apply the reconciled model **to** Project Configuration Properties **and** Relations.

## Scope

(selected RMEDO carriers **in** PROJECT_CONFIGURATION at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION`); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((a selected Carrier uses obsolete temporal **or** role/type representation) **or** (an extension-**only** configuration boundary is broken) **or** (references **or** Subject targets are lost **or** duplicated)).

## Details

perform source Carrier normalization using the passed Core Meta-Model. finalize relevant configuration registrations, **not** unrelated P work. keep project **and** framework Settings values unchanged **and** preserve exact historical versions. generated copies are **not** source edit targets.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
