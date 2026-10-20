---
atom_id: CA-D-559
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Continuant/History/Journal"
  depends_on: ["Implementation", "Entity/Node/Continuant/Projection", "Entity/Node/Continuant/History/Journal", "Entity/Carrier"]
version: 5
updated_at: "2026-10-19 15:56:01 +0400"
relations: {relates_to: [CA-R-1745, CA-R-1720, CA-D-549, CA-D-504]}
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-559-CORE_META_MODEL--deliver-runtime-journals-to-configured-sinks.md
  source_atom_id: CA-D-559
  source_atom_revision: 5
  source_sha256: b9770806ecfdae73697c8ba3486d0b30f2c00e327358db689f3fe8d154fcdfbe
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Deliver runtime Journals to configured sinks

## Scope

technical and business runtime Journal Carriers.

## Claim

runtime technical **and** business Journals **may** be delivered **to** an explicitly configured local database, remote database, **or** governed logging sink. these Carriers **need not** reside under `.caprmedio_<project_name>/_journal/` **or** `.caprmedio_runtime/`.

## Details

Journal classification and recorded-history authority are independent of storage technology. The configuration identifies the intended sink; applicable production logging policy remains in force. The shared Project-control Work Journal and persistent view Projections retain their separate _journal and _projection locations. Runtime cleanup and sink migration must preserve accepted Journal history; this Delivery does not authorize history deletion or change retention policy.
