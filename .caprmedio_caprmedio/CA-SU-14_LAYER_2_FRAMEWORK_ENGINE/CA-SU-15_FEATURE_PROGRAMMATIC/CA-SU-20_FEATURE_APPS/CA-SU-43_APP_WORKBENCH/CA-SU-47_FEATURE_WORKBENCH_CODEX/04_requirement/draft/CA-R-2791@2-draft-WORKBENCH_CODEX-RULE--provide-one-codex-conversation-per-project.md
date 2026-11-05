---
atom_id: CA-R-2791
ref_id: CA-R-2791@2-draft
current_scope_unit: WORKBENCH_CODEX
claim_target_scope_unit: WORKBENCH_CODEX
status: Draft
version: 2
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project
carrier_destination:
  file:
    name: CA-R-2791@2-draft-WORKBENCH_CODEX-RULE--provide-one-codex-conversation-per-project.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-47_FEATURE_WORKBENCH_CODEX/04_requirement/draft
updated_at: 2026-11-05 16:45:35 +0400
---

## Summary

Provide one Codex conversation per Project

## Claim

### Prose Claim

WORKBENCH_CODEX **must** provide the selected Project's one Workspace with exactly one native persisted Codex conversation. CAPRMEDIO requests include the explicit `project_root`. A returning browser resumes that Workspace's conversation.

The conversation operates all Tools exposed by enabled MCP servers in the local Codex configuration. For CAPRMEDIO, it discovers Tools from the generated root `discover_tools` catalog and the current native MCP frontier. For other enabled MCP servers, it uses native discovery. It does not use a Workbench-only or hand-coded Tool allowlist or a unified Tool registry.

The Workbench streams Codex output and presents requested Tool interactions and approvals. It reuses the existing MCP Tools for queries, Views, saved items and service actions.

The conversation inherits the Workbench layout. Its placement, density, resizing and command-palette controls are not defined here.

This first integration does not provide a chat list, multiple conversations, a generic repository or code-editing agent, a separate Tool registry, a queue, scheduler, retry or rollback policy.
