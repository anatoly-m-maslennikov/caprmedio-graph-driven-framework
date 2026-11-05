---
atom_id: CA-D-268
ref_id: CA-D-268
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 3
status: Active
version: 30
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-D-268-CORE_META_MODEL-DECISION--serialize-authored-direct-relations-on-their-owning-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Serialize Authored Direct Relations on Their Owning Atoms

## Claim

### Prose Claim


Authored direct semantic relations.


**every** authored direct semantic relation **must** be serialized once under `relations.<RELATION_KIND>` on the Atom that owns its declared direction as a nonempty unordered collection of unique canonical target references; target position **must not** add, remove, **or** alter a direct relation **or** dependency. source-file target order is nonsemantic; validation **must not** require canonical sorting **or** order normalization. each Relation Kind's direction, endpoint validity **and** other declared semantics remain applicable.

## Details

Serialize only the Relation Kind's declared direct direction, never a second declaration for its derived inverse. For containment, the child carries IS_CONTAINED_BY with the parent reference; CONTAINS is a derived parent view and is not serialized on the parent. A change confined to the child does not request a parent-carrier write or a new parent Version. The relation's spelling does not determine which direction is direct.

This policy governs authored relation declarations. When canonical Carrier nesting already supplies a containment fact under CA-D-264, do not add a second independent declaration for the same fact; CA-D-266 governs that derived view. This source contract does not itself register a new runtime relation key.
