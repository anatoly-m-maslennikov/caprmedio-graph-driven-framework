---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
  depends_on:
  - 'Subject/Graph/Relation/Type: GOVERNS'
atom_id: CA-R-2100@2
content_role: Requirement
type: Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
version: 2
updated_at: 2026-10-24 00:38:25 +0400
author: Anatoly Maslennikov
relations: {}
tier: 1
---
# Summary

Limit each Atom to one governed Subject

## Scope

The direct GOVERNS Subject Relations recorded in an Atom's Subjects.

## Claim

An Atom **may** have zero or one direct GOVERNS Subject Relation. No Atom's Subjects **may** contain more than one direct GOVERNS Subject Relation.

## Details

This Rule limits cardinality only. It does not require an Atom to have a GOVERNS Subject. The Subjects collection is optional, and DEPENDS_ON relations are not limited by this Rule.
