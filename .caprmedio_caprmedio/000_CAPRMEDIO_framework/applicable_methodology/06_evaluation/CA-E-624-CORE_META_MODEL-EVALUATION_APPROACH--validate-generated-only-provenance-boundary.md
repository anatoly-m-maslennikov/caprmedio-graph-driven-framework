---
subjects:
  governs: "Generated-Only Provenance Validation"
  depends_on:
    ["Entity/Continuant/History/Journal.Record", "Implementation Relation", "Entity/Continuant/Projection"]
version: 20
updated_at: "2026-10-15 18:50:37 +0000"
relations:
  evaluation_for:
    - CA-M-135
    - CA-R-1746
atom_id: "CA-E-624"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-624-CORE_META_MODEL-EVALUATION_APPROACH--validate-generated-only-provenance-boundary.md
  source_atom_id: CA-E-624
  source_atom_revision: 20
  source_sha256: 8af8ba9ac73c7ee1f9ef4c12cf06c4645a3ccbe94d452f553da17df305d7b867
  original_relations_sha256: 5c9a4949804f5766c1d28c00f18c57177f447286d4f477f6d0d8cad8ab4acfb7
---
# Summary

Validate Generated-Only Provenance Boundary

## Scope

generated-only provenance validation.

## Claim

generated-only provenance validation **must not** pass **if** an update **only** **to** generated Projections contributes an Implementation Relation **or** a generated Projection cites itself as its semantic input. the same boundary applies with **or** **without** a version-control integration.

## Details
