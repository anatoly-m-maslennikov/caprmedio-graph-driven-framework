---
atom_id: CA-R-2576
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Event Record.object_output
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Event Record.object_output

## Claim

### Formal Claim

```CFEL
# model
Event Record.object_output{:0..1}: []{:0};

Event Record.object_output.*[in(id,version,updated_at)]{:2..3}
```

