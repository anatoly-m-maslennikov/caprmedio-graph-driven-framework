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

Bound independent automatic recovery and prohibit domain effects

## Claim scope

FPF

## Claim

The FPF Extension must provide one independent automatic supervisor that may stop dispatch, restart a failed service within a declared budget, or open its circuit, but must not perform or authorize domain effects. This control path must preserve durable accepted work and report the exact selected release and process state.
