---
atom_id: CA-R-2624
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings.Confidence.Necessary Information Threshold
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
---

## Summary

Define Necessary Information Threshold

## Claim

An absent override uses the governed default.

```CFEL
Project.Settings.Confidence.Necessary Information Threshold{:0..1}: [int]{:1};
Project.Settings.Confidence.Necessary Information Threshold.*[]{:0}
```
