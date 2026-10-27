---
atom_id: CA-P-2180@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Atom
  - Subject
  - Journal
  - Plan
  - Operator
version: 5
updated_at: 2026-10-23 23:03:23 +0400
relations:
  is_decomposition_of:
  - CA-P-2173
  blocks:
  - CA-P-2182
---
# Summary

Integrate Subject application into the MCP update action

## Objective

The existing admitted MCP update action carries the closed one-target Subject variant through its current approval and recording boundary.

## Details

### Local completion — 2026-10-13

Done after independent acceptance of guarded publication, actual selected-route integration, complete independent byte/effect ledgers and actual recording-only repair without replay. The final continuation passed 119 distinct Subject checks and 26 generic Atom Operations checks; it also fixed the refusal-side-effect regression exposed by the broader suite. [Exact evidence, source/code pins and limits](../../../../_projection/core-entity-review/stage2/tools-first/subject-publication-local-completion.md).

This is the Task's local implementation/verification outcome, not installed runtime or migration readiness. Its scope excludes runtime/image/manifest activation. The absent installed confirmation provider therefore does not keep this Task open. Recording-only repair does not reconcile a service's cached pending result. Earlier Active/deferral checkpoints below are historical and are superseded by this completion.

### Current publication decision

CA-P-2179 records the Operator's selected staged-review plus exclusive-window model, with a shared lock for Engine writers and affected-file manual/Git/sync exclusion. This supersedes earlier statements in this Plan that the access/concurrency choice itself remains deferred. It does not waive source/FPF review, implementation, independent verification, actual route admission or separate live migration approval. The changed-Subject guard remains until those gates pass.

Estimated own work: 15 minutes. Assignee: AI Agent. Full application prerequisites: CA-P-2178, CA-P-2179 and CA-P-2170's corresponding current packet independently accepted under CA-P-2171. Bounded closed-request/dispatch and Report fixture work can proceed without enabling publication; successful application and live capability cannot precede these gates.

Exclusive edits: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/lifecycle_intents.py`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/selected_execution.py` and new `tests/test_selected_subject_update.py` in that Orchestrator directory. Reopen callers and coordinate shared interfaces with integration. Other workers own planner/native publication and independent fixtures. Do not edit `selected_routes.py`.

Add only the accepted typed one-target Subject variant to the existing update path. Reuse the actual current Done Report/O145 assessment, CA-D-527 selected envelope, canonical CA-O-030 started Run evidence, approval/currentness checks and prior/change/Run recording. Preserve ordinary update behavior, no-op semantics and no replay. Exact route/packet mismatch or missing required records fails truthfully; recording-only recovery must not republish sources. No local transport exception or invented binding is allowed.

Exercise existing-path happy/no-op/refusal/publication-failure and recording-only recovery fixtures. Deliver actual code/test pins and effect/recording evidence for independent checks. Split a concrete overrun before execution. No Core body, installed runtime/image/manifest or production migration effect occurs; tested integration is not live MCP readiness.

### Bounded integration status

[Recorded integration evidence](../../../../_projection/core-entity-review/stage2/tools-first/intent-and-application-status.md) includes five dispatch and five selected golden-request checks. Actual Session/Run/lifecycle prior is carried into the native path; completed canonical assessment lineage received source review. This does not establish passing end-to-end publication. The Operator deferred concurrency safety, so live changed-Subject writes remain blocked and this Task stays Active until CA-P-2179's later publication design and full application checks are accepted. No concurrency mechanism or live admission follows from safe integration checks.

### Definition of Done

The Plan is **not** Done if concurrent-publication design remains deferred or successful end-to-end application is unaccepted, prerequisite code/contracts are missing/stale, the typed path bypasses actual approval/envelope/Run checks, ordinary behavior regresses, source effects replay during recovery, recording is fabricated/incomplete, focused checks fail, forbidden surfaces change, or own work exceeds 15 minutes without decomposition.
