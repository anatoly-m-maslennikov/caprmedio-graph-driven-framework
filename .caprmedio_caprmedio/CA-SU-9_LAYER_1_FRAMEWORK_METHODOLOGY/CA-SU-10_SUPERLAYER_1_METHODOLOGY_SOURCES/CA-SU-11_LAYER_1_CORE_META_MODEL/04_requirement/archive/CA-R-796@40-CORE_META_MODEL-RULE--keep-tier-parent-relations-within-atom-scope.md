---
subjects:
  governs: Entity/Graph Syntax > Relation//child_of
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Tier
  - Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom.Content.Claim Scope
version: 40
updated_at: 2026-10-29 09:39:47 +0400
relations:
  child_of:
  - CA-R-1174
atom_id: CA-R-796@40
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Relation Definition
---
## Summary

Keep tier-parent relations within Atom Scope

## Claim scope

The existing governing child_of relation, pending its separately planned replacement.

## Claim

child_of is the directed governing connection from a child Atom to the parent Atom whose Claim governs that child's contribution. It is distinct from containment, dependency, classification and source-layer membership. The Atom definition CA-R-655 and ordering definition CA-R-2149 govern endpoint admission and ordering. This definition preserves the existing relation until its separate replacement Epic; it does not migrate its actual links.
