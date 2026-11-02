---
atom_id: CA-R-2364@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern.Local Scope Unit'
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Concern Local Scope Unit

## Claim scope

Explicit Scope Unit references carried by a Concern Atom.

## Claim

Concern Local Scope Unit is the optional explicit Scope Unit reference for a Concern Atom. A Concern spanning multiple Structural scopes belongs to their narrowest common ancestor; this property does not create a separate scope model.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern.Local Scope Unit[string]{0..1}
```

## Details

Source meaning: CA-R-655, CA-R-1770. Scope-specific constraints remain in their governing Rs.
