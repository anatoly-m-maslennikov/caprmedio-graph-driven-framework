---
atom_id: CA-R-2506@3-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Subjects.Passive
version: 3
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Header.Subjects.Passive

## Claim

### Prose Claim

Passive Subjects identify direct contextual dependencies.

### Formal Claim

```CFEL
Atom.Header.Subjects.Passive{:0..1}: [string]{:0+};
Atom.Header.Subjects.Passive.*[]{:0};
COUNT(Atom.Header.Subjects.Passive: $) = COUNT(DISTINCT Atom.Header.Subjects.Passive: $)
```
