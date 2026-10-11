---
atom_id: CA-P-2154
content_role: Plan
type: Plan
label: Task
work_sequence_number: 23
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
updated_at: "2026-10-11 12:12:24 +0400"
relations:
  is_decomposition_of: [CA-P-2045]
  depends_on: ["CA-P-2144","CA-P-2145","CA-P-2146","CA-P-2147","CA-P-2148","CA-P-2149","CA-P-2150","CA-P-2151","CA-P-2152"]
---
# Summary

Verify unqualified Subject layers independently

## Objective

Independent checks reject wrong or missing unqualified layers and accept only the exact prospective output.

## Details

Own work: at most fifteen minutes. Own only support/verify_working_mapping_ledger.py and support/test_working_mapping_ledger.py. Read `working-ledger.followups-2144-2151.contract.md`; exact inputs/ordering/proof/replacement bounds govern this leaf.

Extend the existing closed verifier/test tables for the sixth group without importing the producer. Require current receipts to reject omission of all eight new layers. Preserve actual Core-only proof, final independent-review/report/receipt hashes, exact accepted proof, current source origins, quarantines and lineage. Add valid-control negatives for omitted group/layer/origin, wrong target/order/confidence, stale source/receipt/review hash and executableflags; no draft replacement or new framework.

No original Core, captured/frozen evidence, unrelated helper, native admission, selector adoption, runtime, MCP or FPF changes. Workers are not alone; preserve others. Root owns Plans, receipts, integration and one commit after each actually completed Task. Decompose unfinished own work before exceeding fifteen minutes.

### Definition of Done

Not Done if assigned output, exact current-source/report/receipt/review proof, independent acceptance or proportional tests are missing/stale, rejected guesses are admitted, proof is expanded/normalized, authority changes, or own work exceeds fifteen minutes without decomposition.
