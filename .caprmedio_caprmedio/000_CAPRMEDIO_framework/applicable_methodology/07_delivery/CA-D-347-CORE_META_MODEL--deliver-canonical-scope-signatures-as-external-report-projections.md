---
subjects:
  governs: "Entity/Continuant/Projection/Type: Canonical Scope Signature"
  depends_on:
    ["Entity/Continuant/Projection/Type: Canonical Scope Signature", "Entity/Carrier"]
version: 14
updated_at: "2026-10-15 18:51:24 +0000"
relations:
  child_of:
    - CA-D-266
atom_id: "CA-D-347"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-347-CORE_META_MODEL--deliver-canonical-scope-signatures-as-external-report-projections.md
  source_atom_id: CA-D-347
  source_atom_revision: 14
  source_sha256: 51962bfc9daba1305af8b89c888b5e27914995cd5d0f0d042b8174d3c2cd671b
  original_relations_sha256: 27960d084ae992c89042523b783c283ce26a91ac1b1473d8e6f3ba8c73dade11
---
# Summary

Deliver Canonical Scope Signatures as External Report Projections

## Scope

external report Projections that deliver Canonical Scope Signatures.

## Claim

**every** Canonical Scope Signature Projection **must** be delivered as **`=1`** non-authoritative JSON report under its Project's `.caprmedio_<project_name>/_projection/` Directory Carrier with the selected source frontier digest, **every** source Atom identity **and** revision, source Carrier digest, source Scope Expression occurrence, Canonical Scope Signature, **and** exclusion diagnostic; the Projection **must not** become an Atom Carrier, modify a selected source Carrier, establish Claim equivalence, **or** create a dependency relation.

## Details
