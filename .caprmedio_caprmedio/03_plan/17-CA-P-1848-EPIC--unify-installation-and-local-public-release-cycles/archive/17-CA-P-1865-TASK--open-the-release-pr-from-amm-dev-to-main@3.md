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
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-10 18:08:27 +0400"
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
    - "Workflow"
    - "Action"
    - "Tool"
    - "Journal"
relations:
  is_decomposition_of:
    - CA-P-1848
  blocks:
    - CA-P-1871
---
# Summary

Open the release PR **from** amm/dev **to** main

## Objective

the AI Agent creates **or** updates the release PR **from** `amm/dev` to `main` **with** the reviewed full description.

## Details

- scope: the installation/release contribution of the CAPRMEDIO Framework Instance delivered by the caprmedio Project.
- input: the verified pushed commit, passing public full-suite evidence, the reusable public-release Workflow/Step/Action/Tool binding **and** the full PR description prepared for these exact changes.
- execute the reusable public-release Workflow's bound PR discovery/update Action **through** the discovered native binding: verify personal repository identity, base `main`, head `amm/dev` **and** whether a matching PR already exists; update that PR rather than create a duplicate.
- use the complete description **with** full lists under “What's new” **and** “What's fixed”, install/layout migration, compatibility/rollback, tests **and** remaining limits. the Version History entry retains **only** its concise bullet summary **and** the actual PR link, finalized by Task 19.
- confirm the PR URL, head commit, base branch **and** rendered description against the actual diff. record Workflow, Step, Action **and** Tool-call parentage/evidence **in** the shared Journal; attach the created/existing PR to this task/chat **through** the supported artifact interface.
- opening the PR is the public cycle's requested handoff; do **not** merge it, alter CI/branch protection **or** claim that `main` has shipped **without** separate authority/evidence.
- effort: own work for **=1** AI Agent **must** fit **<=15** minutes. **if** this Plan needs larger own work, decompose it **before** execution **and** preserve its Objective **and** acceptance.
- control: use applicable Operator input **and** inherited Framework Instance Settings for permission, confidence **and** retry gates. creation is planned work **only**, **not** permission to execute the local/public cycle immediately.

### Definition of Done

the Plan is **not** Done **if** the PR is missing, targets the wrong branches/commit, has an inadequate **or** stale description, duplicates an existing PR, **or** its URL/attachment is **not** confirmed.
