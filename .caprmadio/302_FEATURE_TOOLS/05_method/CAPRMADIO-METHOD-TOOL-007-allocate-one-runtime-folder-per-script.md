---
artifact_type: method
artifact_id: CAPRMADIO-METHOD-TOOL-007
scope_path: feature:tools
subject_scopes:
  - runtime
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-111
  child_of:
    - CAPRMADIO-METHOD-TOOL-006
---

# Allocate one runtime folder per script

Give each CAPRMADIO script or executable tool that persists runtime files one
dedicated directory beneath the caprmadio runtime root. Keep its runtime files
inside that directory; concurrent runs may use bounded run-specific descendants.

Do not scatter runtime files, write into another script's directory, or depend
on an unowned shared directory. A shared runtime service owns its own directory
and clients use its service contract rather than its files.
