---
subjects:
  active: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  passive:
  - Scope Unit
  - Carrier
  - Project
  - Project.Settings
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-D-440
atom_id: CA-D-441@22
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 2
role: Delivery
form: Decision
---
## Summary
Encode the Project Structure document schema

## Claim scope
Project Structure TOML documents, including declared non-Project Scope Units **and** the implicit root Project.

## Claim

the Project Structure TOML document **must** contain the integer `schema_version = 1` **and** **`=1`** `scope_units` array of tables, with **`>=0`** rows for declared non-Project Scope Units. an empty array **must** use `scope_units = []`; nonempty arrays use `[[scope_units]]`. the root Project is implicit from Project Settings **and** **must not** have a duplicate row. unknown top-level keys, unknown row keys, duplicate TOML keys, **and** unsupported schema versions **must** be rejected rather than ignored. document comments **may** explain authority **and** retained readability fields, **without** introducing additional authoritative fields.
