---
subjects:
  governs: "Entity/Node/Continuant/Projection/Type: Canonical Scope Signature"
  depends_on:
    ["Entity/Node/Continuant/Projection/Type: Canonical Scope Signature", "Entity/Carrier"]
version: 16
updated_at: "2026-10-19 15:55:32 +0400"
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
  source_atom_revision: 16
  source_sha256: deaabc3990ca6acab8dd764ffe6b24321cfd1729be3a4977474f7ae70a64bc9d
  original_relations_sha256: 27960d084ae992c89042523b783c283ce26a91ac1b1473d8e6f3ba8c73dade11
---
# Summary

Deliver Canonical Scope Signatures as External Report Projections

## Scope

external report Projections that deliver Canonical Scope Signatures.

## Claim

**every** Canonical Scope Signature Projection **must** be delivered as **`=1`** non-authoritative JSON report under its Project's `.caprmedio_<project_name>/_projection/` Directory Carrier with the selected source frontier digest, **every** source Atom identity **and** revision, source Carrier digest, source Scope Expression occurrence, Canonical Scope Signature, **and** exclusion diagnostic; the Projection **must not** become an Atom Carrier, modify a selected source Carrier, establish Claim equivalence, **or** create a dependency relation.

## Details
