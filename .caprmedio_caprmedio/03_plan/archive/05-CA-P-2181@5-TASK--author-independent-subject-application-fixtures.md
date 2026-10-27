---
atom_id: CA-P-2181@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Atom
  - Subject
  - Revision
  - Journal
  - Plan
  - Operator
version: 5
updated_at: 2026-10-24 06:04:18 +0400
relations:
  is_decomposition_of:
  - CA-P-2173
  blocks:
  - CA-P-2182
tier: 3
---
# Summary

Author independent Subject application fixtures

## Objective

An independently authored fixture portfolio checks expected bytes/effects and refusal/recovery cases for the chosen MCP route.

## Details

### Local completion — 2026-10-13

Done after independent acceptance of guarded publication, actual selected-route integration, complete independent byte/effect ledgers and actual recording-only repair without replay. The final continuation passed 119 distinct Subject checks and 26 generic Atom Operations checks; it also fixed the refusal-side-effect regression exposed by the broader suite. [Exact evidence, source/code pins and limits](../../../../_projection/core-entity-review/stage2/tools-first/subject-publication-local-completion.md).

This is the Task's local implementation/verification outcome, not installed runtime or migration readiness. Its scope excludes runtime/image/manifest activation. The absent installed confirmation provider therefore does not keep this Task open. Recording-only repair does not reconcile a service's cached pending result. Earlier Active/deferral checkpoints below are historical and are superseded by this completion.

Estimated own work: 15 minutes. Assignee: AI Agent independent of implementation. Fixture/expected-ledger preparation may start now from the recorded route choice and reviewed contract cases. Final executable assertions require CA-P-2170's corresponding actual current packet independently accepted under CA-P-2171 and the real implementation interfaces; do not guess admission or report expected failures as a completed capability pass.

Exclusive edits: new `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/tests/test_subject_apply_portfolio.py` and new `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_subject_apply_portfolio.py`. Use temporary isolated valid carriers. Production modules and other workers' tests are read-only; do not revert others or use the producer as its own oracle.

Author explicit expected source/history/effect ledgers with LF/CRLF and non-Active current Status. Cover happy/no-op, unauthorized or partial approval, stale source/grammar/evidence, duplicate frontier, intent/envelope/Run mismatch, extra fields, projection/symlink, publication failure, failed restoration and missing/failed recording. Recording-only recovery must not repeat publication. Deliberately wrong bytes/effects must fail the checks.

Deliver independent fixtures, expected ledgers, contract/API pins and actual controls to CA-P-2182. If the required portfolio exceeds 15 minutes, split only its concrete independent remainder before execution. No production source, Core body, runtime publication or live capability claim is included.

The Operator deferred concurrency safety. Safe fixture preparation/refusal/no-op checks may continue, but the successful publication and concurrent restoration/history-ownership portfolio remains unaccepted, so this Task stays Active. Live changed-Subject writes remain blocked pending CA-P-2179's later design and actual review/verification. Do not convert partial integration evidence or expected failures into a complete application pass.

### Definition of Done

The Plan is **not** Done if concurrent-publication design remains deferred or the required successful-publication/concurrent-restoration portfolio is unaccepted, required controls/expected ledgers are missing, assertions merely mirror the producer, deliberately wrong output passes, accepted contracts/interfaces are stale, a predicted failure is reported as a pass, ownership overlaps, or own work exceeds 15 minutes without decomposition.
