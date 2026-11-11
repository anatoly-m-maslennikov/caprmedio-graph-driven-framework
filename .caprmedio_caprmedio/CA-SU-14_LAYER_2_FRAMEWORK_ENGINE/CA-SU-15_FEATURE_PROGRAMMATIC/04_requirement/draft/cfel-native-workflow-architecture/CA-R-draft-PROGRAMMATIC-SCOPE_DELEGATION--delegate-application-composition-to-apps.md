---
identity:
  atom_id: CA-R-draft
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//APPS
  tier: 3
state:
  status: Draft
  version: 1
  updated_at: 2026-11-11 04:14:10 +0400
destination:
  file:
    name: CA-R-draft-PROGRAMMATIC-SCOPE_DELEGATION--delegate-application-composition-to-apps.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/draft/cfel-native-workflow-architecture
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-R-2659
---

## Summary

Delegate application composition to APPS

## Claim


### Prose Claim

The additional admitted local Role/Form pairs are:

- Requirement / Solution;
- Method / Solution;
- Method / Approach Policy;
- Requirement / Rule.

Existing default admissions, including Scope Delegation, remain unchanged. These permissions apply only to local Atoms whose Header.Container-derived IS_CONTAINED_BY target is `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//APPS`.

- Concern / Problem;
- Concern / Question;

Eligible HAS_ACTIVE_SUBJECT targets are exactly the declared model entities or declared instances resolved at these addresses:

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Component Structure`;

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//WORKBENCH`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction <+ Accessibility`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Effect Authorization`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Output Publication`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Recovery`

- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//WORKFLOW_ENGINE`

The selection contains exact objects only, not strings, type members, or descendants; an unresolved address grants no admission.

### Formal Claim

```CFEL
# instances
Scope Unit//APPS.ID == "CA-SU-20";

Scope Unit//APPS.Name == "APPS";

Scope Unit//APPS.Label == "FEATURE";

Scope Unit//APPS.order.ordered == false;

Scope Unit//APPS ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC
```


## Proposed receiving responsibility

APPS owns application composition, including WORKBENCH and the proposed WORKFLOW_ENGINE application. It may carry a Method / Solution for that composition. The proposed Engine consumes the Core language contract; APPS does not define Core CFEL meaning.

The separate WORKFLOW_ENGINE delegation candidate must establish that child before it becomes a Current unit. This candidate preserves APPS identity, Parent and unordered state and is not a command to create or start an application.
