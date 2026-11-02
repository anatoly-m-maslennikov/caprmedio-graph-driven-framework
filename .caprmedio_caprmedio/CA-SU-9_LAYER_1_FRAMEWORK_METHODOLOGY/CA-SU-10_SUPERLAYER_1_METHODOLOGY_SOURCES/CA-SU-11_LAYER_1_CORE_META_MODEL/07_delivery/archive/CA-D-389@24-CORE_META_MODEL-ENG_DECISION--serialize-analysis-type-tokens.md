---
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Analysis/Type'
  passive:
  - Carrier
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-389@24
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Analysis Type Tokens

## Claim scope

the serialization of Analysis Type tokens in an Analysis Atom File Carrier filename.

## Claim

an Analysis Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Rationale: `RATIONALE`.
- External Analysis Report: `EXTERNAL_ANALYSIS_REPORT`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.
