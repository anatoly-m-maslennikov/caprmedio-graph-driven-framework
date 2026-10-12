---
atom_id: CA-P-1867
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Done
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-12 00:24:01 +0000"
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on: [Project, Plan, AI Agent, Operator, Framework Package, Methodology Source, Applicable Methodology, Project Structure, Requirement, Method, Evaluation, Delivery, Workflow, Step, Action, Tool, Journal, Version]
relations:
  is_decomposition_of: [CA-P-1849]
  blocks: [CA-P-1870]
---
# Summary

Update local installation **and** release contracts

## Objective

Specify the direct Local copy, compile, installation and Git checkpoint steps.

## Details

- Follow CA-P-1848's current direct happy path. Earlier snapshot, admission, selector, recovery and complete-corpus gate requirements are superseded.
- Commit everything before every release step and at the end, respecting Git ignore rules and secret exclusions.
- Stop and report a failed step for manual handling; no automatic rollback or retry.
- Preserve configuration, Project records and other Projects. Ignore .DS_Store.

- Completion evidence: The direct Local operation contracts and existing run_local_release entrypoint specify the tested copy, compile, install and Git-all checkpoint sequence. The live Local Run completed.
- Live Local receipt: .caprmedio_runtime/simple_local_release/reports/epic1848-direct-local-20261012-001.md. Consolidated verification: .caprmedio_tmp/epic1848/direct-local-completion.md.

## Definition of Done

The Objective is implemented and verified with actual evidence appropriate to this task. Record remaining manual issues. Mock tests do not prove live release, installation, MCP or PR completion.
