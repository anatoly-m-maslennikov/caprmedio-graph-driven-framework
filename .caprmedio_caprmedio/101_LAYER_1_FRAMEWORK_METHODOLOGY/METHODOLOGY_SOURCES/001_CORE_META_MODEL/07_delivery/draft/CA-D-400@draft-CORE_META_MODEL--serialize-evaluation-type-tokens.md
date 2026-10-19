---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Evaluation/Type"
  depends_on:
    - "Entity/Carrier"
version: 12
updated_at: "2026-10-19 11:46:46 +0000"
relations: {}
atom_id: "CA-D-400@draft"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Evaluation Type Tokens

## Scope

the serialization of Evaluation Type tokens in an Evaluation Atom File Carrier filename.

## Claim

an Evaluation Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- QA Case: `QA_CASE`.
- Evaluation Control: `EVALUATION_CONTROL`.
- Evaluation Approach: `EVALUATION_APPROACH`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.

## Details
