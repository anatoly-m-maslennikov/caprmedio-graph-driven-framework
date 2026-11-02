---
subjects:
  governs: "Entity/Node/Continuant/Atom.Semantics"
  depends_on:
    - "Entity/Node/Continuant/Atom"
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

Require an Atom's present Semantics section to contain text.

```yaml
graph_rule_type: value_constraint
applies_to:
  node: "Entity/Node/Continuant/Atom"
  property: "Entity/Node/Continuant/Atom.Semantics"
condition:
  value_type: string
```

## Details

Provenance: `../CA-R-1946-CORE_META_MODEL-GENERAL--define-atom-semantics.md` defines Semantics as content represented by a section. An absent Semantics section is ignored by this text constraint; optionality is governed separately. The operative block is a proposed value-constraint schema only: `../../07_delivery/CA-D-637-CORE_META_MODEL-CORE--carry-a-formal-graph-rule-as-yaml-with-a-readable-summary.md` does not yet admit value constraints. It creates no parser, validator, resolver, evaluator, or activation.
