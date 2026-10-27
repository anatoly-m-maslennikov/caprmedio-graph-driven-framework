---
atom_id: CA-P-988
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
  - CA-P-987
status: Active
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Validate New Ops model authority

the Assignee **must** verify closure of the new Operations model content.

## Scope

(the reconciled selected RMEDO authority **in** CORE_META_MODEL **and** PROJECT_CONFIGURATION); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((one required definition **or** relation is missing **or** contradictory) **or** (the accepted Action, Process, Actor, ephemeral Task, Tool, **or** Journal example cannot be classified coherently) **or** (a fully **or** partially migrated Claim is lost **or** duplicated) **or** (a later carrier-migration prerequisite remains undefined)).

## Details

test simple Action composition, reuse across two Processes, two executions with different outcomes, an ephemeral Task, an unauthorized Actor, **and** a Tool supporting **only** part of a Process. validate semantics **and** source mappings; do **not** claim executable conformance. record exactly which frontmatter fields remain deliberately pending **until** sub-Epic 3.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
