---
atom_id: CA-E-006
ref_id: CA-E-006
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings
  dependencies:
  - CAPRMEDIO_MODEL <+ Project.Settings
  - Entity/Object/Continuant/Governing Objects/Governing Configuration
tier: 7
status: Active
version: 42
updated_at: "2026-11-07 15:28:42 +0400"
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-E-006-CORE_META_MODEL-EVAL_CASE--canonical-settings-selection.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-006-CORE_META_MODEL-EVAL_CASE--canonical-settings-selection.md
  source_atom_id: CA-E-006
  source_atom_revision: 42
  source_sha256: e09e184336f97a11af1634e13238b38c2ff4026fc2c0aa7c39cd8d28be74543b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Canonical Settings Selection

## Claim

Framework Instance Settings and Project Settings accept exactly their registered values, resolve deterministically, and fail closed on invalid or unknown selections. The Project Scope Unit Declaration and non-Project Scope Delegations own their respective current Scope Unit structure without duplicating Settings selections or requiring a structural Projection.

### Applicable conditions

1. Resolve the exact current Framework Instance Settings, Project Settings, and Default Settings Artifacts.
2. Accept only enabled catalog Artifact Types, Atom Content Roles and qualified Types, and Governance Origins.
3. Accept only `medium` or `high` Artifact creation strictness.
4. Accept only `silent` or `verbose` interaction reporting, and confirm that its effective default follows Framework Instance Settings without changing source Atoms or using Project Settings as reporting authority.
5. Validate initialization inputs against Project Settings field authority and Project Authority Modes against Framework Instance Settings field authority. Do not hard-code this Project's selected values in the Evaluation.
6. Reject unknown keys when the governing schema marks their table closed.
7. Confirm a second parse produces identical effective Settings and consumes the same selected structural Atom bytes and Settings revisions. Deleting a legacy structural Projection does not change those results.

### Acceptance criteria

Every valid selection resolves deterministically and every invalid selection fails closed with the exact key and allowed values.

### Failure disposition

Record a Concern naming the accepted invalid value, rejected valid value, or non-deterministic result, then stop settings-schema readiness.
