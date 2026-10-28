---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Carrier/Directory
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
version: 29
updated_at: 2026-10-27 20:00:11 +0400
relations:
  child_of:
  - CA-R-1484
atom_id: CA-R-862
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Bind Scope Unit Places **without** Requiring Local Delivery Atoms

## Scope

non-Project Scope Units.

## Claim

**every** non-Project Scope Unit **must** have its authority place **and** Implementation Folder bound by its authoritative Project Structure declaration. concrete bindings **must not** be independently maintained **in** Delivery Atoms; applicable Delivery authority governs the representation, placement, **and** general Carrier conventions rather than repeating a unit's selected paths.

## Details
