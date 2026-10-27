---
atom_id: CA-P-1868@7
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 07:45:09 +0400
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Framework Package
  - Methodology Source
  - Applicable Methodology
  - Project Structure
  - Requirement
  - Method
  - Evaluation
  - Delivery
  - Workflow
  - Step
  - Action
  - Subject/Engineering/Tool
  - Subject/Domain/Node/Continuant/History/Journal
  - Version
relations:
  is_decomposition_of:
  - CA-P-1849
  blocks:
  - CA-P-1870
tier: 3
---
# Summary

Specify the portable package **and** installation Tools

## Objective

Specify the reusable package and isolated Project runtime, preserving configuration.

## Details

- Follow CA-P-1848's current direct happy path. Earlier snapshot, admission, selector, recovery and complete-corpus gate requirements are superseded.
- Commit everything before every release step and at the end, respecting Git ignore rules and secret exclusions.
- Stop and report a failed step for manual handling; no automatic rollback or retry.
- Preserve configuration, Project records and other Projects. Ignore .DS_Store.

- Completion evidence: Package and runtime boundaries are implemented and verified by disposable fixtures and the actual 3,065-file installation comparison.
- Live Local receipt: .caprmedio_runtime/simple_local_release/reports/epic1848-direct-local-20261012-001.md. Consolidated verification: .caprmedio_tmp/epic1848/direct-local-completion.md.

## Definition of Done

The Objective is implemented and verified with actual evidence appropriate to this task. Record remaining manual issues. Mock tests do not prove live release, installation, MCP or PR completion.
