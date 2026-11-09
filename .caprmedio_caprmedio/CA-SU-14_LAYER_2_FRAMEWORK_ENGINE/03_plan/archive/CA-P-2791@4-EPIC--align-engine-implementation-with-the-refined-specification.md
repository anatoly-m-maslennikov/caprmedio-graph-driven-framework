---
identity:
  id: CA-P-2791@4
  ref_id: CA-P-2791@4
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
  version: 4
  updated_at: 2026-11-09 15:49:38 +0400
destination:
  file:
    name: CA-P-2791@4-EPIC--align-engine-implementation-with-the-refined-specification.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/archive
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2767
---

## Summary

Align Engine implementation with the refined specification

## Objective

Implement and verify the accepted code corrections identified by the Stage 2 specification review.

## Scope

ENGINE and its eligible descendants, including Workbench capabilities. Old non-Workbench Tools, the 500-Atom benchmark sources, the remaining prior Content migration hold (69 MED after the approved six-Atom C707 review), existing Archives/Drafts, standalone chat and actual native Codex rendering remain outside this active queue. C709–C710 retain the unresolved source handoffs; this Epic does not silently resume them.

## Working procedure

Review and fix the next task before starting. RMED → review/fix → applicable M Policy prompt → RED plus non-Policy M → implementation → E2E → review/fix. Use Terra/Luna where efficient, one Scope Unit per agent, exclusive edit ownership and small Work Reports. Check the model, principles and latest Operator input when unsure; record remaining uncertainty as a C / Question and continue independent work. Specifications stay in RMED, not Tasks.

## Inputs

Stage 2 Current adoption, I7–I9, C711, C712 and the thin implementation map in CA-P-2767. Existing catalog and shared-server wiring is present; do not recreate it from an incomplete package-local search.

## Tasks

- [ ] [Confirm the adopted implementation inputs](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2811-TASK--confirm-the-adopted-implementation-inputs.md)
- [ ] [Fix Workbench editor completion](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2812-TASK--fix-workbench-editor-completion.md)
- [ ] [Reconcile Backend implementation and evaluator pins](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2813-TASK--reconcile-backend-implementation-and-evaluator-pins.md)
- [ ] [Verify MCP registration and discovery contracts](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2814-TASK--verify-mcp-registration-and-discovery-contracts.md)
- [ ] [Verify shared Workbench View and transport behavior](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2815-TASK--verify-shared-workbench-view-and-transport-behavior.md)
- [ ] [Review remaining Engine implementation evidence](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2816-TASK--review-remaining-engine-implementation-evidence.md)
- [ ] [Verify Engine performance and resource regressions](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2817-TASK--verify-engine-performance-and-resource-regressions.md)
- [ ] [Review and deliver the accepted Engine changes](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2818-TASK--review-and-deliver-the-accepted-engine-changes.md)

## Definition of Done

Accepted code corrections match Current RMED and pass their actual acceptance. Latency, throughput, resource use and scope boundaries do not regress. Current module pins describe implemented contracts only. Delivery is independently reported; skipped or deferred native acceptance is never called passed.

## Additional confirmed issue

C712: reproduce and fix stale deleted-Atom rows after a mixed source update/delete batch, with acceptance under E677. Include this in the Backend implementation task before combined regression verification. A full reread is verified recovery, not the incremental-path fix.

## Release implementation ownership

- CA-P-2839 — Relocate release implementation and tests. Backlog; blocked by the reviewed specification move CA-P-2837 and adopted-input confirmation CA-P-2811. The Operator chose specification now, implementation in this Epic.
