---
atom_id: CA-R-2537
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection.ID
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Projection.ID

## Claim

```CFEL
Projection.ID{:1}: [string]{:1};
Projection.ID.*[]{:0};
DETERMINES(Projection//, (.Form, .Source.Named Selection), (.ID));
DETERMINES(Projection//, (.ID), (.Form, .Source.Named Selection))
```
