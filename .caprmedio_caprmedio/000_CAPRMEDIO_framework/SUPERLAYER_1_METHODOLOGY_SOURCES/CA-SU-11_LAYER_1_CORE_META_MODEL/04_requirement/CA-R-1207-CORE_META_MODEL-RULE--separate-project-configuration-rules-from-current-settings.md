---
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  passive:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Extension Sources
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
version: 31
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1207
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Separate Project Configuration Rules from Current Settings

## Claim

### Prose Claim


Ownership of Project-specific expansion rules, constraints, defaults, current Extension activation, and selected Extension revisions.


the Project Configuration **must** own Project-specific expansion rules, constraints, **and** defaults **only** **where** the Core Meta-Model permits expansion; current Extension activation **and** selected Extension revisions **must** remain owned by the Framework Instance Settings Artifact, **not** duplicated **in** Project Configuration Atoms.
