---
atom_id: CA-R-2498
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content
version: 3
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Content

## Claim

### Formal Claim

```CFEL
Atom.Content{:1}: []{:0};
Atom.Content.*[string]{:0+};
Atom.Content.**[string]{:0+}: [markdown]{:0..1}
```

