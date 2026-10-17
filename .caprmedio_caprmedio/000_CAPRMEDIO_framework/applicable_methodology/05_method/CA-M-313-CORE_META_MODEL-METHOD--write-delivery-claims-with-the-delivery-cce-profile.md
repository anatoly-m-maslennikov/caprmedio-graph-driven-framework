---
subjects:
  governs: "Delivery CCE Role Profile"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Delivery", "CCE Operator", "Entity/Carrier", "Entity Carrier Binding", "Entity/Continuant/Object/Atom.Substance", "Entity/Continuant/Object/Atom.Subjects", "Relation Type"]
version: 7
updated_at: "2026-10-15 18:48:44 +0000"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-R-1342
atom_id: "CA-M-313"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-313-CORE_META_MODEL-METHOD--write-delivery-claims-with-the-delivery-cce-profile.md
  source_atom_id: CA-M-313
  source_atom_revision: 7
  source_sha256: 1a68b8dc50f69a6d2945f88c304340f6bb855608843fc1a466ec1523e21e57f1
  original_relations_sha256: df4e705715370cdf548abfbeba9ae0eed904bc3f2977ebc87988f011e0ad7418
---
# Summary

Write Delivery Claims with the Delivery CCE Profile

## Scope

authoring Delivery Claims with the Delivery CCE Role Profile.

## Claim

a Delivery Claim **must** use the Delivery CCE Role Profile **to** express its Carrier contribution with the following authoring conventions:

1. name the governed Carrier **or** Entity/Carrier binding **and** state its definition, classification, **or** constraint directly.
2. include format, content, address, placement, **or** lifecycle conditions **when** they are relevant **to** that contribution.
3. choose CCE Operators **to** express the applicable modality, conditions, quantities, **and** comparisons.
4. use **means** for a definition; express a classification **or** binding through its admitted Relation Type.
5. keep the Claim about the governed Subject; use references for separately governed contributions.

## Details

Carrier definitions **and** classifications need **only** the details relevant **to** their own contribution. they do **not** require an invented filename, format, **or** lifecycle condition.
