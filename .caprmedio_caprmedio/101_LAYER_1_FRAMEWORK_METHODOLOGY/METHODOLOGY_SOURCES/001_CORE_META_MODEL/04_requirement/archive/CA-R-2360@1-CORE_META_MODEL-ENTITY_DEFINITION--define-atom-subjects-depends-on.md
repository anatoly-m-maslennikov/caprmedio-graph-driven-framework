---
atom_id: CA-R-2360@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Subjects.Depends On
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Atom Subjects Depends On

## Claim scope

Direct dependency links under Atom Subjects.

## Claim

Atom Subjects Depends On is the zero-or-more direct dependency reference collection under Subjects. Each link preserves its target identity and does not create a separate Subject object.

### Formal claim

```text
Atom.Subjects.Depends On[string]{0+}
```

## Details

Source meaning: CA-R-1198, CA-R-655. Scope-specific constraints remain in their governing Rs.
