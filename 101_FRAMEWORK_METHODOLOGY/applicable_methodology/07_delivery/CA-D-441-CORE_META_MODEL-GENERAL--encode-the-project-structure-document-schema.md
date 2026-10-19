---
subjects:
  governs: "Entity/Continuant/Node/Project.Structure"
  depends_on:
    ["Entity/Continuant/Node/Scope Unit", "Entity/Carrier", "Entity/Continuant/Node/Project", "Entity/Continuant/Node/Project.Settings"]
version: 9
updated_at: "2026-10-18 07:25:43 +0400"
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
  source_atom_revision: 9
  source_sha256: 061443e54c94fce8ca530eb5ea5f8b884988cf266deb5c1b4f157eb4cd249615
  original_relations_sha256: 4ea2c90f06a6f75bf31082400ec9137e19d06cdfa3e8d7bded3331399aa3453a
---
# Summary
Encode the Project Structure document schema

## Scope
Project Structure TOML documents, including declared non-Project Scope Units **and** the implicit root Project.

## Claim

the Project Structure TOML document **must** contain the integer `schema_version = 1` **and** **`=1`** `scope_units` array of tables, with **`>=0`** rows for declared non-Project Scope Units. an empty array **must** use `scope_units = []`; nonempty arrays use `[[scope_units]]`. the root Project is implicit from Project Settings **and** **must not** have a duplicate row. unknown top-level keys, unknown row keys, duplicate TOML keys, **and** unsupported schema versions **must** be rejected rather than ignored. document comments **may** explain authority **and** retained readability fields, **without** introducing additional authoritative fields.

## Details
