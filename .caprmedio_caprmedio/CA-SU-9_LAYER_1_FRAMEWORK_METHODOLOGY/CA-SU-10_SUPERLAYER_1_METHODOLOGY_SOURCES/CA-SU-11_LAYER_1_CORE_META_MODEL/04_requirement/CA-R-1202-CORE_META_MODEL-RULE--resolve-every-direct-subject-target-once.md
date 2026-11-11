---
atom_id: CA-R-1202
ref_id: CA-R-1202
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context.Topics
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//GOVERNS
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//DEPENDS_ON
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Topics
tier: 1
status: Active
version: 30
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1202-CORE_META_MODEL-RULE--resolve-every-direct-subject-target-once.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Resolve Every Direct Subject Target Once

## Claim

### Prose Claim


direct GOVERNS and DEPENDS_ON values in an Atom's Subjects Property.


**every** direct GOVERNS value **and** **every** direct DEPENDS_ON value **in** an Atom's Subjects Property **must** resolve **to** **`=1`** canonical Subject Target. resolution **must not** require an intermediate Subject/Entity **or** Subject/Reference Property **or** a repeated target-kind field.
