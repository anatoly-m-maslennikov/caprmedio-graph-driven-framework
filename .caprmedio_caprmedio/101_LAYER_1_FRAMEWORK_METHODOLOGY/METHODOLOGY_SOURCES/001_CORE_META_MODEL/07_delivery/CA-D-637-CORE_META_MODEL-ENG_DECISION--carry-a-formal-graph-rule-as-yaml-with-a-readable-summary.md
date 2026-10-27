---
atom_id: CA-D-637
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Rule
  depends_on:
  - Subject/Graph Rule.Type
  - Subject/Graph Rule.Applies To
  - Subject/Graph Rule.Condition
  - Subject/Graph Rule.Default Value
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Graph Rule'
  - Subject/Graph Node/Domain/Continuant/Atom.Summary
  - Subject/Graph Node/Carrier/File
relations: {}
version: 19
updated_at: 2026-10-27 06:04:45 +0400
tier: 1
type: Eng Decision
---
# Summary

Carry a formal Graph Rule as YAML with a readable Summary

## Scope

the Markdown carrier of an R Atom expressing a formal Graph Rule; ordinary R/Type: Rule Atoms and model Definition contracts do not acquire this layout automatically.

## Claim

a formal Graph Rule **must** preserve ordinary Atom metadata and carry exactly one fully formal YAML `claim` mapping in frontmatter. Its Markdown Content has exactly one prose Summary. The `claim` mapping is the Graph Rule's Claim; do not add a duplicate prose Claim or a generic Substance Property or section. Semantics and Details are optional supporting sections, not required content.

## Details

### Body layout

Use the existing literal `# Summary` heading and its source-faithful prose. All operative rule data belongs in the frontmatter `claim` mapping; it is not duplicated in Markdown. Optional `## Semantics` and `## Details` sections may follow the Summary, each at most once and in either order. Usually omit them when no useful explanation or support is needed. Their prose and any fenced examples are supporting content, not another operative rule; they must not duplicate, change or override the formal YAML Claim. Do not add another authoritative prose condition or a separate Rule file. Existing Atom ID, Version, Status, ownership and lifecycle rules remain unchanged.

### Rule mapping

| Property | YAML key | Encoding |
|---|---|---|
| Formal Claim | `claim` | Exactly one structured mapping containing the operative Graph Rule statement |
| Graph Rule Type | `claim.graph_rule_type` | Exactly one canonical string selecting the declared Type schema |
| Applies To | `claim.applies_to` | Required structured mapping identifying the governed cases |
| Condition | `claim.condition` | Required structured mapping conforming to the selected Type schema |
| Default Value | `claim.default_value` | Optional value, only where a value default applies; its type and admissibility follow the governed value's constraints |

The current Type encodings are `whitelist` (Whitelist), `blacklist` (Blacklist), `cardinality` (Cardinality), `value_constraint` (Value Constraint), `topology_constraint` (Topology Constraint), and `endpoint_constraint` (Endpoint Constraint). These are not Atom Type names; frontmatter `type: Graph Rule` remains distinct from `claim.graph_rule_type`. The operative Claim belongs in frontmatter; no generic Subtype is introduced.

### Whitelist schema

For `claim.graph_rule_type: whitelist`, `claim.applies_to` contains `relation_type`, a string resolving to the governed Relation Type. `claim.condition` contains `source` and `target`, each a list of strings using the existing Subject notation to identify allowed endpoint kinds. Both endpoint tests must match; narrower kinds inherit membership. Do not split a Subject into a parallel `kind`/Content Role selector language. These restrictions permit matching connections; they do not require any connection or constrain other Relation Types. Source and target strings containing `:` must be quoted to remain YAML strings.

```yaml
claim:
  graph_rule_type: whitelist
  applies_to:
    relation_type: evaluation_for
  condition:
    source:
      - "Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation"
    target:
      - "Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement"
```

This block illustrates the schema; it is not a second live Rule instance.

### Cardinality schema

For `claim.graph_rule_type: cardinality`, use these closed mappings; all listed fields are required, and additional fields are invalid:

- `claim.applies_to.node`: one string in existing Subject notation, identifying the source-backed node kind or named Selection whose members are checked individually. A named Selection selects its members, not the Selection node itself. The source must establish the complete selected domain independently of whether matching connections exist; include selected nodes with zero connections. Unknown or incomplete membership is unresolved evidence, not an empty passing set. This format creates no Selection resolver or evaluator.
- `claim.applies_to.relation_type`: one nonempty string identifying the counted Relation Type.
- `claim.applies_to.direction`: exactly `outgoing` or `incoming`, relative to each selected node.
- `claim.condition.other_endpoint`: a list of existing Subject strings identifying matching opposite-endpoint kinds. Narrower kinds inherit membership. Matching any listed kind includes a connection; an empty list matches no endpoint. Count each distinct source/type/target Relation once per selected node, without counting repeated filter matches or derived inverse navigation again.
- `claim.condition.minimum`: an exact nonnegative integer, not a Boolean, float or string.
- `claim.condition.maximum`: an exact nonnegative integer greater than or equal to minimum, or explicit YAML null for no upper bound. Do not omit either bound. Equal bounds require the exact count; minimum zero permits absence, minimum one requires a connection, and maximum zero prohibits matching connections.

