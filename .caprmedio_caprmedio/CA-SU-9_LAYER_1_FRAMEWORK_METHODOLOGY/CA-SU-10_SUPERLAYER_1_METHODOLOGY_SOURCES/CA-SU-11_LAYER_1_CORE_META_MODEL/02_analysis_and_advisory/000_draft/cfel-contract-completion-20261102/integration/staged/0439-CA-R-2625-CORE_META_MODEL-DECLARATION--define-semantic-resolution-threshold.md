---
atom_id: CA-R-2625
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Project.Settings.Confidence.Semantic Resolution Threshold
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 07:49:21 +0400
---

## Summary

Define Semantic Resolution Threshold

## Claim

An absent override uses the governed default.

```CFEL
Project.Settings.Confidence.Semantic Resolution Threshold{:0..1}: [int]{:1};
Project.Settings.Confidence.Semantic Resolution Threshold.*[]{:0}
```
