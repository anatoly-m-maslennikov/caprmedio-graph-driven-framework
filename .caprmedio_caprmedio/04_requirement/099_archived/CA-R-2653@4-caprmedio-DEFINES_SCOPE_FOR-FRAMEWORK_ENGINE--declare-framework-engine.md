---
atom_id: CA-R-2653
ref_id: CA-R-2653@4
role: Requirement
form: Scope Delegation
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//FRAMEWORK_ENGINE
tier: 3
status: archived
version: 4
updated_at: 2026-11-10 20:47:54 +0400
container:
  scope_unit: CA-SU-00
destination:
  file:
    name: CA-R-2653@4-caprmedio-DEFINES_SCOPE_FOR-FRAMEWORK_ENGINE--declare-framework-engine.md
    path: .caprmedio_caprmedio/04_requirement/099_archived
author: Anatoly Maslennikov
---

## Summary

Declare FRAMEWORK_ENGINE

## Claim

### Prose Claim

The receiving Scope Unit is FRAMEWORK_ENGINE. The additional local Role/Form pairs are exactly:

- Method / Direct Policy;
- Requirement / Definition;
- Requirement / Goal;
- Requirement / Rule;

- Method / Solution;

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

- `PROJECT STRUCTURE//CAPRMEDIO`;

- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//PROGRAMMATIC`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Component Structure`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Design`;
- `MODEL//CAPRMEDIO <+ Atom/Content Role: Method`;
- `MODEL//CAPRMEDIO <+ Scope Unit`;

- `MODEL//CAPRMEDIO <+ Atom`;
- `MODEL//CAPRMEDIO <+ Execution/Workflow Run`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//AGENTIC`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Frontend Engineering`;

Each address selects one endpoint object, not the address string, other members of its type or descendants. An unresolved address is diagnostic and grants no admission. These permissions apply only to local Atoms whose Header.Container resolves to FRAMEWORK_ENGINE. Its identity, Name, Label, Parent, order and existing responsibility remain unchanged.

### Formal Claim

```CFEL
# instances
Scope Unit//FRAMEWORK_ENGINE.ID == "CA-SU-14";

Scope Unit//FRAMEWORK_ENGINE.Name == "FRAMEWORK_ENGINE";

Scope Unit//FRAMEWORK_ENGINE.Label == "LAYER";

Scope Unit//FRAMEWORK_ENGINE.order.ordered == true;

Scope Unit//FRAMEWORK_ENGINE.order.number == 2;

Scope Unit//FRAMEWORK_ENGINE ((IS_CONTAINED_BY)) Project//caprmedio
```
