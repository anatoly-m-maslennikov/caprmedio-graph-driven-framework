---
atom_id: CA-R-2504@3-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Tier
version: 3
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Header.Tier

## Claim

### Prose Claim

Goals whose active Subject resolves to the Project use Tier -1. Ordinary Scope Unit-owned non-Goal Atoms use Tier 0 or higher.

### Formal Claim

```CFEL
Atom.Header.Tier{:1}: [int]{:1};
Atom.Header.Tier.*[in(Label)]{:0..1};
Atom.Header.Tier >= -1
```
