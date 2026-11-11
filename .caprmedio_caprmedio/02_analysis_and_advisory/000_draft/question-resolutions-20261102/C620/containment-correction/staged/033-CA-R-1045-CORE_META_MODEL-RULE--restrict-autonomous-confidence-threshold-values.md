---
subjects:
  active: Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
  passive: []
version: 26
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-R-1044
atom_id: CA-R-1045
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Restrict Autonomous Confidence Threshold values

## Claim scope

Autonomous Confidence Threshold values.

## Claim

**every** Autonomous Confidence Threshold **must** be an integer percentage **`>=0`** **and** **`<=100`**. resolve its effective value from the applicable source under CA-M-271; the methodology **must not** restrict that value **to** a closed list of preferred percentages.
