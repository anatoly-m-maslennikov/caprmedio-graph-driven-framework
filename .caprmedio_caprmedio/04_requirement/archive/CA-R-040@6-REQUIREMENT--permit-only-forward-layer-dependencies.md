---
subject_scopes:
- scope-topology
version: 6
updated_at: 2026-10-24 01:33:47 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CAPRMEDIO-REQU-001-CORE-REQUIREMENT--keep-nesting-sibling-order-and-navigation-distinct
  - CAPRMEDIO-REQU-031-CORE-REQUIREMENT--model-project-structure-as-numbered-levels
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Archived
atom_id: CA-R-040@6
---
# Permit only forward Layer dependencies

**every** dependency between Project Layers **must** point from the Project root **or** an earlier Layer **to** a later Layer **in** the cumulative order.
