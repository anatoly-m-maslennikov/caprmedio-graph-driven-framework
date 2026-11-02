---
subjects:
  governs: 'Entity/Object/Continuant/Projection/(.Type: Reconciled Projection)'
  depends_on:
  - Entity/Object/Continuant/Projection
  - Entity/Object/Continuant/Projection.Type
  - Entity/Term//Artifact
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Carrier
  - Entity/Object/Continuant/Actor/Operator
version: 23
updated_at: 2026-10-30 17:01:42 +0400
relations: {}
atom_id: CA-R-1461@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Reconciled Projection

## Claim scope

the Reconciled Projection Type value under Projection.

## Claim

Reconciled Projection **means** the Type value under Projection whose instances preserve selected source content, canonical identities, **and** exact final selected Revisions **without** synthesis **or** merge, **and** have no unresolved source conflict under the applicable declared checks.

## Details

source selection **and** conflict resolution remain governed by applicable source authority. **any** needed source correction **must** be separately authorized by the Operator **and** applied upstream **to** that authority, **not** by editing the projected content **or** treating projection production as authorization **to** change a source. a result **must not** be published as a Reconciled Projection **until** its final selected source Revisions have been re-evaluated **after** **any** such correction **and** no conflict remains unresolved under those checks. this classification does **not** grant the result independent source authority **or** determine its Carrier materialization strategy.
