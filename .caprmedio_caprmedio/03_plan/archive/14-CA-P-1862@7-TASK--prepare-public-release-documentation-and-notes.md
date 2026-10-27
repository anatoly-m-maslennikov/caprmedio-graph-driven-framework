---
atom_id: CA-P-1862@7
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 06:04:10 +0400
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on:
  - Project
  - Plan
  - AI Agent
  - Operator
  - Framework Instance Settings
  - Version
  - Framework Package
  - Workflow Run
  - Workflow
  - Action
  - Journal
  - Evaluation
relations:
  is_decomposition_of:
  - CA-P-1848
  blocks:
  - CA-P-1863
tier: 3
---
# Summary

Prepare public release documentation **and** notes

## Objective

Prepare README updates, the complete PR description and Version History bullets through one content prompt.

## Details

- Follow CA-P-1848's current direct happy path. Earlier snapshot, admission, selector, recovery and complete-corpus gate requirements are superseded.
- Commit everything before every release step and at the end, respecting Git ignore rules and secret exclusions.
- Stop and report a failed step for manual handling; no automatic rollback or retry.
- Preserve configuration, Project records and other Projects. Ignore .DS_Store.

- Completion evidence: The single Public content prompt produced the README updates, complete release PR description and concise Version History bullets for version 0.4.3. Actual Public Run epic1848-direct-public-20261012-001 completed and created PR 27; Version History includes that verified PR link.
- Public evidence: Run epic1848-direct-public-20261012-001 completed for 0.4.3; PR https://github.com/anatoly-m-maslennikov/caprmedio-graph-driven-framework/pull/27. Journal started Event 803fbb4b-8b3a-4a2a-9839-a65251d46e02; completed Event 8bdb213a-13be-4f26-9c87-0a44dfc30b34.

- Public completion receipt: .caprmedio_tmp/epic1848/direct-public-completion.md.

## Definition of Done

The Objective is implemented and verified with actual evidence appropriate to this task. Record remaining manual issues. Mock tests do not prove live release, installation, MCP or PR completion.
