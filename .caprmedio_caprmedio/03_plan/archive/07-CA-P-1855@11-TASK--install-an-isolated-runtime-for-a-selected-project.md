---
atom_id: CA-P-1855@11
content_role: Plan
type: Plan
label: Task
work_sequence_number: 7
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-24 13:05:09 +0400
subjects:
  governs: Subject/Engineering/Release Version/Runtime Package Carrier
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Subject/Engineering/Release Version/Runtime Package Carrier
  - Subject/Domain/Node/Continuant/Project.Settings
  - Subject/Engineering/Tool
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Engineering/Carrier
relations:
  is_decomposition_of:
  - CA-P-1848
  blocks:
  - CA-P-1856
tier: 3
---
# Summary

Install an isolated runtime for a selected Project

## Objective

Install the package into the selected Project runtime without replacing configuration or records.

## Details

- Follow CA-P-1848's current direct happy path. Earlier snapshot, admission, selector, recovery and complete-corpus gate requirements are superseded.
- Commit everything before every release step and at the end, respecting Git ignore rules and secret exclusions.
- Stop and report a failed step for manual handling; no automatic rollback or retry.
- Preserve configuration, Project records and other Projects. Ignore .DS_Store.

- Completion evidence: The selected Project's installed runtime package matches the reusable package. Preservation tests passed; existing runtime configuration and records outside the owned replacement target remained in place.
- Live Local receipt: .caprmedio_runtime/simple_local_release/reports/epic1848-direct-local-20261012-001.md. Consolidated verification: .caprmedio_tmp/epic1848/direct-local-completion.md.

## Definition of Done

The Objective is implemented and verified with actual evidence appropriate to this task. Record remaining manual issues. Mock tests do not prove live release, installation, MCP or PR completion.
