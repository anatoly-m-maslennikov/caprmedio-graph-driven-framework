---
atom_id: CA-R-1014
ref_id: CA-R-1014@41-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Topics.Main Subject
  - CAPRMEDIO_MODEL <+ Atom.Content
tier: 3
relations:
  child_of:
  - CA-R-1596
status: Draft
version: 41
updated_at: 2026-11-05 13:47:13 +0400
carrier_destination:
  file:
    name: CA-R-1014@41-draft-RULE--resolve-atom-scope-contextually.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---
## Summary

Resolve Atom Scope Contextually

## Claim

### Prose Claim


Atom Scope.


an Atom Scope **must** include the Scope Unit resolved from its `Header.Container` chain, its **`=1`** Atom Governed Subject, **and** **any** explicit Scope constraints **in** its Claim. Follow Atom container references until a Scope Unit ID is reached; predefined `world` (`CA-SU--1`) is a valid Scope Unit.
