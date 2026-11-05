---
atom_id: CA-R-2521
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action.Execution Kind
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
---
## Summary

Declare Atom/(.Role := Operations)/Action.Execution Kind

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Operations)/Action.Execution Kind{:1}: [string]{:1};

Atom/(.Header.Role: Operations)/Action.Execution Kind.*[]{:0};

Atom/(.Header.Role: Operations)/Action.Execution Kind: Programmatic;

Atom/(.Header.Role: Operations)/Action.Execution Kind: Agentic
```

