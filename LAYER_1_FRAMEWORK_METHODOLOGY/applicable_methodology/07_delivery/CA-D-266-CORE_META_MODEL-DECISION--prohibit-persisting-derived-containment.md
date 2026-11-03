---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Relation
  - CAPRMEDIO <+ MODEL <+ Carrier/Directory
version: 29
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-D-266
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-266-CORE_META_MODEL-DECISION--prohibit-persisting-derived-containment.md
  source_atom_id: CA-D-266
  source_atom_revision: 29
  source_sha256: 9e8a486633ba614c85275205e05bd40c3823350d8c51a89c283ee2c587d15317
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Prohibit Persisting Derived Containment

## Claim scope

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting.

## Claim

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting **must not** be persisted as independent relation declarations.

## Details

This prohibition applies when canonical Carrier nesting already owns the containment fact. It does not ban an independently authored direct IS_CONTAINED_BY fact whose authority is the child's admitted relation declaration rather than nesting. Do not maintain both as independent sources for the same fact. CONTAINS remains a derived inverse in either representation and is not independently authored.
