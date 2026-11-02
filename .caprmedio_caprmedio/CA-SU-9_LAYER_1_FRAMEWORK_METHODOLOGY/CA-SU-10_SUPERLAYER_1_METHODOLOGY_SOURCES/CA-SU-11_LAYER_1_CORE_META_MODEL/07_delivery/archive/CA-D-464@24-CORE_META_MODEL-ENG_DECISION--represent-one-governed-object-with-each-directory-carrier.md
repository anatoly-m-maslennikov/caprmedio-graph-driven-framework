---
subjects:
  governs: Entity/Carrier/Directory
  depends_on:
  - Entity/Term//Artifact
  - Entity
  - Entity/Object/Continuant/Governing Objects/Atom
version: 24
updated_at: 2026-10-30 14:41:19 +0400
relations: {}
atom_id: CA-D-464@24
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Decision
---
## Summary

Represent One Governed Object with Each Directory Carrier

## Claim scope

represented Directory Carriers and their governed object Revisions.

## Claim

**every** represented Directory Carrier **must** carry **`=1`** governed object Revision: either one Structural Entity Revision **or**, **where** an applicable Delivery rule permits it, one Atom Revision; it **must not** establish a second object merely because it contains subordinate Carriers.
