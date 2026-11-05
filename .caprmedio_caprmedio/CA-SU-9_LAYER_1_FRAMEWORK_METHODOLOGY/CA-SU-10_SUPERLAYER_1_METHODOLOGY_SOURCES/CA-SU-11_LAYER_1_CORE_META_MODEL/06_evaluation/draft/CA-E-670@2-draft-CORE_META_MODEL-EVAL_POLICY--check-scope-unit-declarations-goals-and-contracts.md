---
atom_id: CA-E-670
form: Eval Policy
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit
version: 2
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
updated_at: 2026-11-05 12:58:42 +0400
role: Evaluation
carrier_destination:
  file:
    name: CA-E-670@2-draft-CORE_META_MODEL-EVAL_POLICY--check-scope-unit-declarations-goals-and-contracts.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/draft
---
## Summary

Check Scope Unit Declarations, Goals and Contracts

## Claim

### Prose Claim


Identify Scope Unit Declaration Atoms by Role Requirement, Form Scope Unit Declaration and active Subject (`subjects.active`) naming the specific Scope Unit. Count exactly one matching Declaration for every Scope Unit except the predefined Scope Unit `world` (`CA-SU--1`), which has no Declaration; do not count other Requirements about that Scope Unit as Declarations.

Check the selected sources for one external Declaration per Scope Unit except predefined `world`, its declared ID, Name, ordered state, optional Label, conditional order.number and direct containment. Check that Project is unordered and has no order.number. Check that its Declaration is outside Project with external Operator ownership.

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
