---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
  depends_on:
  - 'Subject/Graph/Relation/Type: GOVERNS'
atom_id: CA-R-2100@1
content_role: Requirement
type: Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
status: Archived
version: 1
updated_at: 2026-10-22 16:12:51 +0000
author: Anatoly Maslennikov
global_tier: 9
relations: {}
---
# Summary

Limit each Atom to one governed Subject

## Scope

The direct GOVERNS Subject Relations recorded in an Atom's Subjects.

## Claim

An Atom **may** have zero or one direct GOVERNS Subject Relation. No Atom's Subjects **may** contain more than one direct GOVERNS Subject Relation.

## Details

This Rule limits cardinality only. It does not require an Atom to have a GOVERNS Subject. The Subjects collection is optional, and DEPENDS_ON relations are not limited by this Rule.
