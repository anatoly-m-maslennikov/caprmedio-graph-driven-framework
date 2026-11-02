---
atom_id: CA-R-2381@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Autonomous Confidence Threshold'
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Plan Autonomous Confidence Threshold

## Claim

Plan.Autonomous Confidence Threshold means an optional local integer threshold override used when resolving autonomous Plan execution confidence; when it is absent, the applicable inherited or default resolution remains in force.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Autonomous Confidence Threshold[int]{0..1}
```

## Details

Source meaning: CA-R-1338, CA-R-1587, CA-R-1591, CA-D-472. Scope-specific constraints remain in their governing Rs.
