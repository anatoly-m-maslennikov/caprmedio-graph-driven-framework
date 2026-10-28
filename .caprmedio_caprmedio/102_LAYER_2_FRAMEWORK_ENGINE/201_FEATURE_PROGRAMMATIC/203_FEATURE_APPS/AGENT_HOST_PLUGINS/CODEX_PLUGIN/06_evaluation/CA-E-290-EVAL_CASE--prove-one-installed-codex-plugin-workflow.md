---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing
  depends_on: []
version: 17
updated_at: 2026-10-27 19:59:32 +0400
relations:
  evaluation_for:
  - CA-M-152
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-290
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Eval Case
tier: 3
---
# Prove one installed Codex plugin workflow

## Claim checked

One fresh installed Codex plugin supplies replayable evidence for its declared bounded workflow.

## Test case

Install one packaged plugin from its local marketplace source **and** run one supported workflow **in** a fresh conversation.

## Acceptance criteria

the expected capability activates, declared resources resolve, the result is correct, **and** installation is **not** confused with runtime proof.

## Failure disposition

Reject the installed workflow claim **and** retain the distinct failed outcome.
