---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Assignee'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Assignee'
  - Entity/Carrier/File
version: 24
updated_at: 2026-10-29 10:13:51 +0400
relations:
  delivery_for:
  - CA-R-1585
atom_id: CA-D-473@24
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Serialize explicit Plan Assignees

## Claim scope

explicit Plan Assignee overrides in Plan File Carriers.

## Claim

a Plan File Carrier **may** serialize **`=1`** explicit Assignee override as top-level frontmatter `assignee`; omission **must** preserve CA-R-1585-CORE_META_MODEL-RULE--default-plan-work-assignment-to-an-ai-agent for its own work rather than copying the default.
