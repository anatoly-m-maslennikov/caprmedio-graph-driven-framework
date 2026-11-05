---
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Carrier/Directory
version: 30
updated_at: 2026-11-05 06:15:15 +0400
atom_id: CA-D-266
ref_id: CA-D-266@30-draft
status: Draft
tier: 1
role: Delivery
form: Decision
carrier_destination:
  file:
    name: CA-D-266@30-draft-DECISION--prohibit-persisting-derived-containment.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Prohibit Persisting Derived Containment

## Claim

### Prose Claim

The `IS_CONTAINED_BY` fact declared through an Atom’s `Header.Container` and the `CONTAINS` view derived from it must not be persisted as additional independent Relation declarations merely because Carrier placement is read back.

## Details

Carrier placement follows the declared Container. Its readback identifies the same containment fact; it does not establish another logical parent. An independently admitted direct `IS_CONTAINED_BY` fact remains governed by its own source. `CONTAINS` is the derived inverse and is not independently authored. Do not maintain two independent sources for the same fact.
