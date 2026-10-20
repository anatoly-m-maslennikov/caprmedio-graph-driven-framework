---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Concern/Type"
  depends_on:
    - "Entity/Carrier"
version: 12
updated_at: "2026-10-19 15:55:44 +0400"
relations: {}
atom_id: "CA-D-401"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-401-CORE_META_MODEL--serialize-concern-type-tokens.md
  source_atom_id: CA-D-401
  source_atom_revision: 12
  source_sha256: 16e606d2af30cba865ccb141a68253d3c694b4d4d02316f650b09ee4c0ef9e78
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Concern Type Tokens

## Scope

the serialization of Concern Type tokens in a Concern Atom File Carrier filename.

## Claim

a Concern Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Question: `QUESTION`.
- Problem: `PROBLEM`.
- Risk: `RISK`.
- Opportunity: `OPPORTUNITY`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.

## Details
