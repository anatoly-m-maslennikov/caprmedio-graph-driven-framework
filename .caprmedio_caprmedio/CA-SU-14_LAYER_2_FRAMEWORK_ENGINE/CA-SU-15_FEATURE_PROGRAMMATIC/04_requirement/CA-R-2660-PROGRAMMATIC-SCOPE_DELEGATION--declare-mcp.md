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
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//MCP
  tier: 3
state:
  status: Active
  version: 6
  updated_at: 2026-11-11 15:29:41 +0400
destination:
  file:
    name: CA-R-2660-PROGRAMMATIC-SCOPE_DELEGATION--declare-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
author: Anatoly Maslennikov
---

## Summary

Declare MCP

## Claim


### Prose Claim

The receiving Scope Unit is MCP. The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Data Validation`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Output Publication`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Selection`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Effect Authorization`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Discovery and Navigation`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Entry`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Result and Status Presentation`;
- `MODEL//CAPRMEDIO <+ Project`;

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Resource Limits`;

### Formal Claim

```CFEL
# instances
Scope Unit//MCP.ID == "CA-SU-21";

Scope Unit//MCP.Name == "MCP";

Scope Unit//MCP.Label == "FEATURE";

Scope Unit//MCP.order.ordered == false;

Scope Unit//MCP ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC;

Atom/(.Header.Context.Container.scope_unit in ("CA-SU-21"))/(.Header.Context.Role in (Method)).Header.Context.Form :: Solution;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-21"))/(.Header.Context.Role in (Delivery)).Header.Context.Form :: Solution;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-21"))/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Rule;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-21"))/(.Header.Context.Role in (Concern)).Header.Context.Form :: Question;
```
