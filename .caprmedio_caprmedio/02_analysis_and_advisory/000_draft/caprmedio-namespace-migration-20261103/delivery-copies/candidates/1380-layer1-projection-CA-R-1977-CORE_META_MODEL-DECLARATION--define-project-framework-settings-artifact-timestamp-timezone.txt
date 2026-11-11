---
atom_id: CA-R-1977
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project.Settings.Artifact Timestamp Timezone
relations:
  child_of:
  - CA-R-1176
version: 15
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1977-CORE_META_MODEL-DECLARATION--define-project-framework-settings-artifact-timestamp-timezone.md
  source_atom_id: CA-R-1977
  source_atom_revision: 15
  source_sha256: b18f37106f8e2f99d46f37fdfb4b3837f7c6a45bef893bf7867a1e674d254af5
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
---
## Summary

Define Project.Framework Settings.Artifact Timestamp Timezone

## Claim scope

the Artifact timestamp timezone setting in Framework Settings.

## Claim

The value supplies the timezone used when emitting Artifact timestamps.

```CFEL
Project.Settings.Artifact Timestamp Timezone{:0..1}: [string]{:1};
Project.Settings.Artifact Timestamp Timezone.*[]{:0}
```

## Details

Evidence: CA-D-390 supplies the timezone interpretation and its concrete encoding. Candidate #6 keeps Settings attached to Project and keeps concrete CAPRMEDIO mechanisms in Project Configuration. This definition adds no format, allowed value or default; those remain separate Delivery rules.
