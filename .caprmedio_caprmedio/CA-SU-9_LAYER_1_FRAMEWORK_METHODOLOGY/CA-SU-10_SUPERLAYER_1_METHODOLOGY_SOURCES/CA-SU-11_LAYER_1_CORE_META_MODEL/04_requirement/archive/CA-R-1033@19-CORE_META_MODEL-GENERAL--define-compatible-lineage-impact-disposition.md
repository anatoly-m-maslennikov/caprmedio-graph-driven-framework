---
subjects:
  governs: Compatible Lineage Impact Disposition
  depends_on:
  - Subject/Graph/Relation
version: 19
updated_at: 2026-10-24 01:37:42 +0400
relations: {}
atom_id: CA-R-1033@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Definition
---
# Summary

Define compatible Lineage Impact disposition

## Scope

`compatible` Lineage Impact dispositions.

## Claim

`compatible` **means** the child remains valid against the parent Revision required by the gate **and** traversal stops on that branch **without** a child update. **if** the gate requires the revised parent, **then** compatibility **must** be established against that new Revision; permission **to** consume a pinned earlier Revision **must not** establish compatibility for a gate that requires the new Revision.

## Details
