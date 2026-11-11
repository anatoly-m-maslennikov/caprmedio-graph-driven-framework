---
identity:
  atom_id: CA-R-2658
  ref_id: CA-R-2658
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_TOOLS
  tier: 3
state:
  status: Active
  version: 5
  updated_at: 2026-11-11 15:29:41 +0400
destination:
  file:
    name: CA-R-2658-PROGRAMMATIC-SCOPE_DELEGATION--declare-project-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
---
## Summary

Declare PROJECT_TOOLS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//PROJECT_TOOLS.ID == "CA-SU-19";

Scope Unit//PROJECT_TOOLS.Name == "PROJECT_TOOLS";

Scope Unit//PROJECT_TOOLS.Label == "FEATURE";

Scope Unit//PROJECT_TOOLS.order.ordered == false;

Scope Unit//PROJECT_TOOLS ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC;

Atom/(.Header.Context.Container.scope_unit in ("CA-SU-19"))/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Requirement;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-19"))/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Declaration;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-19"))/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Scope Delegation;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-19"))/(.Header.Context.Role in (Method)).Header.Context.Form :: Decision;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-19"))/(.Header.Context.Role in (Evaluation)).Header.Context.Form :: Decision;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-19"))/(.Header.Context.Role in (Evaluation)).Header.Context.Form :: Eval Case;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-19"))/(.Header.Context.Role in (Delivery)).Header.Context.Form :: Decision;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-19"))/(.Header.Context.Role in (Operations)).Header.Context.Form :: Decision;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-19"))/(.Header.Context.Role in (Operations)).Header.Context.Form :: Workflow;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-19"))/(.Header.Context.Role in (Operations)).Header.Context.Form :: Step;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-19"))/(.Header.Context.Role in (Operations)).Header.Context.Form :: Action;
```


### Prose Claim

Existing global default admissions, including existing Declaration families, remain unchanged; no additional pairs are granted. No exact Current Solution, Direct Policy, or Approach Policy Role/Form pair is selected. Analysis and Advisory / Code Synopsis remains admitted by the global default, and Plan / Work Report remains admitted only for an already admitted Task with the same Container and within the selected target boundary.

For every admitted local Atom, the Header.Container-derived IS_CONTAINED_BY target must be exactly `Scope Unit//PROJECT_TOOLS` (`CA-SU-19`). Its HAS_ACTIVE_SUBJECT target is closed to exactly the declared model entities or declared instances resolved at these Current local main Subject addresses:
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage/Directory Layout`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool`

The selection contains exact objects only, not strings, type members, or descendants; an unresolved address grants no admission.