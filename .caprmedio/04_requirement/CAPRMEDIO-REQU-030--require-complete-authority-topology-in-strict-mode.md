---
subject_scopes:
  - requirement-topology
version: 5
updated_at: 2026-08-20 02:38:43
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-029--govern-each-scope-by-authority-mode
---
# Require complete authority topology in strict mode

A scope in strict authority mode must maintain a complete, conflict-free active RMED topology: every Goal, Principle, and Core has at least one permitted active child unless GOV registers its Type as terminal, the operative graph is acyclic, every edge follows the permitted tier and structural direction, and every operative relation target is active.
