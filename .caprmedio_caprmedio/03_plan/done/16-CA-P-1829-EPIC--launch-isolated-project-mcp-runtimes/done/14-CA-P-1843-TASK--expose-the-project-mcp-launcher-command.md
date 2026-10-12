---
atom_id: CA-P-1843
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Done
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 03:46:50 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Project Settings"
    - "Project Structure"
    - "Framework Instance Settings"
    - "Tool"
    - "Action"
    - "Workflow Run"
    - "Carrier"
    - "Evaluation"
    - "AI Agent"
    - "Operator"
relations:
  is_decomposition_of:
    - CA-P-1829
  blocks:
    - CA-P-1844
    - CA-P-1845
    - CA-P-1846
---
# Summary

Expose the Project MCP launcher command

## Objective

the AI Agent connects the admitted launcher components **to** one usable Python command.

## Details

- input: the selected-Project readers, image/build adapters, startup/reuse path, readiness/results, **and** reviewed CLI Delivery contract.
- output: a discoverable command extending the existing launcher that accepts the Project path, invokes the admitted startup path, **and** returns the MCP URL **and** supported structured output. include the command **in** the intended distributive/runtime package.
- verification: run the mocked command end **to** end for ready, reused, invalid, build-failed, **and** readiness-failed outcomes; preserve existing explicit runtime commands.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

- completion evidence: the existing packaged Engine entry point now exposes `project-mcp`, separate `--source-root`, bounded deadlines, `--no-build` **and** JSON/URL output. 3 command tests passed, including non-success JSON with a nonzero exit; existing worker/stdin commands remain unchanged.

- reopened **after** independent final review: expose the admitted optional explicit port **and** verify propagation **and** refusal at the command boundary. prior command evidence does **not** cover this missing input.

the Plan is **not** Done **if** ((the command cannot resolve its accepted Project input) **or** (its packaged entry point is absent) **or** (the command-level golden tests fail)).

- final completion evidence: **`=5`** command tests pass, including `--port` forwarding **and** bounds refusal. `launcher-proof-0omrljbe/result.json` records a real default `runtime.py ... project-mcp` invocation without `--image` **or** `--no-build`, the resulting immutable image, **and** successful repeated CLI invocations in both Project layouts. independent documentation/package review accepts the Project-root selection, credential, explicit-port, **and** endpoint-only contract.
