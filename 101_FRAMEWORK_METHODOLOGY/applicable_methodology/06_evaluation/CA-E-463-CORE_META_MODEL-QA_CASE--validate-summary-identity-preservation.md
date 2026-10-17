---
subjects:
  governs: "Entity/Continuant/Object/Atom.Summary"
  depends_on:
    ["Entity/Continuant/Object/Atom", "Entity/Continuant/Object/Atom.ID", "Entity/Continuant/Object/Atom.Substance"]
version: 8
updated_at: "2026-10-15 18:49:33 +0000"
relations:
  evaluation_for:
    - CA-R-1464
    - CA-R-1465
    - CA-R-1273
atom_id: "CA-E-463"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-463-CORE_META_MODEL-QA_CASE--validate-summary-identity-preservation.md
  source_atom_id: CA-E-463
  source_atom_revision: 8
  source_sha256: 35dad43f1c1a86d1d8536e875965a118df8a5f19e0fcceaa0265a9b1515c0839
  original_relations_sha256: cb1c9046795a805c03cc62c2e84c370df72f8b2950359a6d813833a2908bbf03
---
# Summary

Validate Summary identity preservation

## Scope

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
