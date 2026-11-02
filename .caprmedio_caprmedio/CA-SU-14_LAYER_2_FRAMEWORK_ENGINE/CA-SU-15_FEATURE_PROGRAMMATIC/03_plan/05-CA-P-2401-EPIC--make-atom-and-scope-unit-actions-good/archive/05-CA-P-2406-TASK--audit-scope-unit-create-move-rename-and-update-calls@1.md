---
atom_id: CA-P-2406
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Property, Relation, Artifact/Carrier, Project Structure, Tool, Workflow]
relations:
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-20 14:24:11 +0400"
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

### Definition of Done

Every assigned Scope Unit action has a traceable outcome and coverage disposition; unsafe or unverified behavior remains a finding, not an executed repair.

Planning checkpoint: not started; this Task record is not audit evidence or a passing result.
