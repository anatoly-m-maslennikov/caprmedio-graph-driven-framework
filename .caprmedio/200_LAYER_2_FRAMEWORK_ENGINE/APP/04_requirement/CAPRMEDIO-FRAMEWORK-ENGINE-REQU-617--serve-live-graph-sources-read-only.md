---
subject_scopes:
  - artifact-query
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 5
updated_at: 2026-08-19 03:43:48
relations:
  child_of:
    - CAPRMEDIO-METHODOLOGY-REQU-630--govern-current-non-authoritative-projections
---
# Serve live graph sources read-only

The APP Feature's local server must give its web pages strictly read-only access to registered current Atoms, Journals, Projections, and derived graph data; return source kind, raw content, canonical path, and current digest where applicable; and reject inactive or unregistered targets, path traversal, symlink escape, and every mutation.
