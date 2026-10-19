---
subjects:
  governs: "Entity/Node/Continuant/Scope Unit.Navigational Order Number"
  depends_on:
    ["Entity/Carrier", "Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Project.Structure"]
version: 10
updated_at: "2026-10-19 11:46:34 +0000"
relations: {}
atom_id: "CA-D-380@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Navigational Order Numbers

## Scope

Carrier renderings of a Navigational Order Number.

## Claim

**every** Carrier rendering of a Navigational Order Number **must** use decimal digits. the default directory-name rendering of a non-Project Scope Unit **must** use **`>=2`** digits; a typed TOML integer stores the numeric value **without** leading-zero padding.

## Details
