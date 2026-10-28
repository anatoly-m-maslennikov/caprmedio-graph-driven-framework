---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Subjects
  depends_on:
  - Subject/CAPRMEDIO/Graph/Relation/Type
  - 'Subject/CAPRMEDIO/Graph/Relation/Type: GOVERNS'
  - 'Subject/CAPRMEDIO/Graph/Relation/Type: DEPENDS_ON'
version: 21
updated_at: 2026-10-27 19:59:52 +0400
relations: {}
atom_id: CA-R-1276
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Type Every Direct Subject Reference

## Scope

direct references in an Atom's Subjects Property.

## Claim

**every** direct reference **in** an Atom's Subjects Property **must** use **`=1`** Relation Kind **in** (GOVERNS, DEPENDS_ON). the relation entry supplies this kind **without** an additional kind Property on a Subject object.

## Details
