---
atom_id: CA-R-2552
ref_id: CA-R-2552
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
tier: 3
status: Active
version: 4
updated_at: 2026-11-04 05:21:15 +0400
carrier_destination:
  file:
    name: CA-R-2552-CORE_META_MODEL-RULE--bind-instance-variables.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Bind instance variables

## Claim

### Prose Claim


- `Kind//` selects existing instances of Kind and its narrower kinds.
- `Kind//{:n}` applies the existing cardinality to the selected logical instances within the Project context, except for the per-bearer Property selection below. Resolve the complete selection and count each instance once across repeated references or Carrier representations. An unresolved population is an error.
- For `Node.**//`, `{:n}`, `{:n+}` and `{:n..m}` count instances separately for each effective applicable model Property and actual corresponding bearer instance. CA-R-2462 uses `{:0..1}`.
- Each instance is `INSTANCE_OF` its model Property and `IS_PROPERTY_OF` its data bearer. The rule also applies when that bearer is a Property instance. Inherited Properties retain their original schema identity and model bearer. Mismatched pairs are invalid; unresolved applicability or population is an error. These constraints do not create Cartesian links.
- A leaf with a positive direct-value minimum requires an instance; zero alone does not require one. Explicit occurrence and other constraints still apply. A present Property has a value; for a structural parent, nonempty child structure can be that value even when its direct-value count is zero.
- `Kind//$x` ranges over the selected instances. Each non-aggregate per-binding constraint must hold for every matching binding. Repeated `$x` references in one Claim block identify the same instance within each binding; an enclosing aggregate retains its selected population.
- `in` and `not in` test an instance's identity against a selected instance set. `=` and `!=` compare bound instance references by identity; they do not test kind membership or broadcast a scalar comparison over a set.
- `Kind//$x.p` selects and binds an instance and reads its Property `p`. `$x.p` reads that same bound instance's Property.
- In an IF condition, `Kind//$c ((R)) Kind//$p` tests a link that already exists, including a legitimately derived inverse. It is not an endpoint signature and does not create a link.
- Evaluate the condition for candidate bindings. Its THEN conclusion applies only to bindings for which that link exists; it does not require links between every candidate pair.
- Endpoint counts aggregate matching links per endpoint; they do not require a link between every pair of bindings.
- Binding selects existing instances. It does not create an instance named `$x` or assign a value imperatively. A bare qualified address refers to its declared target.

In one CFEL Formal Claim fence, the full-line comments `# model` and `# instances` distinguish MODEL constraints from instance constraints. When both are present, write `# model` first. These comments are not operators, Properties, or values. Named MODEL addresses such as `Relation//NAME` and `Operator//NAME` retain their declared identity; a Relation descriptor variable in the MODEL group does not make it a runtime instance constraint.

In the MODEL group, `IF $x in (selection) THEN (conclusion)` binds an unbound `$x` over the selected MODEL entities. If `$x` is already bound, the membership test filters that same binding. References to `$x` throughout the parenthesized conclusion use the same binding; the conclusion may contain nested conditions and semicolon-separated statements. This does not create a MODEL entity or introduce a FOR operator.

`KindSelection//$x` binds existing members of the selected logical instance population. The receiver may be a named Kind or a union Kind selection: `(in (Action, Workflow))//$selected` keeps the Action-or-Workflow population and binds its matching members. An existing filter follows the explicit binder without changing its matching population, as in `Event Record//$event_record(.object_output{=1}, .object_output.id = $projection.ID)`. In an aggregate such as `MAX(Event Record//$event_record(.object_output{=1}).happened_at)`, the argument remains the complete filtered population; inserting the binder does not turn the aggregate into one calculation per selected row.

`Kind//$x{:n}` constrains the count of the entire selected logical population in its Project context, not a count of one already-bound row. The existing `Kind//{:n}` population rule remains readable for historical sources, subject to the per-bearer Property selection above. Neither a binder nor a named reference creates an instance, Property, Relation fact or imperative assignment. Binding alone does not grant an inverse permission or change endpoint counts.

## Details

```CFEL
# instances
Kind//$x
```

This binds one existing selected instance.
