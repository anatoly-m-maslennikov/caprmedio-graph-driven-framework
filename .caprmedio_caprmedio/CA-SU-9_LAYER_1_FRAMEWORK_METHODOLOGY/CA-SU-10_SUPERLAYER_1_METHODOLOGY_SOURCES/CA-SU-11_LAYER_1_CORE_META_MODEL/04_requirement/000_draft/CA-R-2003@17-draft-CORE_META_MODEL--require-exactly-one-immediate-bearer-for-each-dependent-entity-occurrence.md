---
atom_id: CA-R-2003
ref_id: CA-R-2003@17-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Node.**
  dependencies:
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
tier: 1
status: Draft
version: 17
updated_at: 2026-11-05 04:29:34 +0400
carrier_destination:
  file:
    name: CA-R-2003@17-draft-RULE--require-exactly-one-immediate-bearer-for-each-dependent-entity-occurrence.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---
## Summary

Require exactly one immediate bearer for each dependent Entity occurrence

## Claim

### Prose Claim


Model Property occurrences selected by `Node.**` and their direct IS_PROPERTY_OF connections.


Every source-declared model Property occurrence selected by `Node.**` must have exactly one immediate bearer, identified by one outgoing direct IS_PROPERTY_OF connection to that bearer. A source establishes dependence independently of whether the edge is present, so a missing edge fails this requirement. Select source-declared Property occurrences independently of whether their bearer edges exist; do not infer dependence from edges or create a bearer connection.

## Semantics

`Node.**` selects Properties of Node and its narrower branch, grounded in bearer dependence through IS_PROPERTY_OF. Property instances are distinct from model Properties; their HAS_INSTANCE permissions are declared separately. Its lexical Term is separately defined at `Term//Property`. Identifying a source-declared Property occurrence does not invent a bearer edge or treat a missing edge as proof of independence. The Property occurrence has identity qualified by its immediate bearer; the Property definition supplies its value Format and direct-value cardinality. The bearer-Relation count is distinct from the number of values a Property allows.

## Details

This Rule applies to source-declared Properties covered by `Node.**`. Identify the source-declared occurrences independently of their IS_PROPERTY_OF edges. Missing required bearer edges remain failures; this Rule does not infer or create edges.
