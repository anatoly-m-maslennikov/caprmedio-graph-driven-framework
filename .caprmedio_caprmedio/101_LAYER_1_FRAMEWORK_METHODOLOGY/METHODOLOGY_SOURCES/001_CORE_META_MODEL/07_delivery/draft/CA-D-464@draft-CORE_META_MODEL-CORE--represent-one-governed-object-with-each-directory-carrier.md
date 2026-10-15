---
subjects:
  governs: "Directory Carrier"
  depends_on:
    ["Artifact", "Structural Entity", "Atom"]
version: 5
updated_at: "2026-10-15 12:06:14 +0000"
relations: {"relates_to": ["CA-D-259", "CA-D-460"]}
atom_id: "CA-D-464@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Represent One Governed Object with Each Directory Carrier

## Scope

represented Directory Carriers and their governed object Revisions.

## Claim

**every** represented Directory Carrier **must** carry **`=1`** governed object Revision: either one Structural Entity Revision **or**, **where** an applicable Delivery rule permits it, one Atom Revision; it **must not** establish a second object merely because it contains subordinate Carriers.

## Details
