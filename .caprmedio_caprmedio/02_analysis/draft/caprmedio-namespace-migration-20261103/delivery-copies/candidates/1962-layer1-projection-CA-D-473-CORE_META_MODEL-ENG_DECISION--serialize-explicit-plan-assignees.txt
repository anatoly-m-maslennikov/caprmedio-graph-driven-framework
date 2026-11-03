---
subjects:
  active: 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Assignee'
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Assignee'
  - CAPRMEDIO <+ MODEL <+ Carrier/File
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations:
  delivery_for:
  - CA-R-1585
atom_id: CA-D-473
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-473-CORE_META_MODEL-ENG_DECISION--serialize-explicit-plan-assignees.md
  source_atom_id: CA-D-473
  source_atom_revision: 25
  source_sha256: 5ba7ca0b49c34f3c04b5a532ba61ce57656d3e1ca8cc16d0f7770d7b0f8b4c19
  original_relations_sha256: 0accbc26fe2e34a4d38cd81d11579f68b92b90359fd940fc42073d82b28a8919
---
## Summary

Serialize explicit Plan Assignees

## Claim scope

explicit Plan Assignee overrides in Plan File Carriers.

## Claim

a Plan File Carrier **may** serialize **`=1`** explicit Assignee override as top-level frontmatter `assignee`; omission **must** preserve CA-R-1585-CORE_META_MODEL-RULE--default-plan-work-assignment-to-an-ai-agent for its own work rather than copying the default.
