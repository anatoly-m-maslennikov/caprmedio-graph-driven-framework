---
atom_id: CA-P-1861
content_role: Plan
type: Plan
label: Task
work_sequence_number: 13
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Done
author: Anatoly Maslennikov
version: 6
updated_at: "2026-10-12 00:24:01 +0000"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Framework Package, Applicable Methodology, Tool, Workflow, Action, Workflow Run, Journal, Carrier, Evaluation]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1862]
---
# Summary

Verify the local installation **and** finalize its cleanup

## Objective

Verify Methodology, runtime, ca Skill and live MCP; remove only safely identified superseded Project-owned images.

## Details

- Follow CA-P-1848's current direct happy path. Earlier snapshot, admission, selector, recovery and complete-corpus gate requirements are superseded.
- Commit everything before every release step and at the end, respecting Git ignore rules and secret exclusions.
- Stop and report a failed step for manual handling; no automatic rollback or retry.
- Preserve configuration, Project records and other Projects. Ignore .DS_Store.

- Completion evidence: Live file comparisons passed for Methodology, runtime package and ca. Docker MCP initialized successfully; the launcher removed the exact superseded Project-owned image, without global pruning.
- Live Local receipt: .caprmedio_runtime/simple_local_release/reports/epic1848-direct-local-20261012-001.md. Consolidated verification: .caprmedio_tmp/epic1848/direct-local-completion.md.

## Definition of Done

The Objective is implemented and verified with actual evidence appropriate to this task. Record remaining manual issues. Mock tests do not prove live release, installation, MCP or PR completion.
