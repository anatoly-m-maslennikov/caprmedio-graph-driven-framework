---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Assignee'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Assignee'
  - Entity/Carrier/File
version: 22
updated_at: 2026-10-29 07:17:26 +0400
relations:
  delivery_for:
  - CA-R-1585
atom_id: CA-D-473@22
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize explicit Plan Assignees

## Scope

explicit Plan Assignee overrides in Plan File Carriers.

## Claim

a Plan File Carrier **may** serialize **`=1`** explicit Assignee override as top-level frontmatter `assignee`; omission **must** preserve CA-R-1585-CORE_META_MODEL-RULE--default-plan-work-assignment-to-an-ai-agent for its own work rather than copying the default.

## Details
