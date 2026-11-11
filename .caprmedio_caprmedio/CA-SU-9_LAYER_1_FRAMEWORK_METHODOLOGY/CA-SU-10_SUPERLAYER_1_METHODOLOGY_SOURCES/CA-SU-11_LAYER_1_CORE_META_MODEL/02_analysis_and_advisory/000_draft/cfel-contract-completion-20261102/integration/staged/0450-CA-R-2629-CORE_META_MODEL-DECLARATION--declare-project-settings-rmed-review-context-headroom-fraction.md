---
atom_id: CA-R-2629
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Project.Settings.RMED Review.Context Headroom Fraction
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 07:52:54 +0400
---

## Summary

Declare Project.Settings.RMED Review.Context Headroom Fraction

## Claim

When present, the value is finite and strictly between zero and one.

```CFEL
Project.Settings.RMED Review.Context Headroom Fraction{:0..1}: [float]{:1};
Project.Settings.RMED Review.Context Headroom Fraction.*[]{:0}
```
