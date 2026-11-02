---
subjects:
  governs: "Entity/Relation.Authority"
  depends_on:
    ["Entity/Relation", "Relation Kind", "CAPRMEDIO Graph", "Entity/Node/Continuant/Projection", "Single Source of Truth", "Entity/Node/Continuant/Atom.Substance", "Structural Entity", "Entity/Node/Continuant/History/Journal"]
version: 9
updated_at: "2026-10-19 15:53:04 +0400"
relations: {}
atom_id: "CA-R-1437"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1437-CORE_META_MODEL-CORE--keep-one-source-for-each-relation-fact.md
  source_atom_id: CA-R-1437
  source_atom_revision: 9
  source_sha256: 4d0b5984c8817e24dc2b78670151ce22a5bd9c887be012514f7b251a074d8087
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep one source for each relation fact

## Scope

authoritative source declarations for Relation facts.

## Claim

**every** independently authored Relation fact **must** have **`=1`** authoritative source declaration under Single Source of Truth. its representation **in** multiple CAPRMEDIO Graph views remains a reference **or** derived Projection of that declaration **without** creating another independently maintained source.

a Relation derived under admitted derivation authority **must** remain traceable **to** that authority **and** its authoritative input facts, including through upstream Projections. it does **not** require a fabricated direct source declaration for the derived result. this distinction **must not** weaken a Relation Kind's requirement for an explicit source fact **or** permit unsupported inference.

## Details
