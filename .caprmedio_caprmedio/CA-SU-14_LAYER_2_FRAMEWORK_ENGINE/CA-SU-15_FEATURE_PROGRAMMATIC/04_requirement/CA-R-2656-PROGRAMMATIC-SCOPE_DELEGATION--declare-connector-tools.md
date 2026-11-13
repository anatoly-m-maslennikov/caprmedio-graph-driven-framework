---
identity:
  atom_id: CA-R-2656
  ref_id: CA-R-2656
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//CONNECTOR_TOOLS
  tier: 3
state:
  status: Active
  version: 4
  updated_at: '2026-11-12T15:04:13+00:00'
destination:
  file:
    name: CA-R-2656-PROGRAMMATIC-SCOPE_DELEGATION--declare-connector-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
author: Anatoly Maslennikov
---
## Summary

Declare CONNECTOR_TOOLS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//CONNECTOR_TOOLS.ID == "CA-SU-17";

Scope Unit//CONNECTOR_TOOLS.Name == "CONNECTOR_TOOLS";

Scope Unit//CONNECTOR_TOOLS.Label == "FEATURE";

Scope Unit//CONNECTOR_TOOLS.order.ordered == false;

Scope Unit//CONNECTOR_TOOLS ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC;

Atom/(.Header.Context.Container.scope_unit in ("CA-SU-17"))/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Requirement;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-17"))/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Declaration;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-17"))/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Scope Delegation;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-17"))/(.Header.Context.Role in (Method)).Header.Context.Form :: Decision;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-17"))/(.Header.Context.Role in (Evaluation)).Header.Context.Form :: Decision;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-17"))/(.Header.Context.Role in (Evaluation)).Header.Context.Form :: Eval Case;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-17"))/(.Header.Context.Role in (Delivery)).Header.Context.Form :: Decision;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-17"))/(.Header.Context.Role in (Operations)).Header.Context.Form :: Decision;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-17"))/(.Header.Context.Role in (Operations)).Header.Context.Form :: Workflow;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-17"))/(.Header.Context.Role in (Operations)).Header.Context.Form :: Step;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-17"))/(.Header.Context.Role in (Operations)).Header.Context.Form :: Action;
```


### Prose Claim

Existing global default admissions, including existing Declaration families, remain unchanged; no additional pairs are granted. No exact Current Solution, Direct Policy, or Approach Policy Role/Form pair is selected. Plan / Work Report remains admitted only for an already admitted Task with the same Container and within the selected target boundary.

For every admitted local Atom, the Header.Container-derived IS_CONTAINED_BY target must be exactly `Scope Unit//CONNECTOR_TOOLS` (`CA-SU-17`). Its HAS_ACTIVE_SUBJECT target is closed to exactly the declared model entities or declared instances resolved at these Current local main Subject addresses:
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Serialization`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Retrieval`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Selection`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Directory Layout`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Dynamic Testing`
- `MODEL//CAPRMEDIO <+ Governing Configuration`
- `MODEL//CAPRMEDIO <+ Scope Unit`

The selection contains exact objects only, not strings, type members, or descendants; an unresolved address grants no admission.