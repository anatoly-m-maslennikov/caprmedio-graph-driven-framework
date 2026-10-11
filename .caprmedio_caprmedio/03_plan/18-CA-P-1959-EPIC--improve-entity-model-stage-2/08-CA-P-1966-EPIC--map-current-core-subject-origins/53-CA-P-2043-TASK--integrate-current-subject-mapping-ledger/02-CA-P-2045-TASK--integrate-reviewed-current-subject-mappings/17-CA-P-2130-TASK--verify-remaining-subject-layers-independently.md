---
atom_id: CA-P-2130
content_role: Plan
type: Plan
label: Task
work_sequence_number: 17
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Operator]
version: 1
updated_at: "2026-10-11 10:11:27 +0400"
relations:
  is_decomposition_of: [CA-P-2045]
  depends_on: [CA-P-2121, CA-P-2122, CA-P-2123, CA-P-2124, CA-P-2125, CA-P-2126, CA-P-2127, CA-P-2128]
---
# Summary

Verify remaining Subject layers independently

## Objective

Independent checks reject wrong or missing subject-family layers while accepting exact prospective outputs.

## Details

Own work: at most fifteen minutes. Exclusive scope: support/verify_working_mapping_ledger.py and support/test_working_mapping_ledger.py.

Read and follow `_projection/core-entity-review/stage2/working-ledger.followups-2121-2128.contract.md`. Extend the existing independent one-off verifier and its focused tests for the eight exact selected layers, without importing the producer. Enumerate current source origins and verify exact selected coverage, accepted report/receipt provenance, layer order, final target/confidence and complete quarantine/lineage preservation. Add valid-control adversarial cases for omitted layer, missing/extra or stale origin, wrong target and bad acceptance pins. No output replacement.

Root owns integration, Plans, receipts and Git. No original Core, ordinary content, frozen/captured evidence, earlier raw report, Tool, runtime, MCP/FPF or native-admission changes. A completed leaf does not approve migration or complete mapping. Commit after this Task's actual acceptance.

### Definition of Done

Not Done if any required report/receipt/current pin or independent gate is missing, wrong data is accepted, source writes occur, claims exceed evidence, or own work exceeds fifteen minutes without decomposition.
