---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Evaluation/Type"
  depends_on:
    - "Entity/Carrier"
version: 11
updated_at: "2026-10-18 07:18:45 +0400"
relations: {}
atom_id: "CA-D-400"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-400-CORE_META_MODEL--serialize-evaluation-type-tokens.md
  source_atom_id: CA-D-400
  source_atom_revision: 11
  source_sha256: 553d5f855e03774d129422599c552c415ce359d0b37579e14861fe9cd5904e79
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
