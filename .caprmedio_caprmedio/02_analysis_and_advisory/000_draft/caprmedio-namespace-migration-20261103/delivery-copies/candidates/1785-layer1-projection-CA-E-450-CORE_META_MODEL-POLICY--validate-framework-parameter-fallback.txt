---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Parameter Resolution
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
  - CAPRMEDIO <+ MODEL <+ Project
  - CAPRMEDIO <+ MODEL <+ Carrier
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Evaluation)
version: 27
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-D-407
  - CA-D-408
  - CA-M-279
  - CA-R-1441
atom_id: CA-E-450
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Evaluation
form: Eval Policy
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-450-CORE_META_MODEL-POLICY--validate-framework-parameter-fallback.md
  source_atom_id: CA-E-450
  source_atom_revision: 27
  source_sha256: 8df5a2dca118556516581459c309f2bfb05119ae7fd22740b073c2f0824ba3a7
  original_relations_sha256: 65faded9bfe83c5b2b2d5e7359ce3fd2faf6195be2f2ede8ed1cbfde518b2f43
---
## Summary
Validate framework parameter fallback

## Claim scope
Framework parameter resolution across explicit parameters, Framework Instance Settings, **and** Default Settings.

## Claim

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
