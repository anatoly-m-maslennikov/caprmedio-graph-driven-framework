---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Status: Archived'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Status
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Version Number
version: 17
updated_at: 2026-10-27 19:59:54 +0400
relations: {}
atom_id: CA-R-1419
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Restrict Archived Status to Non-Current Revisions

## Scope

the Archived Status of an Atom version.

## Claim

an Atom version **may** have Status Archived **only** **if** it is a prior version **or** the final version of a replaced, absorbed, **or** retired Atom.

## Details
