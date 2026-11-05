---
atom_id: CA-R-1688
ref_id: CA-R-1688
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.Path
tier: 3
relations:
  child_of:
  - CA-M-447
  - CA-R-1776
status: Active
version: 39
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1688-CORE_META_MODEL-RULE--scope-path-does-not-change-semantic-coordinates.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1688-CORE_META_MODEL-RULE--scope-path-does-not-change-semantic-coordinates.md
  source_atom_id: CA-R-1688
  source_atom_revision: 39
  source_sha256: 7a506698a241e1ae2a642ba083acff0f3099dc66c2aa04e6b5968799c1111656
  original_relations_sha256: b8dcfd73d6f0c11b7eaf8d81fb734512e58f3895c78965eff1dcb2306ef36af2
---
## Summary

Scope path does not change semantic coordinates

## Claim

### Prose Claim


Scope paths in the current project.


Scope path is a project-relative address containing **`>=0`** operator-labeled structural scopes ordered from broader parent **to** narrower child.

the current project is ambient. Scope **may** govern ownership, applicability, **and** inheritance, but it never changes stable Artifact identity, Artifact form, Content Role, **or** Governance locus.
