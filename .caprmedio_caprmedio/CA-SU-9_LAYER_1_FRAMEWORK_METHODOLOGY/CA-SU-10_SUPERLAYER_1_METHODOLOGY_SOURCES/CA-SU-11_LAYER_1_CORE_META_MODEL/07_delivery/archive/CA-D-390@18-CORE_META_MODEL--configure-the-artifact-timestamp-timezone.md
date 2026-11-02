---
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Framework Settings.Artifact Timestamp Timezone
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Subject/Engineering/Carrier
version: 18
updated_at: 2026-10-24 00:38:25 +0400
relations:
  child_of:
  - CA-D-311
  - CA-R-1402
atom_id: CA-D-390@18
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Configure the Artifact timestamp timezone

## Scope

the Artifact timestamp timezone setting in Framework Instance Settings.

## Claim

the Framework Instance Settings Artifact **may** set `[artifact_timestamps].timezone` **to** `local`, `UTC`, **or** an IANA timezone name, with `local` as the default; **every** emitted `updated_at` value uses `YYYY-MM-DD HH:MM:SS +ZZZZ` with its explicit numeric UTC offset, **and** the setting supplies its timezone interpretation.

## Details
