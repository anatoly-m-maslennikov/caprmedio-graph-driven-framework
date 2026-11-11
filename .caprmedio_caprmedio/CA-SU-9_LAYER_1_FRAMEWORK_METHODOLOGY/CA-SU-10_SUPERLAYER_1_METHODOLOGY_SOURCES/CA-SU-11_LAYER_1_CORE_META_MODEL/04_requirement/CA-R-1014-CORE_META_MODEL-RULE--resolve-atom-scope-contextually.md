---
atom_id: CA-R-1014
ref_id: CA-R-1014
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
status: Active
version: 40
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1014-CORE_META_MODEL-RULE--resolve-atom-scope-contextually.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Resolve Atom Scope Contextually

## Claim

### Prose Claim


Atom Scope.


an Atom Scope **must** include its current Scope Unit Scope **or** its Author's registered Operator fallback under CA-D-657-CORE_META_MODEL-DELIVERY--use-economical-yaml-frontmatter, its **`=1`** Atom Governed Subject, **and** **any** explicit Scope constraints **in** its Claim.
