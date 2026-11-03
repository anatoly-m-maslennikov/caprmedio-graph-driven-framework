---
atom_id: CA-R-2581
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Event Record.Relations
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Event Record.Relations

## Claim

### Formal Claim

```CFEL
# model
Event Record.Relations{:1}: []{:0};

# instances
Event Record.Relations.*[Relation//$relation]{:0+}
```

