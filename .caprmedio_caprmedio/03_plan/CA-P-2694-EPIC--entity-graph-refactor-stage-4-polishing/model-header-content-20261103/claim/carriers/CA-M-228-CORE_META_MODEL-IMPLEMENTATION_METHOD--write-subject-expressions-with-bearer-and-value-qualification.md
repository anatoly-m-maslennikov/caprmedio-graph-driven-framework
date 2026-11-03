---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
version: 35
updated_at: 2026-11-02 00:55:09 +0400
relations: {}
atom_id: CA-M-228
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
tier: 3
role: Method
form: Implementation Method
---
## Summary

Write Subject Expressions with Bearer and Value Qualification

## Claim

### Prose Claim

Applicability: authoring one Subject expression.

Use the declared Primary Entity and Property paths. `/` selects a narrower Primary Entity; `//` selects a named instance of a declared kind; `.` addresses a declared Property of its bearer. An unchanged inherited Property resolves to its existing declaration. A heading alone does not declare a Property.

Count direct values independently of child Properties. YAML null and empty strings are direct values; state necessary value restrictions through the Format or applicable prose. Use prose when formal machinery is unnecessary. Write a Property value constraint as `property: [format]{:count}`. Use `.*` for immediate child names and `.**` for recursive child names; constrain child values separately. Use `{:n}`, `{:n+}`, and `{:n..m}` for exact, lower-bounded, and inclusive bounded allowed counts. Use `{=n}` for a condition and `{==n}` for setting a count.

Write a named Relation object as `Relation//NAME` and its actual use as `Source {:left}((NAME)){:right} Target`, with each endpoint count optional. A Relation Declaration can state both intrinsic endpoint bounds. A Node-specific Claim addresses its active Node and its own bound. Reversing a written view swaps the bounds; it does not grant opposite-view permission, which must be declared separately. Resolve aliases as typed Relation instances and write a counterpart as `<-->`. Short operators remain valid where declared.

Use `:` for allowed values, `=` for a condition, `==` for setting a value, and `:=` for allowed value and condition in a Subject. Separate complete expressions with semicolons. Use bare Entity references without an `@` reference marker.

An ordinary RMED Claim is a zero-direct-value group with one or both declared Formal Claim and Prose Claim children. Formal Claim contains a CFEL-labelled fence; Prose Claim contains ordinary Markdown.
