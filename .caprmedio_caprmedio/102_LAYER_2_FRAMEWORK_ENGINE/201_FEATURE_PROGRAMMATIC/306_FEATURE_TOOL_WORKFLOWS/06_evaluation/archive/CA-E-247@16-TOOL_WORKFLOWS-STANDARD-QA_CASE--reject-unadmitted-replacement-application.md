---
atom_id: CA-E-247@16
content_role: Evaluation
type: QA Case
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Tool//REPLACE_ATOM
  depends_on: []
version: 16
updated_at: 2026-10-24 00:51:05 +0400
relations:
  evaluation_for:
  - CA-R-1041
  - CA-R-1093
tier: 3
---
# Summary

Reject unadmitted replacement application

## Scope

Workflow admission owns identity, Version/time, lifecycle and complete schema decisions. Connector calls use CA-D-625 only to verify the supplied request, source preconditions and permission and to perform the explicit mechanical operation. A connector does not choose those decisions.

One predecessor's admitted replacement effects under CA-R-1041 and CA-R-1093, and the independent actions used by its workflow.

## Claim

Prepared intent, admitted permission, observed creation, observed archival and completed replacement are distinct. Missing permission, currentness, validation or effect evidence cannot yield completion.

## Details

### Required admission cases

Dry run with one exact predecessor and explicit successor inputs changes no source, history or runtime state. A never-started rejected request invents no Run/Event. An actual started action retains truthful result/recording or pending evidence under the existing shared Run contract, even when no lifecycle effect succeeds.

Reject stale predecessor/successor state, conflicting identity, missing validation authority, denied permission and changed approved inputs before the affected action writes. Every Summary change, including wording-only edits, requires a fresh successor ID and archival of the predecessor; same-ID Modify is not allowed.

### Required effect and result cases

Use full Atom identity strings corresponding to the illustrative IDs 100 and 200. Verify a completed fresh-ID replacement reports target 100, created 200 and archived 100 with exact observed Versions/source-state evidence. Creation is admitted and observed before predecessor archival. A changed same-ID archival state advances the predecessor from N to N+1 with actual time; its exact prior history remains at N. Preserve predecessor content/history and explicit successor lineage. An admitted existing multi-successor mapping retains its complete explicit set.

For independent Create and Archive actions, a later Archive failure does not erase an already completed Create. Report the created successor, failed or uncertain archival and incomplete replacement truthfully; do not report archived 100 without proof. For several predecessor workflows, stop at the first failure, retain earlier completed actions and leave the rest untouched. Preserve safety/all-or-nothing within each individual action's admitted effect boundary.

Incoming references to 100 remain unchanged by replacement. Find the actual referrers separately and Modify only explicitly selected referrer Atoms through their own currentness/permission boundaries.

### Failure and recording cases

Inject denial before effects, an action-local publication/verification failure, uncertain effect and terminal recording failure after an observed effect. Retain actual known/unknown effects and existing accepted history. Existing recording-only recovery follows its already admitted shared contract; it never replays creation or archival. Resume/retry of the new workflow family remains deferred, and no stronger concurrency or publication guarantee is asserted.

### Acceptance and failure disposition

Reject completion from preparation, intake, permission alone or incomplete creation/archive evidence. Reject lost successor IDs, automatic reference rewrites, hidden failed effects or rollback of earlier independent successes. Keep exact input/definition pins, permission decisions, observed effect states and durable or explicitly pending recording evidence.

These are required future verification cases. This source records no runtime pass, new MCP route or proved backend guarantee.
