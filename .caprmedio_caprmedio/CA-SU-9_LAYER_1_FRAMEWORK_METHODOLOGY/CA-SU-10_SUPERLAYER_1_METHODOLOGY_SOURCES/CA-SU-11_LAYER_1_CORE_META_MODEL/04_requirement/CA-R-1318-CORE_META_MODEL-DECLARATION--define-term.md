---
atom_id: CA-R-1318
ref_id: CA-R-1318
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Term
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Term//Entity
  - CAPRMEDIO_MODEL <+ Term.Name
  - CAPRMEDIO_MODEL <+ Term//Term
  - CAPRMEDIO_MODEL <+ Term//Empty
  - CAPRMEDIO_MODEL <+ Term//ID
  - CAPRMEDIO_MODEL <+ Term//Property
tier: 1
status: active
version: 38
updated_at: '2026-11-13T05:35:59.629049+00:00'
carrier_destination:
  file:
    name: CA-R-1318-CORE_META_MODEL-DECLARATION--define-term.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define Term

## Claim

### Prose Claim

A Term is a reusable word or phrase component of entity expressions and authored content. Its Project-specific meaning remains consistent across uses and is owned by its active Method/Form Term Definition. Vocabulary Terms are lexical items, not graph Nodes merely because they are used as words. A Term has one Name.

Use the full admitted canonical expression when identifying or comparing an entity. Reusing a Term within distinct expressions neither makes those expressions synonymous nor establishes a Relation between their referents. Literal source quotations and code identifiers are not automatically renamed. A lexical Term and an Entity whose complete name uses that Term have distinct targets and meaning owners.

### Formal Claim

```python
# model
allowed_children(address='Term', names=('Name',), occurrences='1')
relation(source='Term.**', source_count='1', name='IS_PROPERTY_OF', target='(Term, Term.**)')
relation(source='(Term, Term.**)', source_count='0+', name='HAS_PROPERTY', target='Term.**')
# instances
subject_path(address='Term//$term')
relation(source='$term.**', source_count='1', name='IS_PROPERTY_OF', target='($term, $term.**)')
relation(source='($term, $term.**)', source_count='0+', name='HAS_PROPERTY', target='$term.**')
```

## Semantics

A Term provides a reusable word or phrase; its full context supplies the expression in which it appears.
