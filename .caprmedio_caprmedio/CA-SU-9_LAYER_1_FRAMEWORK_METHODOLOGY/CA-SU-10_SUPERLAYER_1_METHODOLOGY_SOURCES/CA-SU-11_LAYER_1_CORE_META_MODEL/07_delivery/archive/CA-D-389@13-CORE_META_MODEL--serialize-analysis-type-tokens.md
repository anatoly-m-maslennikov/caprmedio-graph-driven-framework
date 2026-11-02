---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Analysis/Type'
  depends_on:
  - Entity/Carrier
version: 13
updated_at: 2026-10-23 03:06:32 +0400
relations: {}
atom_id: CA-D-389@13
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 11
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
