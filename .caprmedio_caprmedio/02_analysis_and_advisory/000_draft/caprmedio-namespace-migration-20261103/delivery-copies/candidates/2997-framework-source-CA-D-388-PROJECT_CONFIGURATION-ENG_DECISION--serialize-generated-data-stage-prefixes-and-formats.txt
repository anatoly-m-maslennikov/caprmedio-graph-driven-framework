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
---
## Summary

Serialize Generated Data Stage Prefixes and Formats

## Claim scope

Journal input and generated Projection Carriers.

## Claim

Journal input **and** generated Projection Carriers **must** use these ordered stage prefixes: canonical Journal input `src`, deterministic lossless staging Projection `stg`, consumer-ready semantic Projection `mrt`, **and** aggregated metrics Projection `biz`. `src` **must** use canonical NDJSON Journal input; `stg` **must** use TOON. these prefixes classify Journal inputs **and** generated Projections **only**. unregistered stage prefixes remain available for later governed Extension.
