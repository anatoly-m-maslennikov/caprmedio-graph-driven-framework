---
atom_id: CA-R-1565
ref_id: CA-R-1565
container:
  scope_unit: CA-SU-11
role: Requirement
form: Requirement
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations).Header.Form
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)
tier: 1
status: Active
version: 23
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-R-1565-CORE_META_MODEL-REQUIREMENT--admit-the-operations-atom-types.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Admit the Operations Atom Types

## Claim

### Prose Claim

internal Form values of Operations Atoms.

the admitted Form values of `Atom/(.Header.Role := Operations).Header.Form` **must** include (Action, Workflow, Step, Scope Delegation, Solution, Direct Policy, Approach Policy, Decision). An Operations Atom may use Scope Delegation, Solution, Direct Policy, Approach Policy, or Decision only when its Claim's actual primary contribution matches the reviewed Operations semantics. Those Forms do not create an Action, Workflow, or Step binding.

## Details

Action, Workflow, and Step retain their existing Form admission and behavior. Branch and Fork remain not admitted internal Form values. Linear and Conditional remain Step forms carried by Step definitions, not additional Operations Atom Forms.
