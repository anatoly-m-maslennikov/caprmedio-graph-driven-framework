---
atom_id: CA-D-637@12
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph/Rule
  depends_on:
  - Subject/Graph/Rule.Type
  - Subject/Graph/Rule.Applies To
  - Subject/Graph/Rule.Condition
  - Subject/Graph/Rule.Default Value
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Graph Rule'
  - Subject/Domain/Node/Continuant/Atom.Summary
  - Subject/Engineering/Carrier/File Carrier
relations: {}
version: 12
updated_at: 2026-10-24 01:37:42 +0400
tier: 1
type: Eng Decision
---
# Summary

Carry a formal Graph Rule as YAML with a readable Summary

## Scope

the Markdown carrier of an R Atom expressing a formal Graph Rule; ordinary R/Type: Rule Atoms and model Definition contracts do not acquire this layout automatically.

## Claim

a formal Graph Rule's Markdown carrier **must** preserve ordinary Atom metadata in YAML frontmatter and carry its Main Content as exactly one prose Summary followed by exactly one operative YAML block. It has no Claim or Substance Property or section and no separate prose Scope. Semantics and Details are optional supporting sections, not required content.

## Details

### Body layout

Use the existing literal `# Summary` heading and its source-faithful prose, followed by one fenced block whose language is `yaml`. All operative rule data belongs in that block; it is not a duplicate metadata/frontmatter representation. Optional `## Semantics` and `## Details` sections may follow the operative block, each at most once and in either order. Usually omit them when no useful explanation or support is needed. Their prose and any fenced examples are supporting content, not another operative rule; they must not duplicate, change or override the operative YAML. Do not add another authoritative prose condition or a separate Rule file. Existing Atom ID, Version, Status, ownership and lifecycle rules remain unchanged.

### Rule mapping

| Property | YAML key | Encoding |
|---|---|---|
| Graph Rule Type | `graph_rule_type` | Exactly one canonical string selecting the declared Type schema |
| Applies To | `applies_to` | Required structured mapping identifying the governed cases |
| Condition | `condition` | Required structured mapping conforming to the selected Type schema |
| Default Value | `default_value` | Optional value, only where a value default applies; its type and admissibility follow the governed value's constraints |

The current Type encodings are `whitelist` (Whitelist), `blacklist` (Blacklist), `cardinality` (Cardinality), `value_constraint` (Value Constraint), `topology_constraint` (Topology Constraint), and `endpoint_constraint` (Endpoint Constraint). These are not Atom Type names; frontmatter `type: Graph Rule` remains distinct from the operative block's `graph_rule_type`. The operative field belongs in the fenced body, not in frontmatter; no generic Subtype is introduced.

### Whitelist schema

For `graph_rule_type: whitelist`, `applies_to` contains `relation_type`, a string resolving to the governed Relation Type. `condition` contains `source` and `target`, each a list of strings using the existing Subject notation to identify allowed endpoint kinds. Both endpoint tests must match; narrower kinds inherit membership. Do not split a Subject into a parallel `kind`/Content Role selector language. These restrictions permit matching connections; they do not require any connection or constrain other Relation Types. Source and target strings containing `:` must be quoted to remain YAML strings.

```yaml
graph_rule_type: whitelist
applies_to:
  relation_type: evaluation_for
condition:
  source:
    - "Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation"
  target:
    - "Subject/Domain/Node/Continuant/Atom/Content Role: Requirement"
```

This block illustrates the schema; it is not a second live Rule instance.

### Cardinality schema

For `graph_rule_type: cardinality`, use these closed mappings; all listed fields are required, and additional fields are invalid:

- `applies_to.node`: one string in existing Subject notation, identifying the source-backed node kind or named Selection whose members are checked individually. A named Selection selects its members, not the Selection node itself. The source must establish the complete selected domain independently of whether matching connections exist; include selected nodes with zero connections. Unknown or incomplete membership is unresolved evidence, not an empty passing set. This format creates no Selection resolver or evaluator.
- `applies_to.relation_type`: one nonempty string identifying the counted Relation Type.
- `applies_to.direction`: exactly `outgoing` or `incoming`, relative to each selected node.
- `condition.other_endpoint`: a list of existing Subject strings identifying matching opposite-endpoint kinds. Narrower kinds inherit membership. Matching any listed kind includes a connection; an empty list matches no endpoint. Count each distinct source/type/target Relation once per selected node, without counting repeated filter matches or derived inverse navigation again.
- `condition.minimum`: an exact nonnegative integer, not a Boolean, float or string.
- `condition.maximum`: an exact nonnegative integer greater than or equal to minimum, or explicit YAML null for no upper bound. Do not omit either bound. Equal bounds require the exact count; minimum zero permits absence, minimum one requires a connection, and maximum zero prohibits matching connections.

Cardinality constrains the number of existing matching connections; it does not supply a fallback value or create a connection. `default_value` is not part of this Type's schema. Operative keys, values and Subject syntax are structurally checked; parsing does not establish node membership, resolve references or evaluate the count.

CA-R-1997 defines the meaning and source-declared membership of the named Selection used below; this Delivery contract specifies its Subject-string encoding.

```yaml
graph_rule_type: cardinality
applies_to:
  node: "Subject/Domain/Node/Continuant/Selection//Dependent Entity Occurrences"
  relation_type: IS_BORNE_BY
  direction: outgoing
condition:
  other_endpoint:
    - Subject/Domain/Node/Continuant/Atom
  minimum: 1
  maximum: 1
```

This block illustrates the encoding and is not a live Rule instance. The concrete rule is authored separately with its own Atom identity.

### Endpoint Constraint schema

For `graph_rule_type: endpoint_constraint`, use this closed mapping; all listed fields are required and additional fields are invalid:

- `applies_to.relation_selection`: one nonempty full Subject string naming a source-declared named Selection. For the approved governing-order Rule, the value is `Subject/Domain/Node/Continuant/Selection//Stored Governing RMED Relation Occurrences`, whose exact membership is defined by CA-R-2148.
- `condition.ordering`: exactly `same_scope_lower_target_tier_or_strict_ancestor`.

The Endpoint Constraint schema compares the stored governing Relation direction selected by CA-R-2148. A selected source must be a Current Requirement, Method, Evaluation, or Delivery Atom; the target may be any Current Atom permitted by the defining Relation requirement, including an Operations target for `evaluation_for`. In the same Scope Unit, the target Atom's numeric Tier must be strictly lower than the source Atom's numeric Tier. In different Scope Units, the target Scope Unit must be a strict ancestor of the source Scope Unit and their Tier numbers must not be compared. A descendant or sibling target is forbidden. Non-RMED source occurrences, including Plan or Operations containment sources, are outside this Selection. Derived inverse views are excluded.

`default_value` is not applicable to Endpoint Constraint and must not be supplied. Unknown or incomplete Selection membership, an unregistered Relation Kind, a non-Current endpoint, a missing endpoint Tier, a missing Scope Unit, or unresolved parentage is unresolved evidence and does not pass the Rule. This schema does not create a resolver, evaluator, fallback or general expression language.

```yaml
graph_rule_type: endpoint_constraint
applies_to:
  relation_selection: "Subject/Domain/Node/Continuant/Selection//Stored Governing RMED Relation Occurrences"
condition:
  ordering: same_scope_lower_target_tier_or_strict_ancestor
```

This block illustrates the closed Endpoint Constraint encoding and is not a second live Rule instance. Multiple-rule combination, unknown Relation Types outside a declared Selection, blacklist precedence and override policies still require their own declarations before use. This Delivery contract does not implement parser, validator, resolver or evaluator support.
