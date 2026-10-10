---
atom_id: CA-P-1856
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-10 18:58:38 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Plan"
    - "AI Agent"
    - "Operator"
    - "Framework Instance Settings"
    - "Framework Package"
    - "Tool"
    - "Action"
    - "Workflow"
    - "Workflow Run"
    - "Carrier"
relations:
  is_decomposition_of:
    - CA-P-1848
  blocks:
    - CA-P-1857
    - CA-P-1858
---
# Summary

Run Tools **and** Docker MCP **from** the installed package

## Objective

the AI Agent connects Tools, ca **and** Docker MCP to the selected installed package rather than an implicit source checkout.

## Details

- scope: the installation/release contribution of the CAPRMEDIO Framework Instance delivered by the caprmedio Project.
- input: the package/runtime installation contract **and** current Tool wrappers, startup scripts, service definitions, MCP gateway, Docker build **and** release verifiers.
- output: installed Tool/Workflow discovery, executors, ca Skill, service startup **and** Docker MCP consume the same admitted per-Project installation-lock package identity, selected extensions/configuration/catalog revisions **and** Project context.
- implement the complete reusable public-release Workflow execution binding defined by Task 01, including documentation preparation, the public gate, commit/push **and** PR discovery/update Actions. package **and** source-admit its executors **and** Journal recording; prove the bindings **with** mocked remote-effect tests **before** their real invocation **in** Tasks 14–17. reuse admitted native bindings **where** valid; exposing a definition **only** is **not** implementation.
- replace stale `301_TOOLS` references **with** admitted `201_TOOLS` paths **by** producing/selecting a corrected package **and** updating its wrappers. preserve immutable retained releases rather than editing an older package. update `start_mcp.py`, Docker image assembly **and** their release/currentness checks so default startup uses installed package bytes.
- retain password-free loopback HTTP MCP, Project isolation, available-port allocation, healthy reuse, bounded calls, explicit reload behavior **and** read-only discovery. bind the running service generation, image **and** release proof to the same installation lock; return the Project MCP URL **and** binding evidence; do **not** start unrelated Workflows automatically.
- test launchers **from** a relocated installation **without** source, stale/missing package **or** lock refusal, immutable image reuse/build, two-Project endpoint isolation, discovery **and** invocation of an installed read-only Tool. preserve running resources belonging to other Projects.
- effort: own work for **=1** AI Agent **must** fit **<=15** minutes. **if** this Plan needs larger own work, decompose it **before** execution **and** preserve its Objective **and** acceptance.
- control: use applicable Operator input **and** inherited Framework Instance Settings for permission, confidence **and** retry gates. creation is planned work **only**, **not** permission to execute the local/public cycle immediately.

### Definition of Done

the Plan is **not** Done **if** any normal installed entrypoint runs unselected checkout code, a stale `301_TOOLS` reference remains, a package/image/context mismatch is accepted, the complete public-release execution binding lacks implementation/test evidence, **or** live MCP capability discovery cannot succeed.
