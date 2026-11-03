---
atom_id: CA-R-2540
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Projection.Source.Atoms
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Projection.Source.Atoms

## Claim

```CFEL
Projection.Source.Atoms{:0..1}: [string]{:0+};
Projection.Source.Atoms.*[]{:0}
```

Each value is an Atom ID with an explicit Version.
