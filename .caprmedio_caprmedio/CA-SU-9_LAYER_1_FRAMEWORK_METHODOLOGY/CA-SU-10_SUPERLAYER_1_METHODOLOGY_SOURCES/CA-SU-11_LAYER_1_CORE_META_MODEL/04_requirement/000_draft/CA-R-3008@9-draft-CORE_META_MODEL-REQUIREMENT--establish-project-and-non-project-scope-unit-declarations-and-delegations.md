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
- During the Python migration, the coexistence and combined-Delegation transition in CA-R-3006 applies until the affected Scope Units have separate Declarations.
- Each non-Project Scope Unit has one or more external Scope Delegations. Each Delegation has an RMEDO Role, identifies the receiving unit as its Main Subject, and is contained by that unit’s direct structural Parent. Only that direct containing Scope Unit owns the Delegations.
- Each non-Project Scope Unit has exactly one direct Parent; Project has none. Project has one root Scope Unit Declaration and at least one Goal. Project may contain Delegations for its direct children and receives no Scope Delegation.
- The direct Parent assigns the receiving unit its contribution through the Scope Delegation. The receiving unit retains its own realization, including shared code, tests and CI; the direct Parent retains its wider scope and accountability.
- Every Scope Unit admits every Role and Form combination valid in its applicable Model. Scope Delegations admit Main Subjects.
- A Plan / Work Report reports an admitted Task. It has the Task's Container and meets the applicable Main Subject boundaries.
- The predefined `world` Scope Unit (`CA-SU--1`) is outside the Project Scope Unit census and receives neither a Scope Unit Declaration nor a Scope Delegation. Project-level Requirement/Goal and root Axioms remain distinct.
