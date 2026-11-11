---
identity:
  id: CA-E-670
  ref_id: CA-E-670@5-draft
context:
  container:
    scope_unit: CA-SU-11
  role: evaluation
  form: eval_policy
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  tier: 3
state:
  status: draft
  version: 5
  updated_at: '2026-11-11T16:37:55+04:00'
destination:
  file:
    name: CA-E-670@5-draft-CORE_META_MODEL-EVAL_POLICY--check-scope-unit-declarations-goals-and-contracts.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/000_draft
---


## Summary

Check Scope Unit Declarations, Goals and Contracts

## Claim

### Prose Claim


Identify every structural Atom by Role Requirement and Form Scope Unit Declaration. The Main Subject names the specific Scope Unit. Count exactly one matching structural Atom for each Scope Unit within the Project; predefined `world` (`CA-SU--1`) has no Declaration or Delegation; do not count unrelated Atoms as structural declarations.

Check the selected sources for one external structural Atom per Scope Unit within the Project, its stable ID, Name, ordered state, optional Label, conditional order.number and direct containment. Check that Project is unordered, has one stable Scope Unit ID and has no order.number. Check that its Declaration is outside Project and contained by predefined `world`.

Check separately that every non-Project Scope Unit receives at least one Scope Delegation from its direct containing Scope Unit. Each Delegation carries the assigned contribution and applicable permissions. Check that Project receives at least one Goal.

Check that folder names are derived by the shared naming Policy rather than copied into a Declaration. Ordered names include order.number; unordered names omit the order segment and separator.

Reject the selected Declaration set when:

- a Scope Unit ID or Name is duplicated or invalid;
- a Scope Unit Declaration uses the ID `CA-SU--1` reserved for predefined `world`;
- a non-Project Scope Unit other than predefined `world` has a missing direct parent, or a declared direct parent is unresolved, self-referential or in another Project;
- parentage has a cycle;
- a retained ancestry or path disagrees with the declared parent chain;
- ordering fields or Labels are invalid, ordered siblings share a number, or an Unordered unit has a number;
- derived paths collide, escape the Project boundary or leave lookup ambiguous;
- unsupported fields or expressions are used as structural declarations.

Label does not determine ordered state. Check a valid example and a falsifying example for each applicable condition.
