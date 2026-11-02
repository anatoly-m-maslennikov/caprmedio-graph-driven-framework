---
subjects:
  governs: "Entity/Node/Continuant/Project.Structure"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit", "Entity/Carrier", "Entity/Node/Continuant/Project", "Entity/Node/Continuant/Project.Settings"]
version: 10
updated_at: "2026-10-19 15:55:47 +0400"
relations:
  child_of:
    - "CA-D-440"
atom_id: "CA-D-441"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-441-CORE_META_MODEL-GENERAL--encode-the-project-structure-document-schema.md
  source_atom_id: CA-D-441
  source_atom_revision: 10
  source_sha256: 008492e965f7af43ced2d6298d294775036e85b3d43b2228fd46325233ef0dfc
  original_relations_sha256: 4ea2c90f06a6f75bf31082400ec9137e19d06cdfa3e8d7bded3331399aa3453a
---
# Summary
Encode the Project Structure document schema

## Scope
Project Structure TOML documents, including declared non-Project Scope Units **and** the implicit root Project.

## Claim

the Project Structure TOML document **must** contain the integer `schema_version = 1` **and** **`=1`** `scope_units` array of tables, with **`>=0`** rows for declared non-Project Scope Units. an empty array **must** use `scope_units = []`; nonempty arrays use `[[scope_units]]`. the root Project is implicit from Project Settings **and** **must not** have a duplicate row. unknown top-level keys, unknown row keys, duplicate TOML keys, **and** unsupported schema versions **must** be rejected rather than ignored. document comments **may** explain authority **and** retained readability fields, **without** introducing additional authoritative fields.

## Details
