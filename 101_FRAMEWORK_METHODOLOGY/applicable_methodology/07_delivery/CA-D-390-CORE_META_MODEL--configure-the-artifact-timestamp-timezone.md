---
subjects:
  governs: "Entity/Continuant/Object/Project.Framework Settings.Artifact Timestamp Timezone"
  depends_on:
    ["Entity/Continuant/Object/Project.Framework Settings", "Entity/Carrier"]
version: 12
updated_at: "2026-10-16 12:09:26 +0000"
relations:
  child_of:
    - "CA-D-311"
    - "CA-R-1402"
atom_id: "CA-D-390"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-390-CORE_META_MODEL--configure-the-artifact-timestamp-timezone.md
  source_atom_id: CA-D-390
  source_atom_revision: 12
  source_sha256: 6ef8df8d7fb892786b7fa61033a8b67c7e0950ffbc6e8f8e4707cc3ed7f73a46
  original_relations_sha256: ad300b03e304b312918653de943d5511c34469376b727407e31a64564f30817e
---
# Summary

Configure the Artifact timestamp timezone

## Scope

the Artifact timestamp timezone setting in Framework Instance Settings.

## Claim

the Framework Instance Settings Artifact **may** set `[artifact_timestamps].timezone` **to** `local`, `UTC`, **or** an IANA timezone name, with `local` as the default; **every** emitted `updated_at` value uses `YYYY-MM-DD HH:MM:SS +ZZZZ` with its explicit numeric UTC offset, **and** the setting supplies its timezone interpretation.

## Details
