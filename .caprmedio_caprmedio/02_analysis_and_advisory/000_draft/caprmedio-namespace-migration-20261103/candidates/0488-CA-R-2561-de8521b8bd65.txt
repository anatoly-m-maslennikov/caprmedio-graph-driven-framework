---
atom_id: CA-R-2561
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Require scalar Property immutability

## Claim

`IMMUTABLE(p)` requires the same valid scalar Property value for one logical bearer from the first point when the surrounding scope selects that Property onward.

- At first applicability, bind the one existing valid scalar value. Existing occurrence, Format and value-cardinality constraints still apply. Guard an optional Property before applying `IMMUTABLE`.
- Bind later versions to the same logical bearer using supplied lineage, not by matching the mutable Property value. A new Version or Carrier representation does not create a new bearer for this check.
- If an IF guard activates `IMMUTABLE`, the constraint remains active for that bearer after the first true condition, including when later versions no longer satisfy the guard.
- Use the first applicable value, not the latest observed value. Missing or invalid required values, unresolved bearer lineage, or incomplete history needed to establish the first applicable value are errors; none proves immutability.
- After activation, every later version of that bearer must still provide exactly one valid scalar value matching the bound value. A later false guard or removal of an optional Property does not suspend the constraint. Compare using the declared scalar Format, without implicit normalization or coercion.

`IMMUTABLE` is a declarative invariant. It does not write, allocate or lock a value, or perform a Workflow step.
