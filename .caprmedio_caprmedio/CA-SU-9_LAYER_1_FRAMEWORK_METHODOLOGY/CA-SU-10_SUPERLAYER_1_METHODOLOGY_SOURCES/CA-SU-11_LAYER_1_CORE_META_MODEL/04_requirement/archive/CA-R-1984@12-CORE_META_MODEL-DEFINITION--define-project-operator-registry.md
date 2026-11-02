---
atom_id: CA-R-1984@12
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Operator Registry
relations:
  child_of:
  - CA-R-1174
version: 12
updated_at: 2026-10-29 09:39:47 +0400
tier: 3
type: Entity Definition
---
## Summary

Define Project.Operator Registry

## Claim scope

the authoritative Operator registry of a Project.

## Claim

Operator Registry **means** the Project's authoritative registry of its Operators **and** their declared identifying information. Registry membership does **not** itself grant execution permission.

### Formal claim

```text
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Operator Registry{0}
```

## Details

Evidence: CA-D-494 defines registered Operator names and roles, exact membership and the no-permission distinction. Candidate #6 keeps Actor distinct from Project and permits abstract, project-independent Core definitions. File format, filename, location and concrete Operator identities remain separate Delivery/configuration concerns; this definition adds none.
