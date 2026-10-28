---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Relation/Type: structural_parent'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
version: 28
updated_at: 2026-10-27 20:00:00 +0400
relations: {}
atom_id: CA-R-1660
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Register structural parent relation

## Scope

the Structural Parent Relation directed from a child to its immediate parent.

## Claim

the Structural Parent Relation **must** be the kind-independent Structural ownership relation directed from a child **to** its immediate parent. Project Structure owns Scope Unit parent declarations; structural graph views derive the corresponding `structural_parent` edge **without** maintaining a second source. a Carrier's physical containment **must not** silently replace a declared logical parent.

## Details
