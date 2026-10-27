---
subjects:
  governs: Subject/Engineering/Autonomous Confidence Threshold
version: 16
updated_at: 2026-10-24 10:48:25 +0400
relations:
  child_of:
  - CA-R-1044
atom_id: CA-R-1045@16
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Restrict Autonomous Confidence Threshold values

## Scope

Autonomous Confidence Threshold values.

## Claim

**every** Autonomous Confidence Threshold **must** be an integer percentage **`>=0`** **and** **`<=100`**. resolve its effective value from the applicable source under CA-M-271; the methodology **must not** restrict that value **to** a closed list of preferred percentages.

## Details
