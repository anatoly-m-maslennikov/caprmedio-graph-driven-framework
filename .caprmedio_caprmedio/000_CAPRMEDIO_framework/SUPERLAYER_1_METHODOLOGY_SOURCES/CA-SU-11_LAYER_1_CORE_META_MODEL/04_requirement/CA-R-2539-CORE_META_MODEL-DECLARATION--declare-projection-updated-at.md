---
atom_id: CA-R-2539
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection.Updated At
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Projection.Updated At

## Claim

```CFEL
Projection.Updated At{:1}: [datetime]{:1};
Projection.Updated At.*[]{:0};
Projection//$projection.Updated At == MAX(Event Record//(.object_output{=1}, .object_output.version{=0}, .object_output.id = $projection.ID, (.action = create OR .action = update)).happened_at)
```
