---
atom_id: CA-R-2359@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Atom Local Scope Unit

## Claim scope

Explicit Scope Unit references carried by an Atom.

## Claim

Atom Local Scope Unit is the optional explicit Scope Unit reference carried by an Atom. When present, Scope Unit references resolve relative to it; the Atom effective Scope must still resolve exactly one through contextual or fallback rules, and Delivery serializes the containing Scope Unit in the filename when applicable.

### Formal claim

```text
Atom.Local Scope Unit[string]{0..1}
```

## Details

Source meaning: CA-R-655, CA-R-1014, CA-R-886, CA-R-920, CA-D-291. Scope-specific constraints remain in their governing Rs.
