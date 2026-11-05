---
atom_id: CA-R-2984
ref_id: CA-R-2984@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Graph Rule
topics:
  main_subject: Entity/Node/Continuant/Atom.Status
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

Require one Status for each Atom.

```yaml
graph_rule_type: cardinality
applies_to:
  node: "Entity/Node/Continuant/Atom"
  property: "Entity/Node/Continuant/Atom.Status"
condition:
  minimum: 1
  maximum: 1
```

## Details

Provenance: `../CA-R-1412-CORE_META_MODEL-CORE--give-every-atom-revision-one-status.md` requires exactly one Status. The operative block is a proposed property-cardinality schema only: current `../../07_delivery/CA-D-637-CORE_META_MODEL-CORE--carry-a-formal-graph-rule-as-yaml-with-a-readable-summary.md` admits cardinality only for relations. It creates no parser, validator, resolver, evaluator, or activation.
