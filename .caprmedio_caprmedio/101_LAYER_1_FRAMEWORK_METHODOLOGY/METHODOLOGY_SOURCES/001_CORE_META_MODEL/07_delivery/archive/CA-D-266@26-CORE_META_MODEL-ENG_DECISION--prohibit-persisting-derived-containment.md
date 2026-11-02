---
subjects:
  governs: Entity/Graph Syntax > Relation
  depends_on:
  - Entity/Graph Syntax > Relation
  - Entity/Carrier/Directory
version: 26
updated_at: 2026-10-29 07:45:29 +0400
relations: {}
atom_id: CA-D-266@26
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Decision
---
## Summary

Prohibit Persisting Derived Containment

## Claim scope

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting.

## Claim

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting **must not** be persisted as independent relation declarations.

## Details

This prohibition applies when canonical Carrier nesting already owns the containment fact. It does not ban an independently authored direct IS_CONTAINED_BY fact whose authority is the child's admitted relation declaration rather than nesting. Do not maintain both as independent sources for the same fact. CONTAINS remains a derived inverse in either representation and is not independently authored.
