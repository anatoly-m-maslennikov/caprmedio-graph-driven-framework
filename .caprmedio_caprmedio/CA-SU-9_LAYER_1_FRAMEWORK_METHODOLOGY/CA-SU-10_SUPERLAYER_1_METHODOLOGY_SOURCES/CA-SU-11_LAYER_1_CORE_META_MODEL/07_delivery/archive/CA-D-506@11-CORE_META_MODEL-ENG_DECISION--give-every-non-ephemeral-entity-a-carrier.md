---
atom_id: CA-D-506@11
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
version: 11
updated_at: 2026-10-25 17:32:27 +0400
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Node
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Domain/Continuant/Term//Property
relations: {}
tier: 1
type: Eng Decision
---
# Summary

Give every non-ephemeral Entity a Carrier

## Scope

non-ephemeral Entities.

## Claim

**every** non-ephemeral Entity **must** have **`>=1`** Carrier through its Entity/Carrier binding.

## Details

a binding **may** use a shared Carrier **or** a location within it. a carried Property does **not** require a separate file merely because it is an Entity.
