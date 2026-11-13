---
atom_id: CA-R-1977
ref_id: CA-R-1977@16
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Artifact Timestamp Timezone
tier: 3
relations:
  child_of:
  - CA-R-1176
status: archived
version: 16
updated_at: 2026-11-04 05:21:15 +0400
carrier_destination:
  file:
    name: CA-R-1977@16-CORE_META_MODEL-DECLARATION--define-project-framework-settings-artifact-timestamp-timezone.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Project.Framework Settings.Artifact Timestamp Timezone

## Claim

### Prose Claim


the Artifact timestamp timezone setting in Framework Settings.


The value supplies the timezone used when emitting Artifact timestamps.


### Formal Claim

```CFEL
# model
Project.Settings.Artifact Timestamp Timezone:: [string]{::0..1};

Project.Settings.Artifact Timestamp Timezone.*[]{::0}
```

## Details

Evidence: CA-D-390 supplies the timezone interpretation and its concrete encoding. Candidate #6 keeps Settings attached to Project and keeps concrete CAPRMEDIO mechanisms in Project Configuration. This definition adds no format, allowed value or default; those remain separate Delivery rules.
