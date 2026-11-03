---
atom_id: CA-R-2499
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content.Summary
version: 3
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Content.Summary

## Claim

### Formal Claim

```CFEL
Atom.Content.Summary{:1}: [markdown]{:1};
Atom.Content.Summary.*[]{:0};
DETERMINES(
  Atom//,
  (.ID),
  (.Content.Summary),
  (Atom.Header.Status >| Status Group = Current) OR (Atom.Header.Status >| Status Group = Archived)
)
```

