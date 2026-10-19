---
subjects:
  governs: "Atom/Content Role: Requirement/Type"
  depends_on:
    - "Carrier"
version: 10
updated_at: "2026-10-18 07:18:35 +0400"
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
  source_atom_revision: 10
  source_sha256: d1613fea2cf59dcaab3ef820d05cd4f2a2c0f4ec2b55241388a717ec04ede7c8
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
