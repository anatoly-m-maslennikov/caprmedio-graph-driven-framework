---
atom_id: CA-R-1419
ref_id: CA-R-1419
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Status:Archived
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
  - CAPRMEDIO_MODEL <+ Atom.Header.Version
tier: 1
status: Active
version: 23
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-1419-CORE_META_MODEL-RULE--restrict-archived-status-to-non-current-revisions.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Restrict Archived Status to Non-Current Revisions

## Claim

### Prose Claim


the Archived Status of an Atom version.


an Atom version **may** have Status Archived **only** **if** it is a prior version **or** the final version of a replaced, absorbed, **or** retired Atom.
