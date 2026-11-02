---
subject_scopes:
- skill-boundary
version: 7
updated_at: 2026-10-24 02:04:43 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-564
  - CAPRMEDIO-METHODOLOGY-REQU-509-FRAMEWORK_METHODOLOGY-REQUIREMENT--govern-session-engine-rehydration-behavior
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: SKILLS
status: Archived
atom_id: CA-R-565@7
type: Rule
---
# Load durable authority only from CAPRMEDIO

CAPRMEDIO Skills **must** load durable project authority **only** from the owning project's governed `.caprmedio/` graph; host- **or** agent-specific memory, instruction, **and** context files, including `MEMORY.md`, `AGENTS.md`, **and** equivalents, **may** supply **only** ephemeral session context **and** operative planning.
