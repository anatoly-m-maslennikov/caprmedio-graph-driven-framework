---
atom_id: CA-R-1779
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Observability <+ Logging
  passive:
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - 'CAPRMEDIO_MODEL <+ Projection/(.Form:=Catalog)'
version: 17
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1779-PROJECT_CONFIGURATION-RULE--require-production-logging-policies.md
  source_atom_id: CA-R-1779
  source_atom_revision: 17
  source_sha256: 2dde910a97d76d03b6b9d2be4d3ddf9f1b421626e91e9910420d0917ac7faf5b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Require production Logging Policies

## Claim

### Prose Claim


production-relevant components **and** their Logging Policies.


**every** production-relevant component **must** define a Logging Policy. that policy:

- governs required log coverage, structure, severity, safety, **and** retention **before** failures occur;
- supports its Evaluation Controls;
- is referenced by the Catalog Projection over its applicable Evaluation Control Atoms; **and**
- identifies the events **and** context required **to** understand normal operation, detect failure, correlate distributed work, **and** investigate real production issues.

## Details

the policy describes the evaluation boundary, while logger Implementation **and** emitted record Carriers realize it.
