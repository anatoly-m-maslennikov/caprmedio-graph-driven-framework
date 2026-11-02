---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Governing Configuration
  depends_on:
  - Entity/Aspect/UX/CAPRMEDIO Skill and MCP Entry Interface
  - Entity/Aspect/Engineering/Execution Control/Effect Authorization
  - Entity/Object/Continuant/Structural Unit/Scope Unit//PROJECT_CONFIGURATION
version: 27
updated_at: 2026-10-29 07:17:27 +0400
relations: {}
atom_id: CA-R-1641@27
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
