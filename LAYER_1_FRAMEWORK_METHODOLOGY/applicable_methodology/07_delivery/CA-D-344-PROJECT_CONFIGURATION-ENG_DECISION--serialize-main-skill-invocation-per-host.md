---
atom_id: CA-D-344
ref_id: CA-D-344
container:
  scope_unit: CA-SU-13
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ UX <+ Entry
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ UX <+ Entry
tier: 3
status: Active
version: 23
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-D-344-PROJECT_CONFIGURATION-DECISION--serialize-main-skill-invocation-per-host.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-344-PROJECT_CONFIGURATION-ENG_DECISION--serialize-main-skill-invocation-per-host.md
  source_atom_id: CA-D-344
  source_atom_revision: 23
  source_sha256: 5c1aebaa4a500b1e0da12dc8226bb190961b03f804896813809f666688b9c69d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Main Skill Invocation per Host

## Claim

### Prose Claim


Host Invocations for the CAPRMEDIO Main Skill **and** separately authorized compatibility layers.


for the CAPRMEDIO Main Skill, the Host Invocation **must** serialize as `$ca` **in** Codex; **if** a Claude compatibility Extension **or** Operator-provided compatibility layer is separately authorized by the Operator, **then** its Host Invocation **must** serialize as `/ca` **in** Claude.
