---
atom_id: CA-D-637@21-draft
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: 'Formal Model::CAPRMEDIO::Continuant/Atom/Content Role: Requirement/Type: Graph Rule.content.claim'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Rule.Type
  - Subject/CAPRMEDIO/Graph/Rule.Applies To
  - Subject/CAPRMEDIO/Graph/Rule.Condition
  - Subject/CAPRMEDIO/Graph/Rule.Default Value
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement/Type: Graph Rule'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  - Subject/CAPRMEDIO/Carrier/File
relations: {}
version: 21
updated_at: 2026-10-28 19:24:50 +0400
tier: 1
type: Eng Decision
---
# Summary

Carry a formal Graph Rule as YAML with a readable Summary

## Claim scope

The formal YAML Claim of an R Atom of Type Graph Rule.

## Claim

A formal Graph Rule must carry its sole operative mapping inside exactly one fenced yaml block under ## Claim. Its frontmatter contains ordinary Atom metadata only; it must not retain another claim or formal_claim mapping. This fenced block is atom.content.claim. Summary is required; Claim scope, Semantics and Details are optional in the RMED order under CA-D-479.

## Details

Inside the Claim block, graph_rule_type, applies_to, condition and any schema-admitted default_value are the mapping's root keys; do not wrap them in another claim key. Type on the Atom remains Graph Rule; graph_rule_type remains the rule's form. Supporting prose may explain but never duplicate or override that formal statement. The existing schemas below retain their logic; moving their carrier does not imply parser/runtime support.

### Whitelist schema

For `graph_rule_type: whitelist`, `applies_to` contains `relation_type`, a string resolving to the governed Relation Type. `condition` contains `source` and `target`, each a list of strings using the existing Subject notation to identify allowed endpoint kinds. Both endpoint tests must match; narrower kinds inherit membership. Do not split a Subject into a parallel `kind`/Content Role selector language. These restrictions permit matching connections; they do not require any connection or constrain other Relation Types. Source and target strings containing `:` must be quoted to remain YAML strings.

```yaml
graph_rule_type: whitelist
applies_to:
  relation_type: evaluation_for
condition:
  source:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  target:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement'
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
  node: Subject/Graph Node/Domain/Continuant/Selection//Dependent Entity Occurrences
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

For `graph_rule_type: endpoint_constraint`, use this closed mapping; all listed fields are required and additional fields are invalid:

- `applies_to.relation_selection`: one nonempty full Subject string naming a source-declared named Selection. For the approved governing-order Rule, the value is `Subject/Graph Node/Domain/Continuant/Selection//Stored Governing RMED Relation Occurrences`, whose exact membership is defined by CA-R-2148.
- `condition.ordering`: exactly `same_scope_lower_target_tier_or_strict_ancestor_or_project_configuration_core_prerequisite`.

The Endpoint Constraint schema compares the stored governing Relation direction selected by CA-R-2148. A selected source must be a Current Requirement, Method, Evaluation, or Delivery Atom; the target may be any Current Atom permitted by the defining Relation requirement, including an Operations target for `evaluation_for`. In the same Scope Unit, the target Atom's numeric Tier must be strictly lower than the source Atom's numeric Tier. In different Scope Units, the target ordering Scope must be a strict ancestor of the source ordering Scope, or the endpoints must resolve within the same Project to the Project Configuration source role and its Core Meta-Model prerequisite role declared by CA-R-1218; Tier numbers are not compared in either case. The prerequisite arm is exactly one-way and non-transitive. It is not inferred from parentage, local order, source-set inclusion, compilation selection, Subjects, Atom relations, or a declaring Atom's owner. Every other descendant or sibling target is forbidden. Non-RMED source occurrences, including Plan or Operations containment sources, are outside this Selection. Derived inverse views are excluded.

For ordering only, an endpoint verified as a Current Requirement of Type Project Goal under CA-R-2152 and CA-R-2132 uses its Target Project as its ordering Scope context. Its actual owner remains the Operator Actor. The Target Project must be the Project containing the other endpoint's declared Local Scope Unit; an unrelated Project does not qualify. Ordinary endpoints, including non-Project Goals, continue to use their Local Scope Unit. Compare the resulting contexts with the same lower-target-Tier, strict-ancestor, or exact logical-role-prerequisite rule. Do not create an Operator Scope Unit, change ownership, add a stored Property, or exempt a Project Goal from ordering. Unverified Goal identity, ownership, Tier or Project membership remains unresolved and does not pass.

`default_value` is not applicable to Endpoint Constraint and must not be supplied. Unknown or incomplete Selection membership, an unregistered Relation Kind, a non-Current endpoint, a missing endpoint Tier, an unresolved ordering Scope context, unresolved parentage, unresolved logical-role identity, unresolved Project correspondence, or an unresolved CA-R-1218 prerequisite declaration is unresolved evidence and does not pass the Rule. This schema does not create a resolver, evaluator, fallback or general expression language.

```yaml
graph_rule_type: endpoint_constraint
applies_to:
  relation_selection: Subject/Graph Node/Domain/Continuant/Selection//Stored Governing RMED Relation Occurrences
condition:
  ordering: same_scope_lower_target_tier_or_strict_ancestor_or_project_configuration_core_prerequisite
```

This block illustrates the closed Endpoint Constraint encoding and is not a second live Rule instance. Multiple-rule combination, unknown Relation Types outside a declared Selection, blacklist precedence and override policies still require their own declarations before use. This Delivery contract does not implement parser, validator, resolver or evaluator support.

Superseded preparation: CA-A-1242 removes the special Graph Rule branch and Atom Type. Do not promote this legacy Graph Rule packet entry as written. Preserve its useful formal constraints/schema evidence for incorporation into the appropriate Definition Claims; no Current rule or predecessor is deleted by this marker.
