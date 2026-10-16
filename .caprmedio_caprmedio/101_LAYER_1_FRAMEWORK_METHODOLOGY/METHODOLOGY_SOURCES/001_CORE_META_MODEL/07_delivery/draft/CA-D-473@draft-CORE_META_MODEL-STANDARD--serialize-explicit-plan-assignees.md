---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Plan.Assignee"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Plan", "Entity/Continuant/Object/Atom/Content Role: Plan.Assignee", "Entity/Carrier/File Carrier"]
version: 7
updated_at: "2026-10-16 12:03:33 +0000"
relations: {"relates_to": ["CA-R-1584", "CA-R-1585"]}
atom_id: "CA-D-473@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize explicit Plan Assignees

## Scope

explicit Plan Assignee overrides in Plan File Carriers.

## Claim

a Plan File Carrier **may** serialize **`=1`** explicit Assignee override as top-level frontmatter `assignee`; omission **must** preserve CA-R-1585-CORE_META_MODEL-GENERAL-REQUIREMENT--default-plan-work-assignment-to-an-ai-agent for its own work rather than copying the default.

## Details
