---
atom_id: "CA-R-1610@draft"
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: "Draft"
subjects:
  governs: "Entity/Node/Continuant/Atom.Status"
  depends_on:
    ["Entity/Node/Continuant/Atom.Substance", "Implementation", "Entity/Node/Continuant/Projection", "Single Source of Truth", "Spec Content Roles"]
version: 7
updated_at: "2026-10-19 11:41:38 +0000"
relations:
  relates_to:
    - CA-R-1470
    - CA-R-1746
global_tier: 11
---
# Summary

Keep reverse-engineered RMED provisional

## Scope

RMED Claims reconstructed from existing Implementation or its Projections.

## Claim

RMED Claims reconstructed from existing Implementation **or** its Projections **must** remain proposed Draft Claims **until** accepted through the applicable Atom acceptance authority.

- extraction **or** inference alone does **not** establish Active authority.
- the accepted RMED, **not** the legacy Implementation **or** its Projection, governs subsequent refactoring **and** Evaluation of the result.

## Details
