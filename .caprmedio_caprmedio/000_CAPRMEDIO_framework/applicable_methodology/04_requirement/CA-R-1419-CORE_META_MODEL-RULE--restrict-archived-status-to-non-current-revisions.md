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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1419-CORE_META_MODEL-RULE--restrict-archived-status-to-non-current-revisions.md
  source_atom_id: CA-R-1419
  source_atom_revision: 23
  source_sha256: 36b34cba3f0a881789c72b811094d084107d087fb61d95c5f0887dd6d211ff56
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Restrict Archived Status to Non-Current Revisions

## Claim

### Prose Claim


the Archived Status of an Atom version.


an Atom version **may** have Status Archived **only** **if** it is a prior version **or** the final version of a replaced, absorbed, **or** retired Atom.
