---
subjects:
  governs: "Entity/Carrier/Directory Carrier"
  depends_on:
    ["Artifact", "Structural Entity", "Entity/Continuant/Object/Atom"]
version: 7
updated_at: "2026-10-17 18:06:20 +0400"
relations: {"relates_to": ["CA-R-1956", "CA-D-460"]}
atom_id: "CA-D-464"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-464-CORE_META_MODEL-CORE--represent-one-governed-object-with-each-directory-carrier.md
  source_atom_id: CA-D-464
  source_atom_revision: 7
  source_sha256: 08c063775889a4d7ffb1bacb930516067466c845944d781b0c3edabca0e43fab
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Represent One Governed Object with Each Directory Carrier

## Scope

represented Directory Carriers and their governed object Revisions.

## Claim

**every** represented Directory Carrier **must** carry **`=1`** governed object Revision: either one Structural Entity Revision **or**, **where** an applicable Delivery rule permits it, one Atom Revision; it **must not** establish a second object merely because it contains subordinate Carriers.

## Details
