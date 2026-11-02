---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Demand"
  depends_on:
    ["Consumer Goal", "Producer Result"]
version: 20
updated_at: "2026-10-19 15:54:30 +0400"
relations:
  child_of:
    - CA-R-932
atom_id: CA-R-933@20
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary
Restrict Demand to one depended-on result

## Scope

Demand Atoms.

## Claim

**every** Demand Atom **must** constrain **`=1`** Producer result on which its Consumer's accepted Goal depends.

## Details
