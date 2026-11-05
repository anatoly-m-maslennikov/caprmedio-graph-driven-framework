---
atom_id: CA-E-463
ref_id: CA-E-463
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content.Summary
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Header.ID
  - CAPRMEDIO_MODEL <+ Atom.Content
tier: 4
relations:
  evaluation_for:
  - CA-R-1464
  - CA-R-2499
  - CA-R-1273
status: Active
version: 23
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-E-463-CORE_META_MODEL-EVAL_CASE--validate-summary-identity-preservation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-463-CORE_META_MODEL-EVAL_CASE--validate-summary-identity-preservation.md
  source_atom_id: CA-E-463
  source_atom_revision: 23
  source_sha256: 09ef001875b903174437aaa916e255f8042dfc191f608816611ed22c5136c33a
  original_relations_sha256: 810dc2051be3ce6bc035323b9af494373476f872a3b764c46205617aae342f98
---
## Summary

Validate Summary identity preservation

## Claim

### Prose Claim


candidate Atom Revisions and their Summary Property.


the Evaluation **must** reject a candidate Atom Revision **if** its Summary differs from the Summary established for that Atom identity, even **when** its Claim is unchanged. it **must** reject treating Summary as an independently identified, versioned, **or** timestamped Artifact; Summary belongs **to** its Atom under CA-R-2499.

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
