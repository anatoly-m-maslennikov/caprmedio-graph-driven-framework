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
  - CAPRMEDIO_MODEL <+ Atom.Header.Topics.Main Subject
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1014-CORE_META_MODEL-RULE--resolve-atom-scope-contextually.md
  source_atom_id: CA-R-1014
  source_atom_revision: 40
  source_sha256: 67d6d03e23ee56c2652e6703c26bb99f40a8afde378f745176a496e01482a46d
  original_relations_sha256: 26aa04726746f899586a0393ece67890930c69f69ffcdcc6cc042d360740bb1b
---
## Summary

Resolve Atom Scope Contextually

## Claim

### Prose Claim


Atom Scope.


an Atom Scope **must** include its current Scope Unit Scope **or** its Author's registered Operator fallback under CA-D-657-CORE_META_MODEL-DELIVERY--use-economical-yaml-frontmatter, its **`=1`** Atom Governed Subject, **and** **any** explicit Scope constraints **in** its Claim.
