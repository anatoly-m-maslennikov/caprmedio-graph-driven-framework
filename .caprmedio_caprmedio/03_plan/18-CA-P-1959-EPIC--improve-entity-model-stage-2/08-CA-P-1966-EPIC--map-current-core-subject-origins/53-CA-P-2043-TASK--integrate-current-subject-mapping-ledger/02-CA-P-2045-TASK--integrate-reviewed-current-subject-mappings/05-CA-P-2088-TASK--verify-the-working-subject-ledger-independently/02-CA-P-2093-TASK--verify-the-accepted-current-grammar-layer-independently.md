---
atom_id: CA-P-2093
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Plan, Tool, Operator]
version: 1
updated_at: "2026-10-11 06:56:14 +0400"
relations:
  is_decomposition_of: [CA-P-2088]
  depends_on: [CA-P-2087, CA-P-2091, CA-P-2092]
---
# Summary

Verify the accepted current grammar layer independently

## Objective

The complete working ledger includes the independently accepted current grammar-source review without hiding remaining nulls.

## Details

Estimated own work: at most 15 minutes. Follow working-ledger.contract.md. Own only verify_working_mapping_ledger.py and test_working_mapping_ledger.py. After CA-P-2091 is independently accepted/committed, extend the independent gate to read accepted CA-P-2087 receipt/report separately from unaccepted reset, require exact 33 current-source occurrences, exact final decisions/targets/confidences and current evidence, and reject omitted accepted grammar layers, stale report/source pins and wrong accepted targets. Preserve the no-receipt reset case and every prior negative. No producer import/output edits or source mutation. Final live run depends on CA-P-2092 output.

Workers are not alone. Root owns receipts, Plans, output replacement approval and Git, with a commit after each Task. Preserve original Core/captured evidence and existing migration gates. No MCP/FPF/runtime, selectors, native admission or authorized source application. Stop for decomposition if own work exceeds the bound.

### Definition of Done

Not Done if exact current coverage/pins/layer priority or existing negative checks fail, unknown meanings become guesses, prior provenance is dropped, authority is changed, or own work exceeds the bound without decomposition.
