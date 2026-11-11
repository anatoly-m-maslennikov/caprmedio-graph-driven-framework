---
atom_id: CA-R-2489
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Updated At
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Updated At

## Claim

```CFEL
Atom.Updated At{:1}: [datetime]{:1};
Atom.Updated At.*[]{:0};
Atom//$atom.Updated At == MAX(Event Record//(.object_output{=1}, .object_output.version{=1}, .object_output.id = $atom.ID, .object_output.version = $atom.Version, (.action = create OR .action = update)).happened_at)
```
