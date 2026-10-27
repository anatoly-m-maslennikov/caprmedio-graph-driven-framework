---
atom_id: CA-P-1852@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-12 00:24:01 +0000
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on:
  - Project
  - Plan
  - AI Agent
  - Operator
  - Framework Instance Settings
  - Methodology Source
  - Atom
  - Status
  - Content Role
  - Framework Package
  - Carrier
  - Projection
relations:
  is_decomposition_of:
  - CA-P-1848
  blocks:
  - CA-P-1853
  - CA-P-1854
---
# Summary

Export only active Methodology

## Objective

Copy active Methodology-source Atoms and compiler support files, excluding drafts and archives.

## Details

- Follow CA-P-1848's current direct happy path. Earlier snapshot, admission, selector, recovery and complete-corpus gate requirements are superseded.
- Commit everything before every release step and at the end, respecting Git ignore rules and secret exclusions.
- Stop and report a failed step for manual handling; no automatic rollback or retry.
- Preserve configuration, Project records and other Projects. Ignore .DS_Store.

- Completion evidence: Live comparison found no differences for 909 Core files, 1 Extension file and 111 Project Configuration files; only active Markdown Atoms and supporting files were delivered.
- Live Local receipt: .caprmedio_runtime/simple_local_release/reports/epic1848-direct-local-20261012-001.md. Consolidated verification: .caprmedio_tmp/epic1848/direct-local-completion.md.

## Definition of Done

The Objective is implemented and verified with actual evidence appropriate to this task. Record remaining manual issues. Mock tests do not prove live release, installation, MCP or PR completion.
