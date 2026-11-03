---
atom_id: CA-R-1978
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings.Code-Root Locators
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

Define Project.Framework Settings.Code-Root Locators

## Claim

### Formal Claim

```CFEL
Project.Settings.Code-Root Locators{:0..1}: [string]{:1+};
Project.Settings.Code-Root Locators.*[]{:0}
```

### Prose Claim


the code-root references in the Project's Framework Settings.



## Details

Evidence: CA-D-371 requires code-root locators in Framework Settings. Candidate #6 keeps concrete CAPRMEDIO mechanisms in Project Configuration. This definition adds no discovery procedure, new root or locator count.
