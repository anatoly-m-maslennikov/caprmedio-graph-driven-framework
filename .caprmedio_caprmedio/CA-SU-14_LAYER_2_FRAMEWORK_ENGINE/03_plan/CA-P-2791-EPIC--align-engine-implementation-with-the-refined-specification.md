---
identity:
  id: CA-P-2791
  ref_id: CA-P-2791
context:
  container:
    scope_unit: CA-SU-14
  role: Plan
  form: Plan
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
  label: Epic
state:
  status: active
  version: 41
  updated_at: '2026-11-11T23:40:04.931365+04:00'
destination:
  file:
    name: CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2767
---

## Summary

Align Engine implementation with the refined specification

## Objective

Implement and verify the accepted code work from the completed Stage 2 source review.

## Scope

All eligible Engine implementation, including Workbench and generic plugin-free hook/session capabilities. Older non-Workbench Tools are fully retired and are not queued for rebuilding. The newly approved Atom Lifecycle Tools are tracked separately in CA-P-2934. Migration of the preserved benchmark source corpus, standalone chat and actual native Codex rendering remain excluded or deferred under their existing boundaries. The former 69-MED hold is lifted. C725 is deferred to the version 0.6 Project Objective; its four proposal Drafts remain unadopted. C726 is Resolved and its three permission-update Drafts are withdrawn. Preserve existing Archives and unrelated work.

The previously approved FRAMEWORK_DELIVERY code/test relocation remains in P2839. No other release-scope work is added.

## Working procedure

Review and fix the next task before starting. Current RMEDO → review/fix → applicable Direct/Approach M Policy prompt → RED plus non-Policy M → implementation → E2E → independent review/fix. Give each worker one Scope Unit and exclusive edit paths. Split subtasks before 20 minutes; use small Work Reports. Tasks track work; RMEDO holds specification.

## Inputs and entry gate

P2767 source refinement, actual Current graph and source reports are the entry baseline. Select Current IDs/Versions through replacement lineage; retained historical module comments and old Synopses are not proof of Current behavior. P2811 must confirm inputs before any implementation. P2767 is Done. Enter implementation through P2811: confirm Current inputs and exclusive ownership for each scoped batch. Hold a batch whose source contract is being revised; continue independent accepted work. Preserved benchmark sources are not migrated; latency, throughput and resource tests remain mandatory.

## Tasks

- [x] [Confirm the adopted implementation inputs](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2811-TASK--confirm-the-adopted-implementation-inputs.md)
- [x] [Fix Workbench editor completion](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2812-TASK--fix-workbench-editor-completion.md)
- [x] [Reconcile Backend implementation and evaluator pins](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2813-TASK--reconcile-backend-implementation-and-evaluator-pins.md)
- [x] [Verify MCP registration and discovery contracts](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2814-TASK--verify-mcp-registration-and-discovery-contracts.md)
- [x] [Verify shared Workbench View and transport behavior](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2815-TASK--verify-shared-workbench-view-and-transport-behavior.md)
- [x] [Review remaining Engine implementation evidence](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2816-TASK--review-remaining-engine-implementation-evidence.md)
- [x] [Verify Engine performance and resource regressions](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2817-TASK--verify-engine-performance-and-resource-regressions.md)
- [x] [Review and deliver the accepted Engine changes](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2818-TASK--review-and-deliver-the-accepted-engine-changes.md)
- [x] [Relocate release implementation and tests](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2839-TASK--relocate-release-implementation-and-tests.md)

- [x] [Add the query-inaccessible Atom audit table](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2842-TASK--add-the-query-inaccessible-atom-audit-table.md)
- [x] [Add the declared carrier consistency audit table](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2843-TASK--add-the-declared-carrier-consistency-audit-table.md)
- [x] [Add the physical carrier consistency audit table](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2844-TASK--add-the-physical-carrier-consistency-audit-table.md)

- [x] [Implement query result files and Bookmarks](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2852-TASK--implement-query-result-files-and-bookmarks.md)

- [x] [Fix newly found reader eligibility gaps](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2859-TASK--fix-newly-found-reader-eligibility-gaps.md)


- [x] [Deliver and verify the standalone Codex hook](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2861-TASK--deliver-and-verify-the-standalone-codex-hook.md)

