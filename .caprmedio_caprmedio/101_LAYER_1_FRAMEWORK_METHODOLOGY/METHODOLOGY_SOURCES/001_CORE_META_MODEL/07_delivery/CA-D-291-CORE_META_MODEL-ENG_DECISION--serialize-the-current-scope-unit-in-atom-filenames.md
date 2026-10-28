---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Local Scope Unit
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Local Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
version: 27
updated_at: 2026-10-27 19:59:23 +0400
relations: {}
atom_id: CA-D-291
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize the Current Scope Unit in Atom Filenames

## Scope

Project-owned Atom filenames for Carriers contained **in** Scope Units.

## Claim

**every** Project-owned Atom filename **must** serialize the Scope Unit that **contains** its authoritative Carrier **`=1`** time **and** **must** omit that segment **if** the Carrier is **in** the Project Scope Unit.

## Details
