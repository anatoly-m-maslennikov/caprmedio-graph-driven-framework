---
subjects:
  governs: "Entity/Continuant/Object/Project.Framework Settings.Interaction.Reporting Mode.Mandatory Information"
  depends_on:
    ["Entity/Continuant/Object/Project.Framework Settings.Interaction.Reporting Mode", "Entity/Continuant/Actor/Type: Operator"]
version: 9
updated_at: "2026-10-15 18:15:08 +0000"
relations:
  child_of:
    - "CA-R-1402"
  relates_to:
    - "CA-R-1420"
atom_id: "CA-R-1440@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Preserve mandatory information in every reporting mode

## Scope

mandatory information reported by **every** interaction reporting mode.

## Claim

**every** interaction reporting mode **must** report the following mandatory information:

- blockers **and** failed operations;
- ambiguity that requires Operator input;
- permission **or** approval requests;
- safety-critical information;
- material deviations from the requested outcome.

## Details
