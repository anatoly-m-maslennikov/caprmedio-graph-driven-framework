---
atom_id: CA-M-143
ref_id: CA-M-143
container:
  scope_unit: CA-SU-16
role: Method
form: Eng Policy
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage/Directory Layout
tier: 2
relations:
  method_for:
  - CA-R-1065
  derived_from:
  - CA-A-057
status: Active
version: 26
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Allocate one runtime folder per script

give **every** CAPRMEDIO script **or** executable tool that persists runtime files one dedicated directory beneath the caprmedio runtime root. keep its runtime files inside that directory; concurrent runs **may** use bounded run-specific descendants.

do **not** scatter runtime files, write into another script's directory, **or** depend on an unowned shared directory. a shared runtime service owns its own directory **and** clients use its service contract rather than its files.
