---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Assignee'
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Assignee'
  - CAPRMEDIO_MODEL <+ Carrier/File
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
  source_sha256: 8e6d9f83ba2ca878ac12332f46fbabb714970f81285695369d5ba06079ff8dc5
  original_relations_sha256: 0accbc26fe2e34a4d38cd81d11579f68b92b90359fd940fc42073d82b28a8919
---
## Summary

Serialize explicit Plan Assignees

## Claim

### Prose Claim


explicit Plan Assignee overrides in Plan File Carriers.


a Plan File Carrier **may** serialize **`=1`** explicit Assignee override as top-level frontmatter `assignee`; omission **must** preserve CA-R-1585-CORE_META_MODEL-RULE--default-plan-work-assignment-to-an-ai-agent for its own work rather than copying the default.
