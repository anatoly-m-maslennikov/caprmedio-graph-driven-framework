---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - Entity/Carrier/Directory
  - Entity/Carrier
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery'
version: 32
updated_at: 2026-10-29 10:13:49 +0400
relations:
  child_of:
  - CA-R-1484
atom_id: CA-R-862@32
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
## Summary

Bind Scope Unit Places **without** Requiring Local Delivery Atoms

## Claim scope

non-Project Scope Units.

## Claim

**every** non-Project Scope Unit **must** have its authority place **and** Implementation Folder bound by its authoritative Project Structure declaration. concrete bindings **must not** be independently maintained **in** Delivery Atoms; applicable Delivery authority governs the representation, placement, **and** general Carrier conventions rather than repeating a unit's selected paths.
