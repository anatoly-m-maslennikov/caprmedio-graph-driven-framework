---
subjects:
  governs: "Entity/Continuant/Relation/Type: evaluation_for"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Evaluation", "Entity/Continuant/Node/Atom/Content Role: Requirement", "Entity/Continuant/Node/Atom/Content Role: Method", "Entity/Continuant/Node/Atom/Content Role: Delivery", "Entity/Continuant/Node/Atom/Content Role: Operations", "Entity/Continuant/Node/Atom.Local Tier"]
version: 21
updated_at: "2026-10-18 03:33:16 +0400"
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
  source_atom_revision: 21
  source_sha256: 183ac76dc0a60852bf6b6325d289a6f8f1b19f5677b5d20d7013a45eb1946cf8
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
