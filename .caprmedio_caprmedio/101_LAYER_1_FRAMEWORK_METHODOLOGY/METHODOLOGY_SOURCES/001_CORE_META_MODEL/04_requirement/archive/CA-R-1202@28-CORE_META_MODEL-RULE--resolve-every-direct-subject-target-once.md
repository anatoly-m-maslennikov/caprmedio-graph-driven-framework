---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Subjects
  depends_on:
  - Entity/Graph Syntax > Relation//GOVERNS
  - Entity/Graph Syntax > Relation//DEPENDS_ON
  - Entity/Object/Continuant/Governing Objects/Atom.Subjects
version: 28
updated_at: 2026-10-29 07:45:26 +0400
relations: {}
atom_id: CA-R-1202@28
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Resolve Every Direct Subject Target Once

## Claim scope

direct GOVERNS and DEPENDS_ON values in an Atom's Subjects Property.

## Claim

**every** direct GOVERNS value **and** **every** direct DEPENDS_ON value **in** an Atom's Subjects Property **must** resolve **to** **`=1`** canonical Subject Target. resolution **must not** require an intermediate Subject/Entity **or** Subject/Reference Property **or** a repeated target-kind field.

## Details
