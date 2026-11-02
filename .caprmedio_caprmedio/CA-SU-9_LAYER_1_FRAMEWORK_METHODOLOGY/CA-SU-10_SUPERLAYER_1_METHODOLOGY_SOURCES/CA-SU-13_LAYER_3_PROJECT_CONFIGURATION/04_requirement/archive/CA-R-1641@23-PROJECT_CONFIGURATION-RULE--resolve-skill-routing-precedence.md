---
subjects:
  governs: Subject/Engineering
  depends_on:
  - Subject/Engineering/CAPRMEDIO Main Skill
  - Subject/Engineering/Skill
  - Subject/Domain/Node/Continuant/Scope Unit//PROJECT_CONFIGURATION
version: 23
updated_at: 2026-10-25 01:04:58 +0400
relations: {}
atom_id: CA-R-1641@23
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary
Resolve skill routing precedence

## Scope
skill route resolution.

## Claim

skill routes **must** resolve by explicit precedence: project-local CAPRMEDIO routes override framework routes, which override provider-global routes.

## Details
