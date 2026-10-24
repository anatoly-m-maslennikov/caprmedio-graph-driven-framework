---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Concern/Type'
  depends_on:
  - Subject/Engineering/Carrier
version: 15
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-D-401@15
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
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
