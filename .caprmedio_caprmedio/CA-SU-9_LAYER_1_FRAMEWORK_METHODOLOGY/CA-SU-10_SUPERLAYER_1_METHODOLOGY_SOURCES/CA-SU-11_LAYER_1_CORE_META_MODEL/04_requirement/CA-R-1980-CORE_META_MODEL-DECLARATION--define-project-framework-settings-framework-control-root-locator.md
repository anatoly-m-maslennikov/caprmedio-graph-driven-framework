---
atom_id: CA-R-1980
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Project.Settings.Framework Control-Root Locator
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

Define Project.Framework Settings.Framework Control-Root Locator

## Claim scope

the Project's framework control-root reference in Framework Settings.

## Claim

```CFEL
Project.Settings.Framework Control-Root Locator{:0..1}: [string]{:1};
Project.Settings.Framework Control-Root Locator.*[]{:0}
```

## Details

Evidence: CA-D-370 requires the locator to resolve to the Directory Carrier prescribed by CA-D-317 without selecting another authority root. Candidate #6 keeps concrete CAPRMEDIO mechanisms in Project Configuration. This definition adds no path or alternative authority root; those remain Delivery rules.
