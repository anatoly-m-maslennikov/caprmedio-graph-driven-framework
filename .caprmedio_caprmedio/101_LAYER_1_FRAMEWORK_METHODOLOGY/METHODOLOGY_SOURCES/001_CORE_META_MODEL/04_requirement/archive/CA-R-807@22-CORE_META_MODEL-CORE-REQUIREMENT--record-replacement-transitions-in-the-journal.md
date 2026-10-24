---
subjects:
  governs: Subject/Graph/Relation
version: 22
updated_at: 2026-10-24 01:18:03 +0400
relations: {}
atom_id: CA-R-807@22
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary

Record replacement transitions in the Journal

## Scope

replacement **or** absorption history.

## Claim

replacement **or** absorption history **must** be recorded **only** **in** the authoritative Journal event that archives the predecessor. the authoritative Journal event that archives the predecessor **must** name the explicit predecessor Atom ID **and** **`>=1`** already active successor Atom IDs. active current-state Atom relations **must not** carry replacement history. formal `replaced_by` **and** `replacement_of` relation realization **must** remain deferred, **and** **any** later replacement navigation **must** be derived from immutable Journal **and** archive history under separately admitted authority.

## Details
