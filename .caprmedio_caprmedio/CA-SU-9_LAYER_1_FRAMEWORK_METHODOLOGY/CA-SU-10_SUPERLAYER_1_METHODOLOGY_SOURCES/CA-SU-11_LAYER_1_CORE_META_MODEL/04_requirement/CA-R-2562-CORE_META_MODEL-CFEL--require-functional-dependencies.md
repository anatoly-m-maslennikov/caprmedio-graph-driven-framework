---
atom_id: CA-R-2562
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Require functional dependencies between Property tuples

## Claim

`DETERMINES(selector, (.key, ...), (.dependent, ...))` requires equal ordered key tuples to have equal ordered dependent tuples. An optional fourth argument, `condition`, restricts the state population: `DETERMINES(selector, (.key, ...), (.dependent, ...), condition)`.

- Use one explicit Project evaluation context. Resolve the complete relevant state history selected by Kind, including versions and rebuild states, rather than only the latest Current snapshot.
- The context supplies the historical population, Property-value resolution and declared reference-identity bindings. These are evaluation inputs, not new Artifact fields.
- Evaluate an optional condition separately on each candidate historical state before resolving tuple Properties. Relative or selected-Kind Property references in that condition bind to that same state. A false condition excludes the state. An unresolved, invalid or ambiguous condition is an error. Without a condition, use all selected states. Do not select by only the latest state and then include its excluded historical states.
- Bind every tuple Property to the same selected state. Each must resolve to exactly one valid scalar value. Missing, invalid or multiple values are errors; do not skip rows.
- Compare tuple positions in order. Compare scalar values using their declared Format without implicit normalization or coercion. A declared reference compares by its resolved target identity. Missing or ambiguous reference bindings are errors; raw text or Carrier locators are not fallback identities.
- For every pair of selected states, equal keys require equal dependents. Repeated keys with equal dependents are allowed. Different keys may have equal dependents.
- An unresolved or incomplete required history is an error. A known complete empty selection satisfies the constraint.

`DETERMINES` does not assert key uniqueness, merge instances, allocate IDs, freeze inputs, assign values or execute a Workflow.
