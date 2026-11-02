---
subjects:
  governs: Subject/Engineering/Runtime
  depends_on: []
version: 16
updated_at: 2026-10-24 23:19:22 +0400
relations:
  evaluation_for:
  - CA-R-2154
  - CA-M-104
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-223@16
content_role: Evaluation
status: Archived
current_scope_unit: ACTION_ENGINE
claim_target_scope_unit: ACTION_ENGINE
type: Eval Case
tier: 3
author: Anatoly Maslennikov
---
# Summary

Start each enabled service once

## Scope

Evaluation of one background-service lifecycle action and its recorded outcome.

## Claim

## Claim checked

Apply starts each enabled installed service once **and** repeated apply recognizes its live process.

## Test case

Install one enabled long-running Python service, invoke dry-run, apply, apply again, **and** status.

## Acceptance criteria

Dry-run predicts one start **without** mutation. First apply starts one process **and** writes its disposable PID state only under its runtime service directory and appends technical and business log Journal records to their explicitly configured governed local or remote sinks. Second apply reports the same PID as already running **and** starts no process. Status reports one enabled **and** running service; `.caprmedio_runtime/tools` **contains** no Python cache; **and** disposable bytecode **and** cache Carriers exist **only** below `.caprmedio_tmp`.

## Failure disposition

Reject delivery **if** dry-run mutates, apply duplicates a live service, disposable process state is written outside `.caprmedio_runtime`, configured log Journal sinks are bypassed, or stopping or cleaning disposable state changes accepted runtime Journal history, implementation is read outside `.caprmedio_runtime/tools`, **or** liveness is reported incorrectly.
