---
atom_id: CA-D-473
ref_id: CA-D-473
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Assignee'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Assignee'
  - CAPRMEDIO_MODEL <+ Carrier/File
tier: 3
relations:
  delivery_for:
  - CA-R-1585
status: Active
version: 25
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-473-CORE_META_MODEL-DECISION--serialize-explicit-plan-assignees.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-473-CORE_META_MODEL-ENG_DECISION--serialize-explicit-plan-assignees.md
  source_atom_id: CA-D-473
  source_atom_revision: 25
  source_sha256: 1179a27fbf9d754f09eaf0277e9de9b846d7c9f3ed81e0b0e38ab9abfcdf1ec1
  original_relations_sha256: 0accbc26fe2e34a4d38cd81d11579f68b92b90359fd940fc42073d82b28a8919
---
## Summary

Serialize explicit Plan Assignees

## Claim

### Prose Claim


explicit Plan Assignee overrides in Plan File Carriers.


a Plan File Carrier **may** serialize **`=1`** explicit Assignee override as top-level frontmatter `assignee`; omission **must** preserve CA-R-1585-CORE_META_MODEL-RULE--default-plan-work-assignment-to-an-ai-agent for its own work rather than copying the default.
