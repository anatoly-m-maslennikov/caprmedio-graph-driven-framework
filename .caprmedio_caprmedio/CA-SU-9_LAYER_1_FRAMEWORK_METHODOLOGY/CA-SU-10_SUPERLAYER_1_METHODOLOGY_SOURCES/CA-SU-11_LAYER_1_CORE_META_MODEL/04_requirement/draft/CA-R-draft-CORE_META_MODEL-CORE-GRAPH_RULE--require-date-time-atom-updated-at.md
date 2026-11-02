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
  governs: Entity/Node/Continuant/Atom.Updated At
  depends_on: []
relations: {}
version: 1
updated_at: "2026-10-22T01:39:08+04:00"
---
# Summary

Require a date-time value for Atom Updated At

```yaml
graph_rule_type: value_constraint
applies_to:
  node: Entity/Node/Continuant/Atom
  property: Entity/Node/Continuant/Atom.Updated At
condition:
  value_type: date_time
```

## Details

Proposed Value Constraint encoding, not an admitted schema in CA-D-637@5. Check each present value; missing-value requiredness belongs to the separate Cardinality rule. Date-time is the semantic type, even when its carrier is a quoted YAML string. No general primitive-type registry is created here.

Source: [CA-R-1416@15](../CA-R-1416-CORE_META_MODEL-GENERAL--give-every-atom-revision-one-updated-at.md). Exact spelling, quoting and timezone representation remain Delivery policies, not another condition in this rule.
