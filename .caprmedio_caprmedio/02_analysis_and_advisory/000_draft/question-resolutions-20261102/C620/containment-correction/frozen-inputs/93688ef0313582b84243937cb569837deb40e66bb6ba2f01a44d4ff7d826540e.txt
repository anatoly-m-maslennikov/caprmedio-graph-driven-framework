---
subjects:
  active: Entity/Object/Continuant/Governing Objects/Governing Configuration
  passive:
  - Entity/Aspect/UX/Entry
  - Entity/Aspect/Engineering/Execution Control/Effect Authorization
  - Scope Unit//PROJECT_CONFIGURATION
version: 31
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1641
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Requirement
form: Rule
---
## Summary
Resolve skill routing precedence

## Claim scope
skill route resolution.

## Claim

skill routes **must** resolve by explicit precedence: project-local CAPRMEDIO routes override framework routes, which override provider-global routes.
