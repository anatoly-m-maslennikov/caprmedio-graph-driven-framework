---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Reconciled Projection'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
version: 20
updated_at: 2026-10-27 19:59:55 +0400
relations: {}
atom_id: CA-R-1461
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Reconciled Projection

## Scope

the Reconciled Projection Type value under Projection.

## Claim

Reconciled Projection **means** the Type value under Projection whose instances preserve selected source content, canonical identities, **and** exact final selected Revisions **without** synthesis **or** merge, **and** have no unresolved source conflict under the applicable declared checks.

## Details

source selection **and** conflict resolution remain governed by applicable source authority. **any** needed source correction **must** be separately authorized by the Operator **and** applied upstream **to** that authority, **not** by editing the projected content **or** treating projection production as authorization **to** change a source. a result **must not** be published as a Reconciled Projection **until** its final selected source Revisions have been re-evaluated **after** **any** such correction **and** no conflict remains unresolved under those checks. this classification does **not** grant the result independent source authority **or** determine its Carrier materialization strategy.
