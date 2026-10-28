---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings.Interaction.Reporting Mode
version: 27
updated_at: 2026-10-27 19:59:24 +0400
relations:
  child_of:
  - CA-D-361
  depends_on:
  - CA-R-1628
atom_id: CA-D-383
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 6
type: Eng Decision
---
# Summary

Serialize Interaction Reporting Mode

## Scope

an explicit instance reporting default **in** the Framework Instance Settings TOML Carrier.

## Claim

an explicit instance reporting default **in** the Framework Instance Settings TOML Carrier **must** use `reporting_mode` **in** the `[interaction]` section, using an allowed value governed by CA-R-1628-CORE_META_MODEL-RULE--allow-silent-and-verbose-reporting-modes.

## Details
