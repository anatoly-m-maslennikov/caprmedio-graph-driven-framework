---
atom_id: CA-M-453
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
version: 3
updated_at: 2026-11-02 00:18:22 +0400
subjects:
  active: Term//Property
  passive:
  - Term
  - Entity/Property
  - CFEL <+ Relation//IS_PROPERTY_OF
  - CFEL <+ Relation//HAS_PROPERTY
  - 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Method)/(.Type: Term Definition)'
relations: {}
role: Method
form: Term Definition
---
## Summary

Define Property

## Claim scope

The reusable lexical Term `Property` in Entity definitions, immediate-bearer
Relations, qualified Subject Paths, and authored content.

## Claim

Property **means** an Entity whose identity depends on its immediate bearer and
whose direct bearer Relation is IS_PROPERTY_OF from that Property to the
bearer. This Claim explicitly introduces the lexical Term instance `Property`
at `Term//Property`.

## Semantics

The Term names the entity kind `Entity/Property`; it is not that entity kind
itself. `Property ((IS_PROPERTY_OF)) Bearer` states the direct Relation, and
`Bearer.Property` is its bearer-to-Property dot display. HAS_PROPERTY is the
strict derived inverse, not an independently stored reverse fact.

A bearer may itself be a Property, so a qualified expression such as
`bearer.property.status` remains permitted. This lexical meaning adds no generic lifecycle or update rule. The structural
Property Definition governs the approved acyclicity constraint on
IS_PROPERTY_OF, including self-loops. A Property is not another name for a YAML field; applicable
Delivery rules determine its representation.

## Details

Property is the sole canonical Term for this meaning. The R / Entity Definition
defines the `Entity/Property` kind, its immediate-bearer cardinality, no
separate Carrier, and direct-value Format/cardinality; this M / Term Definition
owns only the reusable lexical meaning. It introduces no separate Term group,
Terms Graph, projection, parser rule, runtime behavior, or Current-source
change.

The role-only Draft marker allocates no canonical Method identity. Adoption
requires the pending Entity root and Term governance declarations, the
structural Property definition, the Relation Definitions, and normal
identity/lifecycle checks. This Draft supplies no evidence that those effects
occurred.

### Pending governing declarations

- [Term kind and inherited structure](../../04_requirement/draft/CA-R-1318@30-draft-CORE_META_MODEL-DEFINITION--define-term.md).
- [Property kind](../../04_requirement/draft/CA-R-1193@23-draft-CORE_META_MODEL-DEFINITION--define-property.md).
- [IS_PROPERTY_OF Relation](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-is-property-of.md).
- [HAS_PROPERTY Relation](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-has-property.md).
- [Method Type Term Definition](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-method-type-term-definition.md).
- [Dedicated Method meaning owner](../../04_requirement/draft/CA-R-1319@26-draft-CORE_META_MODEL--define-governed-term.md).

These links identify pending Draft dependencies, not Current admission.
