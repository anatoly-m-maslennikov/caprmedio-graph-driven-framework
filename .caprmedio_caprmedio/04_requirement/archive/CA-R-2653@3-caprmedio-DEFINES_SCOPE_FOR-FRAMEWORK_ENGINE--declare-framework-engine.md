---
atom_id: CA-R-2653
ref_id: CA-R-2653@3
role: Requirement
form: Scope Delegation
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//FRAMEWORK_ENGINE
tier: 3
status: Archived
version: 3
updated_at: 2026-11-09 17:00:18 +0400
container:
  scope_unit: CA-SU-00
destination:
  file:
    name: CA-R-2653@3-caprmedio-DEFINES_SCOPE_FOR-FRAMEWORK_ENGINE--declare-framework-engine.md
    path: .caprmedio_caprmedio/04_requirement/archive
---

## Summary

Declare FRAMEWORK_ENGINE

## Claim

### Prose Claim

The receiving Scope Unit is FRAMEWORK_ENGINE. Existing default Role and Form admissions remain applicable. The additional local Role/Form pairs are exactly:

- Method / Direct Policy;
- Requirement / Definition;
- Requirement / Goal;
- Requirement / Rule;

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

- `CAPRMEDIO_STRUCTURE <+ Scope Unit//PROGRAMMATIC`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component Structure`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Test Design`;
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method`;
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit`;

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
