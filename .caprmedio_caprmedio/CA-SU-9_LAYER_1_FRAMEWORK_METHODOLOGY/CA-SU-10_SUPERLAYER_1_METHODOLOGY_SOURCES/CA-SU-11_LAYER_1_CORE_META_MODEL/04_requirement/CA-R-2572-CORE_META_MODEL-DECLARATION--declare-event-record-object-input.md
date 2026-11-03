---
atom_id: CA-R-2572
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Event Record.object_input
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Event Record.object_input

## Claim

### Formal Claim

```CFEL
Event Record.object_input{:0..1}: []{:0};
Event Record.object_input.*[in(id,version,updated_at)]{:2..3}
```

