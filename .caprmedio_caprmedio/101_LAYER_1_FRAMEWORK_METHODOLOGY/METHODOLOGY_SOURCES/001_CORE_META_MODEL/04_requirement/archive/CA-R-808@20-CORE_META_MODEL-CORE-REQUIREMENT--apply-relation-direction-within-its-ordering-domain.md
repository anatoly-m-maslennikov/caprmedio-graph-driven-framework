---
subjects:
  governs: Subject/Graph/Relation
  depends_on:
  - atom-boundary
version: 20
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-R-808@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary

Apply relation direction within its ordering domain

## Scope

declared relations.

## Claim

**every** declared relation **must** satisfy the target position **and** ordering domain registered for its relation family. Normative-authority relations **must** use the global-tier **and** authority hierarchy, temporal relations **must** use lifecycle succession, realization relations **must** use realization order, dependency relations **must** use dependency order, **and** **every** other admitted domain **must** use its own registered order. a universal upstream **or** downstream rule **must not** be inferred across different ordering domains, **and** an inverse-derived view **must not** create another declared edge.

## Details