Cardinality constrains the number of existing matching connections; it does not supply a fallback value or create a connection. `claim.default_value` is not part of this Type's schema. Operative keys, values and Subject syntax are structurally checked; parsing does not establish node membership, resolve references or evaluate the count.

CA-R-1997 defines the meaning and source-declared membership of the named Selection used below; this Delivery contract specifies its Subject-string encoding.

```yaml
claim:
  graph_rule_type: cardinality
  applies_to:
    node: "Subject/Graph Node/Domain/Continuant/Selection//Dependent Entity Occurrences"
    relation_type: IS_BORNE_BY
    direction: outgoing
  condition:
    other_endpoint:
      - Subject/Graph Node/Domain/Continuant/Atom
    minimum: 1
    maximum: 1
```

This block illustrates the encoding and is not a live Rule instance. The concrete rule is authored separately with its own Atom identity.

### Endpoint Constraint schema

For `claim.graph_rule_type: endpoint_constraint`, use this closed mapping; all listed fields are required and additional fields are invalid:

- `claim.applies_to.relation_selection`: one nonempty full Subject string naming a source-declared named Selection. For the approved governing-order Rule, the value is `Subject/Graph Node/Domain/Continuant/Selection//Stored Governing RMED Relation Occurrences`, whose exact membership is defined by CA-R-2148.
- `claim.condition.ordering`: exactly `same_scope_lower_target_tier_or_strict_ancestor_or_project_configuration_core_prerequisite`.

The Endpoint Constraint schema compares the stored governing Relation direction selected by CA-R-2148. A selected source must be a Current Requirement, Method, Evaluation, or Delivery Atom; the target may be any Current Atom permitted by the defining Relation requirement, including an Operations target for `evaluation_for`. In the same Scope Unit, the target Atom's numeric Tier must be strictly lower than the source Atom's numeric Tier. In different Scope Units, the target ordering Scope must be a strict ancestor of the source ordering Scope, or the endpoints must resolve within the same Project to the Project Configuration source role and its Core Meta-Model prerequisite role declared by CA-R-1218; Tier numbers are not compared in either case. The prerequisite arm is exactly one-way and non-transitive. It is not inferred from parentage, local order, source-set inclusion, compilation selection, Subjects, Atom relations, or a declaring Atom's owner. Every other descendant or sibling target is forbidden. Non-RMED source occurrences, including Plan or Operations containment sources, are outside this Selection. Derived inverse views are excluded.

For ordering only, an endpoint verified as a Current Requirement of Type Project Goal under CA-R-2152 and CA-R-2132 uses its Target Project as its ordering Scope context. Its actual owner remains the Operator Actor. The Target Project must be the Project containing the other endpoint's declared Local Scope Unit; an unrelated Project does not qualify. Ordinary endpoints, including non-Project Goals, continue to use their Local Scope Unit. Compare the resulting contexts with the same lower-target-Tier, strict-ancestor, or exact logical-role-prerequisite rule. Do not create an Operator Scope Unit, change ownership, add a stored Property, or exempt a Project Goal from ordering. Unverified Goal identity, ownership, Tier or Project membership remains unresolved and does not pass.

`claim.default_value` is not applicable to Endpoint Constraint and must not be supplied. Unknown or incomplete Selection membership, an unregistered Relation Kind, a non-Current endpoint, a missing endpoint Tier, an unresolved ordering Scope context, unresolved parentage, unresolved logical-role identity, unresolved Project correspondence, or an unresolved CA-R-1218 prerequisite declaration is unresolved evidence and does not pass the Rule. This schema does not create a resolver, evaluator, fallback or general expression language.

```yaml
claim:
  graph_rule_type: endpoint_constraint
  applies_to:
    relation_selection: "Subject/Graph Node/Domain/Continuant/Selection//Stored Governing RMED Relation Occurrences"
  condition:
    ordering: same_scope_lower_target_tier_or_strict_ancestor_or_project_configuration_core_prerequisite
```

This block illustrates the closed Endpoint Constraint encoding and is not a second live Rule instance. Multiple-rule combination, unknown Relation Types outside a declared Selection, blacklist precedence and override policies still require their own declarations before use. This Delivery contract does not implement parser, validator, resolver or evaluator support.
