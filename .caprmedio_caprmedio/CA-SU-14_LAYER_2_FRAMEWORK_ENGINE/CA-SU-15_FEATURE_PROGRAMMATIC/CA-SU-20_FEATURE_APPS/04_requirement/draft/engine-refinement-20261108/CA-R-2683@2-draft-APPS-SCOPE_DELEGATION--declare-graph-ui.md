---
identity:
  atom_id: CA-R-2683
  ref_id: CA-R-2683@2-draft
context:
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//GRAPH_UI
  tier: 3
  container:
    scope_unit: CA-SU-20
state:
  status: Draft
  version: 2
  updated_at: 2026-11-08 20:11:06 +0400
destination:
  file:
    name: CA-R-2683@2-draft-APPS-SCOPE_DELEGATION--declare-graph-ui.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/draft/engine-refinement-20261108
---
## Summary

Declare GRAPH_UI

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//GRAPH_UI.ID == "CA-SU-44";

Scope Unit//GRAPH_UI.Name == "GRAPH_UI";

Scope Unit//GRAPH_UI.Label == "APP";

Scope Unit//GRAPH_UI.order.ordered == false;

Scope Unit//GRAPH_UI ((IS_CONTAINED_BY)) Scope Unit//APPS
```

