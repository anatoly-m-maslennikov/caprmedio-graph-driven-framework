---
atom_id: CA-P-2181
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Revision, Journal, Plan, Operator]
version: 1
updated_at: "2026-10-12 04:16:55 +0400"
relations:
  is_decomposition_of: [CA-P-2173]
  blocks: [CA-P-2182]
---
# Summary

Author independent Subject application fixtures

## Objective

An independently authored fixture portfolio checks expected bytes/effects and refusal/recovery cases for the chosen MCP route.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent independent of implementation. Fixture/expected-ledger preparation may start now from the recorded route choice and reviewed contract cases. Final executable assertions require CA-P-2170's corresponding actual current packet independently accepted under CA-P-2171 and the real implementation interfaces; do not guess admission or report expected failures as a completed capability pass.

Exclusive edits: new `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/tests/test_subject_apply_portfolio.py` and new `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_subject_apply_portfolio.py`. Use temporary isolated valid carriers. Production modules and other workers' tests are read-only; do not revert others or use the producer as its own oracle.

Author explicit expected source/history/effect ledgers with LF/CRLF and non-Active current Status. Cover happy/no-op, unauthorized or partial approval, stale source/grammar/evidence, duplicate frontier, intent/envelope/Run mismatch, extra fields, projection/symlink, publication failure, failed restoration and missing/failed recording. Recording-only recovery must not repeat publication. Deliberately wrong bytes/effects must fail the checks.

Deliver independent fixtures, expected ledgers, contract/API pins and actual controls to CA-P-2182. If the required portfolio exceeds 15 minutes, split only its concrete independent remainder before execution. No production source, Core body, runtime publication or live capability claim is included.

### Definition of Done

The Plan is **not** Done if required controls/expected ledgers are missing, assertions merely mirror the producer, deliberately wrong output passes, accepted contracts/interfaces are stale, a predicted failure is reported as a pass, ownership overlaps, or own work exceeds 15 minutes without decomposition.
