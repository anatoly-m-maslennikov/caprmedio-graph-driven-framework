---
atom_id: CA-E-670
ref_id: CA-E-670
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
tier: 3
status: Active
version: 4
updated_at: "2026-11-07 15:28:42 +0400"
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-E-670-CORE_META_MODEL-EVAL_POLICY--check-scope-unit-declarations-goals-and-contracts.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-670-CORE_META_MODEL-EVAL_POLICY--check-scope-unit-declarations-goals-and-contracts.md
  source_atom_id: CA-E-670
  source_atom_revision: 4
  source_sha256: 10dac2f750cb84abe722cf48c627cf73666ec33a4478a403f25614e733cd6509
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Check Scope Unit Declarations, Goals and Contracts

## Claim

### Prose Claim


Identify the Project root structural Atom by Role Requirement and Form Scope Unit Declaration, and each non-Project Scope Unit’s structural Atom by Form Scope Delegation and its admitted RMEDO Role. The Main Subject names the specific Scope Unit. Count exactly one matching structural Atom for each Scope Unit within the Project; predefined `world` (`CA-SU--1`) has no Declaration or Delegation; do not count unrelated Atoms as structural declarations.

Check the selected sources for one external structural Atom per Scope Unit within the Project, its stable ID, Name, ordered state, optional Label, conditional order.number and direct containment. Check that Project is unordered, has one stable Scope Unit ID and has no order.number. Check that its Declaration is outside Project and contained by predefined `world`.

Check that folder names are derived by the shared naming Policy rather than copied into a Declaration. Ordered names include order.number; unordered names omit the order segment and separator.

Reject the selected Declaration set when:

- a Scope Unit ID or Name is duplicated or invalid;
- a Project Scope Unit Declaration or Scope Delegation uses the ID `CA-SU--1` reserved for predefined `world`;
- a non-Project Scope Unit other than predefined `world` has a missing direct parent, or a declared direct parent is unresolved, self-referential or in another Project;
- parentage has a cycle;
- a retained ancestry or path disagrees with the declared parent chain;
- ordering fields or Labels are invalid, ordered siblings share a number, or an Unordered unit has a number;
- derived paths collide, escape the Project boundary or leave lookup ambiguous;
- unsupported fields or expressions are used as structural declarations.

Label does not determine ordered state. Check a valid example and a falsifying example for each applicable condition.
