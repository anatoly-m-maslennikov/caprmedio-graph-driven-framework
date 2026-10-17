---
subjects:
  governs: "relation-model"
  depends_on:
    ["Atom Scope", "Entity/Continuant/Object/Atom.Target Scope Unit"]
version: 21
updated_at: "2026-10-15 18:46:43 +0000"
relations:
  child_of:
    - CA-R-932
atom_id: "CA-R-916"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-916-CORE_META_MODEL-CORE-REQUIREMENT--restrict-ordered-demands-to-earlier-producers.md
  source_atom_id: CA-R-916
  source_atom_revision: 21
  source_sha256: c574f331de1d8641d0fcdbfba854acbc07358c883e740ac7c250d04d7ce48c70
  original_relations_sha256: 986ab56d61737841b77ed4fc4f1a391a0c8ad370d896e576cf2be7bdd2bdf459
---
# Summary
Restrict ordered Demands to earlier Producers

## Scope

Demand Atoms whose Consumer Atom Scope Unit and Producer Claim Target Scope Unit are ordered siblings.

## Claim

**if** a Demand Atom's Consumer Atom Scope Unit **and** Producer Claim Target Scope Unit are ordered siblings, **then** its Producer Claim Target Scope Unit **must** precede its Consumer Atom Scope Unit.

## Details
