---
subjects:
  governs: "Entity/Continuant/Projection/Type: Applicable Methodology"
  depends_on:
    ["Applicable Methodology Conflict", "Applicable Methodology Source Frontier Digest", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/History/Journal.Record", "Methodology Source.Expansion Boundary"]
version: 14
updated_at: "2026-10-18 07:49:39 +0400"
relations:
  relates_to:
    - CA-O-007
    - CA-O-011
atom_id: "CA-R-1317"
content_role: "Requirement"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1317-PROJECT_CONFIGURATION-REQUIREMENT--fail-closed-on-unresolved-methodology-conflicts.md
  source_atom_id: CA-R-1317
  source_atom_revision: 14
  source_sha256: 5dc4c3d7180ccf4c5c3aac9d00fe7865b425f6e34033d07430fbd6f6e5d36548
  original_relations_sha256: 56595bb1f3f9fe9f5b758e4de0a03aa828cc25314d286bc50f06905262bd2204
---
# Summary

Fail Closed on Unresolved Methodology Conflicts

## Scope

unresolved conflicts in Applicable Methodology **and** their required Operator approvals.

## Claim

**if** an Applicable Methodology conflict remains unresolved **or** its required Operator approval is missing, stale, partial, ambiguous, **or** mismatched, **then** compilation **must** fail **without** changing Applicable Methodology membership.

## Details

qualifying approval **must** be the Operator's actual decision recorded **in** the Journal under CA-O-007 **and** bound **to** the exact conflict **and** source-frontier digest under CA-O-011. a Project Configuration approval Atom, an LLM judgment, **or** the mere presence of a Journal record **must not** substitute for that decision **or** bypass the Core expansion boundary.
