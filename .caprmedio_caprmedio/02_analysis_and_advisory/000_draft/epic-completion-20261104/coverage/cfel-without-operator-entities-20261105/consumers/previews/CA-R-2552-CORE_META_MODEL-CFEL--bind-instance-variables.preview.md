---
atom_id: CA-R-2552
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL
version: 4
updated_at: 2026-11-04 05:21:15 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Bind instance variables

## Claim

### Prose Claim


- `$x[<Kind>]` selects existing instances of Kind and its narrower kinds.
- `$x[<Kind>]{::n}` applies the existing cardinality to the selected logical instances within the Project context, except for the per-bearer Property selection below. Resolve the complete selection and count each instance once across repeated references or Carrier representations. An unresolved population is an error.
- For `$x[<Node.**>]`, `{::n}`, `{::n+}` and `{::n..m}` count instances separately for each effective applicable model Property and actual corresponding bearer instance. CA-R-2462 uses `{::0..1}`.
- Each instance is `INSTANCE_OF` its model Property and `IS_PROPERTY_OF` its data bearer. The rule also applies when that bearer is a Property instance. Inherited Properties retain their original schema identity and model bearer. Mismatched pairs are invalid; unresolved applicability or population is an error. These constraints do not create Cartesian links.
- A leaf with a positive direct-value minimum requires an instance; zero alone does not require one. Explicit occurrence and other constraints still apply. A present Property has a value; for a structural parent, nonempty child structure can be that value even when its direct-value count is zero.
- `$x[<Kind>]` ranges over the selected instances. Each non-aggregate per-binding constraint must hold for every matching binding. Repeated `$x` references in one Claim block identify the same instance within each binding; an enclosing aggregate retains its selected population.
- `in` and `not in` test an instance's identity against a selected instance set. `=` and `!=` compare bound instance references by identity; they do not test kind membership or broadcast a scalar comparison over a set.
- `$x[<Kind>].p` selects and binds an instance and reads its Property `p`. `$x.p` reads that same bound instance's Property.
- In an IF condition, `$c[<Kind>] ((R)) $p[<Kind>]` tests a link that already exists, including a legitimately derived inverse. It is not an endpoint signature and does not create a link.
- Evaluate the condition for candidate bindings. Its THEN conclusion applies only to bindings for which that link exists; it does not require links between every candidate pair.
- Endpoint counts aggregate matching links per endpoint; they do not require a link between every pair of bindings.
- Binding selects existing instances. It does not create an instance named `$x` or assign a value imperatively. A bare qualified address refers to its declared target.

In one CFEL Formal Claim fence, the full-line comments `# model` and `# instances` distinguish MODEL constraints from instance constraints. When both are present, write `# model` first. These comments are not operators, Properties, or values. A named MODEL selector such as `$relation[<Relation>, (.Name = NAME)]` retains its declared identity; a Relation descriptor variable in the MODEL group does not make it a runtime instance constraint.

In the MODEL group, `IF $x in (selection) THEN (conclusion)` binds an unbound `$x` over the selected MODEL entities. If `$x` is already bound, the membership test filters that same binding. References to `$x` throughout the parenthesized conclusion use the same binding; the conclusion may contain nested conditions and semicolon-separated statements. This does not create a MODEL entity or introduce a FOR operator.

`$x[<Kind>]` binds existing members of the selected logical instance population. A typed participant can bind the selected Action-or-Workflow population. An existing filter remains in the typed selector without changing its matching population, as in `$event_record[<Event Record>, (.object_output{=1}, .object_output.id = $projection.ID)]`. In an aggregate such as `MAX($event_record[<Event Record>, (.object_output{=1}, .object_output.id = $projection.ID)].happened_at)`, the argument remains the complete filtered population; inserting the binder does not turn the aggregate into one calculation per selected row.

`$x[<Kind>]{::n}` constrains the count of the entire selected logical population in its Project context, not a count of one already-bound row. Neither a binder nor a named reference creates an instance, Property, Relation fact or imperative assignment. Binding alone does not grant an inverse permission or change endpoint counts.

## Details

```CFEL
# instances
$x[<Kind>]
```

This binds one existing selected instance.
