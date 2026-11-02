---
atom_id: CA-P-2406@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Graph/Relation
  - Artifact/Carrier
  - Project Structure
  - Workflow
relations:
  is_decomposition_of:
  - CA-P-2401
version: 6
updated_at: 2026-10-24 06:12:45 +0400
tier: 3
---
# Summary

Audit Scope Unit create, move, rename and update calls

## Objective

Assess only historical project-session MCP calls that change Scope Unit declarations or their governed/delivery bindings.

## Details

Consume a disjoint t01 partition. Record operation kind, project/Scope Unit identity, old and requested new declaration/binding values, response/output, refusal reason or effect receipt, and the manual/session/workflow/bug classification. Check the historical call's handling of project_structure, governing and delivery places, references, relative/path semantics, and nonempty-content deletion safety where applicable. Keep observed symptoms separate from any present-day verification and do not execute or replay a Scope Unit mutation.

### Inputs and dependencies

Parent: [CA-P-2401](../05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good.md).

- [CA-P-2402 — Freeze the exact five-day project-session MCP call corpus](01-CA-P-2402-TASK--freeze-the-exact-five-day-project-session-mcp-call-corpus.md)

The historical window is [2026-10-15 14:13:44 +0400, 2026-10-20 14:13:44 +0400), exactly 120 hours anchored at this audit's first observation. Filter by event timestamps and project association, not session filenames or model. Missing/truncated/nonpairable calls stay explicit coverage gaps.

### Execution budget and safety

Estimated own work: at most 15 minutes. Before further work that would exceed this limit, split into separately recorded bounded subtasks with disjoint responsibility and acceptance checks. Use Luna workers for every delegated audit lane, dispatch all useful independent ready lanes within capacity, and create no filler lanes. After completion, review/update each dependent next Task before it starts. Historical review is read-only and needs no test server. All current MCP reproductions/tests require a verified isolated nonproduction instance, distinct port, project/golden fixture and state namespace; never test, stop, reload, restart or redeploy production. No historical mutation is replayed. A local fix/test does not establish deployed resolution. Concern creation/status changes remain governed operations and are not covered by the manual planning-only exception. Record blockers as Problems and unresolved choices as Questions without fabricating completion.

### Reviewed historical input

Use immutable .caprmedio_tmp/mcp-audit-20261020/corpus-v2/release-v2 and verify SHA256SUMS first. Review Scope Unit create/move/rename/update/delete requests and results in the 344 auxiliary direct CAPRMEDIO calls. Dedicated Scope Unit action partition is empty; inspect generic-dispatch request/action parameters before concluding missing observed coverage. Do not infer a successful or broken mutation from no observed call. Preserve exact native IDs, timestamps, source file/line, requests/results and diagnostic text. Embedded/wrapper names are annotations, not extra executions. Source hashes are scan-time; 4 KiB header pins do not cover distant call lines, so no full-session immutability/completeness claim is admitted. Wrapper/async reports remain supporting evidence with explicit ambiguity. No calls, effects, tests or production probes are authorized by this historical review.

### Definition of Done

Every assigned Scope Unit action has a traceable outcome and coverage disposition; unsafe or unverified behavior remains a finding, not an executed repair.

Execution checkpoint: Completed bounded historical Scope Unit action review: no actual create/move/rename/update/delete invocation is proven. Four move/rename context lookups were observed (one complete, three uncertain implementation failures); these are not mutation effects. Evidence: .caprmedio_tmp/mcp-audit-20261020/semantic/scope-actions/. Current capability remains unverified.
