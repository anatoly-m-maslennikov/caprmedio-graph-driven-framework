---
subjects:
  active: CAPRMEDIO_MODEL <+ Term
  passive:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Term.Name
  - CAPRMEDIO_MODEL <+ Term//Term
  - CAPRMEDIO_MODEL <+ Term//Empty
  - CAPRMEDIO_MODEL <+ Term//ID
  - CAPRMEDIO_MODEL <+ Term//Entity
  - CAPRMEDIO_MODEL <+ Entity/Property
  - CAPRMEDIO_MODEL <+ Term//Property
version: 33
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
atom_id: CA-R-1318
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1318-CORE_META_MODEL-DEFINITION--define-term.md
  source_atom_id: CA-R-1318
  source_atom_revision: 33
  source_sha256: 35014effa7d6d7ab7f57e2b5dddae8523f151b2208842d0e97bfe1661107e273
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Term

## Claim

### Formal Claim

```CFEL
# model
Term.*[in (Name)]{:1}
```

### Prose Claim

A Term is a reusable word or phrase component of entity expressions and authored content. Its Project-specific meaning remains consistent across uses and is owned by its active Method/Form Term Definition. Vocabulary Terms are lexical items, not graph Nodes merely because they are used as words. A Term has one Name.

Use the full admitted canonical expression when identifying or comparing an entity. Reusing a Term within distinct expressions neither makes those expressions synonymous nor establishes a Relation between their referents. Literal source quotations and code identifiers are not automatically renamed. A lexical Term and an Entity whose complete name uses that Term have distinct targets and meaning owners.

## Semantics

A Term provides a reusable word or phrase; its full context supplies the expression in which it appears.
