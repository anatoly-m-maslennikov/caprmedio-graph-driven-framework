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
status: Active
version: 37
updated_at: 2026-11-04 22:22:34 +0400
carrier_destination:
  file:
    name: CA-R-1318-DECLARATION--define-term.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define Term

## Claim

### Prose Claim

A Term is a reusable word or phrase component of entity expressions and authored content. Its Project-specific meaning remains consistent across uses and is owned by its active Method/Form Term Definition. Vocabulary Terms are lexical items, not graph Nodes merely because they are used as words. A Term has one Name.

Use the full admitted canonical expression when identifying or comparing an entity. Reusing a Term within distinct expressions neither makes those expressions synonymous nor establishes a Relation between their referents. Literal source quotations and code identifiers are not automatically renamed. A lexical Term and an Entity whose complete name uses that Term have distinct targets and meaning owners.

### Formal Claim

```CFEL
# model
Term.*[in (Name)]{::1};

Term.** {::1}((IS_PROPERTY_OF)) (Term, Term.**);
(Term, Term.**) {::0+}((HAS_PROPERTY)) Term.**;

# instances
Term//$term;
$term.** {::1}((IS_PROPERTY_OF)) ($term, $term.**);
($term, $term.**) {::0+}((HAS_PROPERTY)) $term.**;
```

## Semantics

A Term provides a reusable word or phrase; its full context supplies the expression in which it appears.
