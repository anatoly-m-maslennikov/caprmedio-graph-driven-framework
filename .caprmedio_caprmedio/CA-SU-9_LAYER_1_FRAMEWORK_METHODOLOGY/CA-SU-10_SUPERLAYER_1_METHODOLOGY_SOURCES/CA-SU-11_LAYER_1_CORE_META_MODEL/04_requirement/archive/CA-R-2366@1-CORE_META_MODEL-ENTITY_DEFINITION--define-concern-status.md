---
atom_id: CA-R-2366@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern.Status'
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Concern Status

## Claim scope

Lifecycle status of a Concern Atom.

## Claim

Concern Status is the one-string lifecycle classification of a Concern under its applicable status model. It inherits Atom Status values and adds Resolved and Canceled; a Concern is active while its matter needs disposition and solved only after terminal disposition, while archival does not mean solved.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern.Status[string]{1}
```

## Details

Source meaning: CA-R-1989, CA-R-655, CA-R-1608, CA-R-1726. Scope-specific constraints remain in their governing Rs.
