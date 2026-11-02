---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
  depends_on:
  - Subject/Graph/Relation/Type
  - 'Subject/Graph/Relation/Type: GOVERNS'
  - 'Subject/Graph/Relation/Type: DEPENDS_ON'
version: 19
updated_at: 2026-10-24 12:35:51 +0400
relations: {}
atom_id: CA-R-1276@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
