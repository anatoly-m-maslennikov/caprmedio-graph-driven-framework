---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Rule
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - 'Subject/caprmedio/Product: CAPRMEDIO Framework'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
version: 32
updated_at: 2026-10-27 19:59:59 +0400
relations: {}
atom_id: CA-R-1645
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Define self-hosted Governance origins

## Scope

Governance Origin for the self-hosted caprmedio Project and its distributed CAPRMEDIO sources.

## Claim

Governance Origin for the self-hosted caprmedio Project **and** its distributed CAPRMEDIO sources follows the ownership distinction **in** CA-R-1709-CORE_META_MODEL-DEFINITION--define-two-governance-origins:

- within the caprmedio Project, its Project-owned Methodology authority, framework authority, **and** other Project-owned Artifacts have internal Governance Origin.
- a distributed CAPRMEDIO framework source has external Governance Origin relative **to** a consuming Project. that Project's own adaptation authority has internal Governance Origin; creating it does **not** transfer ownership of the external source **or** change that source's origin.
- graph Relations, version-control authorship, filesystem ownership, **and** byte identity do **not** replace the governing ownership distinction.

## Details
