---
subjects:
  governs: "Atom/Content Role: Method/Type"
  depends_on:
    - "Entity/Carrier"
version: 11
updated_at: "2026-10-19 11:46:46 +0000"
relations: {}
atom_id: "CA-D-404@draft"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
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
