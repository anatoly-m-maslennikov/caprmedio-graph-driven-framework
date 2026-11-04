---
atom_id: CA-R-2625
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings.Confidence.Semantic Resolution Threshold
version: 2
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-04 05:21:15 +0400
---

## Summary

Define Semantic Resolution Threshold

## Claim

### Formal Claim

```CFEL
# model
Project.Settings.Confidence.Semantic Resolution Threshold: {:0..1};

Project.Settings.Confidence.Semantic Resolution Threshold.*[]{:0}
```

### Prose Claim


An absent override uses the governed default.

