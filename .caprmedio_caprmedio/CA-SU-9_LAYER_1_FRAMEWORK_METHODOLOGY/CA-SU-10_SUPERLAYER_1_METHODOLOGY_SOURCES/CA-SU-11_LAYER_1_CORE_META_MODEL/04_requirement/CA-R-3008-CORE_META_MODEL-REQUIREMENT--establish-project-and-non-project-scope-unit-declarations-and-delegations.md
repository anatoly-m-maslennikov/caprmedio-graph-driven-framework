---
atom_id: CA-R-3008
ref_id: CA-R-3008
container:
  scope_unit: CA-SU-11
role: Requirement
form: Requirement
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
tier: 3
status: Active
version: 8
updated_at: 2026-11-11 15:25:07 +0400
carrier_destination:
  file:
    name: CA-R-3008-CORE_META_MODEL-REQUIREMENT--establish-project-and-non-project-scope-unit-declarations-and-delegations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Establish Project and non-Project Scope Unit declarations and delegations

## Claim

### Prose Claim

- Each non-Project Scope Unit within the Project has exactly one external Scope Delegation. Its active Subject identifies the receiving unit, and its Container is the unit’s one direct structural Parent. Only that direct containing Scope Unit owns the delegation; ancestors and unrelated units do not.
- Each non-Project Scope Unit within the Project has exactly one direct Parent; Project has none. Project has one root Scope Unit Declaration, may contain delegations for its direct children, and receives none.
- Scope Delegation is admitted by default in every containing Scope Unit, including Project.
- The direct Parent assigns the receiving unit its contribution through the Scope Delegation. The receiving unit retains its own realization, including shared code, tests and CI; the direct Parent retains its wider scope and accountability.
- Local Role permissions: a Requirement delegation permits all RMEDO Roles; a Method, Evaluation, Delivery or Operations delegation permits its matching Role.
- Plan / Work Report is admitted for an already admitted Task, with the same Container and within the applicable Subject boundaries. This admits reporting for existing work and requires no report to be created automatically.
- Local Form defaults: Requirement permits Requirement and existing Declaration families; Method permits Decision; Evaluation permits Decision and Eval Case; Delivery permits Decision; Operations permits Decision, Workflow, Step and Action. Decision is limited to MEDO Roles. Solution, Direct Policy and Approach Policy are RMEDO Forms, but a local Scope Delegation must explicitly include them in its Role/Form whitelist; they are not default local Forms.
- The predefined `world` Scope Unit (`CA-SU--1`) is outside the Project Scope Unit census and receives neither a Project declaration nor a Scope Delegation. Project-level Requirement/Goal and root Axioms remain distinct.
