---
subjects:
  governs: "Entity/Continuant/Object/Atom.Substance"
  depends_on:
    ["Entity/Continuant/Object/Atom", "Entity/Continuant/Object/Atom/Content Role: Evaluation", "Entity/Continuant/Object/Scope Unit", "Entity/Continuant/Object/Atom.Target Scope Unit"]
version: 11
updated_at: "2026-10-15 18:49:31 +0000"
relations: {}
atom_id: "CA-E-461"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-461-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--warn-about-selected-sibling-claim-boundaries.md
  source_atom_id: CA-E-461
  source_atom_revision: 11
  source_sha256: f26e81dc504f5f57ca98dc266e0fbc4ea9b1708adaf549d2aa20228e8d5bb4e2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Warn About Selected-sibling Claim Boundaries

## Scope

an Atom Claim concerning **only** selected sibling Scope Units.

## Claim

**when** **`=1`** Atom Claim concerns **only** **`>=2`** selected sibling Scope Units **and** does **not** apply **to** their containing Scope Unit as a whole, the Evaluation **must** report a non-blocking boundary warning for review; that restriction alone **must not** make the Atom invalid **or** trigger automatic rejection, splitting, **or** retargeting **to** their parent.

## Details
