---
subjects:
  governs: "Entity/Continuant/Relation/Type: evaluation_for"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Evaluation", "Entity/Continuant/Node/Atom/Content Role: Requirement", "Entity/Continuant/Node/Atom/Content Role: Method", "Entity/Continuant/Node/Atom/Content Role: Delivery", "Entity/Continuant/Node/Atom/Content Role: Operations", "Entity/Continuant/Node/Atom.Local Tier"]
version: 21
updated_at: "2026-10-17 23:20:59 +0000"
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
