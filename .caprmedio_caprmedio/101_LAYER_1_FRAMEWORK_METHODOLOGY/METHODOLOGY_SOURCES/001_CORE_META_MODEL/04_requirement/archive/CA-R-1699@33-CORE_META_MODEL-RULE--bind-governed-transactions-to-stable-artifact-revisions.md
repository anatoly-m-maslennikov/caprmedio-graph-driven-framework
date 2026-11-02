---
subjects:
  governs: Entity/Graph Syntax > Relation
  depends_on: []
version: 33
updated_at: 2026-10-30 00:32:29 +0400
relations: {}
atom_id: CA-R-1699@33
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
