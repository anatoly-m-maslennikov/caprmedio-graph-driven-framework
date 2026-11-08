---
atom_id: CA-R-1629
ref_id: CA-R-1629
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern).Header.Priority
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern)
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
tier: 3
status: Active
version: 39
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1629-CORE_META_MODEL-RULE--effective-priority-conflict-selection.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1629-CORE_META_MODEL-RULE--effective-priority-conflict-selection.md
  source_atom_id: CA-R-1629
  source_atom_revision: 39
  source_sha256: 8e3645c65080bd039337d4056fb09f5816669bd30ddcedc3d7b1cfb565d1a001
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Effective priority conflict selection

## Claim

### Prose Claim


priority-conflict selection for Concern Atoms.


a Concern Atom has **`=1`** Priority value: High, Medium, **or** Low.

direct comparison of Concern Atoms **must** follow the admissible Operator-selected priority model governed by CA-R-1487:

- use the selected model, its effective parameters, **and** its active criteria.
- Scope Unit ancestry **must not** add an implicit Priority increment.
- **if** the model **or** its application does **not** justify a selection, leave the conflict unresolved **and** ask the Operator.

the Framework Instance Settings Artifact exposes **`=2`** selection modes:

- `ask_always`, the default, explains the conflict **and** asks the operator; **and**
- `auto_by_effective_priority`, which **may** select **only** one uniquely eligible winner.

the selection mode **must** ask the Operator **if** ties, incomparable structure, uncertainty, **or** multiple winners occur. mutually unsatisfiable external obligations stop for Operator **or** external resolution. PRMEDO Tier precedence, deterministic replacement, explicit scoped override, stale-view routing, **and** Implementation drift follow their own semantics rather than this selection mode.
