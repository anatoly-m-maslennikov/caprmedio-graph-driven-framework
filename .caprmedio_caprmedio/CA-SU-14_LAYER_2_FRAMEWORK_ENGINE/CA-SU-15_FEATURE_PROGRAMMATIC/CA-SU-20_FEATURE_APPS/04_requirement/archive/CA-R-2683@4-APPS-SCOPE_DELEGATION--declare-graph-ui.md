---
identity:
  atom_id: CA-R-2683
  ref_id: CA-R-2683@4
context:
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//GRAPH_UI
  tier: 3
  container:
    scope_unit: CA-SU-20
state:
  status: Archived
  version: 4
  updated_at: 2026-11-09 17:00:18 +0400
destination:
  file:
    name: CA-R-2683@4-APPS-SCOPE_DELEGATION--declare-graph-ui.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/archive
---

## Summary

Declare GRAPH_UI

## Claim


### Prose Claim

The receiving Scope Unit is GRAPH_UI. Existing default Role and Form admissions remain applicable. The additional local Role/Form pairs are exactly:

- Method / Solution;

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

- `Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation`;

Each address selects one endpoint object, not the address string, other members of its type or descendants. An unresolved address is diagnostic and grants no admission. These permissions apply only to local Atoms whose Header.Container resolves to GRAPH_UI. The Scope Unit identity, Parent, responsibility and structural tree are unchanged.

### Formal Claim

```CFEL
# instances
Scope Unit//GRAPH_UI.ID == "CA-SU-44";

Scope Unit//GRAPH_UI.Name == "GRAPH_UI";

Scope Unit//GRAPH_UI.Label == "APP";

Scope Unit//GRAPH_UI.order.ordered == false;

Scope Unit//GRAPH_UI ((IS_CONTAINED_BY)) Scope Unit//APPS
```
