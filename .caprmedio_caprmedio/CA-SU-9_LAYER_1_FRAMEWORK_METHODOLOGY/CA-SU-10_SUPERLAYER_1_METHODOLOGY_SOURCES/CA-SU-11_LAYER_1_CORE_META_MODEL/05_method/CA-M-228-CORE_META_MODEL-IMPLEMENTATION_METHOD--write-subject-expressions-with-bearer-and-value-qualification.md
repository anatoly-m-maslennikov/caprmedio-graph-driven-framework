---
atom_id: CA-M-228
ref_id: CA-M-228
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 3
status: Active
version: 37
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-M-228-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-subject-expressions-with-bearer-and-value-qualification.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
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

When a CFEL Formal Claim has both MODEL and instance constraints, use one fence with full-line `# model` and `# instances` comments, in that order. The comments classify the statements without changing the meaning of named addresses. Existing ungrouped Claims remain readable as historical sources.

For a selected MODEL population, write `IF $x in (selection) THEN ( ... )`. An unbound `$x` ranges over the selection; membership of an already bound `$x` filters that binding. Reuse it throughout the parenthesized conclusion, separating complete statements with semicolons. Do not write a FOR operator.

In instance constraints, `Kind//$x` binds an existing selected instance and `$x.Property` reads the same binding. A union receiver can bind as `(in (Action, Workflow))//$selected`. Insert a binder before an existing filter, as in `Event Record//$event_record(.object_output{=1}, .object_output.id = $projection.ID)`, preserving the filter and any enclosing aggregate population, as in `MAX(Event Record//$event_record(.object_output{=1}).happened_at)`. `Kind//$x{:n}` constrains the count of the selected logical population, not one bound row; existing `Kind//{:n}` remains readable in historical Claims.

Keep MODEL Relation descriptor variables in the MODEL group and preserve named `Relation//NAME` and `Operator//NAME` addresses. A `//` spelling alone does not make a named MODEL object a runtime constraint. Preserve inherited Property contracts at the declared bearer; a reference to an inherited Property does not create another Declaration.
