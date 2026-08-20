---
subject_scopes:
  - relation-model
tier: core
version: 2
updated_at: 2026-08-20 19:54:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-085--separate-active-authority-from-preserved-history
---
# Keep active RMEDO relations within active authority

Every direct relation authored by an active RMEDO Atom must target another active Atom. A target in draft, done, archived, or otherwise inactive lifecycle placement is invalid even when its historical carrier remains addressable.
