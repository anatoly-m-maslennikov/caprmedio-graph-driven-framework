---
subjects:
  governs: "Framework Instance.Settings.Interaction.Reporting Mode: silent"
  depends_on:
    ["Framework Instance.Settings.Interaction.Reporting Mode", "Framework Instance.Settings.Interaction.Reporting Mode.Effects", "Framework Instance.Settings.Interaction.Reporting Mode.Mandatory Information", "Artifact", "Skill", "Project"]
version: 12
updated_at: "2026-10-15 12:19:54 +0000"
relations: {"relates_to":["CA-R-1628","CA-R-1439","CA-R-1440","CA-R-1558","CA-O-052","CA-R-1750"]}
atom_id: "CA-M-277"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Report **in** silent mode

## Scope

silent-mode reporting.

## Claim

**to** report **in** `silent` mode, answer exploratory input normally **and**, apart from the mandatory information governed by CA-R-1440-CORE_META_MODEL-GENERAL-REQUIREMENT--preserve-mandatory-information-in-every-reporting-mode, report **only** durable Artifacts **or** Project state that CAPRMEDIO created, updated, archived, committed, **or** **otherwise** changed; omit ordinary announcements of mode selection, workflow routing, Skill chaining, **and** gate transitions.

## Details
