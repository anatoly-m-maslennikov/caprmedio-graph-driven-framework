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
  governs: Entity/Node/Continuant/Atom.Status
  depends_on:
    - Entity/Node/Continuant/Atom/Content Role
relations: {}
version: 1
updated_at: "2026-10-22T01:39:08+04:00"
---
# Summary

Preserve inherited Status values in narrower Atom kinds

```yaml
graph_rule_type: value_constraint
applies_to:
  node: Entity/Node/Continuant/Atom
  property: Entity/Node/Continuant/Atom.Status
condition:
  allowed_value_domain:
    includes_inherited_values: true
    permits_declared_additions: true
```

## Details

Proposed Value Constraint encoding, not an admitted schema in CA-D-637@5. It constrains source-declared allowed-value domains, not the number of Status values on one Atom. It introduces no resolver or universal rule-merging policy.

Each narrower Atom kind retains its inherited Status values and may admit additional values for its qualified Content Role or Type. Inherited values need not be declared again. This does not replace the qualified domain with a closed global list or decide inheritance for other properties.

Sources: [CA-R-1308@13](../CA-R-1308-CORE_META_MODEL-CORE-REQUIREMENT--resolve-status-domains-from-complete-qualified-paths.md) and [CA-R-1947@3](../CA-R-1947-CORE_META_MODEL-GENERAL--define-atom-status-allowed-values.md). The base values and qualified additions remain owned by those source declarations, not copied into this rule.
