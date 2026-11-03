---
atom_id: CA-R-2518@3-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern).Header.Priority
version: 3
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
---
## Summary

Declare Atom/(.Header.Role := Concern).Header.Priority

## Claim

### Formal Claim

```CFEL
Atom/(.Header.Role: Concern).Header.Priority{:1}: [string]{:1};
Atom/(.Header.Role: Concern).Header.Priority.*[]{:0};
Atom/(.Header.Role: Concern).Header.Priority: High;
Atom/(.Header.Role: Concern).Header.Priority: Medium;
Atom/(.Header.Role: Concern).Header.Priority: Low
```
