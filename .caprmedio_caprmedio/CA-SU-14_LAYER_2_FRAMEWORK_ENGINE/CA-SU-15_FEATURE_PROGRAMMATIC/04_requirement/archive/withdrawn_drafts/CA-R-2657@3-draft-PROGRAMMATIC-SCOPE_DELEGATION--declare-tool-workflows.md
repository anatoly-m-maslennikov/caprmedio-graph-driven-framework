---
identity:
  atom_id: CA-R-2657
  ref_id: CA-R-2657@3-draft
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//TOOL_WORKFLOWS
  tier: 3
state:
  status: Draft
  version: 3
  updated_at: 2026-11-10 17:28:03 +0400
destination:
  file:
    name: CA-R-2657@3-draft-PROGRAMMATIC-SCOPE_DELEGATION--declare-tool-workflows.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/draft
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

Scope Unit//TOOL_WORKFLOWS ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC
```


### Prose Claim

The explicit default Role/Form pairs below are: `Requirement/Requirement`, `Requirement/Declaration`, `Requirement/Scope Delegation`, `Method/Decision`, `Evaluation/Decision`, `Evaluation/Eval Case`, `Delivery/Decision`, `Operations/Decision`, `Operations/Workflow`, `Operations/Step`, `Operations/Action`. Existing global default admissions, including existing Declaration families, remain unchanged; no additional pairs are granted. No exact Current Solution, Direct Policy, or Approach Policy Role/Form pair is selected. Analysis & Advisory / Code Synopsis remains admitted by the global default, and Plan / Work Report remains admitted only for an already admitted Task with the same Container and within the selected target boundary.

For every admitted local Atom, the Header.Container-derived IS_CONTAINED_BY target must be exactly `Scope Unit//TOOL_WORKFLOWS` (`CA-SU-18`). Its HAS_ACTIVE_SUBJECT target is closed to exactly the declared model entities or declared instances resolved at these Current local main Subject addresses:
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Serialization`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Selection`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Effect Authorization`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Directory Layout`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Dynamic Testing`
- `MODEL//CAPRMEDIO <+ Atom`
- `MODEL//CAPRMEDIO <+ Governing Configuration`
- `MODEL//CAPRMEDIO <+ Scope Unit`
- `Subject/CAPRMEDIO/Graph/Rule`

The selection contains exact objects only, not strings, type members, or descendants; an unresolved address grants no admission.