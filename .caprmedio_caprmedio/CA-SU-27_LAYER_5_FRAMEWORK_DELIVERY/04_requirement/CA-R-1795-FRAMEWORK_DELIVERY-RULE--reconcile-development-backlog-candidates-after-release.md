---
atom_id: CA-R-1795
ref_id: CA-R-1795
container:
  scope_unit: CA-SU-27
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering
tier: 4
relations:
  depends_on:
  - CA-O-058
  - CA-R-1702
status: Active
version: 16
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-R-1795-FRAMEWORK_DELIVERY-RULE--reconcile-development-backlog-candidates-after-release.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/04_requirement
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
---

## Summary
Reconcile Development Backlog candidates **after** release

## Claim

### Prose Claim

Development Backlog candidates **after** a Release Record is accepted.


CAPRMEDIO **must** reconcile the Development Backlog against its exact released manifest as follows:

- remove a candidate whose promoted Atoms were fully delivered **in** that release.
- **every** candidate that is unfinished, partially delivered, excluded, **or** newly deferred **must** remain unscheduled **or** move **to** another target version.
- a candidate **must not** be removed as shipped **unless** the released manifest accounts for its promoted Atoms.
