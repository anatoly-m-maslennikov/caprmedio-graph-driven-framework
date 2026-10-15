---
subjects:
  governs: "Atom Carrier.Filename.Owning Scope Unit"
  depends_on:
    ["Atom Scope", "Scope Unit"]
version: 16
updated_at: "2026-10-15 12:04:57 +0000"
relations: {}
atom_id: "CA-D-291@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize the Current Scope Unit in Atom Filenames

## Scope

Project-owned Atom filenames for Carriers contained **in** Scope Units.

## Claim

**every** Project-owned Atom filename **must** serialize the Scope Unit that **contains** its authoritative Carrier **`=1`** time **and** **must** omit that segment **if** the Carrier is **in** the Project Scope Unit.

## Details
