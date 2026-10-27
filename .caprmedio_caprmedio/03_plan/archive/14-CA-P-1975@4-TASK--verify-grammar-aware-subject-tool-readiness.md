---
atom_id: CA-P-1975@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Entity
  depends_on:
  - Atom
  - Subject
  - Projection
  - Plan
  - Tool
  - Operator
version: 4
updated_at: 2026-10-24 06:04:16 +0400
relations:
  is_decomposition_of:
  - CA-P-1959
  blocks:
  - CA-P-1909
  - CA-P-1967
tier: 3
---
# Summary

Verify grammar-aware Subject Tool readiness

## Objective

Independently verify the final grammar-aware Subject implementation before the accepted graph or migration preview.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisites: CA-P-1963 and CA-P-1965.

Recheck the exact current lookup, parser, graph producer, validator and patch-preview implementation after grammar support changes. Bind both grammar profiles and implementation/source pins. The older CA-P-1963 receipt cannot accept later code.

Use isolated fixtures and a separately authored occurrence/edge ledger; the checker must not derive expected results from the producer's graph builder. Verify correct direction for /, . and :, old-profile handling, explicit RMEDO including Operations, excluded C/A/P, path/owner diagnostics, prefix boundaries and complete non-Subjects byte preservation. Verify exact Version +1 and sealed illustrative preview metadata. Under the current CA-P-2062 ordinary-operations contract there is no live writer; actual execution-time metadata binding belongs to CA-P-1910's final migration packet. Tamper with one output and prove rejection.

Run affected tests with uv. Record actual results and pinned coverage; no authority, history, Journal, runtime or live graph writes. Split larger work before execution.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Completion

Completed at 2026-10-11 05:09:57 +0400. All Search/Update suites passed (44 + 33 tests), including the independently authored approved-profile ledger and deliberate graph/preview corruption checks. Real complete-carrier validation passed for both profiles and mixed dot/colon syntax, with exact proposed-byte comparison, Version +1, sealed illustrative time and no source writes. Current Tool/grammar/code pins and frozen evidence were independently checked.

Fresh exact evidence is in `stage2/task-1975.receipt.json`. The wider graph suite has 217 passes and one recorded pre-existing protected-registry authority-path failure; it is not a whole-graph pass. This closes ordinary Subject Tool readiness only, not semantic mapping, native admission, source cutover or migration approval.

### Definition of Done

The Plan is **not** Done if the final implementation lacks current passing evidence; an old receipt is reused after code changes; the independent corruption check fails; selection or byte preservation is unproved; or authoritative data changes; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.
