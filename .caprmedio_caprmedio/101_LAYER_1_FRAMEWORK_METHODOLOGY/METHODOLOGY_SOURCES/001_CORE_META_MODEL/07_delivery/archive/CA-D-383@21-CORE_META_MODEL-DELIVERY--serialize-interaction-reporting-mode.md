---
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Framework Settings
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Project.Framework Settings.Interaction.Reporting Mode
version: 21
updated_at: 2026-10-24 01:37:42 +0400
relations:
  child_of:
  - CA-D-361
  relates_to:
  - CA-R-1628
  - CA-R-1750
atom_id: CA-D-383@21
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize Interaction Reporting Mode

## Scope

an explicit instance reporting default **in** the Framework Instance Settings TOML Carrier.

## Claim

an explicit instance reporting default **in** the Framework Instance Settings TOML Carrier **must** use `reporting_mode` **in** the `[interaction]` section, using an allowed value governed by CA-R-1628-CORE_META_MODEL-REQUIREMENT--allow-silent-and-verbose-reporting-modes.

## Details
