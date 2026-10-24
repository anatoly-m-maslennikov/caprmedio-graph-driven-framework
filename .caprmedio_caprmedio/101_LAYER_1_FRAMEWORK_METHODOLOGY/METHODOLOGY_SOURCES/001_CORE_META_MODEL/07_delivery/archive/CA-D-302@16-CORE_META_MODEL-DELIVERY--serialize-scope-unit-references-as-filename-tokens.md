---
subjects:
  governs: "Atom Carrier.Filename.Scope Unit Token"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit.Name", "Project Configuration"]
version: 16
updated_at: "2026-10-19 15:55:26 +0400"
relations: {}
atom_id: CA-D-302@16
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary
Serialize Scope Unit References as Filename Tokens

## Scope
Scope Unit references serialized **in** Atom filenames.

## Claim

**every** Scope Unit reference serialized **in** an Atom filename **must** use **`=1`** stable uppercase token selected from its Scope Unit Name by Project Configuration.

## Details
