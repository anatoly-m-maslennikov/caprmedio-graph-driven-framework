---
subjects:
  governs: Entity/Graph Syntax > Relation//structural_parent
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
version: 29
updated_at: 2026-10-29 07:17:18 +0400
relations: {}
atom_id: CA-R-1660@29
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
