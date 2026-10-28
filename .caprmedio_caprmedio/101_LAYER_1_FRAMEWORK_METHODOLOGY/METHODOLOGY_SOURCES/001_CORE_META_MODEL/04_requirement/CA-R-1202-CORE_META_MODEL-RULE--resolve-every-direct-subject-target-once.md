---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Subjects
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Relation/Type: GOVERNS'
  - 'Subject/CAPRMEDIO/Graph/Relation/Type: DEPENDS_ON'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Subjects
version: 26
updated_at: 2026-10-27 19:59:52 +0400
relations: {}
atom_id: CA-R-1202
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Resolve Every Direct Subject Target Once

## Scope

direct GOVERNS and DEPENDS_ON values in an Atom's Subjects Property.

## Claim

**every** direct GOVERNS value **and** **every** direct DEPENDS_ON value **in** an Atom's Subjects Property **must** resolve **to** **`=1`** canonical Subject Target. resolution **must not** require an intermediate Subject/Entity **or** Subject/Reference Property **or** a repeated target-kind field.

## Details
