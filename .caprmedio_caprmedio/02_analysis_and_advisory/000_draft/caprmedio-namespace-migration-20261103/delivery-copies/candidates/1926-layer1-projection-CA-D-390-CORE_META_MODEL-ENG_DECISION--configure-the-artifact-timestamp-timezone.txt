---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Artifact Timestamp Timezone
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO <+ MODEL <+ Carrier
version: 27
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-D-311
  - CA-R-1402@27
atom_id: CA-D-390
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-390-CORE_META_MODEL-ENG_DECISION--configure-the-artifact-timestamp-timezone.md
  source_atom_id: CA-D-390
  source_atom_revision: 27
  source_sha256: 5e804eafa5d7c2be34c4f83342f41de697cfd521afc128ed84b3c08d20741231
  original_relations_sha256: 670262d86fa94914f8b8bd77ee8a8e752d93a7ac0d854cc505c5e89351ba40ee
---
## Summary

Configure the Artifact timestamp timezone

## Claim scope

the Artifact timestamp timezone setting in Framework Instance Settings.

## Claim

the Framework Instance Settings Artifact **may** set `[artifact_timestamps].timezone` **to** `local`, `UTC`, **or** an IANA timezone name, with `local` as the default; **every** emitted `updated_at` value uses `YYYY-MM-DD HH:MM:SS +ZZZZ` with its explicit numeric UTC offset, **and** the setting supplies its timezone interpretation.
