---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  depends_on:
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
version: 19
updated_at: 2026-10-27 19:59:25 +0400
relations:
  child_of:
  - CA-D-440
atom_id: CA-D-444
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Separate candidate Project Structure from active authority

## Scope

the transition of a staged Project Structure candidate to active authority.

## Claim

a staged Project Structure candidate **must** use the filename `project_structure.candidate.toml` inside the explicitly selected migration workspace, outside the canonical active path. no ordinary consumer **may** discover it as active authority; candidate validation requires an explicit candidate path. cutover **must** install the validated candidate at the canonical path **only** **after** freshness, authorization, reference repairs, consumer readiness **and** recoverability checks pass. the old active bytes **must** remain recoverable through accepted change evidence **without** becoming another active structural source. the candidate **must** be retired **after** successful activation **or** rejection; failure **must not** leave two files eligible for normal authority resolution.

## Details
