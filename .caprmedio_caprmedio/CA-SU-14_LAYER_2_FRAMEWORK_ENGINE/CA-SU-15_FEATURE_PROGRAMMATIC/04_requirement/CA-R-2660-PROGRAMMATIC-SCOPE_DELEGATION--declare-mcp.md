---
identity:
  atom_id: CA-R-2660
  ref_id: CA-R-2660
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//MCP
  tier: 3
state:
  status: Active
  version: 4
  updated_at: 2026-11-09 17:00:18 +0400
destination:
  file:
    name: CA-R-2660-PROGRAMMATIC-SCOPE_DELEGATION--declare-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
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

The receiving Scope Unit is MCP. Existing default Role and Form admissions remain applicable. The additional local Role/Form pairs are exactly:

- Method / Solution;
- Delivery / Solution;

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data Validation`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Output Publication`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source Selection`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect Authorization`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Entry`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Result and Status Presentation`;
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Project`;

Each address selects one endpoint object, not the address string, other members of its type or descendants. An unresolved address is diagnostic and grants no admission. These permissions apply only to local Atoms whose Header.Container resolves to MCP. The Scope Unit identity, Parent, responsibility and structural tree are unchanged.
