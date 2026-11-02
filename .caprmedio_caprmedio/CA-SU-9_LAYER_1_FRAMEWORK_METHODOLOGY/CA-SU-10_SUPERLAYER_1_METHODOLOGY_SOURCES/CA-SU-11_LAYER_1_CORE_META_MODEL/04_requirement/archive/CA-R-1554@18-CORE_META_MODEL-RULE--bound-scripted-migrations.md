---
subjects:
  governs: Entity/Object/Continuant/Actor/AI Agent
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - Entity/Object/Continuant/Actor/AI Agent
  - Entity/Aspect/Engineering
  - Entity/Object/Continuant/Selection
version: 18
updated_at: 2026-10-29 07:17:17 +0400
relations: {}
atom_id: CA-R-1554@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Bound Scripted Migrations

## Scope

AI Agent participation in Scripted Migrations.

## Claim

an AI Agent that performs a Scripted Migration **must** satisfy **all** of these participation conditions:

- bind the migration **to** an exact governed Target Set;
- fail **when** an expected target is absent;
- produce a reviewable change set.

these conditions constrain the AI Agent's participation; they do **not** define the migration's Steps **or** Workflow control flow **or** grant additional mutation authority.

## Details
