---
atom_id: CA-P-2403@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Atom
  - Scope Unit
  - Property
  - Relation
  - Artifact/Carrier
  - Project Structure
  - Tool
  - Workflow
relations:
  is_decomposition_of:
  - CA-P-2401
version: 5
updated_at: 2026-10-24 06:04:43 +0400
tier: 3
---
# Summary

Audit Scope Unit and project_structure validation calls

## Objective

Assess only eligible project-session MCP calls that validate Scope Units or project_structure, preserving the distinction between historical observation and current truth.

## Details

Consume the frozen t01 manifest or its assigned disjoint partition. For every in-scope call, retain request, target project/Scope Unit, declaration and binding fields examined, response/output, and outcome. Classify a workflow result, manual/session interaction, intentional refusal, or bug symptom separately; do not convert a refusal into a defect without evidence. Compare only what the historical call actually checked, including declared parent, unordered classification, name/prefix, governing/delivery bindings, materialization and drift. No mutation or replay is authorized.

### Inputs and dependencies

Parent: [CA-P-2401](../05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good.md).

- [CA-P-2402 — Freeze the exact five-day project-session MCP call corpus](01-CA-P-2402-TASK--freeze-the-exact-five-day-project-session-mcp-call-corpus.md)

The historical window is [2026-10-15 14:13:44 +0400, 2026-10-20 14:13:44 +0400), exactly 120 hours anchored at this audit's first observation. Filter by event timestamps and project association, not session filenames or model. Missing/truncated/nonpairable calls stay explicit coverage gaps.

### Execution budget and safety

Estimated own work: at most 15 minutes. Before further work that would exceed this limit, split into separately recorded bounded subtasks with disjoint responsibility and acceptance checks. Use Luna workers for every delegated audit lane, dispatch all useful independent ready lanes within capacity, and create no filler lanes. After completion, review/update each dependent next Task before it starts. Historical review is read-only and needs no test server. All current MCP reproductions/tests require a verified isolated nonproduction instance, distinct port, project/golden fixture and state namespace; never test, stop, reload, restart or redeploy production. No historical mutation is replayed. A local fix/test does not establish deployed resolution. Concern creation/status changes remain governed operations and are not covered by the manual planning-only exception. Record blockers as Problems and unresolved choices as Questions without fabricating completion.

### Reviewed historical input

Use immutable .caprmedio_tmp/mcp-audit-20261020/corpus-v2/release-v2 and verify SHA256SUMS first. Review scope/Project Structure validation requests and results in the 344 auxiliary direct CAPRMEDIO calls. The dedicated validation partition is empty. Search actual request/action parameters and results, not only tool names, for generic-dispatch validation. Missing observed coverage is not a passing validator or proof of a defect. Preserve exact native IDs, timestamps, source file/line, requests/results and diagnostic text. Embedded/wrapper names are annotations, not extra executions. Source hashes are scan-time; 4 KiB header pins do not cover distant call lines, so no full-session immutability/completeness claim is admitted. Wrapper/async reports remain supporting evidence with explicit ambiguity. No calls, effects, tests or production probes are authorized by this historical review.

### Definition of Done

A complete per-call table and bounded finding list covers the assigned call IDs, identifies missing/incomplete validation, and labels each concern as historical observed, not current verified.

Execution checkpoint: Completed bounded historical review of all 344 auxiliary rows and the empty dedicated validation partition. No executed Scope Unit, Project Structure, governing-place or delivery-place check was proven. Discovery filters, quoted checks and workflow status were not treated as validator runs. Missing coverage is neither a passing validator nor a defect. Evidence: .caprmedio_tmp/mcp-audit-20261020/semantic/scope-validation/.
