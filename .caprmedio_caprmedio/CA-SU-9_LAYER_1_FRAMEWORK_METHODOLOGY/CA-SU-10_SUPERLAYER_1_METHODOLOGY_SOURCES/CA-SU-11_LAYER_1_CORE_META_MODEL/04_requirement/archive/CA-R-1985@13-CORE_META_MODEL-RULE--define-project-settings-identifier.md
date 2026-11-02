---
atom_id: CA-R-1985@13
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Identifier
relations:
  child_of:
  - CA-R-1174
version: 13
updated_at: 2026-10-29 10:03:18 +0400
tier: 3
type: Entity Definition
---
## Summary

Define Project.Settings.Identifier

## Claim scope

the identifier of a Project's authoritative Settings configuration.

## Claim

Project Settings Identifier identifies the Project's authoritative Settings configuration, **not** an Atom.

### Formal claim

```text
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Identifier[string]{1}
```

## Details

Evidence: CA-R-1738 defines Project Settings, CA-R-1401 keeps it outside the Atom type, and CA-D-362 supplies concrete identification. Candidate #6 decisions 11 and 18 preserve the Project path and distinguish Project identity from the delivered framework's name. This generic definition adds no filename, identifier spelling or duplicate Project Name setting.
