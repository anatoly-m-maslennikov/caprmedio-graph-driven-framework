---
subjects:
  active: CFEL > Relation
  passive:
  - CFEL > Relation
  - Carrier/Directory
version: 27
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-266@27
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 1
role: Delivery
form: Decision
---
## Summary

Prohibit Persisting Derived Containment

## Claim scope

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting.

## Claim

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting **must not** be persisted as independent relation declarations.

## Details

This prohibition applies when canonical Carrier nesting already owns the containment fact. It does not ban an independently authored direct IS_CONTAINED_BY fact whose authority is the child's admitted relation declaration rather than nesting. Do not maintain both as independent sources for the same fact. CONTAINS remains a derived inverse in either representation and is not independently authored.
