---
identity:
  atom_id: CA-R-2683@2
  ref_id: CA-R-2683@2
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
  version: 2
  updated_at: 2026-11-08 23:18:49 +0400
destination:
  file:
    name: CA-R-2683@2-APPS-SCOPE_DELEGATION--declare-graph-ui.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/archive
---
## Summary

Declare GRAPH_UI

## Claim

Within this delegation, the admitted local Role/Form pairs used by the reviewed current local RMEDO are exactly: Evaluation/Eval Case, already globally admitted by CA-R-3008. No additional Role/Form pair is admitted.

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared model entities or declared instances resolved at this existing active Subject address:

- Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation

Each entry selects that single endpoint object. It does not select the address string, other members of its type, or descendants. An unresolved entry remains a diagnostic and grants no admission.

These permissions apply only to Atoms whose Header.Container-derived IS_CONTAINED_BY target is GRAPH_UI.

### Formal Claim

```CFEL
# instances
Scope Unit//GRAPH_UI.ID == "CA-SU-44";

Scope Unit//GRAPH_UI.Name == "GRAPH_UI";

Scope Unit//GRAPH_UI.Label == "APP";

Scope Unit//GRAPH_UI.order.ordered == false;

Scope Unit//GRAPH_UI ((IS_CONTAINED_BY)) Scope Unit//APPS
```

