---
atom_id: CA-R-2361@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Type
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Atom Type

## Claim scope

The admitted Type of an Atom under its Content Role.

## Claim

Atom Type is the required substantive admitted Type under the Atom Content Role; exactly one string value identifies an independently governed atomic unit and must not be invented as a placeholder. Relational classifications and external-name derivation remain governed by their cited rules.

### Formal claim

```text
Atom.Type[string]{1}
```

## Details

Source meaning: CA-R-655, CA-R-1700, CA-R-924, CA-D-393. Scope-specific constraints remain in their governing Rs.
