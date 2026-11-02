---
subjects:
  governs: Entity/Graph Syntax > Relation
  depends_on: []
version: 32
updated_at: 2026-10-29 10:13:49 +0400
relations:
  child_of:
  - CA-E-002
atom_id: CA-R-1699@32
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Bind governed transactions to stable artifact revisions

## Claim scope

governed changes.

## Claim

**every** governed change forms one directed provenance transaction from exact parent Artifact revisions **to** the governed Artifacts **or** native targets created **or** revised by that change.