- [x] [Verify content extraction for admitted Engine carriers](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2866-TASK--verify-content-extraction-for-admitted-engine-carriers.md)

- [x] [Implement generic runtime session context](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2910-TASK--implement-generic-runtime-session-context.md)

- [x] [Implement the new Atom Lifecycle Tools](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-2934-TASK--implement-the-new-atom-lifecycle-tools.md)

- [x] [Verify the six lifecycle tools in the final image](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done/CA-P-3003-TASK--verify-the-six-lifecycle-tools-in-the-final-image.md)
- [ ] [Verify lifecycle input handling against CA-E-824](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-3004-TASK--verify-lifecycle-input-handling-against-ca-e-824.md)
- [ ] [Release the final Engine image locally](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-3005-TASK--release-the-final-engine-image-locally.md)

- [ ] [Fix live Atom lifecycle latency and Scope Unit refresh](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-3006-TASK--fix-live-atom-lifecycle-latency-and-scope-refresh.md)

## Definition of Done

A working current-code image remains required. Build and start it, then verify health, Workbench frontend/backend and query_run through their actual interfaces. Workflow-engine deferral does not waive these checks or the existing Workbench performance/resource guards.

Implemented behavior matches the accepted Current specification with actual acceptance evidence. Preserve latency, throughput and resource guards. Reconcile module IDs/Versions only for directly implemented contracts after verification; never mass-bump pins. Report skipped native acceptance and unrun tests explicitly. Delivery is a separate checked result.

## Handoff

Use the refreshed implementation-map.tsv and P2902/P2903 reports in P2767. The map preserves historical pins and provides Current lineage separately. No Current Code Synopsis remains; do not reopen I7–I9 automatically.

P2812 retains C711 editor completion; P2813 retains C712 incremental delete and Backend pin reconciliation; P2814 retains C714 removed MCP locator and actual registry/discovery verification. P2859/P2866 retain reader eligibility and C716 declared-content extraction. P2815 covers shared View/grid/HTTP/MCP behavior; P2816 completed the bounded evidence review; its Workflow/prompt follow-up is deferred.

Verify the new shared Workspace Project-name case E819 under existing Workbench acceptance. Preserve P2852 query-result file/Bookmark work, P2842–P2844 audits, deferred P2860 session reads and active P2910/P2861 context and hook delivery. Old Graph UI/Graph Server contracts and retired pin-refresh gates must not be restored merely to satisfy historical comments. Existing tasks are reused; no duplicate implementation Epic is created.

## Deferred work

Formal Scope Delegation admission is deferred to version 0.7. CA-P-3000 tracks the redesign of allowed Roles, Forms, and Subjects. CA-P-2934 tracks lifecycle Tool delivery separately.

The Operator deferred all Workflow-engine work on 11 November 2026: execution, orchestration, queues/scheduling, Step/Substep routing, Run state/history, recovery, and stale Workflow/prompt-frontier repairs (including C727 and P2708). Resume only on an explicit Operator instruction. These are excluded from implementation and acceptance gates; they do not block a working image. Retain MCP, Workbench, query_run and their shared backend, direct release runners, and independent generic session-context/hook work. Keep relevant RMEDO and existing code; this is a work deferral, not a code-removal or source-retirement instruction.

The Operator re-added Atom Lifecycle Workflow implementation only as new Tools using the existing adapters (CA-P-2934). This does not resume the generic Workflow engine, queues, Run history, or retired Tool implementations.

The Operator deferred [P2860 Run/history reads](../001_backlog/CA-P-2860-TASK--implement-session-bound-workflow-run-reads.md). P2910 implements generic runtime session context and P2861 delivers the plugin-free hook; no missing executor or history service is introduced here.

## Adopted-source scope update

The SQL UPDATE portion of the concurrent source handoff has been returned to Draft; its previous read-only Current contracts are restored. Other source decisions retain their status. The Operator assigned new SQL scripts, source-backed UPDATE/Draft state and associated Tab/help capability integration to [P2912](../001_backlog/CA-P-2912-EPIC--implement-workbench-sql-scripts-and-source-updates.md). P2791 implements the applicable pre-existing result-file, audit, completion, registry, context, hook and release-refinement subset only; it does not claim full implementation of the newly expanded Claims.
