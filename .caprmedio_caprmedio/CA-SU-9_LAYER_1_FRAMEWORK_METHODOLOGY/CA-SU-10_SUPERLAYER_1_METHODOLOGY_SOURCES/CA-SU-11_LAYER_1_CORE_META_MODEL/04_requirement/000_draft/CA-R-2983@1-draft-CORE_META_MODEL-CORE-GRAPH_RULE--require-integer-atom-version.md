---
atom_id: CA-R-2983
ref_id: CA-R-2983@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Graph Rule
topics:
  main_subject: Entity/Node/Continuant/Atom.Header.State.Version Number
  dependencies:
  - Entity/Node/Continuant/Atom
status: Draft
version: 1
updated_at: '2026-10-22T01:39:08+04:00'
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
author: Anatoly Maslennikov
---
# Summary

Require each Atom Version Number to be an integer.

```yaml
graph_rule_type: value_constraint
applies_to:
  node: "Entity/Node/Continuant/Atom"
  property: "Entity/Node/Continuant/Atom.Version Number"
condition:
  value_type: integer
```

## Details

Provenance: `../CA-R-1415-CORE_META_MODEL-GENERAL--give-every-atom-revision-one-version.md` requires a positive integer Version. The operative block is a proposed value-constraint schema only: `../../07_delivery/CA-D-637-CORE_META_MODEL-CORE--carry-a-formal-graph-rule-as-yaml-with-a-readable-summary.md` does not yet admit value constraints. It creates no parser, validator, resolver, evaluator, or activation.
