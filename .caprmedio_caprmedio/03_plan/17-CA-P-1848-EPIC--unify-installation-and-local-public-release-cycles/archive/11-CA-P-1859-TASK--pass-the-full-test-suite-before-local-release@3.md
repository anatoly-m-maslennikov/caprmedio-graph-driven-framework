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
version: 3
updated_at: "2026-10-10 18:08:27 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Evaluation, Framework Package, Methodology Source, Version, Workflow Run, Journal]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1860]
---
# Summary

Pass the full test suite before local release

## Objective

the AI Agent obtains a fresh complete full-suite preflight for the exact Local release closure before its first destructive product wipe.

## Details

1. Seal the active Methodology-source selection, Engine/package candidate, image, configuration/catalog/lock and expected product/install/runtime replacement without altering product or installed contents.
2. Run the complete current suite, including required host, Docker and MCP end-to-end checks, before the first destructive product wipe. Record expected/executed coverage, identities, commands, exit states and full results; do not repeat it solely for the deterministic generated product/install copy.
3. A failed, missing, skipped or incomplete check blocks Local release. Focused, mock or old evidence does not substitute, and a repaired product closure requires a new full pass.
4. Perform contract conformance checks inside the Local command; do not require a separately commanded review, approval or handover.

### Definition of Done

the Plan is **not** Done **if** a required suite fails, skips or lacks coverage, frozen inputs changed, results cannot prove the complete local gate, or runtime effects could precede the pass.
