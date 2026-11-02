---
subjects:
  governs: Entity
  depends_on:
  - Entity/Graph Syntax > Relation
version: 25
updated_at: 2026-10-29 07:45:26 +0400
relations: {}
atom_id: CA-R-1033@25
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Entity Definition
---
## Summary

Define compatible Lineage Impact disposition

## Claim scope

`compatible` Lineage Impact dispositions.

## Claim

`compatible` **means** the child remains valid against the parent Revision required by the gate **and** traversal stops on that branch **without** a child update. **if** the gate requires the revised parent, **then** compatibility **must** be established against that new Revision; permission **to** consume a pinned earlier Revision **must not** establish compatibility for a gate that requires the new Revision.

## Details
