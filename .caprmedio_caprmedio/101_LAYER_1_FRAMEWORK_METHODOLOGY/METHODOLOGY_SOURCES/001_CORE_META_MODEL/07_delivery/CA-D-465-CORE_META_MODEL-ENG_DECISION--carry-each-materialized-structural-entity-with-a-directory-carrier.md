---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node
  - Subject/CAPRMEDIO/Carrier/Directory
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
version: 19
updated_at: 2026-10-27 19:59:25 +0400
relations:
  delivery_for:
  - CA-R-1484
atom_id: CA-D-465
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Carry Each Materialized Structural Entity with a Directory Carrier

## Scope

materialized Structural Entities and Scope Units established by Project Structure.

## Claim

**every** materialized Structural Entity **must** be carried by **`>=1`** Directory Carrier; a Scope Unit established by Project Structure **may** remain unmaterialized under CA-R-1484-CORE_META_MODEL-RULE--establish-scope-units-through-project-structure-declarations without losing its declaration **or** identity.

## Details
