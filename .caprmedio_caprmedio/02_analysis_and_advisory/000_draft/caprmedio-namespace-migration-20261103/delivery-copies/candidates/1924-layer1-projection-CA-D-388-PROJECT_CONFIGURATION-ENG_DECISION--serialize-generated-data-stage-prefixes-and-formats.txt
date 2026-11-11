---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier
  passive:
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Serialization
  - CAPRMEDIO <+ MODEL <+ Projection
  - CAPRMEDIO <+ MODEL <+ Carrier.Format
version: 23
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-D-388
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-388-PROJECT_CONFIGURATION-ENG_DECISION--serialize-generated-data-stage-prefixes-and-formats.md
  source_atom_id: CA-D-388
  source_atom_revision: 23
  source_sha256: d31d32afd43e152d05d4533ca295f62d658669c4f3e31d3d65637c29091735f8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Generated Data Stage Prefixes and Formats

## Claim scope

Journal input and generated Projection Carriers.

## Claim

Journal input **and** generated Projection Carriers **must** use these ordered stage prefixes: canonical Journal input `src`, deterministic lossless staging Projection `stg`, consumer-ready semantic Projection `mrt`, **and** aggregated metrics Projection `biz`. `src` **must** use canonical NDJSON Journal input; `stg` **must** use TOON. these prefixes classify Journal inputs **and** generated Projections **only**. unregistered stage prefixes remain available for later governed Extension.
