---
atom_id: CA-R-2519
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom/(.Role := Plan).AI Agent Confidence Threshold
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
---
## Summary

Declare Atom/(.Role := Plan).AI Agent Confidence Threshold

## Claim

```CFEL
Atom/(.Role: Plan).AI Agent Confidence Threshold{:0..1}: [int]{:1};
Atom/(.Role: Plan).AI Agent Confidence Threshold.*[]{:0};
Atom/(.Role: Plan).AI Agent Confidence Threshold
  ?= LOOKUP(IS_CONTAINED_BY, Atom/(.Role: Plan).AI Agent Confidence Threshold)
  ?= Scope Unit/Project//$project.Settings.AI Agent Confidence Threshold
```
