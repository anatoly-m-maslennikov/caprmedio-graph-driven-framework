---
atom_id: CA-R-1873
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Carrier
version: 15
updated_at: 2026-10-27 20:00:05 +0400
relations: {}
tier: 1
type: Rule
---
# Summary

Derive Implementation and use its actual state as source

## Scope

native Implementation production and subsequent use as a source.

## Claim

Implementation production **must** derive I from current applicable RMED using governed Operations: **RMED → using O → I**. native I **may** subsequently act as source truth for its actual realized content, structure, dependencies, **and** behavior. a further view derived from I using O, including a dependency graph, **must** remain a non-authoritative Projection: **I → using O → Projection**.

## Details

Generation need not be deterministic. Derivation is a relation to governing intent, not perpetual loss of actual-state authority. Actual code may predate CAPRMEDIO authority; its observations support adoption, reconciliation, and continuation without automatically accepting inferred CRMED drafts or changing governing RMED. Existing I is not a prerequisite for reconstructing I from current RMED. Ordinary view Projections never replace the authority of their represented sources.
