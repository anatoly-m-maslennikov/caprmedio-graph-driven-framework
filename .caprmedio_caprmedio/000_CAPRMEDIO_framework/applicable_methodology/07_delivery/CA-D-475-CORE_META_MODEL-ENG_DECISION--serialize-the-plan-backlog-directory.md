---
atom_id: CA-D-475
ref_id: CA-D-475
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Status: Backlog'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Label'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Status'
  - CAPRMEDIO_MODEL <+ Carrier/Directory
tier: 3
status: Active
version: 24
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-475-CORE_META_MODEL-DECISION--serialize-the-plan-backlog-directory.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-475-CORE_META_MODEL-ENG_DECISION--serialize-the-plan-backlog-directory.md
  source_atom_id: CA-D-475
  source_atom_revision: 24
  source_sha256: 9064d741cfee4f3da654276bd23d3889b510080ac224a25997b67a78bf668fb6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize the Plan Backlog directory

## Claim

### Prose Claim


the Plan Backlog Directory and version-labeled Plan Carrier locations.


the Plan Backlog Directory **must** be `03_plan/001_backlog`; it is a Status container, **not** a Plan Atom. a Version-labeled Plan uses the ordinary Plan Carrier grammar under CA-D-469-CORE_META_MODEL-DELIVERY--serialize-plan-carrier-stems rather than an independently identified Version Plan Collection **or** special `version-<VERSION>` container.
