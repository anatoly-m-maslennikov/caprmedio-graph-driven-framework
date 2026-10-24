---
subjects:
  governs: Subject/Graph/Relation
  depends_on: []
version: 25
updated_at: 2026-10-24 04:38:42 +0400
relations:
  child_of:
  - CA-E-002
atom_id: CA-R-1699
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Bind governed transactions to stable artifact revisions

## Scope

governed changes.

## Claim

**every** governed change forms one directed provenance transaction from exact parent Artifact revisions **to** the governed Artifacts **or** native targets created **or** revised by that change.

## Details
