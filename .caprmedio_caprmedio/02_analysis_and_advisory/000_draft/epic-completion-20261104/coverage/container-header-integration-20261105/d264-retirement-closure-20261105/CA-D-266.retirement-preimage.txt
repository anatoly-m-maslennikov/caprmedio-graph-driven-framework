---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Carrier/Directory
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
---
## Summary

Prohibit Persisting Derived Containment

## Claim

### Prose Claim


`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting.


`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting **must not** be persisted as independent relation declarations.

## Details

This prohibition applies when canonical Carrier nesting already owns the containment fact. It does not ban an independently authored direct IS_CONTAINED_BY fact whose authority is the child's admitted relation declaration rather than nesting. Do not maintain both as independent sources for the same fact. CONTAINS remains a derived inverse in either representation and is not independently authored.
