---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Governance Origin
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Term//Artifact
  - 'Entity/Aspect/Product: CAPRMEDIO Framework'
  - Entity/Object/Continuant/Structural Unit/Scope Unit//PROJECT_CONFIGURATION
version: 36
updated_at: 2026-10-29 10:13:51 +0400
relations: {}
atom_id: CA-R-1645@36
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Define self-hosted Governance origins

## Claim scope

Governance Origin for the self-hosted caprmedio Project and its distributed CAPRMEDIO sources.

## Claim

Governance Origin for the self-hosted caprmedio Project **and** its distributed CAPRMEDIO sources follows the ownership distinction **in** CA-R-1709-CORE_META_MODEL-DEFINITION--define-two-governance-origins:

- within the caprmedio Project, its Project-owned Methodology authority, framework authority, **and** other Project-owned Artifacts have internal Governance Origin.
- a distributed CAPRMEDIO framework source has external Governance Origin relative **to** a consuming Project. that Project's own adaptation authority has internal Governance Origin; creating it does **not** transfer ownership of the external source **or** change that source's origin.
- graph Relations, version-control authorship, filesystem ownership, **and** byte identity do **not** replace the governing ownership distinction.
