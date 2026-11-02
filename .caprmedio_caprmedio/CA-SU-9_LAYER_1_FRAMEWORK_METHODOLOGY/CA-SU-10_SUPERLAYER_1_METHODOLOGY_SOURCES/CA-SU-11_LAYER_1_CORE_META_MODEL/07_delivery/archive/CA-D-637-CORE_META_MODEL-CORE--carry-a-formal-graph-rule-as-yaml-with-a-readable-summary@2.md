---
atom_id: CA-D-637
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Rule
  depends_on:
  - Entity/Graph Rule.Type
  - Entity/Graph Rule.Applies To
  - Entity/Graph Rule.Condition
  - Entity/Graph Rule.Default Value
  - 'Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Graph Rule'
  - Entity/Node/Continuant/Atom.Summary
  - Entity/Carrier/File Carrier
relations: {}
version: 2
updated_at: "2026-10-20 00:26:02 +0400"
---
# Summary

Carry a formal Graph Rule as YAML with a readable Summary

## Scope

the Markdown carrier of an R Atom expressing a formal Graph Rule; ordinary R/Type: Rule Atoms and model Definition contracts do not acquire this layout automatically.

## Claim

a formal Graph Rule's Markdown carrier **must** preserve the ordinary Atom metadata in YAML frontmatter and carry its Main Content as exactly one prose Summary followed by exactly one operative YAML block, without duplicate prose Scope, Claim or Details sections.

## Details

### Body layout

Use the existing literal `# Summary` heading and its source-faithful prose, followed by one fenced block whose language is `yaml`. All operative rule data belongs in that block; it is not a duplicate metadata/frontmatter representation. Do not add another authoritative prose condition or a separate Rule file. Existing Atom ID, Version, Status, ownership and lifecycle rules remain unchanged.

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
    - "Entity/Node/Continuant/Atom/Content Role: Evaluation"
  target:
    - "Entity/Node/Continuant/Atom/Content Role: Requirement"
```

This block illustrates the schema; it is not a second live Rule instance. Other Type schemas, multiple-whitelist combination, unknown Relation Types, blacklist precedence and override policies still require their own declarations before use. This Delivery contract does not implement parser or validator support.
