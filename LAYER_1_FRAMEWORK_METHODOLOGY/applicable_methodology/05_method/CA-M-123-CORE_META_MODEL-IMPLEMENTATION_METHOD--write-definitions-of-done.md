---
atom_id: CA-M-123
ref_id: CA-M-123
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
tier: 6
relations:
  child_of:
  - CA-M-113
  - CA-M-122
  - CA-R-1581@23
  - CA-R-1583@26
status: Active
version: 31
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-M-123-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-definitions-of-done.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-123-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-definitions-of-done.md
  source_atom_id: CA-M-123
  source_atom_revision: 31
  source_sha256: 7b14c2a2520bb301343c224cd3d0cb52af4b4b4c5eef8ffbbe83ce577c54df54
  original_relations_sha256: f4e336e4d641a310c7347debd28bda8e85f49bc1e4112b1b7f49fd05272a6d97
---
## Summary

Write Definitions of Done

## Claim

### Prose Claim


authoring one Definition of Done.


**to** write one Definition of Done, the Author **must** perform **all** of:

1. begin the falsification condition expression with: the Plan is **not** Done **if**.
2. make **every** atomic condition observable **and** decidable.
3. enclose **every** composite condition **and** **every** function argument **in** explicit parentheses.
4. evaluate the condition expression according **to** CA-M-122-CORE_META_MODEL-IMPLEMENTATION_METHOD--evaluate-condition-expressions.
