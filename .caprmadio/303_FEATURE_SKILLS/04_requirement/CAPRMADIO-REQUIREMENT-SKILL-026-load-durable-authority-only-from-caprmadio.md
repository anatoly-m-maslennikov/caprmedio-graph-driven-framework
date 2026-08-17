---
subject_scopes:
  - skill-boundary
version: 1
updated_at: 2026-08-17 18:57:41
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-SKILL-025-use-one-portable-shared-skill-runtime
    - CAPRMADIO-REQUIREMENT-SPEC-020-govern-session-engine-rehydration-behavior
---
# Load durable authority only from CAPRMADIO

CAPRMADIO Skills must load durable project authority only from the owning project's governed `.caprmadio/` graph; host- or agent-specific memory, instruction, and context files, including `MEMORY.md`, `AGENTS.md`, and equivalents, may supply only ephemeral session context and operative planning.
