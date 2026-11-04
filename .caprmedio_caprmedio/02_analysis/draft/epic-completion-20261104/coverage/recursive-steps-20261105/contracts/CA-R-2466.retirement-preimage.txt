---
atom_id: CA-R-2466
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Substep
version: 4
updated_at: 2026-11-02 17:54:42 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Substep

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Operations)/Substep;

# instances
Substep//$substep{:1}((IS_CONTAINED_BY)) Step//$step;

Substep//$substep_2{:1}((RUNS)) Action//$action
```

## Semantics

A Substep is a leaf unit within a Step and runs exactly one reusable Action.
