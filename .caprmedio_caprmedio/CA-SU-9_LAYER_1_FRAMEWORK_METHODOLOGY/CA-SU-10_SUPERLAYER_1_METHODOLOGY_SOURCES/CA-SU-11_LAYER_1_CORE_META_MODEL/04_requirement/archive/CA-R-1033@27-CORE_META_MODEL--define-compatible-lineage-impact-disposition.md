---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom
  depends_on:
  - Entity/Graph Syntax > Relation
version: 27
updated_at: 2026-10-29 17:09:47 +0400
relations: {}
atom_id: CA-R-1033@27
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Define compatible Lineage Impact disposition

## Claim scope

`compatible` Lineage Impact dispositions.

## Claim


When a Lineage Impact analysis addresses an Atom, `compatible` must mean the child remains valid against the parent Revision required by the gate and traversal stops without a child update; a pinned earlier Revision does not establish compatibility where the new Revision is required.

