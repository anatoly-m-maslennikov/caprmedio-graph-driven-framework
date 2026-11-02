---
atom_id: CA-R-2362@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Updated At
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Atom Updated At

## Claim scope

Updated-at timestamp of every Atom.

## Claim

Atom Updated At is one unambiguous datetime for every Atom. An accepted edit refreshes it to the actual project-time edit instant; an exact no-op retains it, and an archived predecessor retains its prior timestamp.

### Formal claim

```text
Atom.Updated At[datetime]{1}
```

## Details

Source meaning: CA-R-655, CA-R-1416, CA-R-1788, CA-E-521. Scope-specific constraints remain in their governing Rs.
