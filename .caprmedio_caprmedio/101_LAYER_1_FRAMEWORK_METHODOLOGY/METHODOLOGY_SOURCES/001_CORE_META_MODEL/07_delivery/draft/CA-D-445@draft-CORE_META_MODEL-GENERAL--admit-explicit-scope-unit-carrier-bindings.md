---
subjects:
  governs: "Entity/Node/Continuant/Scope Unit"
  depends_on:
    ["Entity/Node/Continuant/Project.Structure", "Entity/Carrier", "Implementation Folder"]
version: 7
updated_at: "2026-10-19 11:46:57 +0000"
relations:
  relates_to:
    - "CA-R-862"
    - "CA-R-1485"
    - "CA-D-297"
    - "CA-D-299"
    - "CA-D-442"
atom_id: "CA-D-445@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Admit explicit Scope Unit Carrier bindings

## Scope

explicit Scope Unit authority and Implementation Folder bindings in Project Structure.

## Claim

an explicit Scope Unit authority **or** Implementation Folder binding **in** Project Structure **may** select a native directory layout instead of the default Scope Unit directory convention. the binding **must** remain unambiguous, inside authorized path boundaries, distinct from another unit's exact authority binding, **and** explicit about its owning unit. a selected native layout **must not** change declared parentage, Structural Level, Type, Local Order, **or** Name merely because its path has different nesting **or** numeric tokens. ordinary physical containment remains observable **without** becoming a second declaration of structural parentage.

## Details
