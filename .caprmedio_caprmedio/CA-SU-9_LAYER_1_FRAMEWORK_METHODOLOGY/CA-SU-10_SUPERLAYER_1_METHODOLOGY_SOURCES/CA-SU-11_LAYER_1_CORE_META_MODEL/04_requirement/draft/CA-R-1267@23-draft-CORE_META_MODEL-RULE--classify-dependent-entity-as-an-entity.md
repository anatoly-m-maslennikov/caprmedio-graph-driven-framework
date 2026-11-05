---
atom_id: CA-R-1267@23-draft
ref_id: CA-R-1267@23-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: Entity/Dependent Entity
  dependencies:
  - Entity
  - Entity/Term//Dependent Entity
  - Entity/Graph Syntax > Relation//IS_BORNE_BY
tier: 1
status: Draft
version: 23
updated_at: 2026-10-29 21:54:09 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
## Summary

Classify Dependent Entity as an Entity

## Claim scope

the `Entity/Dependent Entity` kind and its relation to Entity.

## Claim

`Entity/Dependent Entity` **must** be NARROWER_THAN `Entity`.

## Details

`Entity/Dependent Entity` names an Entity kind; its `/` path expresses
specialization. `Entity/Term//Dependent Entity` names the reusable lexical
Term used to write that kind and other qualified entity names. The Term is not
the kind, and mentioning or parsing the Term does not introduce an Entity
occurrence.

An `Entity/Dependent Entity` occurrence has an immediate bearer identified by
an outgoing direct IS_BORNE_BY Relation to that bearer. This Rule classifies
the kind; the Relation Definition supplies relation meaning and the separate
bearer-cardinality Rule supplies the occurrence constraint.

### Withdrawn preparation — Property consolidation

The Property kind is defined directly under Entity by R1193's successor. This former separate Dependent Entity classification preparation is redundant after the Operator's consolidation decision. Current R1267 remains unchanged until an explicitly governed adoption disposition. The prior preparation is retained as historical review evidence. Do not promote this Draft as written or treat this marker as Current-source retirement.
