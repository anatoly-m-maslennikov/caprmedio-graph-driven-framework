---
identity:
  id: CA-R-3008
  ref_id: CA-R-3008@9-draft
context:
  container:
    scope_unit: CA-SU-11
  role: requirement
  form: requirement
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  tier: 3
state:
  status: draft
  version: 9
  updated_at: '2026-11-11T16:37:55+04:00'
destination:
  file:
    name: CA-R-3008@9-draft-CORE_META_MODEL-REQUIREMENT--establish-project-and-non-project-scope-unit-declarations-and-delegations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---


## Summary

Establish Project and non-Project Scope Unit declarations and delegations

## Claim

### Prose Claim

- Each Scope Unit within the Project has exactly one Scope Unit Declaration. The Declaration has Requirement Role and states the unit’s structural facts. A non-Project unit’s Declaration is contained by its direct Parent. The Project Declaration is contained by predefined `world` (`CA-SU--1`).
- Each non-Project Scope Unit has one or more external Scope Delegations. Each Delegation has an RMEDO Role, identifies the receiving unit as its active Subject, and is contained by that unit’s direct structural Parent. Only that direct containing Scope Unit owns the Delegations.
- Each non-Project Scope Unit has exactly one direct Parent; Project has none. Project has one root Scope Unit Declaration and at least one Goal. Project may contain Delegations for its direct children and receives no Scope Delegation.
- Scope Delegation is admitted by default in every containing Scope Unit, including Project.
- The direct Parent assigns the receiving unit its contribution through the Scope Delegation. The receiving unit retains its own realization, including shared code, tests and CI; the direct Parent retains its wider scope and accountability.
- Local Role permissions: a Requirement delegation permits all RMEDO Roles; a Method, Evaluation, Delivery or Operations delegation permits its matching Role. When several Delegations apply, a local Atom requiring a listed Role/Form pair must have its pair and active Subject admitted by the same Delegation.
- Analysis and Advisory / Code Synopsis is admitted by default in every Scope Unit, including Project, subject to its applicable Subject and Container boundaries. This permission does not require a Code Synopsis and does not admit other Analysis and Advisory Forms.
- Plan / Work Report is admitted for an already admitted Task, with the same Container and within the applicable Subject boundaries. This admits reporting for existing work and requires no report to be created automatically.
- Local Form defaults: Requirement permits Requirement and existing Declaration families; Method permits Decision; Evaluation permits Decision and Eval Case; Delivery permits Decision; Operations permits Decision, Workflow, Step and Action. Decision is limited to MEDO Roles. Solution, Direct Policy and Approach Policy are RMEDO Forms, but a local Scope Delegation must explicitly include them in its Role/Form whitelist; they are not default local Forms.
- The predefined `world` Scope Unit (`CA-SU--1`) is outside the Project Scope Unit census and receives neither a Scope Unit Declaration nor a Scope Delegation. Project-level Requirement/Goal and root Axioms remain distinct.
