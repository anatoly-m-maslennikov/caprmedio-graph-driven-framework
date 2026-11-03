---
atom_id: CA-R-2530
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit.Path
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Scope Unit Path

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.Path{:1}: [string]{:1+};

Scope Unit.Path.*[]{:0}
```

### Prose Claim


The Path lists Scope Unit identities along the complete declared containment chain from the root to the addressed Scope Unit.

