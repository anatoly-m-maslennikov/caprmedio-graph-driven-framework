---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Carrier/Directory
version: 30
updated_at: 2026-11-05 03:53:43 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-D-266
status: Draft
tier: 1
role: Delivery
form: Decision
carrier_destination:
  file:
    name: CA-D-266@30-draft-CORE_META_MODEL-DECISION--prohibit-persisting-derived-containment.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/draft
---
## Summary

Prohibit Persisting Derived Containment

## Claim

### Prose Claim


`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting.


`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting **must not** be persisted as independent relation declarations.

## Details

This prohibition applies when canonical Carrier nesting already owns a non-Atom containment fact. An Atom stores its own container in `Header.Container`; its logical parent is not inferred from a directory. For non-Atom facts, this does not ban an independently authored direct `IS_CONTAINED_BY` whose authority is the child's admitted Relation declaration rather than nesting. Do not maintain two independent sources for the same fact. `CONTAINS` remains a derived inverse and is not independently authored.
