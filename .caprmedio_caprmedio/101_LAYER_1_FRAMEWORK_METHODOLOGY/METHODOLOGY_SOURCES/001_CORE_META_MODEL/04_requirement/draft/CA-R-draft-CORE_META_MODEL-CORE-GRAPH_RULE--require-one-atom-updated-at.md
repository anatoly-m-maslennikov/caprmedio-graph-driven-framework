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

Require one Updated At value per Atom

```yaml
graph_rule_type: cardinality
applies_to:
  node: Entity/Node/Continuant/Atom
  property: Entity/Node/Continuant/Atom.Updated At
condition:
  minimum: 1
  maximum: 1
```

## Details

Proposed property-value Cardinality encoding, not the relation-counting schema admitted by CA-D-637@5. Count the values of this property on each Atom, including zero for a missing property; do not count IS_BORNE_BY edges as property values.

Source: [CA-R-1416@15](../CA-R-1416-CORE_META_MODEL-GENERAL--give-every-atom-revision-one-updated-at.md). This Draft does not change timestamp serialization, timezone selection or update procedures.
