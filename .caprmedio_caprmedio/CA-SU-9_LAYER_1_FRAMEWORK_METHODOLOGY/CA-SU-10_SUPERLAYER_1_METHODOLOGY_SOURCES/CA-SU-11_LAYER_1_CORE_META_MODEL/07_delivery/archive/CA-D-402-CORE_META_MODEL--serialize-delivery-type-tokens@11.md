---
subjects:
  governs: "Atom/Content Role: Delivery/Type"
  depends_on:
    - "Entity/Carrier"
version: 11
updated_at: "2026-10-19 15:55:45 +0400"
relations: {}
atom_id: "CA-D-402"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Delivery Type Tokens

## Scope

the serialization of Delivery Type tokens in a Delivery Atom File Carrier filename.

## Claim

a Delivery Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283-CORE_META_MODEL-DELIVERY--serialize-project-owned-markdown-atom-filenames **and** CA-D-284-CORE_META_MODEL-DELIVERY--serialize-filename-token-case:

- Release Definition: `RELEASE_DEFINITION`.
- Environment Definition: `ENVIRONMENT_DEFINITION`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.

## Details
