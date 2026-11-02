---
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Carrier
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Carrier/Journal Serialization
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Engineering/Continuant/Carrier.Format
version: 15
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-D-388@15
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize Generated Data Stage Prefixes and Formats

## Scope

Journal input and generated Projection Carriers.

## Claim

Journal input **and** generated Projection Carriers **must** use these ordered stage prefixes: canonical Journal input `src`, deterministic lossless staging Projection `stg`, consumer-ready semantic Projection `mrt`, **and** aggregated metrics Projection `biz`. `src` **must** use canonical NDJSON Journal input; `stg` **must** use TOON. these prefixes classify Journal inputs **and** generated Projections **only**. unregistered stage prefixes remain available for later governed Extension.

## Details
