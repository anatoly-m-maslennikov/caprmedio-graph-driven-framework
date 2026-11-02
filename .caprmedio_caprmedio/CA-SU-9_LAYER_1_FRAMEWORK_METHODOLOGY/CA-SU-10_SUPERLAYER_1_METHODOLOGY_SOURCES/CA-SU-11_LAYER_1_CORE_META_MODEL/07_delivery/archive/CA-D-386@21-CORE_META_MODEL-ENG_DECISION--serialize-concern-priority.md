---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern.Priority'
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern.Priority'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
version: 21
updated_at: 2026-10-29 07:45:30 +0400
relations: {}
atom_id: CA-D-386@21
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Serialize Concern Priority

## Claim scope

Concern Atom Carriers and non-Concern Content Role Atom Carriers.

## Claim

a Concern Atom Carrier **must** serialize **`=1`** selected Priority as `priority` with the lowercase value `high`, `medium`, **or** `low`. **every** non-Concern Content Role Atom Carrier **must** omit `priority`; virtual `highest` **must not** be stored.

## Details
