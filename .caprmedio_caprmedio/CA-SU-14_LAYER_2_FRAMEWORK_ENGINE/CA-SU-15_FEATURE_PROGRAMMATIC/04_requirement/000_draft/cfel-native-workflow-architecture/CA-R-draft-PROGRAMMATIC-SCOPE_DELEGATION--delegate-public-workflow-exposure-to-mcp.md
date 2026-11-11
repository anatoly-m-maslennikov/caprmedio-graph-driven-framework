---
identity:
  atom_id: CA-R-draft
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//MCP
  tier: 3
state:
  status: Draft
  version: 1
  updated_at: 2026-11-11 04:14:10 +0400
destination:
  file:
    name: CA-R-draft-PROGRAMMATIC-SCOPE_DELEGATION--delegate-public-workflow-exposure-to-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/000_draft/cfel-native-workflow-architecture
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-R-2660
---

## Summary

Delegate public Workflow exposure to MCP

## Claim


### Prose Claim

The receiving Scope Unit is MCP. The additional local Role/Form pairs are exactly:

- Method / Solution;
- Delivery / Solution;

- Requirement / Rule;

- Concern / Question;

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

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

Scope Unit//MCP ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC
```


## Proposed receiving responsibility

MCP owns public MCP transport and the exposure of selected Workflows as MCP Tools. It consumes the Workflow Engine API and derives the public boundary from Workflow contracts. It does not own internal Tool implementations, Workflow control flow or Core CFEL semantics. Preserve the receiving unit identity, Parent, unordered state and the existing exact Role/Form and active Subject admissions above.

## Adoption boundary

This candidate replaces CA-R-2660 only if adopted. It does not modify the live Tool registry or reinterpret an installed provider as an executable Workflow before the corresponding definitions and engine exist.
