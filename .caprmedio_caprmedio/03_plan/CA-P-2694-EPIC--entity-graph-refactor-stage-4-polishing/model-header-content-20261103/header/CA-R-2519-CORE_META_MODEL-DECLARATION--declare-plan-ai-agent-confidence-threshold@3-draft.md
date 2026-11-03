---
atom_id: CA-R-2519@3-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.AI Agent Confidence Threshold
version: 3
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
---
## Summary

Declare Atom/(.Header.Role := Plan).Header.AI Agent Confidence Threshold

## Claim

### Formal Claim

```CFEL
Atom/(.Header.Role: Plan).Header.AI Agent Confidence Threshold{:0..1}: [int]{:1};
Atom/(.Header.Role: Plan).Header.AI Agent Confidence Threshold.*[]{:0};
Atom/(.Header.Role: Plan).Header.AI Agent Confidence Threshold
  ?= LOOKUP(Relation//IS_CONTAINED_BY, Atom/(.Header.Role: Plan).Header.AI Agent Confidence Threshold)
  ?= Scope Unit/Project//$project.Settings.AI Agent Confidence Threshold
```
