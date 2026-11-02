---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/caprmedio/Extension//FPF
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime
version: 1
updated_at: 2026-10-29 20:32:25 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Requirement
current_scope_unit: CORE_EXTENSIONS
status: Draft
author: Anatoly Maslennikov
atom_id: CA-R-draft
type: Requirement
tier: 1
claim_target_scope_unit: FPF
---
## Summary

Provide independent manual recovery with durable work and exact state reporting

## Claim scope

FPF

## Claim

The FPF Extension must provide one bounded manual recovery entrypoint for `status`, `stop`, `start`, and `reload` that remains operable without invoking an active Hook, Skill, MCP request, decision manager, or domain worker. This control path must preserve durable accepted work and report the exact selected release and process state.
