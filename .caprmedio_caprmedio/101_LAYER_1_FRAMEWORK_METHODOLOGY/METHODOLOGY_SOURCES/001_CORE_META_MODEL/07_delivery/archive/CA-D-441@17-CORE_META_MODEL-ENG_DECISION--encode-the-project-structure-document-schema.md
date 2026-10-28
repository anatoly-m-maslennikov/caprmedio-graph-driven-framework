---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Project.Structure
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Carrier
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Settings
version: 17
updated_at: 2026-10-27 06:04:45 +0400
relations:
  child_of:
  - CA-D-440
atom_id: CA-D-441@17
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Eng Decision
---
# Summary
Encode the Project Structure document schema

## Scope
Project Structure TOML documents, including declared non-Project Scope Units **and** the implicit root Project.

## Claim

the Project Structure TOML document **must** contain the integer `schema_version = 1` **and** **`=1`** `scope_units` array of tables, with **`>=0`** rows for declared non-Project Scope Units. an empty array **must** use `scope_units = []`; nonempty arrays use `[[scope_units]]`. the root Project is implicit from Project Settings **and** **must not** have a duplicate row. unknown top-level keys, unknown row keys, duplicate TOML keys, **and** unsupported schema versions **must** be rejected rather than ignored. document comments **may** explain authority **and** retained readability fields, **without** introducing additional authoritative fields.

## Details
