---
subjects:
  governs: "Entity/Continuant/Projection/Type: Reconciled Projection"
  depends_on:
    ["Entity/Continuant/Projection", "Type", "Artifact", "Entity/Continuant/Object/Atom.Substance", "Entity/Carrier", "Entity/Continuant/Actor/Type: Operator"]
version: 7
updated_at: "2026-10-15 18:43:19 +0000"
relations: {}
atom_id: "CA-R-1461"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1461-CORE_META_MODEL-CORE-REQUIREMENT--define-reconciled-projection.md
  source_atom_id: CA-R-1461
  source_atom_revision: 7
  source_sha256: a5abe00228c29e789745199758a4e86e7882e6ac977a55c9a06dbfc8db3acdc7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Reconciled Projection

## Scope

the Reconciled Projection Type value under Projection.

## Claim

Reconciled Projection **means** the Type value under Projection whose instances preserve selected source content, canonical identities, **and** exact final selected Revisions **without** synthesis **or** merge, **and** have no unresolved source conflict under the applicable declared checks.

## Details

source selection **and** conflict resolution remain governed by applicable source authority. **any** needed source correction **must** be separately authorized by the Operator **and** applied upstream **to** that authority, **not** by editing the projected content **or** treating projection production as authorization **to** change a source. a result **must not** be published as a Reconciled Projection **until** its final selected source Revisions have been re-evaluated **after** **any** such correction **and** no conflict remains unresolved under those checks. this classification does **not** grant the result independent source authority **or** determine its Carrier materialization strategy.
