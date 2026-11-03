---
atom_id: CA-R-1977
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project.Settings.Artifact Timestamp Timezone
relations:
  child_of:
  - CA-R-1176
version: 15
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
---
## Summary

Define Project.Framework Settings.Artifact Timestamp Timezone

## Claim scope

the Artifact timestamp timezone setting in Framework Settings.

## Claim

The value supplies the timezone used when emitting Artifact timestamps.

```CFEL
Project.Settings.Artifact Timestamp Timezone{:0..1}: [string]{:1};
Project.Settings.Artifact Timestamp Timezone.*[]{:0}
```

## Details

Evidence: CA-D-390 supplies the timezone interpretation and its concrete encoding. Candidate #6 keeps Settings attached to Project and keeps concrete CAPRMEDIO mechanisms in Project Configuration. This definition adds no format, allowed value or default; those remain separate Delivery rules.
