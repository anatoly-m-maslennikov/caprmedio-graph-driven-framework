---
atom_id: CA-R-2379@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow.Enabled Relations.Contains'
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Workflow Enabled Relations Contains

## Claim scope

Containment capability of a Workflow Atom.

## Claim

For a Workflow Atom, Enabled Relations.Contains is the Boolean containment capability and must be True; the Workflow may contain Step Atoms. It does not copy shared Actions or replace declared control flow with folder order.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow.Enabled Relations.Contains[bool]{1}
```

## Details

Source meaning: CA-R-1945, CA-R-1991. Scope-specific constraints remain in their governing Rs.
