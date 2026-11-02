---
atom_id: CA-R-draft
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: Entity/Dependent Entity
  depends_on:
  - Entity
  - Entity/Term//Dependent Entity
  - Entity/Graph Syntax > Relation//IS_BORNE_BY
  - Entity/Graph Syntax > Relation//BEARS
version: 1
updated_at: 2026-10-29 21:54:09 +0400
relations: {}
tier: 1
---
## Summary

Define Dependent Entity

## Claim scope

The Entity kind whose identity requires an immediate bearer.

## Claim

A Dependent Entity is an Entity at `Entity/Dependent Entity` whose identity requires exactly one immediate bearer. Its direct bearer-dependence fact is an outgoing IS_BORNE_BY Relation from the Dependent Entity to that bearer.

### Formal claim

```text
Entity/Dependent Entity
```

## Semantics

The dot in a Subject Path addresses a bearer-to-dependent path, for example `Atom.Status`. The direct Relation is in the opposite direction: `Status ((IS_BORNE_BY)) Atom`. BEARS is the declared derived inverse; a reverse fact is not stored independently.

The relation condition applies to each Dependent Entity occurrence; the kind node itself is not asserted to be borne by Entity. This kind classifies bearer dependence only. It does not state that a Dependent Entity is a Continuant, an Occurrent, a Property, or a mutually exclusive alternative to every other Entity kind. Generic DEPENDS_ON neither establishes nor replaces IS_BORNE_BY. An absent edge in an incomplete view does not establish independence; the applicable conformance Rule determines whether a declared occurrence has its required edge.

## Details

The Operator explicitly admitted `Entity/Dependent Entity` while retaining the distinct lexical Term target `Entity/Term//Dependent Entity`. This Requirement Atom defines the Entity kind and its relation-bound identity condition. It does not supply the Term's lexical meaning, create a Term group, or redefine the `IS_BORNE_BY` Relation itself.

The separate Term Definition Method is the dedicated lexical owner for the reusable Term `Dependent Entity`; its wording must remain consistent with this structural definition. Exactly one Entity Definition defines this Entity kind under CA-R-2278. This role-only Draft assigns no canonical identity and performs no promotion or runtime change.

### Pending governing declarations

- [Entity root with the Term branch](CA-R-1248@24-draft-CORE_META_MODEL-DEFINITION--define-entity.md).
- [Term kind and inherited structure](CA-R-1318@30-draft-CORE_META_MODEL-DEFINITION--define-term.md).
- [Method Type Term Definition](CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-method-type-term-definition.md).
- [Dedicated Method meaning owner](CA-R-1319@26-draft-CORE_META_MODEL--define-governed-term.md).

These links identify pending Draft dependencies, not Current admission.

### Withdrawn preparation — Property consolidation

R1193's successor defines the selected Entity/Property kind. This separate Dependent Entity kind Draft would duplicate the concept under the superseded name and is withdrawn from the active packet. It has no assigned canonical identity to transfer or retire. The prior preparation is retained as historical review evidence. Do not promote this Draft as written or treat this marker as Current-source retirement.
