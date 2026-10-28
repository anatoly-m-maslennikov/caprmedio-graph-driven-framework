---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.ID
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
version: 18
updated_at: 2026-10-27 19:59:55 +0400
relations: {}
atom_id: CA-R-1464
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Keep Summary fixed for Atom identity

## Scope

the Summary of an Atom across its Revisions.

## Claim

an Atom **must** keep the Summary created with it across **all** of its Revisions. **if** its Summary needs a change, **then** it **must** be replaced by a new Atom with a new Atom ID, even **if** its Claim is unchanged.

## Details
