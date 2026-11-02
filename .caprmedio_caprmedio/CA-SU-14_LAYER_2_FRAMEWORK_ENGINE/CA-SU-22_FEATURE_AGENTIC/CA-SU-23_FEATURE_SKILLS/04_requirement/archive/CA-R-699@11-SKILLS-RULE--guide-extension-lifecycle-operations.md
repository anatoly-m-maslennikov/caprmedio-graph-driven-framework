---
subject_scopes:
- extension-lifecycle
version: 11
updated_at: 2026-10-26 00:46:35 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-1722
  - CAPRMEDIO-REQU-702--define-framework-engine-layer-scope
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: SKILLS
status: Archived
atom_id: CA-R-699@11
tier: 1
type: Rule
subjects:
  governs: Subject/Graph Node/UX/Extension Lifecycle Skill Interface
---
# Guide Extension lifecycle operations

the framework **must** provide one Skill that resolves an operator's Extension install, uninstall, update, **or** downgrade intent, presents the exact source **and** target version, **and** invokes the governed Tool **only** **after** explicit approval.
