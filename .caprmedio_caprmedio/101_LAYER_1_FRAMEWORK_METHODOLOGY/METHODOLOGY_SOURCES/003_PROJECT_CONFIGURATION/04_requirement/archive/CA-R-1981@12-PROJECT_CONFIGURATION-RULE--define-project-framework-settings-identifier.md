---
atom_id: CA-R-1981@12
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Identifier
relations:
  child_of:
  - CA-R-1176
version: 12
updated_at: 2026-10-29 09:55:37 +0400
tier: 3
type: Rule
---
## Summary

Define Project.Framework Settings.Identifier

## Claim scope

the identifier of the Project's authoritative Framework Settings configuration.

## Claim

Framework Settings Identifier identifies the Project's authoritative Framework Settings configuration, **not** an Atom.

### Formal claim

```text
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Identifier[string]{1}
```

## Details

Evidence: CA-R-1402 defines the owning configuration; CA-R-1404 keeps it outside the Atom type; CA-D-358 supplies its concrete identifier. Candidate #6 decision 11 places Project under Continuant; concrete CAPRMEDIO identity encodings belong in Project Configuration. This definition does not duplicate the concrete identifier spelling or create an Atom ID.
