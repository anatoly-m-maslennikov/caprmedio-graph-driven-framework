---
atom_id: CA-P-1853@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 06:04:10 +0400
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on:
  - Project
  - Plan
  - AI Agent
  - Operator
  - Framework Instance Settings
  - Applicable Methodology
  - Methodology Source
  - Projection
  - Atom
  - Project Settings
  - Workflow
  - Evaluation
relations:
  is_decomposition_of:
  - CA-P-1848
  blocks:
  - CA-P-1855
tier: 3
---
# Summary

Compile **and** install Project Methodology

## Objective

Compile Applicable Methodology in the product and copy the product as-is to the installed framework, preserving configuration.

## Details

- Follow CA-P-1848's current direct happy path. Earlier snapshot, admission, selector, recovery and complete-corpus gate requirements are superseded.
- Commit everything before every release step and at the end, respecting Git ignore rules and secret exclusions.
- Stop and report a failed step for manual handling; no automatic rollback or retry.
- Preserve configuration, Project records and other Projects. Ignore .DS_Store.

- Completion evidence: The compiler completed. All 2,038 delivered Methodology files match the installed copy, excluding preserved configuration and ignored .DS_Store files.
- Live Local receipt: .caprmedio_runtime/simple_local_release/reports/epic1848-direct-local-20261012-001.md. Consolidated verification: .caprmedio_tmp/epic1848/direct-local-completion.md.

## Definition of Done

The Objective is implemented and verified with actual evidence appropriate to this task. Record remaining manual issues. Mock tests do not prove live release, installation, MCP or PR completion.
