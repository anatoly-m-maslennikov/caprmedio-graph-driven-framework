---
atom_id: CA-R-1247
ref_id: CA-R-1247@25-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Node.**
  dependencies:
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ CFEL
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
tier: 1
status: Draft
version: 25
updated_at: 2026-11-05 04:29:34 +0400
carrier_destination:
  file:
    name: CA-R-1247@25-draft-RULE--identify-dependent-entity-occurrences-by-complete-subject-path.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Identify Dependent-Entity Occurrences by Complete Subject Path

## Claim

### Prose Claim


Model Property occurrences selected by `Node.**`, their immediate bearers, and their complete Subject Paths.


**every** model Property occurrence selected by `Node.**` **must** derive its
source-admitted bearer-qualified identity from its complete Subject Path
**without** imposing one global ordinal position on a reusable Term. Its
outgoing direct IS_PROPERTY_OF Relation identifies its immediate bearer. Distinct
model Property occurrences **must** use distinct complete canonical names, while repeated
references **to** the same occurrence **must** retain its same complete canonical
name.

## Details

The complete Subject Path preserves source-admitted bearer qualification.
Ordinal position and display placement do not create entity identity.
Qualification is part of the complete property name used for collision checks.
A repeated display or reference of one model Property remains the same Property, and
parsing a name does not introduce another graph entity.

`Node.**` selects Properties of Node and its narrower branch. Property instances are distinct from their model Properties; the applicable Declarations govern their HAS_INSTANCE links.
`Term//Property` is its reusable lexical Term; the Term is not the
selector or an occurrence. The direct IS_PROPERTY_OF Relation runs from the
Property occurrence to its bearer. The separate bearer-cardinality Rule owns
the exactly-one constraint; this Rule owns only the complete-path identity.


The contextual topic/code spellings `atom.id` and `projection.id` distinguish their respective ID Properties; they are not alternative complete canonical Subject names or case-folded aliases. Authored Subjects use their full admitted expressions. `ID` is reusable and the terminal label need not be globally unique. Shared `Unit` components remain permitted in `Scope Unit` and `Code Unit`. This preserves complete-path identity without imposing disjoint lexical components or a new global ordinal position.
