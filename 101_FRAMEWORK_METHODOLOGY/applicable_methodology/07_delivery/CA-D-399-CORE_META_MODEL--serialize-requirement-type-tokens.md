---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Requirement/Type"
  depends_on:
    - "Entity/Carrier"
version: 12
updated_at: "2026-10-20 15:50:37 +0400"
relations: {}
atom_id: "CA-D-399"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-399-CORE_META_MODEL--serialize-requirement-type-tokens.md
  source_atom_id: CA-D-399
  source_atom_revision: 12
  source_sha256: 3b6da68ce83a92d8cd8ff73be5ba232452b0a3c7b27c4b47dfce73de06b3ab90
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Requirement Type Tokens

## Scope

the serialization of Requirement Type tokens in a Requirement Atom File Carrier filename.

## Claim

a Requirement Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Constraint: `CONSTRAINT`.
- Boundary: `BOUNDARY`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.

## Details
