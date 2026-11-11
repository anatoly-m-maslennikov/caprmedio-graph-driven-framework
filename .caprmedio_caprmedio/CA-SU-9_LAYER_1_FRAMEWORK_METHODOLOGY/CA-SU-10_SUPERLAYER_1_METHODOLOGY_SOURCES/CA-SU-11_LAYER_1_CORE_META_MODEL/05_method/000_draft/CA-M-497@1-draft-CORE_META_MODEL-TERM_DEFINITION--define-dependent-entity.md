---
atom_id: CA-M-497
ref_id: CA-M-497@1-draft
container:
  scope_unit: CA-SU-11
role: Method
form: Term Definition
topics:
  main_subject: Entity/Term//Dependent Entity
  dependencies:
  - Entity/Term
  - Entity/Dependent Entity
  - Entity/Graph Syntax > Relation//IS_BORNE_BY
  - Entity/Graph Syntax > Relation//BEARS
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Method/Type: Term Definition'
tier: 1
status: Draft
version: 1
updated_at: 2026-10-29 21:54:09 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
## Summary

Define Dependent Entity

## Claim scope

The reusable lexical Term `Dependent Entity` in Entity definitions, bearer-dependence Rules, and qualified Subject Paths.

## Claim

Dependent Entity **means** an Entity whose identity requires an immediate bearer and whose direct bearer-dependence Relation is IS_BORNE_BY from that Entity to the bearer. This Claim explicitly introduces the lexical Term instance named Dependent Entity at `Entity/Term//Dependent Entity`.

## Semantics

The Term names the entity kind `Entity/Dependent Entity`; it is not that entity kind itself. In a Subject Path, `Bearer.Dependent` uses the dot to address the dependent through its bearer, while `Dependent ((IS_BORNE_BY)) Bearer` states the direct Relation. BEARS is the declared derived inverse, not an independently stored reverse fact.

This meaning does not classify the Entity as a Property, Continuant, Occurrent, or a member of a disjoint taxonomy. It does not infer bearer dependence from generic DEPENDS_ON or from a missing edge in an incomplete view.

## Details

This Draft records the Operator-confirmed distinction between `Entity/Dependent Entity` and `Entity/Term//Dependent Entity`. The former is structurally defined by the paired Entity Definition Draft; this Method Atom owns the reusable word or phrase's lexical meaning. It neither redefines IS_BORNE_BY nor creates a separate Term group, Terms Graph, projection, parser rule, or runtime behavior.

The role-only Draft marker allocates no canonical Method identity. Adoption requires the pending Entity root and Term governance declarations, the structural Entity Definition, and normal identity/lifecycle checks. This Draft supplies no evidence that those effects occurred.

### Pending governing declarations

- [Entity root with the Term branch](../../04_requirement/draft/CA-R-1248@24-draft-CORE_META_MODEL-DEFINITION--define-entity.md).
- [Term kind and inherited structure](../../04_requirement/draft/CA-R-1318@30-draft-CORE_META_MODEL-DEFINITION--define-term.md).
- [Dependent Entity kind](../../04_requirement/draft/CA-R-2993@1-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-dependent-entity.md).
- [Method Type Term Definition](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-method-type-term-definition.md).
- [Dedicated Method meaning owner](../../04_requirement/draft/CA-R-1319@26-draft-CORE_META_MODEL--define-governed-term.md).

These links identify pending Draft dependencies, not Current admission.

### Withdrawn preparation — Property consolidation

The new Property Term Definition Draft owns Entity/Term//Property. This separate Dependent Entity lexical Draft would preserve a superseded synonym and is withdrawn from the active packet. Its role-only marker has allocated no canonical Method identity. The prior preparation is retained as historical review evidence. Do not promote this Draft as written or treat this marker as Current-source retirement.
