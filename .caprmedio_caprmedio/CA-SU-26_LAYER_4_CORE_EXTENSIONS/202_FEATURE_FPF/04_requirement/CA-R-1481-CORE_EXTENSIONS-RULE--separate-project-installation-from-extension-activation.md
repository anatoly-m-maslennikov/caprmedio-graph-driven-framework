---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - Subject/caprmedio/Extension//FPF
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
version: 16
updated_at: 2026-10-27 19:59:56 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Requirement
current_scope_unit: CORE_EXTENSIONS
status: Active
author: Anatoly Maslennikov
atom_id: CA-R-1481
type: Rule
tier: 1
---
# Separate Project installation from Extension activation

Installing an immutable FPF Extension Candidate **must** register its exact provenance **and** make its project-local `fpf` Skill available **without** activating its methodology authority; activation **must** require a separate current Project Configuration selection, **must not** mutate upstream **or** user-global FPF sources, **and** **must not** be claimed **until** a fresh Codex session resolves the selected project-local package **and** invokes it directly as `$fpf` **without** a `ca` wrapper.
