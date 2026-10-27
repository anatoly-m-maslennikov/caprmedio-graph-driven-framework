---
atom_id: CA-P-1869@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 06:04:10 +0400
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on:
  - Project
  - Plan
  - AI Agent
  - Operator
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
  - Tool
  - Journal
  - Version
relations:
  is_decomposition_of:
  - CA-P-1849
  blocks:
  - CA-P-1870
tier: 3
---
# Summary

Define the public-release Workflow **and** Tool contract

## Objective

Specify Public release, its one content prompt, version bump and GitHub publication.

## Details

- Follow CA-P-1848's current direct happy path. Earlier snapshot, admission, selector, recovery and complete-corpus gate requirements are superseded.
- Commit everything before every release step and at the end, respecting Git ignore rules and secret exclusions.
- Stop and report a failed step for manual handling; no automatic rollback or retry.
- Preserve configuration, Project records and other Projects. Ignore .DS_Store.

- Completion evidence: The Project-local Public operation and existing run_public_release entrypoint specify one content draft, Public version bump, Git-all checkpoints, amm/dev push and main PR publication without merge. Contract tests passed; this specification task does not claim live Public publication.
- Live Local receipt: .caprmedio_runtime/simple_local_release/reports/epic1848-direct-local-20261012-001.md. Consolidated verification: .caprmedio_tmp/epic1848/direct-local-completion.md.

## Definition of Done

The Objective is implemented and verified with actual evidence appropriate to this task. Record remaining manual issues. Mock tests do not prove live release, installation, MCP or PR completion.
