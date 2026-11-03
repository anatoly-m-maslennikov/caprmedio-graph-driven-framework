---
atom_id: CA-R-2566
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
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2566-CORE_META_MODEL-CFEL--filter-instances-and-select-maximum-values.md
  source_atom_id: CA-R-2566
  source_atom_revision: 2
  source_sha256: 8f8693e6c6f62038a4a098e20d0359b4c127d78d169373bf53eaa083240d8a99
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Filter instances and select maximum values

## Claim

`Kind//(c1, ...).p` selects p from matching instances of Kind and its narrower kinds in one explicit current-Project instance snapshot.

- Relative filter paths bind the same candidate instance. Outer variables retain their enclosing bindings; an unbound or ambiguous variable is an error.
- Every filter condition must hold. Commas inside filter parentheses mean AND. Outside them, selector commas retain their existing union meaning. Existing AND, OR and grouping remain available. Filter conditions and AND groups evaluate left-to-right with short-circuiting: a later field read is evaluated only after its earlier guard holds.
- A missing, invalid or unresolved evaluated filter is an error, not false. Short-circuiting excludes only an unevaluated later condition; it never turns an evaluated invalid value into a skipped record. Reference comparisons use resolved target identity, not raw identifiers or Carrier data.
- Each matching instance contributes exactly one valid scalar p. Selection does not implicitly expand lifecycle history.
- `MAX(selection)` returns the greatest selected scalar under its Format-defined ordering. Numeric and datetime values are orderable. Compare datetimes as instants, not lexical strings.
- Empty, incomplete, incompatible or non-orderable selections are errors.
- Equal greatest values return that scalar value. MAX does not select a record row.

Both operations are read-only. They create no record, Property, Relation, value or lifecycle transition.
