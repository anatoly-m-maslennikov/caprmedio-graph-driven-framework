---
subject_scopes:
  - requirement-topology
version: 3
updated_at: 2026-08-17 18:42:51
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-224-govern-each-scope-by-authority-mode
---
# Require complete authority topology in strict mode

A scope in strict authority mode must maintain a complete, conflict-free active RMAD topology: every Principle and Core has at least one permitted active child, the operative graph is acyclic, every edge follows the permitted tier and structural direction, and every operative relation target is active.
