---
atom_id: CA-R-2503
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content.Details
version: 3
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Content.Details

## Claim

### Formal Claim

```CFEL
Atom/(.Header.Role in RMED).Content.Details{:0..1}: [markdown]{:1};
Atom/(.Header.Role in RMED).Content.Details.*[string]{:0+}
```

