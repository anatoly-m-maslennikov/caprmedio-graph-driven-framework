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
version: 1
updated_at: "2026-10-09 15:41:25 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Plan"
    - "AI Agent"
    - "Operator"
    - "Framework Instance Settings"
    - "Version"
    - "Framework Package"
    - "Evaluation"
    - "Workflow Run"
relations:
  is_decomposition_of:
    - CA-P-1848
  blocks:
    - CA-P-1866
---
# Summary

Open the release PR **from** amm/dev **to** main

## Objective

the AI Agent creates **or** updates the release PR from `amm/dev` to `main` **with** the reviewed full description.

## Details

- scope: the installation/release contribution of the CAPRMEDIO Framework Instance delivered by the caprmedio Project.
- input: the verified pushed commit, passing public full-suite evidence **and** the full PR description prepared for these exact changes.
- verify personal repository identity, base `main`, head `amm/dev` **and** whether a matching PR already exists; update that PR rather than create a duplicate.
- use the complete description **with** meaningful change groups, install/layout migration, compatibility/rollback, tests **and** remaining limits. the Version History entry stays its concise bullet summary.
- confirm the PR URL, head commit, base branch **and** rendered description against the actual diff. attach the created/existing PR to this task/chat **through** the supported artifact interface.
- opening the PR is the public cycle's requested handoff; do **not** merge it, alter CI/branch protection **or** claim that `main` has shipped without separate authority/evidence.
- effort: own work for **=1** AI Agent **must** fit **<=15** minutes. **if** this Plan needs larger own work, decompose it **before** execution **and** preserve its Objective **and** acceptance.
- control: use applicable Operator input **and** inherited Framework Instance Settings for permission, confidence **and** retry gates. creation is planned work **only**, **not** permission to execute the local/public cycle immediately.

### Definition of Done

the Plan is **not** Done **if** the PR is missing, targets the wrong branches/commit, has an inadequate **or** stale description, duplicates an existing PR, **or** its URL/attachment is not confirmed.
