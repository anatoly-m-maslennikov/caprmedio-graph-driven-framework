---
atom_id: CA-P-2514@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 74
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 3
updated_at: '2026-10-21T01:15:09Z'
---
# Summary

Repair stale Plan predecessor expectations

## Objective

Align only confirmed stale synthetic test expectations with current flat Plan predecessor placement before the next full local release.

## Details

At most15 minutes own work; split before extending. Depends on completion of the currently running failed full suite and C557 diagnosis. Own ATOM_UPDATE/tests/test_subject_intent_materialization.py and WORKFLOW_ORCHESTRATOR/tests/test_selected_subject_apply_portfolio.py expectation helpers only. Use current shared Plan destination03_plan/archived; preserve Requirement archive and deliberate legacy-history fixtures. No production change, weakened assertion, live corpus fallback, gate waiver or held replay. Acceptance: both focused modules and one narrow adjacent suite pass; independent exact-diff review approves no weakened proof. After completion review/update P2513 with a fresh Run ID and rerun every normal full-release gate. Source edits wait until the current suite has finished collecting its failure set.

### Complete gate result and execution review

The full run local-20261021-mcp-health-verified-env has finished:424 modules,3796 tests,zero skips,six failed modules; launcher integration passed. No install/startup phase ran. Source repair may now begin under the exclusive scope below, followed by independent diff review and fresh focused/full checks. No failed receipt is reused as acceptance.

### Verified completion and next dependency review

Frozen expectation-only changes align Plan predecessor paths with owning shared archived, preserving Requirement archive. Release virtualenv checks: intent10/10, independent portfolio6/6, adjacent subject acceptance10/10 pass. Independent exact-diff review APPROVE; bytes/effects/no-op assertions and production remain unchanged. Review P2513 against this accepted increment; full release still waits for C558/C559 source repairs and a fresh integrated/full gate.
