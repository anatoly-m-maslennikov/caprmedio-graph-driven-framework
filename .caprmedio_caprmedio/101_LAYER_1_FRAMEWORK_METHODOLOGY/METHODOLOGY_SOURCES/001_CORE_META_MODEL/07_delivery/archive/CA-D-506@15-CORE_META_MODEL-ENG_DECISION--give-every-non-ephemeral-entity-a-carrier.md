---
atom_id: CA-D-506@15
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
version: 15
updated_at: 2026-10-29 07:45:30 +0400
author: Anatoly Maslennikov
subjects:
  governs: Entity
  depends_on:
  - Entity/Carrier
  - Entity/Object/Continuant/Term//Property
relations: {}
tier: 1
type: Decision
---
## Summary

Give every non-ephemeral Entity a Carrier

## Claim scope

non-ephemeral Entities.

## Claim

**every** non-ephemeral Entity **must** have **`>=1`** Carrier through its Entity/Carrier binding.

## Details

a binding **may** use a shared Carrier **or** a location within it. a carried Property does **not** require a separate file merely because it is an Entity.
