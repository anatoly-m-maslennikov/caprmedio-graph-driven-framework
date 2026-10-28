---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/caprmedio/Extension//FPF
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime
version: 12
updated_at: 2026-10-27 19:59:56 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Requirement
current_scope_unit: CORE_EXTENSIONS
status: Active
author: Anatoly Maslennikov
atom_id: CA-R-1482
type: Goal
tier: 1
---
# Keep recovery controls independent from the active Tool path

the FPF Extension **must** provide one bounded manual recovery entrypoint for `status`, `stop`, `start`, **and** `reload` that remains operable **without** invoking an active Hook, Skill, MCP request, decision manager, **or** domain worker, **and** one independent automatic supervisor that **may** stop dispatch, restart a failed service within a declared budget, **or** open its circuit but **must not** perform **or** authorize domain effects; both control paths **must** preserve durable accepted work **and** report the exact selected release **and** process state.
