---
subjects:
  active: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Artifact Timestamp Timezone
  passive:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - Carrier
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
---
## Summary

Configure the Artifact timestamp timezone

## Claim scope

the Artifact timestamp timezone setting in Framework Instance Settings.

## Claim

the Framework Instance Settings Artifact **may** set `[artifact_timestamps].timezone` **to** `local`, `UTC`, **or** an IANA timezone name, with `local` as the default; **every** emitted `updated_at` value uses `YYYY-MM-DD HH:MM:SS +ZZZZ` with its explicit numeric UTC offset, **and** the setting supplies its timezone interpretation.
