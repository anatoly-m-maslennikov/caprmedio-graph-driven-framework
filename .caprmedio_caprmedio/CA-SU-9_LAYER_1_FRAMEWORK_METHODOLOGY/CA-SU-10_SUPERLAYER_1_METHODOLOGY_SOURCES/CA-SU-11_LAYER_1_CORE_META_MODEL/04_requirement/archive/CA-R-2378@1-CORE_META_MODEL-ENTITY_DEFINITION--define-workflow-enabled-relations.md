---
atom_id: CA-R-2378@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow.Enabled Relations'
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Workflow Enabled Relations

## Claim scope

Containment capabilities grouped under a Workflow Atom.

## Claim

For a Workflow Atom, Enabled Relations is the non-scalar optional grouping property for enabled relation capabilities. Its Contains child is required True under the Workflow rule, permitting containment of Step Atoms without copying Actions or replacing declared control flow with folder order.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow.Enabled Relations{0}
```

## Details

Source meaning: CA-R-1945, CA-R-1991. Scope-specific constraints remain in their governing Rs.
