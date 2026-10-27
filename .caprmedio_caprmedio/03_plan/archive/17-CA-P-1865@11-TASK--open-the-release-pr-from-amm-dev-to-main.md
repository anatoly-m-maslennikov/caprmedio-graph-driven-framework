---
atom_id: CA-P-1865@11
content_role: Plan
type: Plan
label: Task
work_sequence_number: 17
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-24 09:20:34 +0400
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Version
  - Framework Package
  - Subject/Engineering/Evaluation
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Engineering/Workflow
  - Subject/Engineering/Action
  - Subject/Engineering/Tool
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  is_decomposition_of:
  - CA-P-1848
  blocks:
  - CA-P-1871
tier: 3
---
# Summary

Open the release PR **from** amm/dev **to** main

## Objective

Create or update the Public PR from amm/dev to main with the complete description; do not merge.

## Details

- Follow CA-P-1848's current direct happy path. Earlier snapshot, admission, selector, recovery and complete-corpus gate requirements are superseded.
- Commit everything before every release step and at the end, respecting Git ignore rules and secret exclusions.
- Stop and report a failed step for manual handling; no automatic rollback or retry.
- Preserve configuration, Project records and other Projects. Ignore .DS_Store.

- Completion evidence: Actual Public Run epic1848-direct-public-20261012-001 created PR 27 from amm/dev to main with the complete release description. The workflow issued no merge command. The external github-actions bot subsequently merged PR 27 at 2026-10-12 00:39:03 UTC (merge commit d3dcbf3f2d3ab2e29f4ae4300a78f45c628cbd7e), before the final history push; this external outcome is recorded transparently without rollback.
- Public evidence: Run epic1848-direct-public-20261012-001 completed for 0.4.3; PR https://github.com/anatoly-m-maslennikov/caprmedio-graph-driven-framework/pull/27. Journal started Event 803fbb4b-8b3a-4a2a-9839-a65251d46e02; completed Event 8bdb213a-13be-4f26-9c87-0a44dfc30b34.

- Public completion receipt: .caprmedio_tmp/epic1848/direct-public-completion.md.

- No-merge correction verified: new Public PRs are created Draft and an existing open PR is converted to Draft before editing. Five focused Public tests passed; PR 27's earlier external bot merge remains recorded rather than rolled back.

## Definition of Done

The Objective is implemented and verified with actual evidence appropriate to this task. Record remaining manual issues. Mock tests do not prove live release, installation, MCP or PR completion.
