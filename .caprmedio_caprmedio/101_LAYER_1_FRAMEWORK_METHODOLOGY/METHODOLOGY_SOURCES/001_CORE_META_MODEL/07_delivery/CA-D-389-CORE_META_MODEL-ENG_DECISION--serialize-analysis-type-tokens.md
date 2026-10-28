---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Analysis/Type'
  depends_on:
  - Subject/CAPRMEDIO/Carrier
version: 20
updated_at: 2026-10-27 19:59:24 +0400
relations: {}
atom_id: CA-D-389
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
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
