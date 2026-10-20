---
atom_id: CA-P-2404
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Property, Relation, Artifact/Carrier, Project Structure, Tool, Workflow]
relations:
  is_decomposition_of: [CA-P-2401]
version: 4
updated_at: "2026-10-20 15:30:14 +0400"
---
# Summary

Audit Atom YAML, body, filename and placement validity calls

## Objective

Assess only historical project-session validity checks for Atom carriers and containers, without performing a repair or assuming a current defect.

## Details

Consume the explicitly assigned validation-facet view of frozen t01 calls; canonical lifecycle call ownership remains unchanged. For each eligible call, record the exact carrier identity/revision if present, YAML parse and typed-field result, required body heading/order result, filename and placement result, Scope/Role/Type context, and response/output. Include folder-backed Plan and Operations containers when the call covers them. Separate invalid-input/refusal, workflow/manual/session behavior, observed bug symptoms, and absent coverage. Preserve source call evidence and do not re-read or rewrite a carrier as a substitute for the historical result.

### Inputs and dependencies

Parent: [CA-P-2401](../05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good.md).

- [CA-P-2402 — Freeze the exact five-day project-session MCP call corpus](01-CA-P-2402-TASK--freeze-the-exact-five-day-project-session-mcp-call-corpus.md)

The historical window is [2026-10-15 14:13:44 +0400, 2026-10-20 14:13:44 +0400), exactly 120 hours anchored at this audit's first observation. Filter by event timestamps and project association, not session filenames or model. Missing/truncated/nonpairable calls stay explicit coverage gaps.

### Execution budget and safety

Estimated own work: at most 15 minutes. Before further work that would exceed this limit, split into separately recorded bounded subtasks with disjoint responsibility and acceptance checks. Use Luna workers for every delegated audit lane, dispatch all useful independent ready lanes within capacity, and create no filler lanes. After completion, review/update each dependent next Task before it starts. Historical review is read-only and needs no test server. All current MCP reproductions/tests require a verified isolated nonproduction instance, distinct port, project/golden fixture and state namespace; never test, stop, reload, restart or redeploy production. No historical mutation is replayed. A local fix/test does not establish deployed resolution. Concern creation/status changes remain governed operations and are not covered by the manual planning-only exception. Record blockers as Problems and unresolved choices as Questions without fabricating completion.

### Reviewed validation facet input

Use immutable .caprmedio_tmp/mcp-audit-20261020/corpus-v2/release-v2 and verify SHA256SUMS first. Inspect validation diagnostics across the 384 lifecycle direct calls plus relevant auxiliary requests. This is a cross-cutting facet, not 384 additional calls or independent Problem ownership. Cover YAML, Role/Type fields, heading order, filename/location, P/O containers only where the exact response supplies evidence; separate input errors and coverage gaps. Preserve exact native IDs, timestamps, source file/line, requests/results and diagnostic text. Embedded/wrapper names are annotations, not extra executions. Source hashes are scan-time; 4 KiB header pins do not cover distant call lines, so no full-session immutability/completeness claim is admitted. Wrapper/async reports remain supporting evidence with explicit ambiguity. No calls, effects, tests or production probes are authorized by this historical review.

### Definition of Done

Every assigned validity call has an evidence row and a bounded finding/coverage disposition; historical observations are explicitly marked unverified until t07.

Execution checkpoint: all 728 canonical rows have distinct-call outcome records, and independent consolidation reviewed the diagnostic facets. The requested validator matrix is not established by these calls; three lookup schema_invalid outcomes and repeated CarrierError coverage entries remain non-confirmed/coverage signals, not extra calls or invented defects. The worker turn ended at its output limit after producing the artifacts; retained report/ledger counts and independent review support this bounded historical-analysis completion, not a claimed native validation pass.
