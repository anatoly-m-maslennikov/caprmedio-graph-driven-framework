---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Assignee'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Assignee'
  - Subject/Engineering/Carrier/File Carrier
version: 16
updated_at: 2026-10-24 10:48:25 +0400
relations:
  relates_to:
  - CA-R-1584
  - CA-R-1585
atom_id: CA-D-473@16
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

a Plan File Carrier **may** serialize **`=1`** explicit Assignee override as top-level frontmatter `assignee`; omission **must** preserve CA-R-1585-CORE_META_MODEL-REQUIREMENT--default-plan-work-assignment-to-an-ai-agent for its own work rather than copying the default.

## Details
