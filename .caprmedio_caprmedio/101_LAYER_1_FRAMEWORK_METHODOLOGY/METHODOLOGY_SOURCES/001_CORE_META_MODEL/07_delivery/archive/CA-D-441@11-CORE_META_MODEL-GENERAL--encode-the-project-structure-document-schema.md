---
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Structure
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Project
  - Subject/Domain/Node/Continuant/Project.Settings
version: 11
updated_at: 2026-10-23 03:14:50 +0400
relations:
  child_of:
  - CA-D-440
atom_id: CA-D-441@11
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
status: Archived
author: Anatoly Maslennikov
global_tier: 10
---
# Summary
Encode the Project Structure document schema

## Scope
Project Structure TOML documents, including declared non-Project Scope Units **and** the implicit root Project.

## Claim

the Project Structure TOML document **must** contain the integer `schema_version = 1` **and** **`=1`** `scope_units` array of tables, with **`>=0`** rows for declared non-Project Scope Units. an empty array **must** use `scope_units = []`; nonempty arrays use `[[scope_units]]`. the root Project is implicit from Project Settings **and** **must not** have a duplicate row. unknown top-level keys, unknown row keys, duplicate TOML keys, **and** unsupported schema versions **must** be rejected rather than ignored. document comments **may** explain authority **and** retained readability fields, **without** introducing additional authoritative fields.

## Details
