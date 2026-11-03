---
atom_id: CA-R-2504
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Tier
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Tier

## Claim

Goals whose active Subject resolves to the Project use Tier -1. Ordinary Scope Unit-owned non-Goal Atoms use Tier 0 or higher.

```CFEL
Atom.Tier{:1}: [int]{:1};
Atom.Tier.*[in(Label)]{:0..1};
Atom.Tier >= -1
```
