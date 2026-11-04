---
atom_id: CA-R-2003
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Node.**
  passive:
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Property Occurrences
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
version: 17
updated_at: 2026-11-04 18:25:15 +0400
tier: 1
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-2003@17-draft-CORE_META_MODEL--require-exactly-one-immediate-bearer-for-each-dependent-entity-occurrence.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Require exactly one immediate bearer for each dependent Entity occurrence

## Claim

### Prose Claim


Declared Property occurrences and their direct IS_PROPERTY_OF connections.


Every declared Property occurrence must have exactly one immediate bearer, identified by one outgoing direct IS_PROPERTY_OF connection to that bearer. A source establishes dependence independently of whether the edge is present, so a missing edge fails this requirement. The named Selection “Property Occurrences” selects those declared occurrences; it does not infer dependence from edges or create a bearer connection.

## Semantics

Property is the proposed kind `Node.**`, grounded in bearer dependence through IS_PROPERTY_OF. Its lexical Term is separately defined at `Term//Property`. Classifying an occurrence in that kind does not invent a bearer edge or treat a missing edge as proof of independence. The Property occurrence has identity qualified by its immediate bearer; the Property definition supplies its value Format and direct-value cardinality. The bearer-Relation count is distinct from the number of values a Property allows.

## Details

This Rule applies to every Property in the Node.** branch. The named Selection “Property Occurrences” selects source-declared occurrences independently of whether their IS_PROPERTY_OF edge exists. Missing required bearer edges remain failures; this Rule does not infer or create edges.
