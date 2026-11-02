---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom.Status: Archived'
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Status
  - Entity/Object/Continuant/Governing Objects/Atom.Version Number
version: 20
updated_at: 2026-10-29 10:13:48 +0400
relations: {}
atom_id: CA-R-1419@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Restrict Archived Status to Non-Current Revisions

## Claim scope

the Archived Status of an Atom version.

## Claim

an Atom version **may** have Status Archived **only** **if** it is a prior version **or** the final version of a replaced, absorbed, **or** retired Atom.
