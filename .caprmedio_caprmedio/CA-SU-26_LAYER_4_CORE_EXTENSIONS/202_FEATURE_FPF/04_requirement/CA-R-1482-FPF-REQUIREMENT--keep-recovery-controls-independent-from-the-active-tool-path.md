---
atom_id: CA-R-1482
ref_id: CA-R-1482
container:
  scope_unit: CA-SU-26
role: Requirement
form: Goal
topics:
  main_subject: Subject/caprmedio/Extension//FPF
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime
tier: 1
status: Active
version: 12
updated_at: 2026-10-27 19:59:56 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: CORE_EXTENSIONS
author: Anatoly Maslennikov
---
# Keep recovery controls independent from the active Tool path

the FPF Extension **must** provide one bounded manual recovery entrypoint for `status`, `stop`, `start`, **and** `reload` that remains operable **without** invoking an active Hook, Skill, MCP request, decision manager, **or** domain worker, **and** one independent automatic supervisor that **may** stop dispatch, restart a failed service within a declared budget, **or** open its circuit but **must not** perform **or** authorize domain effects; both control paths **must** preserve durable accepted work **and** report the exact selected release **and** process state.
