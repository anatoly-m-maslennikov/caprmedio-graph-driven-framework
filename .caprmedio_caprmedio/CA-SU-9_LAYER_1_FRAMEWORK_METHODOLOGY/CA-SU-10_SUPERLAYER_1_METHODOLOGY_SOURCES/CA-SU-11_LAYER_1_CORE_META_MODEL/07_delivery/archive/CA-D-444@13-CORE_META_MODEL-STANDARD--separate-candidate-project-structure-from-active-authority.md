---
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Structure
  depends_on:
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Project.Structure
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 13
updated_at: 2026-10-24 01:37:42 +0400
relations:
  child_of:
  - CA-D-440
  relates_to:
  - CA-O-015
atom_id: CA-D-444@13
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
