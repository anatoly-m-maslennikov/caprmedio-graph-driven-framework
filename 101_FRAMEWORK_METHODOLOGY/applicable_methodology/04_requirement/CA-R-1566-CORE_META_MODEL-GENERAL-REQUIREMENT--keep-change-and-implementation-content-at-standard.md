---
subjects:
  governs: "Entity/Continuant/Object/Atom.Local Tier"
  depends_on:
    ["Change Content Roles", "Implementation", "Entity/Continuant/Object/Atom", "Entity/Continuant/Object/Atom.Local Tier: Standard"]
version: 7
updated_at: "2026-10-15 18:44:28 +0000"
relations: {"relates_to": ["CA-R-1549", "CA-R-1343", "CA-R-660"]}
atom_id: "CA-R-1566"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1566-CORE_META_MODEL-GENERAL-REQUIREMENT--keep-change-and-implementation-content-at-standard.md
  source_atom_id: CA-R-1566
  source_atom_revision: 7
  source_sha256: b552c7ca1500bdc13f83f8a998be6bbfa9a6f0796bd406e7dad74d1a4f44e5a7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep Change **and** Implementation content at Standard

## Scope

Atoms whose Content Role is Concern, Analysis, Plan, Operations, **or** Implementation.

## Claim

an Atom whose Content Role is **in** (Concern, Analysis, Plan, Operations, Implementation) **must** resolve **to** Local Tier Standard.

- an omitted filename tier token denotes Standard, **not** the absence of the internally carried Local Tier; persistence, reuse, importance, **or** nesting does **not** promote that content **to** Core **or** General.
- the RMED Atoms specifying that content retain their own Local Tiers; the content does **not** inherit its specification's tier.

## Details
