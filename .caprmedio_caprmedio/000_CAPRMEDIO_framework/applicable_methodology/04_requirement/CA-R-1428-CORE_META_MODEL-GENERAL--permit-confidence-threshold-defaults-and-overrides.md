---
subjects:
  governs: "Confidence Threshold.Source"
  depends_on:
    ["Confidence Threshold", "Entity/Continuant/Actor/Type: Operator", "Atom/Content Role: Plan/Type: Plan", "Hub Atom", "Property", "Entity/Continuant/Object/Project.Framework Settings"]
version: 11
updated_at: "2026-10-15 18:42:52 +0000"
relations:
  child_of:
    - "CA-R-1427"
atom_id: "CA-R-1428"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1428-CORE_META_MODEL-GENERAL--permit-confidence-threshold-defaults-and-overrides.md
  source_atom_id: CA-R-1428
  source_atom_revision: 11
  source_sha256: 4cc058aa26f3b306987d88904b451ef685acb6268af2b80c9b1851de288498ff
  original_relations_sha256: b9ddd5f70b093dcd4d45ab17e845ea6ec539b7ffb12ebf514ff45f075ec5936d
---
# Summary

Permit confidence-threshold defaults and overrides

## Scope

the source of a Confidence Threshold value.

## Claim

a Confidence Threshold **must** take its value from applicable direct Operator input, an explicit Property on the current Plan, the nearest enclosing Hub Plan with an explicit Property, **or** the Framework Instance Settings default; the Hub chain follows `IS_DECOMPOSITION_OF`, **not** Label spelling.

## Details
