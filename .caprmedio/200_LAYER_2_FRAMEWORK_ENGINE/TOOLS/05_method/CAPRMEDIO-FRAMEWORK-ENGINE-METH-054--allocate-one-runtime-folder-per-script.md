---
subject_scopes:
  - runtime
tier: core
version: 3
updated_at: 2026-08-19 16:45:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-264--one-runtime-folder-per-script
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-METH-053--isolate-runtime-state-under-caprmedio-runtime
---

# Allocate one runtime folder per script

Give each CAPRMEDIO script or executable tool that persists runtime files one
dedicated directory beneath the caprmedio runtime root. Keep its runtime files
inside that directory; concurrent runs may use bounded run-specific descendants.

Do not scatter runtime files, write into another script's directory, or depend
on an unowned shared directory. A shared runtime service owns its own directory
and clients use its service contract rather than its files.
