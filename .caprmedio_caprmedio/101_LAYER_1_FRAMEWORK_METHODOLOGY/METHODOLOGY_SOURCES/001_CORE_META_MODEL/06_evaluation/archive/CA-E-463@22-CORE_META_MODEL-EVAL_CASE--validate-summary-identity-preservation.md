---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Content.Summary
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom.ID
  - Entity/Object/Continuant/Governing Objects/Atom.Content
version: 22
updated_at: 2026-10-29 07:45:29 +0400
relations:
  evaluation_for:
  - CA-R-1464
  - CA-R-1465
  - CA-R-1273
atom_id: CA-E-463@22
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Eval Case
tier: 4
---
## Summary

Validate Summary identity preservation

## Claim scope

candidate Atom Revisions and their Summary Property.

## Claim

the Evaluation **must** reject a candidate Atom Revision **if** its Summary differs from the Summary established for that Atom identity, even **when** its Claim is unchanged. it **must** reject treating Summary as an independently identified, versioned, **or** timestamped Artifact; Summary belongs **to** its Atom under CA-R-1465.

## Details

### Test cases

| Case | Expected result |
|---|---|
| new Atom with its initial source-faithful Summary | pass |
| same Atom ID, new Revision, unchanged source-faithful Summary | pass |
| same Atom ID, changed Summary, unchanged Claim | fail |
| same Atom ID, Summary spelling correction **only** | fail |
| same Atom ID, unchanged Summary that no longer represents the revised Claim | fail under CA-R-1273 |
| new Atom ID for the changed Summary, with preserved predecessor **and** replacement evidence | pass **if** the replacement checks under CA-E-462 pass |
| independently versioned Summary **or** independent Summary Updated At | fail |
| lossless Carrier serialization of the same Summary value | pass **if** the applicable Delivery checks pass |

passing this Evaluation does **not** establish the validity of unrelated Claim, Carrier, **or** replacement-history constraints.
