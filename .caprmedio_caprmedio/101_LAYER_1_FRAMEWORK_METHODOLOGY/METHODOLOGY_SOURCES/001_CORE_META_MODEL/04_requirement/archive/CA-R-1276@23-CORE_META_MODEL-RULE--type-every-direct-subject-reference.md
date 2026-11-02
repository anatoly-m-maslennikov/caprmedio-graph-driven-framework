---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Subjects
  depends_on:
  - Entity/Graph Syntax > Relation
  - Entity/Graph Syntax > Relation//GOVERNS
  - Entity/Graph Syntax > Relation//DEPENDS_ON
version: 23
updated_at: 2026-10-29 07:45:26 +0400
relations: {}
atom_id: CA-R-1276@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Type Every Direct Subject Reference

## Claim scope

direct references in an Atom's Subjects Property.

## Claim

**every** direct reference **in** an Atom's Subjects Property **must** use **`=1`** Relation Kind **in** (GOVERNS, DEPENDS_ON). the relation entry supplies this kind **without** an additional kind Property on a Subject object.

## Details
