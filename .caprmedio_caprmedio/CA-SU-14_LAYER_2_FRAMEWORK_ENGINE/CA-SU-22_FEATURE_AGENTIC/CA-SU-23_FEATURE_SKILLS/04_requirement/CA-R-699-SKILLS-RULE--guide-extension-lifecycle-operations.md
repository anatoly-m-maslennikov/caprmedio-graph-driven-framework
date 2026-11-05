---
atom_id: CA-R-699
ref_id: CA-R-699
container:
  scope_unit: CA-SU-23
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Interaction/Decision
tier: 1
relations:
  child_of:
  - CA-R-1722
  - CAPRMEDIO-REQU-702--define-framework-engine-layer-scope
status: Active
version: 12
updated_at: 2026-10-27 20:00:10 +0400
subject_scopes:
- extension-lifecycle
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: SKILLS
---
# Guide Extension lifecycle operations

the framework **must** provide one Skill that resolves an operator's Extension install, uninstall, update, **or** downgrade intent, presents the exact source **and** target version, **and** invokes the governed Tool **only** **after** explicit approval.
