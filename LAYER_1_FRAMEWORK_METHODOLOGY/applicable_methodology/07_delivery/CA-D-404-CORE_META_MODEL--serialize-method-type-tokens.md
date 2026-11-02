---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Method/Type"
  depends_on:
    - "Entity/Carrier"
version: 12
updated_at: "2026-10-20 15:51:30 +0400"
relations: {}
atom_id: "CA-D-404"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-404-CORE_META_MODEL--serialize-method-type-tokens.md
  source_atom_id: CA-D-404
  source_atom_revision: 12
  source_sha256: d325fb012132fbc1bf9fc1c4a3985d59520c41cb60e8f0e5871a7d0e9bb5a0ea
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Method Type Tokens

## Scope

Method Atom File Carriers.

## Claim

a Method Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283-CORE_META_MODEL-CORE-DELIVERY--serialize-project-owned-markdown-atom-filenames **and** CA-D-284-CORE_META_MODEL-CORE-DELIVERY--serialize-filename-token-case:

- Implementation Method: `IMPLEMENTATION_METHOD`.
- Implementation Decision: `IMPLEMENTATION_DECISION`.
- External Implementation Method: `EXTERNAL_IMPLEMENTATION_METHOD`.
- Method Binding: `METHOD_BINDING`.

## Details

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.
