---
subjects:
  active: Atom/(.Role := Operations)/Step
  passive:
  - Atom/(.Role := Operations)
  - Atom/(.Role := Operations)/Substep
  - Atom/(.Role := Operations)/Action
  - Atom.Content
  - Atom.Type
version: 25
updated_at: 2026-11-02 07:49:21 +0400
relations: {}
atom_id: CA-R-1569
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Define the Step Operations Atom Type

## Claim scope

the Step model kind of Operations Atoms.

## Claim

a Step model definition **must** declare exactly one of these alternatives:

- it RUNs exactly **`1`** Action model kind; **or**
- it has one or more Substep model-kind children through their canonical direct `IS_CONTAINED_BY` facts and RUNs no Action model kind.

## Details

- the child endpoint is the retained Substep model kind declared by CA-R-2466; the direct fact is authored only from the Substep to its parent Step, and the Step's `CONTAINS` view is derived.
- a Linear Step model definition has ordered nonconditional Substep definitions only.
- a Conditional Step model definition chooses exactly **`1`** branch in its own definition from its declared result condition and **may** use Actor input; result-based routing belongs to that definition.
- different Step model definitions **may** RUN the same Action model kind with different parameter and input-binding definitions without copying or redefining that Action.
- this Draft constrains MODEL kinds only. Review or migration of actual Workflow, Step, Substep, and Action instances is deferred.
