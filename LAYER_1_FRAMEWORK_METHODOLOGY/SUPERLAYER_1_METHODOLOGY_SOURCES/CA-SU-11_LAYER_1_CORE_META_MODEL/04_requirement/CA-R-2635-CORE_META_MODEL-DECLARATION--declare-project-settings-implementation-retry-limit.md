---
atom_id: CA-R-2635
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project.Settings.Implementation Retry Limit
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
---

## Summary

Declare Project.Settings.Implementation Retry Limit

## Claim

An omitted value follows the governed default resolution. A value is an integer at least zero. Zero permits no retries after the initial failure. The limit does not grant repair permission or bypass authority or confidence rules.

```CFEL
Project.Settings.Implementation Retry Limit{:0..1}: [int]{:1};
Project.Settings.Implementation Retry Limit.*[]{:0}
```
