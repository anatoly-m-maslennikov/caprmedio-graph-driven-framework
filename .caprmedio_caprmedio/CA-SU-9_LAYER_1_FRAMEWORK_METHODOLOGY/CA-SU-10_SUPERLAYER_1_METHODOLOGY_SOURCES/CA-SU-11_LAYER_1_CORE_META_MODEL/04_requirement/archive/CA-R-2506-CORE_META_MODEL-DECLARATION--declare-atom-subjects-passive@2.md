---
atom_id: CA-R-2506
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Subjects.Passive
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Subjects.Passive

## Claim

Passive Subjects identify direct contextual dependencies.

```CFEL
Atom.Subjects.Passive{:0..1}: [string]{:0+};
Atom.Subjects.Passive.*[]{:0};
COUNT(Atom.Subjects.Passive: $) = COUNT(DISTINCT Atom.Subjects.Passive: $)
```
