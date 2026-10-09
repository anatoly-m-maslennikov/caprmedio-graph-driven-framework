---
atom_id: CA-P-1859
content_role: Plan
type: Plan
label: Task
work_sequence_number: 11
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
    - "Evaluation"
    - "Framework Package"
    - "Methodology Source"
    - "Version"
    - "Workflow Run"
    - "Journal"
relations:
  is_decomposition_of:
    - CA-P-1848
  blocks:
    - CA-P-1860
---
# Summary

Pass the full test suite before local release

## Objective

the AI Agent obtains a complete passing full-suite gate for the exact inputs selected for the local release cycle.

## Details

- scope: the installation/release contribution of the CAPRMEDIO Framework Instance delivered by the caprmedio Project.
- input: the final source Methodology, Engine, package/installer changes, dependency lock, defaults, selected Project configuration **and** complete current test inventory.
- freeze input identities **and** the selected Version **before** testing. run the full current suite, including golden/unit/integration **and** required host/Docker/MCP e2e gates, through uv-managed environments.
- record every expected suite/module, executed cases, failures, skipped/incomplete coverage, exit status **and** source/package identities. focused tests, mocked evidence, queued work **or** an old green receipt are **not** this gate.
- failed, unavailable **or** incomplete required tests block local release. handle retry/escalation under the applicable settings; do **not** bypass the gate because a dependency, cleanup **or** host permission is inconvenient.
- source/configuration changes that affect the validated closure invalidate this gate. this Task records acceptance **only**; it does **not** perform live package/runtime/source promotion.
- effort: own work for **=1** AI Agent **must** fit **<=15** minutes. **if** this Plan needs larger own work, decompose it **before** execution **and** preserve its Objective **and** acceptance.
- control: use applicable Operator input **and** inherited Framework Instance Settings for permission, confidence **and** retry gates. creation is planned work **only**, **not** permission to execute the local/public cycle immediately.

### Definition of Done

the Plan is **not** Done **if** any required suite has failed, skipped **or** incomplete coverage, the frozen inputs changed, **or** an exit/status/report cannot prove the complete local gate passed.
