---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory").Header.Form
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier
version: 27
updated_at: 2026-11-02 19:33:47 +0400
atom_id: CA-D-389
ref_id: CA-D-389
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-D-389-CORE_META_MODEL-DECISION--serialize-analysis-type-tokens.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
---
## Summary

Serialize Analysis Type Tokens

## Claim

### Prose Claim


the serialization of Analysis & Advisory Form tokens in an Analysis & Advisory Atom File Carrier filename.


an Analysis & Advisory Atom File Carrier **must** serialize the following Form components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Rationale: `RATIONALE`.
- External Analysis Report: `EXTERNAL_ANALYSIS_REPORT`.

these mappings govern filename representation; they do **not** rename a Form, admit a new Form, **or** prescribe a YAML Form value.

