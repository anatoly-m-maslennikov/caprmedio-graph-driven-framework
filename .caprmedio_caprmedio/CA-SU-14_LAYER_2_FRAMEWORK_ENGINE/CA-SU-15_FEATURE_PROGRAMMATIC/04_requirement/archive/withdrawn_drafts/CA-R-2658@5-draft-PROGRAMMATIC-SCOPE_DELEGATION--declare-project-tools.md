---
identity:
  atom_id: CA-R-2658
  ref_id: CA-R-2658@5-draft
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//PROJECT_TOOLS
  tier: 3
state:
  status: Draft
  version: 5
  updated_at: 2026-11-10 17:28:03 +0400
destination:
  file:
    name: CA-R-2658@5-draft-PROGRAMMATIC-SCOPE_DELEGATION--declare-project-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/draft
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

Scope Unit//PROJECT_TOOLS ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC
```


### Prose Claim

The explicit default Role/Form pairs below are: `Requirement/Requirement`, `Requirement/Declaration`, `Requirement/Scope Delegation`, `Method/Decision`, `Evaluation/Decision`, `Evaluation/Eval Case`, `Delivery/Decision`, `Operations/Decision`, `Operations/Workflow`, `Operations/Step`, `Operations/Action`. Existing global default admissions, including existing Declaration families, remain unchanged; no additional pairs are granted. No exact Current Solution, Direct Policy, or Approach Policy Role/Form pair is selected. Analysis & Advisory / Code Synopsis remains admitted by the global default, and Plan / Work Report remains admitted only for an already admitted Task with the same Container and within the selected target boundary.

For every admitted local Atom, the Header.Container-derived IS_CONTAINED_BY target must be exactly `Scope Unit//PROJECT_TOOLS` (`CA-SU-19`). Its HAS_ACTIVE_SUBJECT target is closed to exactly the declared model entities or declared instances resolved at these Current local main Subject addresses:
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Serialization`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Directory Layout`
- `MODEL//CAPRMEDIO <+ Event Record`
- `MODEL//CAPRMEDIO <+ Package/Project Package`
- `MODEL//CAPRMEDIO <+ Implementation/Code/Tool`

The selection contains exact objects only, not strings, type members, or descendants; an unresolved address grants no admission.