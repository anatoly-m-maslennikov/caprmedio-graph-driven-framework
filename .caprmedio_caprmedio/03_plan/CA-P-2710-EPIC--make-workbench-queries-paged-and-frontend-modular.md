---
atom_id: CA-P-2710
ref_id: CA-P-2710
container:
  scope_unit: CA-SU-00
role: Plan
form: Plan
label: Epic
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 3
status: Done
version: 66
updated_at: 2026-11-07 15:46:07 +0400
carrier_destination:
  file:
    name: CA-P-2710-EPIC--make-workbench-queries-paged-and-frontend-modular.md
    path: .caprmedio_caprmedio/03_plan
---

## Summary

Make Workbench queries paged and the frontend modular

## Objective

Complete and verify the Workbench runtime improvements:

- Less latency.
- More throughput.
- Less RAM and CPU during cold startup, peak load and background work.
- Less boilerplate through the shared MCP and Workbench backend API.
- Better architecture.

Latency and throughput remain regression constraints. The existing performance limits are unchanged. The Operator accepted lower total CPU work with the documented higher brief peak in the uncapped diagnostic; the deployed service retains its one-core cap.

## Scope

Workbench/runtime RMED, implementation, tests, documentation and local deployment. Workflow definitions, Atom migrations and unrelated methodology changes are outside this completion scope. Design is in RMED; these tasks record execution.

## Completed tasks

- [x] Create, review and adopt the accepted RMED.
- [x] Gather or reuse the applicable scoped Method Policy prompts.
- [x] Implement and review the accepted runtime changes.
- [x] Verify shared MCP/web behavior and code-owned registration.
- [x] Verify package/image generation and the retained launcher behavior.
- [x] Run the unchanged latency, throughput and rebuild gates.
- [x] Measure profiler-off cold, peak and background resources on the same source snapshot.
- [x] Perform the local release and verify the installed runtime.
- [x] Strengthen and run the real-project lifecycle canary.
- [x] Record acceptance, limits and deferred follow-ups.
- [x] Review the five objectives and complete this Epic.

## Acceptance

Done. **0.4.4.34** is installed and healthy. All **21 unchanged performance gates** and **16 live-project visibility checks** passed. The resource review passed: cold CPU work fell 25.9%, reread CPU work 9.0%, and peak cgroup memory 47.8% on the paired frozen-source workload. Idle CPU remains low; a reliable idle-CPU reduction is not claimed. The higher brief uncapped CPU peak is explicitly accepted and recorded.

Evidence and measurement limits: [completion report](CA-P-2710-EPIC--make-workbench-queries-paged-and-frontend-modular/runtime-completion-20261107.md).

Accepted source references include M465, M506, D704, E798, E677@21 and E794@2. Historical implementation cycles and their earlier receipts remain in [predecessor 65](archive/CA-P-2710@65-EPIC--make-workbench-queries-paged-and-frontend-modular.md) and this Epic's evidence folder.

## Deferred follow-ups

- C705: actual native Codex Workbench UI acceptance, deferred by the Operator.
- A1329: optional, unselected performance experiments, including signed state, alternative libraries, concurrency and partitioning. These are not required for the accepted runtime goals.
- A1322: general PROGRAMMATIC Policy proposals, not adopted by this Epic.
- Disabled standalone-chat work remains deferred.
- Unchanged lifecycle/Atom-migration and Journal fixtures remain with their owning work: [handoff](CA-P-2710-EPIC--make-workbench-queries-paged-and-frontend-modular/legacy-fixture-followups-20261107.md).

The full repository suite is not claimed green. No deferred item is recorded as implemented or verified.
