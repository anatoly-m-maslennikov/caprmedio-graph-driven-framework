---
atom_id: CA-P-1858@8
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-24 06:04:10 +0400
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on:
  - Project
  - Plan
  - AI Agent
  - Operator
  - Framework Instance Settings
  - Evaluation
  - Framework Package
  - Atom
  - Tool
  - Workflow
  - Workflow Run
  - Journal
  - Carrier
relations:
  is_decomposition_of:
  - CA-P-1848
  blocks:
  - CA-P-1859
tier: 3
---
# Summary

Test installation across fresh Projects

## Objective

Test installation and configuration preservation in disposable Project fixtures.

## Details

- Follow CA-P-1848's current direct happy path. Earlier snapshot, admission, selector, recovery and complete-corpus gate requirements are superseded.
- Commit everything before every release step and at the end, respecting Git ignore rules and secret exclusions.
- Stop and report a failed step for manual handling; no automatic rollback or retry.
- Preserve configuration, Project records and other Projects. Ignore .DS_Store.

- Completion evidence: Six Local fixture tests passed, including active-only copy, configuration preservation, failure stop, actual temporary Git, and Local version numbering.
- Live Local receipt: .caprmedio_runtime/simple_local_release/reports/epic1848-direct-local-20261012-001.md. Consolidated verification: .caprmedio_tmp/epic1848/direct-local-completion.md.

## Definition of Done

The Objective is implemented and verified with actual evidence appropriate to this task. Record remaining manual issues. Mock tests do not prove live release, installation, MCP or PR completion.
