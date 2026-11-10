---
atom_id: CA-R-565
ref_id: CA-R-565@12
container:
  scope_unit: CA-SU-23
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source
    Retrieval
tier: 2
relations:
  child_of:
  - CA-R-564
  - CAPRMEDIO-METHODOLOGY-REQU-509-FRAMEWORK_METHODOLOGY-REQUIREMENT--govern-session-engine-rehydration-behavior
status: Archived
version: 12
updated_at: 2026-10-27 20:00:09 +0400
subject_scopes:
- skill-boundary
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: SKILLS
carrier_destination:
  file:
    name: CA-R-565@12-SKILLS-RULE--load-durable-authority-only-from-caprmedio.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-23_FEATURE_SKILLS/04_requirement/archive
---
## Summary

Load durable authority only from CAPRMEDIO

## Claim

### Prose Claim

CAPRMEDIO Skills **must** load durable project authority **only** from the owning project's governed `.caprmedio/` graph; host- **or** agent-specific memory, instruction, **and** context files, including `MEMORY.md`, `AGENTS.md`, **and** equivalents, **may** supply **only** ephemeral session context **and** operative planning.
