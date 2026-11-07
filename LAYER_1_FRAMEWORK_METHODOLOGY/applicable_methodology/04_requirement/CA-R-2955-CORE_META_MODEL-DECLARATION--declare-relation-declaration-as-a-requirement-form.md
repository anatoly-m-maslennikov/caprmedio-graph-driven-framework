---
atom_id: CA-R-2955
ref_id: CA-R-2955
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Relation Declaration)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
tier: 3
status: Active
version: 1
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-R-2955-CORE_META_MODEL-DECLARATION--declare-relation-declaration-as-a-requirement-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2955-CORE_META_MODEL-DECLARATION--declare-relation-declaration-as-a-requirement-form.md
  source_atom_id: CA-R-2955
  source_atom_revision: 1
  source_sha256: eb8bcefcf2c1443680af58e1863b4b963bc99765eefbfc552afc0f295ff9fb73
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Relation Declaration as a Requirement Form

## Claim

### Prose Claim

This Form uses the Declaration contract.

### Formal Claim

```CFEL
# model
Atom//(.Header.Role := Requirement).Header.Form := Relation Declaration;
Atom//(.Header.Role := Requirement)//(.Header.Form := Relation Declaration)
```

## Semantics

A Relation Declaration defines a canonical binary Relation, its endpoint domains and applicable inverse aliases.
