---
identity:
  id: CA-P-2791
  ref_id: CA-P-2791@21
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
  status: Archived
  version: 21
  updated_at: 2026-11-11 00:44:42 +0400
destination:
  file:
    name: CA-P-2791@21-EPIC--align-engine-implementation-with-the-refined-specification.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/archive
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

All eligible Engine implementation, including Workbench and generic plugin-free hook/session capabilities. Older non-Workbench Tools are fully retired and are not queued for rebuilding. Migration of the preserved benchmark source corpus, standalone chat and actual native Codex rendering remain excluded or deferred under their existing boundaries. The former 69-MED hold is lifted. C725 is deferred to the version 0.6 Project Objective; its four proposal Drafts remain unadopted. C726 is Resolved and its three permission-update Drafts are withdrawn. Preserve existing Archives and unrelated work.

The previously approved FRAMEWORK_DELIVERY code/test relocation remains in P2839. No other release-scope work is added.

## Working procedure

Review and fix the next task before starting. Current RMEDO → review/fix → applicable Direct/Approach M Policy prompt → RED plus non-Policy M → implementation → E2E → independent review/fix. Give each worker one Scope Unit and exclusive edit paths. Split subtasks before 20 minutes; use small Work Reports. Tasks track work; RMEDO holds specification.

## Inputs and entry gate

P2767 source refinement, actual Current graph and source reports are the entry baseline. Select Current IDs/Versions through replacement lineage; retained historical module comments and old Synopses are not proof of Current behavior. P2811 must confirm inputs before any implementation. P2767 is Done. Enter implementation through P2811: confirm Current inputs and exclusive ownership for each scoped batch. Hold a batch whose source contract is being revised; continue independent accepted work. Preserved benchmark sources are not migrated; latency, throughput and resource tests remain mandatory.

## Tasks

- [ ] [Confirm the adopted implementation inputs](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2811-TASK--confirm-the-adopted-implementation-inputs.md)
- [ ] [Fix Workbench editor completion](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2812-TASK--fix-workbench-editor-completion.md)
- [ ] [Reconcile Backend implementation and evaluator pins](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2813-TASK--reconcile-backend-implementation-and-evaluator-pins.md)
- [ ] [Verify MCP registration and discovery contracts](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2814-TASK--verify-mcp-registration-and-discovery-contracts.md)
- [ ] [Verify shared Workbench View and transport behavior](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2815-TASK--verify-shared-workbench-view-and-transport-behavior.md)
- [x] [Review remaining Engine implementation evidence](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2816-TASK--review-remaining-engine-implementation-evidence.md)
- [ ] [Verify Engine performance and resource regressions](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2817-TASK--verify-engine-performance-and-resource-regressions.md)
- [ ] [Review and deliver the accepted Engine changes](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2818-TASK--review-and-deliver-the-accepted-engine-changes.md)
- [x] [Relocate release implementation and tests](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2839-TASK--relocate-release-implementation-and-tests.md)

- [ ] [Add the query-inaccessible Atom audit table](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2842-TASK--add-the-query-inaccessible-atom-audit-table.md)
- [ ] [Add the declared carrier consistency audit table](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2843-TASK--add-the-declared-carrier-consistency-audit-table.md)
- [ ] [Add the physical carrier consistency audit table](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2844-TASK--add-the-physical-carrier-consistency-audit-table.md)

- [ ] [Implement query result files and Bookmarks](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2852-TASK--implement-query-result-files-and-bookmarks.md)

- [ ] [Fix newly found reader eligibility gaps](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2859-TASK--fix-newly-found-reader-eligibility-gaps.md)


- [ ] [Deliver and verify the standalone Codex hook](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2861-TASK--deliver-and-verify-the-standalone-codex-hook.md)

- [ ] [Verify content extraction for admitted Engine carriers](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2866-TASK--verify-content-extraction-for-admitted-engine-carriers.md)

- [ ] [Implement generic runtime session context](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2910-TASK--implement-generic-runtime-session-context.md)

## Definition of Done

Implemented behavior matches the accepted Current specification with actual acceptance evidence. Preserve latency, throughput and resource guards. Reconcile module IDs/Versions only for directly implemented contracts after verification; never mass-bump pins. Report skipped native acceptance and unrun tests explicitly. Delivery is a separate checked result.

## Handoff

Use the refreshed implementation-map.tsv and P2902/P2903 reports in P2767. The map preserves historical pins and provides Current lineage separately. No Current Code Synopsis remains; do not reopen I7–I9 automatically.

P2812 retains C711 editor completion; P2813 retains C712 incremental delete and Backend pin reconciliation; P2814 retains C714 removed MCP locator and actual registry/discovery verification. P2859/P2866 retain reader eligibility and C716 declared-content extraction. P2815 covers shared View/grid/HTTP/MCP behavior; P2816 handles remaining orchestration and prompt evidence without restoring removed Agent execution.

Verify the new shared Workspace Project-name case E819 under existing Workbench acceptance. Preserve P2852 query-result file/Bookmark work, P2842–P2844 audits, deferred P2860 session reads and active P2910/P2861 context and hook delivery. Old Graph UI/Graph Server contracts and retired pin-refresh gates must not be restored merely to satisfy historical comments. Existing tasks are reused; no duplicate implementation Epic is created.

## Deferred work

The Operator deferred [P2860 Run/history reads](backlog/CA-P-2860-TASK--implement-session-bound-workflow-run-reads.md). P2910 implements generic runtime session context and P2861 delivers the plugin-free hook; no missing executor or history service is introduced here.
