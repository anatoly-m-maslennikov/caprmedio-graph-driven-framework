---
subjects:
  governs: "Entity/Node/Continuant/Atom.Status"
  depends_on:
    - "Entity/Node/Continuant/Atom"
    - "Entity/Node/Continuant/Atom/Content Role"
version: 1
updated_at: "2026-10-22T01:39:08+04:00"
relations: {}
content_role: Requirement
type: Graph Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Draft
author: Anatoly Maslennikov
---
# Summary

Use the Status values from each Atom's applicable qualified Status model.

```yaml
graph_rule_type: value_constraint
applies_to:
  node: "Entity/Node/Continuant/Atom"
  property: "Entity/Node/Continuant/Atom.Status"
condition:
  allowed_values_source: qualified_status_model
```

## Details

Provenance: `../CA-R-1308-CORE_META_MODEL-CORE-REQUIREMENT--resolve-status-domains-from-complete-qualified-paths.md` requires inherited Atom.Status values plus additions admitted by the complete qualified Content Role and Type path; `../CA-R-1947-CORE_META_MODEL-GENERAL--define-atom-status-allowed-values.md` declares the base Draft, Active, and Archived values while permitting narrower additions. This is a proposed value-constraint schema with a reference to the qualified model, not a flat global enum or a precedence engine; `../../07_delivery/CA-D-637-CORE_META_MODEL-CORE--carry-a-formal-graph-rule-as-yaml-with-a-readable-summary.md` does not yet admit value constraints. It creates no parser, validator, resolver, evaluator, or activation.
