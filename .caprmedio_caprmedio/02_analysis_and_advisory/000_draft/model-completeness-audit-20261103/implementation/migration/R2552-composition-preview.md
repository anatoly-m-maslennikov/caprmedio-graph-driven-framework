# R2552 compositional rule preview

Proposed addition to the variable-binding rule, for root review and adoption with
its source packet. This file does not modify the Current source.

`KindSelection//$variable` names the existing selected instance population.
The receiver may be a named Kind or an existing union Kind selection. For example,
`(in (Action, Workflow))//$selected` preserves the selection of instances admitted
by Action or Workflow; `$selected` names matching members without creating them.

An existing filter after anonymous `//` remains after the explicit binder:
`Event Record//$event_record(.object_output{=1}, .object_output.id = $projection.ID)`.
Adding the name does not change the filter, its matching range, or aggregation.
`MAX(Event Record//$event_record(.filters).happened_at)` retains the original
filtered population as the argument of MAX; it does not force a separate MAX per
bound row. The real filters remain written in full in source; `.filters` here is
only an explanatory placeholder.

`Kind//$variable{:n}` retains the count on the whole selected population, not a
new count of one per matching binding. A binder neither creates nor admits an
instance. Repeated uses of its variable refer to the same matching member within
the applicable Claim binding.

For a model selection, `IF $model_node in (Node, Node.**) THEN (...)` binds an
unbound variable over the selection; membership of an already bound variable
filters that binding. The same binding applies throughout the complete
parenthesized conclusion, whose statements are separated with semicolons.
`# model` and `# instances` remain comments inside one CFEL fence, with model
clauses first. There is no new FOR primitive.
