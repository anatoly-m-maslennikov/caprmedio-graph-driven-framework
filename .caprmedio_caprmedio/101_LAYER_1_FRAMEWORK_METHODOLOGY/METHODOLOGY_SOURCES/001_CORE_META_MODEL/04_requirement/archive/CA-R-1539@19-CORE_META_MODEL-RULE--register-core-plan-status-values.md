---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Status'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  - Entity/Object/Continuant/Governing Objects/Atom.Status
version: 19
updated_at: 2026-10-29 07:17:17 +0400
relations: {}
atom_id: CA-R-1539@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Register Core Plan Status Values

## Scope

Core Plan Status values.

## Claim

the Core Plan Status model **must** inherit the allowed values of Atom.Status and add (Backlog, Done, Canceled). Planned **must not** be a distinct Plan Status.

## Details
