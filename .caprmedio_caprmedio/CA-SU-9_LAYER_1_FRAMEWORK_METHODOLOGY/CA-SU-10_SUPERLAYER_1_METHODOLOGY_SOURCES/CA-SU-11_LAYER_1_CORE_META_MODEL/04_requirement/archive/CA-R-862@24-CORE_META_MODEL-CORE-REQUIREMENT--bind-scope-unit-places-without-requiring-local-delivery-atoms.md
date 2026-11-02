---
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Engineering/Implementation Folder
  - Subject/Engineering/Carrier
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
version: 24
updated_at: 2026-10-24 02:14:24 +0400
relations:
  child_of:
  - CA-R-1484
atom_id: CA-R-862@24
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
