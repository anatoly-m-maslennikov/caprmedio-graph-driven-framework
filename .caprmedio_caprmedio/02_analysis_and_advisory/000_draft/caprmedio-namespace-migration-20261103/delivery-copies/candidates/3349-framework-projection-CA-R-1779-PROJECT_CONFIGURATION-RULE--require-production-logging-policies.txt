---
atom_id: CA-R-1779
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Observability <+ Logging
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Evaluation)
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Projection/Type: Catalog'
version: 17
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1779-PROJECT_CONFIGURATION-RULE--require-production-logging-policies.md
  source_atom_id: CA-R-1779
  source_atom_revision: 17
  source_sha256: f12e1d214ed11f20779d90feed6e689f7dbd5b204fd8a4e04938e45b212fd3e4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Require production Logging Policies

## Claim scope

production-relevant components **and** their Logging Policies.

## Claim

**every** production-relevant component **must** define a Logging Policy. that policy:

- governs required log coverage, structure, severity, safety, **and** retention **before** failures occur;
- supports its Evaluation Controls;
- is referenced by the Catalog Projection over its applicable Evaluation Control Atoms; **and**
- identifies the events **and** context required **to** understand normal operation, detect failure, correlate distributed work, **and** investigate real production issues.

## Details

the policy describes the evaluation boundary, while logger Implementation **and** emitted record Carriers realize it.
