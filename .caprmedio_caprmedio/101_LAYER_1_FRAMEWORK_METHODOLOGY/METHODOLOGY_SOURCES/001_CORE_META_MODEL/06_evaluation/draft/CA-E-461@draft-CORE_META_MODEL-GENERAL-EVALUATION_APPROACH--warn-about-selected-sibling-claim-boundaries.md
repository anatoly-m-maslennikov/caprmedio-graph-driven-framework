---
subjects:
  governs: "Entity/Continuant/Object/Atom.Substance"
  depends_on:
    ["Entity/Continuant/Object/Atom", "Entity/Continuant/Object/Atom/Content Role: Evaluation", "Entity/Continuant/Object/Scope Unit", "Entity/Continuant/Object/Atom.Target Scope Unit"]
version: 11
updated_at: "2026-10-15 18:25:56 +0000"
relations: {}
atom_id: "CA-E-461@draft"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 10
---
# Summary

Warn About Selected-sibling Claim Boundaries

## Scope

an Atom Claim concerning **only** selected sibling Scope Units.

## Claim

**when** **`=1`** Atom Claim concerns **only** **`>=2`** selected sibling Scope Units **and** does **not** apply **to** their containing Scope Unit as a whole, the Evaluation **must** report a non-blocking boundary warning for review; that restriction alone **must not** make the Atom invalid **or** trigger automatic rejection, splitting, **or** retargeting **to** their parent.

## Details
