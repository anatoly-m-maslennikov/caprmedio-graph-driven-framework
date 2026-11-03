---
atom_id: CA-E-670
form: Eval Policy
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Scope Unit
version: 1
relations: {}
tier: 3
updated_at: 2026-11-02 19:17:40 +0400
role: Evaluation
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-670-CORE_META_MODEL-EVAL_POLICY--check-scope-unit-declarations-goals-and-contracts.md
  source_atom_id: CA-E-670
  source_atom_revision: 1
  source_sha256: e3c94fdfc7e0e75bacc9edfeb1dc1b223dd9501c4b41455bfcc241ed53bd252a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Check Scope Unit Declarations, Goals and Contracts

## Claim

Identify Scope Unit Declaration Atoms by Role Requirement, Form Scope Unit Declaration and active Subject (`subjects.active`) naming the specific Scope Unit. Count exactly one matching Declaration for each Scope Unit; do not count other Requirements about that Scope Unit as Declarations.

Check the selected sources for one external Declaration per Scope Unit, its declared ID where applicable, Name, ordered state, optional Label, conditional order.number and direct containment. Check that Project is unordered and has neither Scope Unit ID nor order.number. Check that its Declaration is outside Project with external Operator ownership.

Check that folder names are derived by the shared naming Policy rather than copied into a Declaration. Ordered names include order.number; unordered names omit the order segment and separator.

Reject the selected Declaration set when:

- a Scope Unit ID or Name is duplicated or invalid;
- a direct parent is missing, unresolved, self-referential or in another Project;
- parentage has a cycle;
- a retained ancestry or path disagrees with the declared parent chain;
- ordering fields or Labels are invalid, ordered siblings share a number, or an Unordered unit has a number;
- derived paths collide, escape the Project boundary or leave lookup ambiguous;
- unsupported fields or expressions are used as structural declarations.

Label does not determine ordered state. Check a valid example and a falsifying example for each applicable condition.
