---
subjects:
  governs: Subject/Engineering/Tool//COMMIT_AUTOMATION.Operational Status
  depends_on: []
version: 14
updated_at: 2026-10-24 01:18:03 +0400
relations:
  evaluation_for:
  - CA-M-087
  - CA-M-104
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-217@14
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
---
# Report complete auto-commit operational status

## Claim checked

an Operator can inspect complete current commit-automation transport, service, queue, action, Git-gate, failure, **and** recovery state through one read-only interface.

## Test case

prepare an enabled asynchronous Codex adapter, one live service, queued **and** active actions, one fenced repository lease, one blocked action, one dead letter, partly consumed budgets, an open circuit, **and** prior completed real-change **and** Journal-only actions; invoke integrated status once.

## Acceptance criteria

one schema-versioned result reports Hook activation, service process **and** selected release, admission, queue count **and** bytes, current action **and** phase, pending state, lease, last success **and** failure, budget usage, circuit state, dead letters, receipts, **and** deterministic recovery instructions. the invocation changes no Hook carrier, process, queue item, action state, file, index entry, ref, Journal record, lease, budget, circuit, **or** adapter state.

## Failure disposition

reject the delivery **if** required state is absent, stale, ambiguous, available **only** through Runtime-file inspection, **or** changed by status.
