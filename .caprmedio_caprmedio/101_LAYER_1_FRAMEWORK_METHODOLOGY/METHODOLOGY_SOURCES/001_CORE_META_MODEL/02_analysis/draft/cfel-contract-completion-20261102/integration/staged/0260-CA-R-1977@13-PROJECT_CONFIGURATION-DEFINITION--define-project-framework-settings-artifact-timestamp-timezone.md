---
atom_id: CA-R-1977@13
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
subjects:
  active: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Artifact Timestamp Timezone
relations:
  child_of:
  - CA-R-1176
version: 13
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Entity Definition
---
## Summary

Define Project.Framework Settings.Artifact Timestamp Timezone

## Claim scope

the Artifact timestamp timezone setting in Framework Settings.

## Claim

Artifact Timestamp Timezone **means** the Framework Settings value that supplies the timezone interpretation used when emitting Artifact timestamps.

### Formal claim

```text
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Artifact Timestamp Timezone[string]{0..1}
```

## Details

Evidence: CA-D-390 supplies the timezone interpretation and its concrete encoding. Candidate #6 keeps Settings attached to Project and keeps concrete CAPRMEDIO mechanisms in Project Configuration. This definition adds no format, allowed value or default; those remain separate Delivery rules.
