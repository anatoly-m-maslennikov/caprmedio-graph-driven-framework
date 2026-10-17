---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Analysis/Type"
  depends_on:
    ["Entity/Carrier"]
version: 10
updated_at: "2026-10-16 12:09:24 +0000"
relations: {}
atom_id: "CA-D-389"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-389-CORE_META_MODEL--serialize-analysis-type-tokens.md
  source_atom_id: CA-D-389
  source_atom_revision: 10
  source_sha256: ff5cf6b73e5912b80506543110bfe155e6ee6206cf3a2628472194e32ea15370
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Analysis Type Tokens

## Scope

the serialization of Analysis Type tokens in an Analysis Atom File Carrier filename.

## Claim

an Analysis Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Rationale: `RATIONALE`.
- External Analysis Report: `EXTERNAL_ANALYSIS_REPORT`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.

## Details
