---
atom_id: CA-M-453
status: Active
tier: 1
version: 5
updated_at: 2026-11-04 18:28:33 +0400
subjects:
  active: CAPRMEDIO_MODEL <+ Term//Property
  passive:
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ Entity/Property
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_PROPERTY
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)/(.Header.Form := Term Definition)
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
role: Method
form: Term Definition
carrier_destination:
  file:
    name: CA-M-453-CORE_META_MODEL-TERM_DEFINITION--define-property.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-453-CORE_META_MODEL-TERM_DEFINITION--define-property.md
  source_atom_id: CA-M-453
  source_atom_revision: 5
  source_sha256: fb9d0205cf7d78c1adc9b44326a43ec6d793058862c834439cc0e58d25c659d4
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

Define Property

## Claim

### Prose Claim


The reusable lexical Term `Property` in Entity definitions, immediate-bearer
Relations, qualified Subject Paths, and authored content.


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
