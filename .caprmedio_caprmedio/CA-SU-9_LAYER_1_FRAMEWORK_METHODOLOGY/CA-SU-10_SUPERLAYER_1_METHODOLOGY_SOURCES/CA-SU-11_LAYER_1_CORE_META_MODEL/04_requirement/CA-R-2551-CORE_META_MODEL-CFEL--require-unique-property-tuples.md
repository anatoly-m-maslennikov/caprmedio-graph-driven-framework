---
atom_id: CA-R-2551
ref_id: CA-R-2551
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2551-CORE_META_MODEL-RULE--require-unique-property-tuples.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Require unique Property tuples

## Claim

### Prose Claim


`UNIQUE(selector, (.p, .q))` requires unique tuples of the selected Properties across the selected logical instances in the explicit Project evaluation context. An optional third argument, `condition`, restricts the population: `UNIQUE(selector, (.p, .q), condition)`.

- Use each selected instance's state in one explicit Project snapshot. Do not expand earlier lifecycle states as DETERMINES does. Without a condition, evaluate the complete selected population regardless of Status Group or containment, including selected Drafts and Archived instances. An incomplete or unresolved population is an error. A known empty population satisfies uniqueness.
- Evaluate a condition on each candidate instance before resolving tuple Properties. Relative Properties bind to that same instance. False excludes it; unresolved, invalid or ambiguous conditions are errors. Use the existing Boolean grouping and AND/OR syntax.
- For each selected instance, bind every tuple Property to that same instance. Each must have exactly one valid scalar value; missing, invalid or multiple values fail the constraint.
- Two distinct selected logical instances must not have equal value tuples. Repeated references or Carrier representations of the same logical instance do not create additional instances. Do not infer that two instances are one merely because their key tuples match.
- Compare scalar values in their declared Format without implicit normalization or coercion. A declared reference compares by its resolved target identity; an absent or ambiguous binding is an error, with no raw Carrier-locator fallback. Tuple components need not be individually unique.
- Optional Properties require an explicitly resolved subset whose members carry the required values; do not silently skip missing rows.

`UNIQUE` is a declarative condition. It does not allocate, renumber or write values.
