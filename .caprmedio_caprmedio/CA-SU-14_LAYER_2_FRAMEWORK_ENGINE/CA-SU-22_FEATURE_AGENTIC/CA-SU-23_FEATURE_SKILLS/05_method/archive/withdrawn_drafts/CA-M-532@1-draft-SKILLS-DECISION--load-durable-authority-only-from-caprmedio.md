---
atom_id: CA-M-532
ref_id: CA-M-532@1-draft
container:
  scope_unit: CA-SU-23
role: Method
form: Decision
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data
    Handling <+ Source Retrieval
tier: 2
relations:
  child_of:
  - CA-R-564
  IS_REPLACEMENT_FOR:
  - CA-R-565
status: Draft
version: 1
updated_at: 2026-11-10 11:53:32 +0400
subject_scopes:
- skill-boundary
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: SKILLS
destination:
  file:
    name: CA-M-532@1-draft-SKILLS-DECISION--load-durable-authority-only-from-caprmedio.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-23_FEATURE_SKILLS/05_method/draft
---
## Summary

Load durable authority only from CAPRMEDIO

## Claim

### Prose Claim

CAPRMEDIO Skills **must** load durable project authority **only** from the owning project's governed `.caprmedio/` graph; host- **or** agent-specific memory, instruction, **and** context files, including `MEMORY.md`, `AGENTS.md`, **and** equivalents, **may** supply **only** ephemeral session context **and** operative planning.
