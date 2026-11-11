---
atom_id: CA-P-2386
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, "Atom/Status", Journal, Workflow, Operator]
version: 2
updated_at: "2026-10-15 23:39:30 +0400"
relations:
  is_decomposition_of: [CA-P-2385]
---
# Summary

Align Atom Status and Journal contracts

## Objective

Affected R/M/E/D/O contracts consistently permit requested admitted Status on create/update, require neither retained Draft history nor a complete Journal, and introduce no replacement registration, reconstruction, confirmation or proof gate.

## Details

Align Project-local atoms first, then methodology sources, then Engine contracts. Remove mandatory retained Draft-history/head/lineage records and Journal completeness/baseline/receipt checks as creation, Status-change, promotion or mutation-success prerequisites. Replace contradictory active receiving rules rather than inventing a manual-Draft exception. Preserve actual old records as history, not admission gates.

Estimated own work: at most 15 minutes; split further before execution if needed. After completion, review/update the next dependent task. A blocked leaf is postponed with a truthful Problem/Question Concern as appropriate; independent ready work continues.

### Execution split — 2026-10-15

The contract frontier exceeds one 15-minute leaf, so this task now coordinates the bounded children below. Project-local review precedes methodology; Engine alignment follows the reconciled methodology. Read-only implementation/test preparation can proceed independently. After each child, review the next dependent before authorizing it.

- [CA-P-2391 — Review Project-local Status and Journal authority](01-CA-P-2386-TASK--align-atom-status-and-journal-contracts/01-CA-P-2391-TASK--review-project-local-status-and-journal-authority.md)
- [CA-P-2392 — Align methodology Draft-history contracts](01-CA-P-2386-TASK--align-atom-status-and-journal-contracts/02-CA-P-2392-TASK--align-methodology-draft-history-contracts.md)
- [CA-P-2393 — Align methodology Status and Journal contracts](01-CA-P-2386-TASK--align-atom-status-and-journal-contracts/03-CA-P-2393-TASK--align-methodology-status-and-journal-contracts.md)
- [CA-P-2394 — Align Engine Status receiving contracts](01-CA-P-2386-TASK--align-atom-status-and-journal-contracts/04-CA-P-2394-TASK--align-engine-status-receiving-contracts.md)

## Definition of Done

Affected R/M/E/D/O contracts consistently permit requested admitted Status on create/update, require neither retained Draft history nor a complete Journal, and introduce no replacement registration, reconstruction, confirmation or proof gate.
