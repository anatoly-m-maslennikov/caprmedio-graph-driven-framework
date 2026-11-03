---
atom_id: CA-R-2497@3-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Label
version: 3
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Header.Label

## Claim

### Formal Claim

```CFEL
Atom.Header.Label{:0..1}: [string]{:1};
Atom.Header.Label.*[]{:0};
Atom.Header.Label ?= Atom.Header.Form
```
