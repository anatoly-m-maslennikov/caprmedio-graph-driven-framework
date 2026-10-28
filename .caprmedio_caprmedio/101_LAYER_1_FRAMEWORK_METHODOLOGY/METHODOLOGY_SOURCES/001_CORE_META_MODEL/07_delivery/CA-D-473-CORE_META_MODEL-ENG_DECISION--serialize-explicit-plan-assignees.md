---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Assignee'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Assignee'
  - Subject/CAPRMEDIO/Carrier/File
version: 21
updated_at: 2026-10-27 19:59:25 +0400
relations:
  delivery_for:
  - CA-R-1585
atom_id: CA-D-473
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
