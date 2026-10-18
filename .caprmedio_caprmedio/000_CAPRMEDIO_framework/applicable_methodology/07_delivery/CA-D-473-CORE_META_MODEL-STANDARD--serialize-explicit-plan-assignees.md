---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Plan.Assignee"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Plan", "Entity/Continuant/Node/Atom/Content Role: Plan.Assignee", "Entity/Carrier/File Carrier"]
version: 8
updated_at: "2026-10-18 03:34:51 +0400"
relations: {"relates_to": ["CA-R-1584", "CA-R-1585"]}
atom_id: "CA-D-473"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-473-CORE_META_MODEL-STANDARD--serialize-explicit-plan-assignees.md
  source_atom_id: CA-D-473
  source_atom_revision: 8
  source_sha256: 2c63989a566b604cd36aec083996cd07d03014497765a7a4e2ecd5997c12de31
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize explicit Plan Assignees

## Scope

explicit Plan Assignee overrides in Plan File Carriers.

## Claim

a Plan File Carrier **may** serialize **`=1`** explicit Assignee override as top-level frontmatter `assignee`; omission **must** preserve CA-R-1585-CORE_META_MODEL-GENERAL-REQUIREMENT--default-plan-work-assignment-to-an-ai-agent for its own work rather than copying the default.

## Details
