---
atom_id: CA-P-2154@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 23
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 5
updated_at: 2026-10-24 08:22:45 +0400
relations:
  is_decomposition_of:
  - CA-P-2045
  depends_on:
  - CA-P-2144
  - CA-P-2145
  - CA-P-2146
  - CA-P-2147
  - CA-P-2148
  - CA-P-2149
  - CA-P-2150
  - CA-P-2151
  - CA-P-2152
tier: 3
---
# Summary

Verify unqualified Subject layers independently

## Objective

Independent checks reject wrong or missing unqualified layers and accept only the exact prospective output.

## Details

Own work: at most fifteen minutes. Own only support/verify_working_mapping_ledger.py and support/test_working_mapping_ledger.py. Read `working-ledger.followups-2144-2151.contract.md`; exact inputs/ordering/proof/replacement bounds govern this leaf.

Extend the existing closed verifier/test tables for the sixth group without importing the producer. Require current receipts to reject omission of all eight new layers. Preserve actual Core-only proof, final independent-review/report/receipt hashes, exact accepted proof, current source origins, quarantines and lineage. Add valid-control negatives for omitted group/layer/origin, wrong target/order/confidence, stale source/receipt/review hash and executableflags; no draft replacement or new framework.

No original Core, captured/frozen evidence, unrelated helper, native admission, selector adoption, runtime, MCP or FPF changes. Workers are not alone; preserve others. Root owns Plans, receipts, integration and one commit after each actually completed Task. Decompose unfinished own work before exceeding fifteen minutes.

### Completion

The closed sixth-group verifier and tests are independently accepted. Root's prospective current-source gate passes for 907 sources and 4534 occurrences (1928 proposed, 1540 unchanged, 1066 unresolved); all ten deliberately wrong complete-ledger variants reject, and the 33-test focused suite passes. The immutable CA-P-2151 Counter-zero receipt is accepted only after fixed and actual-row counts establish zero; missing nonzero, unknown, non-integer, boolean, negative and wrong counts reject. This completes support verification, not saved-ledger replacement, semantic final mapping or source migration. Exact verification is recorded in `_projection/core-entity-review/stage2/task-2154.receipt.json`.

### Definition of Done

Not Done if assigned output, exact current-source/report/receipt/review proof, independent acceptance or proportional tests are missing/stale, rejected guesses are admitted, proof is expanded/normalized, authority changes, or own work exceeds fifteen minutes without decomposition.
