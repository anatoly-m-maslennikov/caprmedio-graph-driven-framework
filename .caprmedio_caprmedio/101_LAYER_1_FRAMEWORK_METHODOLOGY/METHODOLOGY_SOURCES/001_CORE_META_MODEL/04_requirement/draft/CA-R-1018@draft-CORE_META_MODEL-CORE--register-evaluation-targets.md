---
subjects:
  governs: "Entity/Continuant/Object/Relation/Type: evaluation_for"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Evaluation", "Entity/Continuant/Object/Atom/Content Role: Requirement", "Entity/Continuant/Object/Atom/Content Role: Method", "Entity/Continuant/Object/Atom/Content Role: Delivery", "Entity/Continuant/Object/Atom/Content Role: Operations", "Entity/Continuant/Object/Atom.Local Tier"]
version: 20
updated_at: "2026-10-16 11:57:50 +0000"
relations: {}
atom_id: "CA-R-1018@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
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
