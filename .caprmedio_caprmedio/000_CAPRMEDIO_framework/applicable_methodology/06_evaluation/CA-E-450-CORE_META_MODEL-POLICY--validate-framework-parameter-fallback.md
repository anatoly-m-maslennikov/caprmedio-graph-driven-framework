---
atom_id: CA-E-450
ref_id: CA-E-450
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Parameter Resolution
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
tier: 5
relations:
  evaluation_for:
  - CA-D-407
  - CA-D-408
  - CA-M-279
  - CA-R-1441
status: Active
version: 27
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-E-450-CORE_META_MODEL-EVAL_POLICY--validate-framework-parameter-fallback.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-450-CORE_META_MODEL-POLICY--validate-framework-parameter-fallback.md
  source_atom_id: CA-E-450
  source_atom_revision: 27
  source_sha256: 4400fcdf08d191562a08f1be0919ecfa456af4fb129a3653a046ccf469c11ebb
  original_relations_sha256: 65faded9bfe83c5b2b2d5e7359ce3fd2faf6195be2f2ede8ed1cbfde518b2f43
---
## Summary
Validate framework parameter fallback

## Claim

### Prose Claim

Framework parameter resolution across explicit parameters, Framework Instance Settings, **and** Default Settings.


the Evaluation **must** reject framework parameter resolution **if** **any** of the following falsifying conditions holds:

- a valid explicit parameter loses **to** a Default Settings value;
- a missing parameter fails **to** inherit its available valid default, including **when** another parameter **in** the same section is explicit;
- a valid explicit `false`, `0`, **or** empty value is mistaken for an absent parameter;
- an invalid explicit value is accepted **or** replaced by a fallback value;
- an invalid selected default is accepted, **or** a required parameter missing from Framework Instance Settings **and** Default Settings receives an invented value;
- an optional parameter absent from Framework Instance Settings **and** Default Settings is rejected solely for its absence;
- resolution reads another Project's instance selections **or** writes inherited values back as explicit selections;
- unchanged input values resolve differently on a repeated read;
- Default Settings uses an unregistered Carrier location **or** a parameter representation that differs from its registered Framework Instance Settings representation.

use the registered parameter constraints for the cases; **when** the current parameter catalog lacks a Boolean, zero-valued, **or** empty-valued example, use isolated test-fixture parameters **without** adding them **to** authoritative Settings.
