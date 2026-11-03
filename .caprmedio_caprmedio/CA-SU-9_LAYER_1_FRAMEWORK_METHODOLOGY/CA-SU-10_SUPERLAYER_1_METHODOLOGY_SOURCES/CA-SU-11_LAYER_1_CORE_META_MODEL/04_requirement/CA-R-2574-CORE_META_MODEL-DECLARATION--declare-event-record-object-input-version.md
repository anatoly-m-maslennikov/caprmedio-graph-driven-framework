---
atom_id: CA-R-2574
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Event Record.object_input.version
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Event Record.object_input.version

## Claim

### Formal Claim

```CFEL
# model
Event Record.object_input.version{:0..1}: [int]{:1};

Event Record.object_input.version.*[]{:0}
```

