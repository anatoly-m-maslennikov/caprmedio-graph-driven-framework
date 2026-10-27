---
atom_id: CA-R-1873@11
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Engineering/Implementation
  depends_on:
  - Subject/Engineering/Implementation
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Engineering/Carrier
version: 11
updated_at: 2026-10-25 05:08:06 +0400
relations:
  relates_to:
  - CA-R-1470
  - CA-R-1746
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
