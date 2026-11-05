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
---
## Summary

Serialize explicit Plan Assignees

## Claim

### Prose Claim


explicit Plan Assignee overrides in Plan File Carriers.


a Plan File Carrier **may** serialize **`=1`** explicit Assignee override as top-level frontmatter `assignee`; omission **must** preserve CA-R-1585-CORE_META_MODEL-RULE--default-plan-work-assignment-to-an-ai-agent for its own work rather than copying the default.
