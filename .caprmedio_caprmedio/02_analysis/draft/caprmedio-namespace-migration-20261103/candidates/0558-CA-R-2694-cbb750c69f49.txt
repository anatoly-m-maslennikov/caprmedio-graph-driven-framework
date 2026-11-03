---
atom_id: CA-R-2694
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 1
relations: {}
tier: 3
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Carrier Destination.File.Name
role: Requirement
form: Declaration
updated_at: 2026-11-03 00:20:05 +0400
---
## Summary

Declare Atom.Carrier Destination.File.Name

## Claim

```CFEL
Atom.Carrier Destination.File.Name{:1}: [string]{:1};
Atom.Carrier Destination.File.Name.*[]{:0}
```

Calculated full filename, including its extension.
