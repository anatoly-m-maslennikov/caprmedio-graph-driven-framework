---
atom_id: CA-R-1982
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Project.Settings.Interaction
relations:
  child_of:
  - CA-R-1176
version: 15
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 07:52:54 +0400
---
## Summary

Define Project.Framework Settings.Interaction

## Claim scope

the Interaction grouping in the Project's Framework Settings.

## Claim

```CFEL
Project.Settings.Interaction{:0..1}: []{:0};
Project.Settings.Interaction.*[in (Reporting Mode)]{:1}
```

## Details

Evidence: CA-R-1628 defines reporting-mode values; CA-R-1439 limits effects to presentation; CA-R-1440 preserves mandatory information. These define the child setting and its constraints, not the parent grouping. Candidate #6 keeps concrete CAPRMEDIO mechanisms in Project Configuration. This grouping adds no authorization, workflow, validation or safety behavior.
