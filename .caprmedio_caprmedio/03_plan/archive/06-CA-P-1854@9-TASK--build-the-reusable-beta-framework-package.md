---
atom_id: CA-P-1854@9
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-24 09:20:34 +0400
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Framework Package
  - Methodology Source
  - Applicable Methodology
  - Subject/Engineering/Tool
  - Subject/Engineering/Carrier
  - Version
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  is_decomposition_of:
  - CA-P-1848
  blocks:
  - CA-P-1855
tier: 3
---
# Summary

Build the reusable beta Framework package

## Objective

Build the reusable installation folder from Engine code, Methodology, locked dependencies and the ca Skill.

## Details

- Follow CA-P-1848's current direct happy path. Earlier snapshot, admission, selector, recovery and complete-corpus gate requirements are superseded.
- Commit everything before every release step and at the end, respecting Git ignore rules and secret exclusions.
- Stop and report a failed step for manual handling; no automatic rollback or retry.
- Preserve configuration, Project records and other Projects. Ignore .DS_Store.

- Completion evidence: The reusable package contains Engine code, delivered Methodology, pyproject.toml, uv.lock, version.toml and the ca Skill; 3,065 delivered files match the installed runtime package.
- Live Local receipt: .caprmedio_runtime/simple_local_release/reports/epic1848-direct-local-20261012-001.md. Consolidated verification: .caprmedio_tmp/epic1848/direct-local-completion.md.

## Definition of Done

The Objective is implemented and verified with actual evidence appropriate to this task. Record remaining manual issues. Mock tests do not prove live release, installation, MCP or PR completion.
