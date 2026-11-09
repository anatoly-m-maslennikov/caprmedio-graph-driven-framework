---
identity:
  atom_id: CA-R-2660@2
  ref_id: CA-R-2660@2
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//MCP
  tier: 3
state:
  status: Archived
  version: 2
  updated_at: 2026-11-08 23:18:49 +0400
destination:
  file:
    name: CA-R-2660@2-PROGRAMMATIC-SCOPE_DELEGATION--declare-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/archive
---
## Summary

Declare MCP

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//MCP.ID == "CA-SU-21";

Scope Unit//MCP.Name == "MCP";

Scope Unit//MCP.Label == "FEATURE";

Scope Unit//MCP.order.ordered == false;

Scope Unit//MCP ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC
```


### Prose Claim

The explicit default Role/Form pairs below are: `Requirement/Requirement`, `Requirement/Declaration`, `Requirement/Scope Delegation`, `Method/Decision`, `Evaluation/Decision`, `Evaluation/Eval Case`, `Delivery/Decision`, `Operations/Decision`, `Operations/Workflow`, `Operations/Step`, `Operations/Action`. Existing global default admissions, including existing Declaration families, remain unchanged; no additional pairs are granted. No exact Current Solution, Direct Policy, or Approach Policy Role/Form pair is selected. Implementation / Code Synopsis remains admitted by the global default, and Plan / Work Report remains admitted only for an already admitted Task with the same Container and within the selected target boundary.

For every admitted local Atom, the Header.Container-derived IS_CONTAINED_BY target must be exactly `Scope Unit//MCP` (`CA-SU-21`). Its HAS_ACTIVE_SUBJECT target is closed to exactly the declared model entities or declared instances resolved at these Current local main Subject addresses:
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Output Publication`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Selection`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Entry`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Result and Status Presentation`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Project`

The selection contains exact objects only, not strings, type members, or descendants; an unresolved address grants no admission.