---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Concern/Type"
  depends_on:
    - "Entity/Carrier"
version: 11
updated_at: "2026-10-18 07:18:55 +0400"
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
  source_atom_revision: 11
  source_sha256: 45f75bcd2f436fa8fdef1e85a1d2ca37281e989ba138ee72197074035e809c38
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
