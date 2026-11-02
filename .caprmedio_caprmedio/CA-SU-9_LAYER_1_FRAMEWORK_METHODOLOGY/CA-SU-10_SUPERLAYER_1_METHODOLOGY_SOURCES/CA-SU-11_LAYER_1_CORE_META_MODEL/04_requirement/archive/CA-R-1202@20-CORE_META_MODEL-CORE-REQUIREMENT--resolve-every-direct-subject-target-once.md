---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
  depends_on:
  - 'Subject/Graph/Relation/Type: GOVERNS'
  - 'Subject/Graph/Relation/Type: DEPENDS_ON'
  - Subject Target
version: 20
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-R-1202@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary

Resolve Every Direct Subject Target Once

## Scope

direct GOVERNS and DEPENDS_ON values in an Atom's Subjects Property.

## Claim

**every** direct GOVERNS value **and** **every** direct DEPENDS_ON value **in** an Atom's Subjects Property **must** resolve **to** **`=1`** canonical Subject Target. resolution **must not** require an intermediate Subject/Entity **or** Subject/Reference Property **or** a repeated target-kind field.

## Details
