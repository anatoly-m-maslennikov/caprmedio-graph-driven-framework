---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := "Analysis & Advisory").Form
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier
version: 27
updated_at: 2026-11-02 19:33:47 +0400
relations: {}
atom_id: CA-D-389
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Analysis Type Tokens

## Claim scope

the serialization of Analysis & Advisory Form tokens in an Analysis & Advisory Atom File Carrier filename.

## Claim

an Analysis & Advisory Atom File Carrier **must** serialize the following Form components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Rationale: `RATIONALE`.
- External Analysis Report: `EXTERNAL_ANALYSIS_REPORT`.

these mappings govern filename representation; they do **not** rename a Form, admit a new Form, **or** prescribe a YAML Form value.

