---
subjects:
  governs: Entity/Carrier/File.Filename.Scope Unit Token
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Name
  - Entity/Object/Continuant/Structural Unit/Scope Unit//PROJECT_CONFIGURATION
version: 26
updated_at: 2026-10-29 07:45:30 +0400
relations: {}
atom_id: CA-D-302@26
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary
Serialize Scope Unit References as Filename Tokens

## Claim scope
Scope Unit references serialized **in** Atom filenames.

## Claim

**every** Scope Unit reference serialized **in** an Atom filename **must** use **`=1`** stable uppercase token selected from its Scope Unit Name by Project Configuration.

## Details
