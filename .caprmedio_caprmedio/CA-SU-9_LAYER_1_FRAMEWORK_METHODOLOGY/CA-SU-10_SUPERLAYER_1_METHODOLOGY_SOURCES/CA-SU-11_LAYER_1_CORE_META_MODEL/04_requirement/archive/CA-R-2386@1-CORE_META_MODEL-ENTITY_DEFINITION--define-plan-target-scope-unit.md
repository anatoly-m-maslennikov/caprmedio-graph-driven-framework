---
atom_id: CA-R-2386@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Target Scope Unit'
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Plan Target Scope Unit

## Claim


Plan.Target Scope Unit is the optional authoring selection of the Plan's Claim Target Scope Unit. Without a separate selection, it resolves to the owning Scope Unit under CA-R-1588. The resolved target is represented under CA-D-482; an omitted authoring override does not leave the effective target unresolved or waive its carrier requirement.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Target Scope Unit[string]{0..1}
```

## Details

Source meaning: CA-R-655, CA-R-1588. Scope-specific constraints remain in their governing Rs.
