---
atom_id: CA-P-1863
content_role: Plan
type: Plan
label: Task
work_sequence_number: 15
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-10 18:08:27 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Evaluation, Version, Framework Package, Workflow Run]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1864]
---
# Summary

Pass the full test suite before public release

## Objective

the AI Agent obtains a fresh complete full-suite gate for the exact final snapshot to be pushed publicly.

## Details

1. Freeze the publishable closure after its automatic documentation preparation and one content prompt.
2. Run the complete current suite, including all required host/Docker/MCP end-to-end checks, before `amm/dev` push or PR publication. The Local pass is evidence, not a substitute.
3. Record expected/executed coverage, identities, commands, exit states and full results. Failed, missing or incomplete checks stop the Public release command; focused, mocked or old results cannot waive it.
4. Product, package, source, configuration or documentation changes require a new complete suite. A URL-only metadata follow-up after a new PR does not.
5. Validate conformance inside Public release; do not introduce a separately commanded review, approval or handover.

### Definition of Done

the Plan is **not** Done **if** the fresh full public suite is incomplete or failed, its snapshot differs from the publishable closure, a material change bypasses the gate, or a release prerequisite is unverified.
