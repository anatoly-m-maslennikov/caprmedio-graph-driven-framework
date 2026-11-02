---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Requirement/Type"
  depends_on:
    - "Entity/Carrier"
version: 12
updated_at: "2026-10-20 15:50:37 +0400"
relations: {}
atom_id: CA-D-399@12
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 11
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
