---
atom_id: CA-R-3034
ref_id: CA-R-3034@1
container:
  scope_unit: CA-SU-00
role: requirement
form: scope_delegation
subjects:
  active: scope_unit//FRAMEWORK_METHODOLOGY
tier: 3
status: archived
version: 1
updated_at: '2026-11-12T15:04:13+00:00'
destination:
  file:
    name: CA-R-3034@1-CAPRMEDIO-SCOPE_DELEGATION-FRAMEWORK_METHODOLOGY--delegate-framework-methodology.md
    path: .caprmedio_caprmedio/04_requirement/099_archived
---

## Summary

Delegate FRAMEWORK_METHODOLOGY

## Claim

### Prose Claim

Project//caprmedio assigns Scope Unit//FRAMEWORK_METHODOLOGY responsibility for defining how Projects are represented and operated, including the Methodology used to develop CAPRMEDIO and its own Methodology. Project//caprmedio remains its direct containing Scope Unit and retains its wider scope and accountability. FRAMEWORK_METHODOLOGY retains its own realization.

In addition to the applicable model defaults, the admitted local Role/Form pairs are exactly:

- Requirement / Rule;
- Requirement / Goal;
- Method / Direct Policy.

The admitted HAS_ACTIVE_SUBJECT targets are exactly the endpoint objects at these typed addresses:

- `Aspects <+ Product`;
- `Scope Unit//FRAMEWORK_METHODOLOGY`;
- `Scope Unit//METHODOLOGY_SOURCES`.

Each address selects only its endpoint object, not its descendants or other members of its kind. An unresolved address grants no admission. These local permissions apply only when Header.Container resolves to FRAMEWORK_METHODOLOGY. The applicable default admission of Scope Delegation and supporting Plan / Work Report remains unchanged.

### Formal Claim

```CFEL
# instances
Scope Unit//FRAMEWORK_METHODOLOGY.ID == "CA-SU-9";

Scope Unit//FRAMEWORK_METHODOLOGY.Name == "FRAMEWORK_METHODOLOGY";

Scope Unit//FRAMEWORK_METHODOLOGY.Label == "LAYER";

Scope Unit//FRAMEWORK_METHODOLOGY.order.ordered == true;

Scope Unit//FRAMEWORK_METHODOLOGY.order.number == 1;

Scope Unit//FRAMEWORK_METHODOLOGY ((IS_CONTAINED_BY)) Project//caprmedio
```
