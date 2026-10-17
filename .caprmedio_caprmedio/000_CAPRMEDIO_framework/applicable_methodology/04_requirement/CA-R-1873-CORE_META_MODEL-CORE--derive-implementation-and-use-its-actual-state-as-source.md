---
atom_id: CA-R-1873
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Implementation"
  depends_on: ["Implementation", "Entity/Continuant/Projection", "Entity/Continuant/History/Journal", "Entity/Carrier"]
version: 4
updated_at: "2026-10-15 18:46:10 +0000"
relations: {relates_to: [CA-R-1470, CA-R-1746, CA-R-1343]}
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1873-CORE_META_MODEL-CORE--derive-implementation-and-use-its-actual-state-as-source.md
  source_atom_id: CA-R-1873
  source_atom_revision: 4
  source_sha256: 85e0161211b0c490cabae80cb1af0d70f9cc59a08583b9b0b5d2bf934db8bc2b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Implementation and use its actual state as source

## Scope

native Implementation production and subsequent use as a source.

## Claim

Implementation production **must** derive I from current applicable RMED using governed Operations: **RMED → using O → I**. native I **may** subsequently act as source truth for its actual realized content, structure, dependencies, **and** behavior. a further view derived from I using O, including a dependency graph, **must** remain a non-authoritative Projection: **I → using O → Projection**.

## Details

Generation need not be deterministic. Derivation is a relation to governing intent, not perpetual loss of actual-state authority. Actual code may predate CAPRMEDIO authority; its observations support adoption, reconciliation, and continuation without automatically accepting inferred CRMED drafts or changing governing RMED. Existing I is not a prerequisite for reconstructing I from current RMED. Ordinary view Projections never replace the authority of their represented sources.
