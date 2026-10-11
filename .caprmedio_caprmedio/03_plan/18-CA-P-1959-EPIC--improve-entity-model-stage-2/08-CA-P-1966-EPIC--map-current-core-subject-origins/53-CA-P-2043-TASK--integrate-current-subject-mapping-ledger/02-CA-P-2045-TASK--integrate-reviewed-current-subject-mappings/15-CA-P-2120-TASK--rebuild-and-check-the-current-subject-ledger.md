---
atom_id: CA-P-2120
content_role: Plan
type: Plan
label: Task
work_sequence_number: 15
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Plan, Operator]
version: 1
updated_at: "2026-10-11 09:17:26 +0400"
relations:
  is_decomposition_of: [CA-P-2045]
  depends_on: [CA-P-2118, CA-P-2119]
---
# Summary

Rebuild and check the current subject ledger

## Objective

The current derived ledger includes all six accepted research layers and passes independent verification.

## Details

Estimated own work: at most 15 minutes. Follow `_projection/core-entity-review/stage2/working-ledger.followups-2112-2117.contract.md`. Own only working-ledger/working-mapping-ledger.json, working-ledger/source-frontier.json, working-ledger/diagnostics.json and a new integration checkpoint. After both support Tasks are accepted, Root may replace only the three owned derived drafts whose exact previous hashes are declared in the additive integration contract. Preserve prior versions in Git, not backup copies. Regenerate once with the create-only ad-hoc producer, then run the independent current-source/layer gate and adversarial suite. The accepted report totals determine the forecast; actual counts are checked, not assumed. Original Core Subjects/content, captured evidence and raw reports remain unchanged. Full mapping, selectors and final graph/approval/application gates remain open.

Workers are not alone. Root owns integration, lifecycle and a commit after completion. Preserve original Core, frozen/captured evidence, prior reports, unrelated work and later migration gates. No MCP/FPF/runtime/Tool/source/Git writes by workers. Use uv offline with --no-project; scratch/cache in .caprmedio_tmp. Compile in memory, not source-directory pycache. Decompose work exceeding the bound.

### Definition of Done

Not Done if exact coverage/provenance or independent checks fail, current source/evidence drift is hidden, authority changes, completion exceeds actual evidence, or own work exceeds the bound without decomposition.
