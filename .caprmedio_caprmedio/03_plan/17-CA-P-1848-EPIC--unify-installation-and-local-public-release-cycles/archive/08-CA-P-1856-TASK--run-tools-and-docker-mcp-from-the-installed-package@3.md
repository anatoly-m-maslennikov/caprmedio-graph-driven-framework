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
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-10 18:58:38 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Framework Package, Tool, Action, Workflow, Workflow Run, Carrier]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1857, CA-P-1858]
---
# Summary

Run Tools **and** Docker MCP **from** the installed package

## Objective

the AI Agent connects reusable Tools, ca **and** Docker MCP to the selected installed package rather than an implicit source checkout.

## Details

1. Keep reusable compiler, installer, shared package/gate models/codecs, detached readers and generic O200 install/bootstrap/restore capability currently in `RELEASE_VERSION` in `TOOLS`, so a fresh arbitrary or non-Git target does not need the project-development checkout.
2. Relocate/exclude CAPRMEDIO-specific Local/Public Release Operations and helper-tool code from general Methodology and the reusable Engine/package. Their delivery is Project-owned: Operations in `.caprmedio_caprmedio/09_operations` and helper tools in root `PROJECT_TOOLS` outside the reusable Engine.
3. Register a delivery boundary that excludes ProjectTools D declarations from the exporter frontier rather than treating them as an outside-Engine error or shipping them in the generic package.
4. Bind the two Project release Workflows to these Project-owned deliveries while retaining package/runtime selection, Journal evidence and Docker/MCP smoke from the installed package. No additional Operator Workflow is introduced.
5. Prove the boundaries with focused contract tests before real invocation; full preflight remains the Local/Public release gate.

### Definition of Done

the Plan is **not** Done **if** an installed entrypoint uses checkout code, reusable package/gate/O200 capability leaves `TOOLS`, a project-specific release feature is delivered as general framework/Methodology/package content, ProjectTools D declarations ship in or fault the generic exporter frontier, package/image/context mismatch is accepted, or required MCP discovery fails.
