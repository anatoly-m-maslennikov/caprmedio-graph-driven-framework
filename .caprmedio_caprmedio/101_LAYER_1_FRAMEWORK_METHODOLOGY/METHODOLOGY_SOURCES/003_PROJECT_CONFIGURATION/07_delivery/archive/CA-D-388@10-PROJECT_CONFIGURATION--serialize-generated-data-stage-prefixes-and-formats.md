---
subjects:
  governs: Generated Data Stage Prefix
  depends_on:
  - Subject/Engineering/Carrier/Journal Serialization
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Engineering/Carrier.Format
version: 10
updated_at: 2026-10-23 03:14:50 +0400
relations: {}
atom_id: CA-D-388@10
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
global_tier: 11
---
# Summary

Serialize Generated Data Stage Prefixes and Formats

## Scope

Journal input and generated Projection Carriers.

## Claim

Journal input **and** generated Projection Carriers **must** use these ordered stage prefixes: canonical Journal input `src`, deterministic lossless staging Projection `stg`, consumer-ready semantic Projection `mrt`, **and** aggregated metrics Projection `biz`. `src` **must** use canonical NDJSON Journal input; `stg` **must** use TOON. these prefixes classify Journal inputs **and** generated Projections **only**. unregistered stage prefixes remain available for later governed Extension.

## Details
