---
atom_id: CA-P-1871
content_role: Plan
type: Plan
label: Task
work_sequence_number: 19
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-10 18:08:27 +0400"
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on: [Project, Plan, Operator, Version, Workflow, Step, Action, Tool, Journal, Evaluation]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1866]
---
# Summary

Finalize Version History **with** the verified release PR link

## Objective

the AI Agent finalizes the release Version History entry as **only** a concise summary **and** a link to the actual verified PR.

## Details

1. Reuse a matching known PR URL in the Public release command; do not guess a number, use a placeholder or substitute a compare URL.
2. If a new PR provides its URL after its creation, append that actual URL to the concise Version History entry in the same command's mechanical metadata-only follow-up commit/push. Do not run a second full suite solely for this link.
3. The PR retains the complete “What's new” and “What's fixed” lists and evidence; Version History retains only short bullets and the actual URL. This does not merge `main` or change the sealed Version.

### Definition of Done

the Plan is **not** Done **if** the entry lacks the verified actual PR link, duplicates full change lists, the PR lacks complete new/fixed lists, or a material release change bypasses its complete public gate.
