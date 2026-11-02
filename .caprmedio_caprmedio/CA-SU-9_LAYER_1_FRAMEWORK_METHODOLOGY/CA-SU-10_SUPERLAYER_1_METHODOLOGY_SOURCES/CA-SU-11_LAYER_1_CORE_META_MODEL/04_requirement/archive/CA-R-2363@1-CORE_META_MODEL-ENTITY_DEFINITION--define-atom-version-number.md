---
atom_id: CA-R-2363@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Version Number
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Atom Version Number

## Claim scope

Version of every Atom.

## Claim

Atom Version Number is one positive integer for each Atom and increases monotonically across successive versions of the same Atom.

### Formal claim

```text
Atom.Version Number[int]{1}
```

## Details

Source meaning: CA-R-655, CA-R-1415. Scope-specific constraints remain in their governing Rs.
