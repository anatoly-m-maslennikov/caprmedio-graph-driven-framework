---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Recovery
  depends_on: []
version: 19
updated_at: 2026-10-27 19:59:33 +0400
relations:
  evaluation_for:
  - CA-M-104
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-344
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: ACTION_ENGINE
type: Eval Case
tier: 3
claim_target_scope_unit: ACTION_ENGINE
---
# Open one service circuit at a declared failure budget

## Claim checked

automatic recovery is bounded **and** integrity-sensitive failures require Operator action.

## Test case

exhaust one measured transient restart budget, **then** separately inject governance, Journal, staging, ambiguous Git, **and** lease-integrity failures.

## Acceptance criteria

transient recovery stops at the declared budget **and** opens a visible circuit. **every** integrity-sensitive failure pauses autonomous dispatch immediately, preserves accepted state, **and** reports deterministic Operator recovery instructions. no unconditional auto-resume occurs.

## Failure disposition

reject the service **if** it loops, hides budget use, drops work, **or** retries an integrity-sensitive failure autonomously.
