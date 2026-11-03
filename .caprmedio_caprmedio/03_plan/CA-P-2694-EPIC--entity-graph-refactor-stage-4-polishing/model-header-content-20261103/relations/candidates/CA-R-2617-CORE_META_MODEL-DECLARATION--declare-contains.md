---
atom_id: CA-R-2617
role: Requirement
form: Declaration
status: Active
version: 1
updated_at: 2026-11-02 08:06:47 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//CONTAINS
relations: {}
---
## Summary

Declare CONTAINS

## Claim

### Formal Claim

```CFEL
Relation//CONTAINS <((HAS_INVERSE)) Relation//IS_CONTAINED_BY;
alias(Relation//CONTAINS) == "<+"
```
