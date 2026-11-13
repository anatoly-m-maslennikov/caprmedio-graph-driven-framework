---
identity:
  atom_id: CA-R-2657
  ref_id: CA-R-2657
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//TOOL_WORKFLOWS
  tier: 3
state:
  status: Active
  version: 3
  updated_at: '2026-11-12T15:04:13+00:00'
destination:
  file:
    name: CA-R-2657-PROGRAMMATIC-SCOPE_DELEGATION--declare-tool-workflows.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
---
## Summary

Declare TOOL_WORKFLOWS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//TOOL_WORKFLOWS.ID == "CA-SU-18";

Scope Unit//TOOL_WORKFLOWS.Name == "TOOL_WORKFLOWS";

Scope Unit//TOOL_WORKFLOWS.Label == "FEATURE";

Scope Unit//TOOL_WORKFLOWS.order.ordered == false;

Scope Unit//TOOL_WORKFLOWS ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC;

Atom/(.Header.Context.Container.scope_unit in ("CA-SU-18"))/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Requirement;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-18"))/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Declaration;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-18"))/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Scope Delegation;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-18"))/(.Header.Context.Role in (Method)).Header.Context.Form :: Decision;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-18"))/(.Header.Context.Role in (Evaluation)).Header.Context.Form :: Decision;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-18"))/(.Header.Context.Role in (Evaluation)).Header.Context.Form :: Eval Case;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-18"))/(.Header.Context.Role in (Delivery)).Header.Context.Form :: Decision;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-18"))/(.Header.Context.Role in (Operations)).Header.Context.Form :: Decision;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-18"))/(.Header.Context.Role in (Operations)).Header.Context.Form :: Workflow;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-18"))/(.Header.Context.Role in (Operations)).Header.Context.Form :: Step;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-18"))/(.Header.Context.Role in (Operations)).Header.Context.Form :: Action;
```


### Prose Claim

Existing global default admissions, including existing Declaration families, remain unchanged; no additional pairs are granted. No exact Current Solution, Direct Policy, or Approach Policy Role/Form pair is selected. Plan / Work Report remains admitted only for an already admitted Task with the same Container and within the selected target boundary.

For every admitted local Atom, the Header.Container-derived IS_CONTAINED_BY target must be exactly `Scope Unit//TOOL_WORKFLOWS` (`CA-SU-18`). Its HAS_ACTIVE_SUBJECT target is closed to exactly the declared model entities or declared instances resolved at these Current local main Subject addresses:
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Selection`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage/Directory Layout`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Atom`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Governing Configuration`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit`
- `Subject/CAPRMEDIO/Graph/Rule`

The selection contains exact objects only, not strings, type members, or descendants; an unresolved address grants no admission.