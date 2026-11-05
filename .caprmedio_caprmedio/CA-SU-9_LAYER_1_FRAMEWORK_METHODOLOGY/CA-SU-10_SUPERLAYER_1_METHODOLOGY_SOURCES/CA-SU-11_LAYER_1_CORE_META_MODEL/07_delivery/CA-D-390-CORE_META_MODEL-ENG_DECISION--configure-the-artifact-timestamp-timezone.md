---
atom_id: CA-D-390
ref_id: CA-D-390
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Artifact Timestamp Timezone
  dependencies:
  - CAPRMEDIO_MODEL <+ Project.Settings
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
relations:
  child_of:
  - CA-D-311
  - CA-R-1402@27
status: Active
version: 28
updated_at: 2026-11-04 09:30:21 +0400
carrier_destination:
  file:
    name: CA-D-390-CORE_META_MODEL-DECISION--configure-the-artifact-timestamp-timezone.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Configure the Artifact timestamp timezone

## Claim

### Prose Claim


the Artifact timestamp timezone setting in Project Settings.


the Project Settings **may** set `[artifact_timestamps].timezone` **to** `local`, `UTC`, **or** an IANA timezone name, with `local` as the default; **every** emitted `updated_at` value uses `YYYY-MM-DD HH:MM:SS +ZZZZ` with its explicit numeric UTC offset, **and** the setting supplies its timezone interpretation.
