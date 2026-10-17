---
subjects:
  governs: "Entity/Continuant/Object/Relation/Type: evaluation_for"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Evaluation", "Entity/Continuant/Object/Atom/Content Role: Requirement", "Entity/Continuant/Object/Atom/Content Role: Method", "Entity/Continuant/Object/Atom/Content Role: Delivery", "Entity/Continuant/Object/Atom/Content Role: Operations", "Entity/Continuant/Object/Atom.Local Tier"]
version: 20
updated_at: "2026-10-16 12:08:16 +0000"
relations: {}
atom_id: "CA-R-1018"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1018-CORE_META_MODEL-CORE--register-evaluation-targets.md
  source_atom_id: CA-R-1018
  source_atom_revision: 20
  source_sha256: 5c89462b1b128b20bb6dfc74d6651257d07d17e3a5140f1a0ece71efda410127
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Register Evaluation targets

## Scope

direct `evaluation_for` relations.

## Claim

`evaluation_for` **means** a direct relation owned by an Evaluation Atom **and** directed **to** an Atom whose Content Role is **in** (Requirement, Method, Evaluation, Delivery, Operations) **and** whose authority the Evaluation checks;

- a Standard Evaluation Atom **must** own **`>=1`** such target relations,
- while a Core **or** General Evaluation **may** state a representation-independent evaluation policy **without** an artificial list of individual targets.

**every** supplied target relation **must** retain the same checked-authority qualification regardless of the Evaluation's Local Tier.

## Details
