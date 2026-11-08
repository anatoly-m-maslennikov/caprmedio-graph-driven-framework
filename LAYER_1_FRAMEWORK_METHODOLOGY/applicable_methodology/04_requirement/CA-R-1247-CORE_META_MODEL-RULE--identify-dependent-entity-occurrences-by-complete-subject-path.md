---
atom_id: CA-R-1247
ref_id: CA-R-1247
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Property
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ CFEL
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
tier: 1
status: Active
version: 24
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1247-CORE_META_MODEL-RULE--identify-dependent-entity-occurrences-by-complete-subject-path.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1247-CORE_META_MODEL-RULE--identify-dependent-entity-occurrences-by-complete-subject-path.md
  source_atom_id: CA-R-1247
  source_atom_revision: 24
  source_sha256: ab4e29daa98c74eb0e22772581008689bc7863879b6d57dc51e1c9497da79880
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Identify Dependent-Entity Occurrences by Complete Subject Path

## Claim

### Prose Claim


`Entity/Property` occurrences, their immediate bearers, and their
complete Subject Paths.


**every** `Entity/Property` occurrence **must** derive its
source-admitted bearer-qualified identity from its complete Subject Path
**without** imposing one global ordinal position on a reusable Term. Its
outgoing direct IS_PROPERTY_OF Relation identifies its immediate bearer. Distinct
modeled entities **must** use distinct complete canonical names, while repeated
references **to** the same entity **must** retain its same complete canonical
name.

## Details

The complete Subject Path preserves source-admitted bearer qualification.
Ordinal position and display placement do not create entity identity.
Qualification is part of the complete property name used for collision checks.
A repeated display or reference of one entity remains the same entity, and
parsing a name does not introduce another graph entity.

`Entity/Property` is the Entity kind governed by this Rule.
`Term//Property` is its reusable lexical Term; the Term is not the
Entity kind or an occurrence. The direct IS_PROPERTY_OF Relation runs from the
Property occurrence to its bearer. The separate bearer-cardinality Rule owns
the exactly-one constraint; this Rule owns only the complete-path identity.

The inherited Summary and filename identify the predecessor Draft only. They
are historical lineage metadata, not an admitted lexical alias, entity kind,
or Relation token. This Draft introduces neither a new Selection name nor a
rename of a Current carrier.

The contextual topic/code spellings `atom.id` and `projection.id` distinguish their respective ID Properties; they are not alternative complete canonical Subject names or case-folded aliases. Authored Subjects use their full admitted expressions. `ID` is reusable and the terminal label need not be globally unique. Shared `Unit` components remain permitted in `Scope Unit` and `Code Unit`. This preserves complete-path identity without imposing disjoint lexical components or a new global ordinal position.
