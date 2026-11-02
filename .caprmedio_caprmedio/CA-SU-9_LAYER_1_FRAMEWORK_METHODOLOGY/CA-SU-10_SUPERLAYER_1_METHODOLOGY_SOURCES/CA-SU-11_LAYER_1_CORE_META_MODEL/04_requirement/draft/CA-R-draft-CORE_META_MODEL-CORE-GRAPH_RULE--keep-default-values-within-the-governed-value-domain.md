---
content_role: Requirement
type: Graph Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Rule.Default Value
  depends_on:
    - Entity/Graph Rule.Condition
relations: {}
version: 1
updated_at: "2026-10-22T01:39:08+04:00"
---
# Summary

Keep a default within the governed value's constraints

```yaml
graph_rule_type: value_constraint
applies_to:
  node: Entity/Graph Rule
  property: Entity/Graph Rule.Default Value
condition:
  when_present:
    conforms_to: governed_value_constraints
```

## Details

Proposed Value Constraint encoding, not an admitted schema in CA-D-637@5. This Draft introduces no validator or resolver support.

An absent default has nothing to check. A declared default must satisfy the same applicable value constraints as an explicit governed value. An explicit null is a declared value, not absence; its admissibility depends on the governed value's constraints. This rule selects no concrete default and no cross-rule precedence.

Source: [CA-R-1999@1](../CA-R-1999-CORE_META_MODEL-CORE--define-entity-graph-rule-default-value.md). Its fallback-only meaning remains: resolving a default does not automatically write a value or create a relation. Cardinality rules continue to forbid default_value under the existing Delivery schema.
