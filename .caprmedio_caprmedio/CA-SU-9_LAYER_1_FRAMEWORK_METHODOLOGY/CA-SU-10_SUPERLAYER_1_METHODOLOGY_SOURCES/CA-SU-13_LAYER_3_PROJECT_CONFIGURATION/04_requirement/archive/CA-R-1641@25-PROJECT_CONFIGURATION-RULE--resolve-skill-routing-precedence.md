---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Governing Configuration
  depends_on:
  - Subject/Graph Node/UX/CAPRMEDIO Skill and MCP Entry Interface
  - Subject/Graph Node/Engineering/Execution Control/Effect Authorization
  - Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
version: 25
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-R-1641@25
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
