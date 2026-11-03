---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Constraint)'
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement).Header.Form'
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Actor
version: 18
updated_at: 2026-11-02 00:18:22 +0400
relations:
  method_for:
  - CA-R-1673@37
atom_id: CA-M-300
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Method
form: Implementation Method
---
## Summary
Use Constraint only for external limitations

## Claim

### Prose Claim

selection of a Requirement Type.


**to** select a Requirement Type, the Author **must** use Constraint **only** for a limitation imposed from outside the Project choice boundary.
