---
atom_id: CA-R-2490@3-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Relations.IS_CONTAINED_BY
version: 3
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Header.Relations.IS_CONTAINED_BY

## Claim

### Formal Claim

```CFEL
Atom.Header.Relations.IS_CONTAINED_BY{:0..1}: []{:0};
Atom.Header.Relations.IS_CONTAINED_BY.*[in(atom,scope_unit)]{:1}
```
