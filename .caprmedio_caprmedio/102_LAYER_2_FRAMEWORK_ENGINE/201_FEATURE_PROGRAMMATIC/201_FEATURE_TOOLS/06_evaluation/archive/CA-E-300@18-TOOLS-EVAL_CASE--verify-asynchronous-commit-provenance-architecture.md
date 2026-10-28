---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control
  depends_on: []
version: 18
updated_at: 2026-10-27 06:04:45 +0400
relations:
  evaluation_for:
  - CA-M-182
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-300@18
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 3
---
# Verify asynchronous commit-provenance architecture

## Claim checked

CA-M-182 realizes CA-R-802 through one pure decision manager, one mechanical recoverable Scheduler, atomic non-deciding workers, durable state, **and** one serialized Git boundary.

## Test case

inspect the exact source frontier **and** run a controlled plan whose ready worker succeeds, whose completion is delivered twice, whose service stops **before** the next dispatch, **and** whose fixture attempts one undeclared transition **and** one second concurrent Git claim.

## Acceptance criteria

the manager performs no I/O **and** returns the same typed plan for equal inputs. **only** declared steps become ready. repeated completion is idempotent. restart resumes the persisted plan. the undeclared transition **and** second Git claim are rejected **without** mutation. no worker selects downstream work, **and** COMMIT_CHANGE_SET neither imports nor invokes a peer Tool.

## Failure disposition

reject the realization **and** preserve the first impurity, discretionary worker decision, undeclared transition, lost state, duplicate effect, peer orchestration, **or** concurrent Git mutation as a blocked architecture discrepancy.
