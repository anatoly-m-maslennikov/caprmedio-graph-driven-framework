---
atom_id: CA-P-1865
content_role: Plan
type: Plan
label: Task
work_sequence_number: 17
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-10 18:08:27 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Version, Framework Package, Evaluation, Workflow Run, Workflow, Action, Tool, Journal]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1871]
---
# Summary

Open the release PR **from** amm/dev **to** main

## Objective

the AI Agent creates **or** updates the release PR **from** `amm/dev` to `main` **with** the full description as an internal Public release stage.

## Details

1. Verify the personal repository, base `main`, head `amm/dev` and whether a matching PR exists. Reuse/update the matching PR rather than create a duplicate.
2. Use the one-prompt full description with complete “What's new” and “What's fixed” lists; retain only concise history bullets and the actual URL in Version History.
3. Confirm the PR URL, head commit, base branch and rendered description against the actual diff, then record exact command evidence. If the URL is new, the command's metadata-only follow-up appends it and pushes; no second full suite is needed solely for that link.
4. Do not merge, alter CI/branch protection or claim that `main` shipped. This stage is not a separate handover command.

### Definition of Done

the Plan is **not** Done **if** the PR is missing or targets wrong branches/commit, has an inadequate or stale description, duplicates a matching PR, or its actual URL is unconfirmed.
