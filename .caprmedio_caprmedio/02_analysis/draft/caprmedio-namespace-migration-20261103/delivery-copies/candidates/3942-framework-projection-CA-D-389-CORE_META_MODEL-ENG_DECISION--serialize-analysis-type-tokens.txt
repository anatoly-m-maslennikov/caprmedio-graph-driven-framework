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
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-389-CORE_META_MODEL-ENG_DECISION--serialize-analysis-type-tokens.md
  source_atom_id: CA-D-389
  source_atom_revision: 27
  source_sha256: 5ae311e1763c70b2d35d1eada0a3c03ef27003d030e549eab0e076c65204e39e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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

