---
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Engineering/Carrier
  - Subject/Engineering/Implementation Folder
version: 12
updated_at: 2026-10-24 01:37:42 +0400
relations:
  relates_to:
  - CA-R-862
  - CA-R-1485
  - CA-D-297
  - CA-D-299
  - CA-D-442
atom_id: CA-D-445@12
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Eng Decision
---
# Summary

Admit explicit Scope Unit Carrier bindings

## Scope

explicit Scope Unit authority and Implementation Folder bindings in Project Structure.

## Claim

an explicit Scope Unit authority **or** Implementation Folder binding **in** Project Structure **may** select a native directory layout instead of the default Scope Unit directory convention. the binding **must** remain unambiguous, inside authorized path boundaries, distinct from another unit's exact authority binding, **and** explicit about its owning unit. a selected native layout **must not** change declared parentage, derived ancestry/path, Type, Local Order, **or** Name merely because its path has different nesting **or** numeric tokens. ordinary physical containment remains observable **without** becoming a second declaration of structural parentage.

## Details
