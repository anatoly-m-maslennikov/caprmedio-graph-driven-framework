---
subjects:
  governs: "Dependency Order Derivation Evaluation"
  depends_on:
    ["Artifact", "DEPENDS_ON", "DERIVED_FROM", "Atom Direct Relation", "Dependency Order Derivation"]
version: 13
updated_at: "2026-10-15 12:19:10 +0000"
relations: {"evaluation_for": ["CA-R-1026", "CA-R-915", "CA-D-268", "CA-M-239", "CA-R-1580"]}
atom_id: "CA-E-404"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-404-CORE_META_MODEL-EVALUATION_APPROACH--reject-invalid-dependency-order-derivations.md
  source_atom_id: CA-E-404
  source_atom_revision: 13
  source_sha256: 506ad2141f3c4cd641cfeba04cc48925bbf57520106f0214d3a45ef2cc51ec24
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Reject Invalid Dependency-Order Derivations

## Scope

derived non-Plan Artifact dependency orders.

## Claim

the Evaluation **must** reject one derived non-Plan Artifact dependency order **if** a relation endpoint is **not** an admitted non-Plan Artifact, one `relations.depends_on` target reference repeats, a permutation of target-list positions changes its direct-edge set **or** derived order, an edge is absent from `relations.depends_on`, `relations.derived_from` contributes an edge, **or** the direct dependency graph **contains** a cycle.

## Details

Plan blocking **must** be checked separately under CA-E-504-CORE_META_MODEL-QA_CASE--validate-plan-blocking-and-parallel-readiness; a Plan `BLOCKS` fact **must not** fail merely because it is absent from `relations.depends_on`.
