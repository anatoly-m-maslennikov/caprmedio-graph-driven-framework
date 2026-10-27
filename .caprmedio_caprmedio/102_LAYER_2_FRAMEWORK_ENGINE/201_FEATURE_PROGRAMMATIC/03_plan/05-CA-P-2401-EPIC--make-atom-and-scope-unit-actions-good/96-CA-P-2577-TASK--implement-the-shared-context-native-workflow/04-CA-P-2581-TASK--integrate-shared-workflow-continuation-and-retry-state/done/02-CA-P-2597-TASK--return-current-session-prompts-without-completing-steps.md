---
atom_id: CA-P-2597
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Done
version: 7
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Workflow Orchestration/Action Realization
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2581
  depends_on:
  - CA-P-2596
  - CA-P-2580
  relates_to:
  - CA-R-1527
  - CA-R-1843
  - CA-R-1845
  - CA-M-328
  - CA-D-544
  - CA-O-016
tier: 3
---
# Summary

Return current-session prompts without completing Steps

## Objective

For an Integrated Step, return bound Action instructions and inputs to the current participating session, retaining an open pending Step/Action frontier. Do not invoke the separate CLI Agent, complete the Step or select its successor before submission.

## Details

At most 15 minutes of own work per leaf; split before expanding. One Task per file. Review and update dependent Tasks after actual predecessor acceptance and before execution. Current source R1527@7 defines Integrated as the current participating session; a separate ephemeral CLI is not an Integrated implementation. Preserve existing native packet fields and current M/E/D guidance, explicit Project binding, source freshness, actual evidence and business-only Journal semantics. Use locked uv and configured Project Temporary State. Create a Concern for a real unresolved decision or blocker. No feature work before CA-P-2595 acceptance; no release, deployment, production MCP calls, full-suite run, uncertain replay or Git publication.

### Definition of Done

Retain exact changed paths/source bindings, focused functional and source-conformance evidence, observed limitations and the reviewed next dependent Task. Count fixture integrity, implementation, pending/current-session execution and runtime admission separately.

### Reviewed parallel storage boundary — 22 October 2026

Dependency review keeps this prompt-publication leaf Backlog until both CA-P-2596 durable-state acceptance and CA-P-2580 Action acceptance. The independent store lane may execute first without authorizing this leaf. Use the exact current Action capture contract, no CLI substitution and no premature terminal/interruption; preserve actual outputs and current source/permission/retry bindings.

### Accepted Action and persistence handoff — 22 October 2026

Active after actual acceptance of both CA-P-2580 and complete CA-P-2596. Reuse the current Action bridge and checkpoint APIs with an independently supplied Method inventory; do not call the legacy CLI or unconditional interrupt wrapper. Initial current graph execution must return the same pending invocation on reconnect, keep the actual Workflow/Step/Action open, revalidate sources/candidate/auth/inventory, and retain current Tool outputs. Select the exact current source-bound graph, not caller flags. Result submission, continuation and public MCP exposure remain subsequent leaves. Focused disposable graph tests may now run; production admission remains held.

### Bounded initial dispatch checkpoint — 22 October 2026

The bounded current-session prompt dispatch passed seven focused checks and an independent review. This Done status covers only initial dispatch; the complete real-Manifest journey, continuation/reconnect proof and runtime admission remain separate acceptance work.

