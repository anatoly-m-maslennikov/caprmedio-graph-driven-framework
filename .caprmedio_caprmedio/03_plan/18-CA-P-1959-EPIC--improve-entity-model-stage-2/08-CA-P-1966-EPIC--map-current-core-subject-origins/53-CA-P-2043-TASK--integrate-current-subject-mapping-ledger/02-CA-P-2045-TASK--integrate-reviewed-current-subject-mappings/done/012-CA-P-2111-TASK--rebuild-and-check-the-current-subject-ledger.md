---
atom_id: CA-P-2111
content_role: Plan
type: Plan
label: Task
work_sequence_number: 12
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Plan, Operator]
version: 2
updated_at: "2026-10-11 08:51:34 +0400"
relations:
  is_decomposition_of: [CA-P-2045]
  follows: [CA-P-2109, CA-P-2110]
---
# Summary

Rebuild and check the current subject ledger

## Objective

The current derived ledger includes all six accepted research layers and passes independent verification.

## Details

Estimated own work: at most15 minutes. Follow `_projection/core-entity-review/stage2/working-ledger.followups-2103-2108.contract.md`. Exclusive edit scope: working-ledger/working-mapping-ledger.json, working-ledger/source-frontier.json, working-ledger/diagnostics.json and a new integration checkpoint. After both support Tasks pass, Root replaces only the three exact derived drafts declared in the contract, verifies Git recoverability, regenerates once and verifies actual full current outputs. Expected change: one hundred additional supported proposals. Keep all source/captured/raw evidence unchanged and final migration gates open.

Workers are not alone. Root owns acceptance, controlled lifecycle, shared output replacement and a commit after each completed Task. No Core, Tool, captured evidence, prior report, runtime, MCP, FPF or worker Git writes. Decompose work that exceeds the bound.

### Completion

Only the three exact owned derived drafts were replaced after prior hashes and Git recovery were checked. The actual persisted ledger passes independent907/4534 coverage with1648 proposals,1540 unchanged and1346 nulls; all317 tests, ten whole-ledger controls and66 report controls pass. Original Core and frozen/raw evidence remain unchanged; final migration/content gates remain open. Exact verification is recorded in `_projection/core-entity-review/stage2/task-2111.receipt.json`.

### Definition of Done

Not Done if a prerequisite is not Done, exact coverage/provenance/current pins fail, an earlier layer is omitted, wrong data passes, source/captured output changes, verification is only a forecast, or own work exceeds the bound without decomposition.
