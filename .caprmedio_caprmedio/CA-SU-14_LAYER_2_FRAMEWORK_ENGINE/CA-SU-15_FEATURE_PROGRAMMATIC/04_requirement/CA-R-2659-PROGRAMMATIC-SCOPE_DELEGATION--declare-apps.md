---
identity:
  atom_id: CA-R-2659
  ref_id: CA-R-2659
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//APPS
  tier: 3
state:
  status: Active
  version: 3
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-2659-PROGRAMMATIC-SCOPE_DELEGATION--declare-apps.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
author: Anatoly Maslennikov
---
## Summary

Declare APPS

## Claim


### Prose Claim

The additional admitted local Role/Form pairs are:

- Requirement / Solution;
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
