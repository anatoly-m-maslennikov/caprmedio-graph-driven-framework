---
cce_version: cce_1
cce_form: evaluation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Recovery
version: 20
updated_at: 2026-11-02 19:44:26 +0400
relations:
  evaluation_for:
  - CA-M-104
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-344
ref_id: CA-E-344
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: ACTION_ENGINE
form: Eval Case
tier: 3
claim_target_scope_unit: ACTION_ENGINE
container:
  scope_unit: CA-SU-34
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
