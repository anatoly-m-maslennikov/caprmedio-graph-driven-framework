---
subjects:
  governs: "Entity/Node/Continuant/Project.Structure"
  depends_on:
    ["Entity/Carrier", "Entity/Node/Continuant/Project.Structure", "Entity/Node/Continuant/Actor/Type: Operator"]
version: 10
updated_at: "2026-10-19 15:55:48 +0400"
relations:
  child_of:
    - "CA-D-440"
  relates_to:
    - "CA-O-015"
atom_id: "CA-D-444"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-444-CORE_META_MODEL-STANDARD--separate-candidate-project-structure-from-active-authority.md
  source_atom_id: CA-D-444
  source_atom_revision: 10
  source_sha256: da343240575da402564abd7b9aec093c7c94afc7fb70656f6a14d0c2f584a37f
  original_relations_sha256: b3dc811146ee62c18ef50f82ff64aab425c31a30946049ab1ef214daa4b99a41
---
# Summary

Separate candidate Project Structure from active authority

## Scope

the transition of a staged Project Structure candidate to active authority.

## Claim

a staged Project Structure candidate **must** use the filename `project_structure.candidate.toml` inside the explicitly selected migration workspace, outside the canonical active path. no ordinary consumer **may** discover it as active authority; candidate validation requires an explicit candidate path. cutover **must** install the validated candidate at the canonical path **only** **after** freshness, authorization, reference repairs, consumer readiness **and** recoverability checks pass. the old active bytes **must** remain recoverable through accepted change evidence **without** becoming another active structural source. the candidate **must** be retired **after** successful activation **or** rejection; failure **must not** leave two files eligible for normal authority resolution.

## Details
