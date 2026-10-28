---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Governing Configuration
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/UX/CAPRMEDIO Skill and MCP Entry Interface
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
version: 26
updated_at: 2026-10-27 19:59:59 +0400
relations: {}
atom_id: CA-R-1641
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
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
