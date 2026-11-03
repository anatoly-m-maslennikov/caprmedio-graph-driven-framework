---
atom_id: CA-R-2497
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Label
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Label

## Claim

```CFEL
Atom.Label{:0..1}: [string]{:1};
Atom.Label.*[]{:0};
Atom.Label ?= Atom.Form
```
