---
atom_id: CA-R-2454@2
content_role: Requirement
type: Relation Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
version: 2
updated_at: 2026-10-30 14:13:08 +0400
subjects:
  governs: Entity/Graph Syntax <+ Relation//IS_PROPERTY_OF
  depends_on:
  - Entity/Property
  - Entity/Term//Property
  - Entity/Graph Syntax <+ Relation//HAS_PROPERTY
relations: {}
---
## Summary

Define IS_PROPERTY_OF Relation

## Claim scope

The direct Relation from a Property to its immediate bearer.

## Claim

IS_PROPERTY_OF is the direct Relation from Property to its immediate bearer.
It means that the Property's identity depends on that bearer. One stored direct
Relation fact is the source of the derived inverse HAS_PROPERTY; it does not
introduce an independently stored reverse fact.

### Formal claim

```text
Entity/Graph Syntax <+ Relation//IS_PROPERTY_OF
```

## Semantics

Each IS_PROPERTY_OF Relation instance has exactly two endpoints: its source
Property node or instance and its target immediate bearer node or instance.
IS_PROPERTY_OF classifies the Relation; it is not a third endpoint.
`Bearer.Property` preserves the dot display from
bearer to Property; it does not reverse the source-to-target direction of the
direct Relation.

The pending CA-R-1193 successor owns the Property Formal Constraint requiring
exactly one outgoing IS_PROPERTY_OF Relation per Property. In that Formal Constraint,
`{1}` counts outgoing Relation instances of Type IS_PROPERTY_OF for each
Property. It does not count distinct targets, specify Relation arity, or count
incoming edges. Direct-value Format and cardinality are independent of this
Relation Definition.

A Property may be the immediate bearer of another Property. The pending Property Definition governs the approved
acyclicity constraint on IS_PROPERTY_OF, including self-loops. This Relation
Definition adds no generic lifecycle restriction or cycle rule for other
Relation Types.

## Notation for subject

```text
.
```

## Details

Property is the canonical entity kind at `Entity/Property`; its lexical Term is
`Entity/Term//Property`. This Relation Definition does not define either one.

This Draft proposes IS_PROPERTY_OF as the replacement direct Relation for the
historical IS_BORNE_BY source in CA-R-1260. That provenance neither admits
IS_BORNE_BY as an alias nor repurposes CA-R-1260 or its Draft successor.

### Pending governing declarations

- [Property kind and Formal Constraint](CA-R-1193@23-draft-CORE_META_MODEL-DEFINITION--define-property.md).
- [Property lexical meaning](../../05_method/draft/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-property.md).
- [Derived inverse HAS_PROPERTY](CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-has-property.md).

These links identify pending Draft dependencies, not Current admission.

### Historical source snapshot

Exact predecessor carrier: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1260-CORE_META_MODEL-DEFINITION--define-is-borne-by.md`, Version 32, SHA-256 `5e974a0bb1c0e0da94906026b2f7777601cd14fb9b11837989099c6dd321698c`. This is lineage evidence for a fresh Relation identity, not authority admitting the new name.
