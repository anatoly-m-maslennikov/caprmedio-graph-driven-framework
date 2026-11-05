---
atom_id: CA-D-342
ref_id: CA-D-342
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Project Goal)
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier/File
tier: 3
status: Active
version: 29
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-D-342-CORE_META_MODEL-DECISION--serialize-external-project-goal-references.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Serialize External Project Goal References

## Claim

### Prose Claim


references to Current and historical external Project Goal Atoms.


**every** Reference **to** a Current external Project Goal Atom **must** use its canonical Current Atom ID, not its current Carrier filename stem.

A Reference **to** an Archived external Project Goal Atom **must** use its canonical Atom ID qualified once with its unchanged numeric Version when historical identity is required. A Current Project Goal reference **must not** omit the canonical ID or fall back to a filename stem; this Delivery creates no ID-less Current exception.
