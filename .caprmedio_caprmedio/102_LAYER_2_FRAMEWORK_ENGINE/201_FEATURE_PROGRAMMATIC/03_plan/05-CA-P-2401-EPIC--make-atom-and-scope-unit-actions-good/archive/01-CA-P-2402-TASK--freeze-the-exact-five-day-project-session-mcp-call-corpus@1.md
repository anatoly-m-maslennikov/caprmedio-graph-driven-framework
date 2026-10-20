---
atom_id: CA-P-2402
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
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

Freeze the exact five-day project-session MCP call corpus

## Objective

Create the bounded, reproducible input manifest for the four audit lanes without deciding findings or changing project state.

## Details

Read only the relevant project session records after publication, irrespective of which worker or model made the calls. Resolve the exact inclusive/exclusive five-day window from the latest audit anchor, record timezone, session/turn/call identifiers, project and Scope Unit, requested operation, response/output, and any missing or refused result. Keep only the four allowed MCP call families; mark excluded calls and non-MCP/manual/session material rather than silently dropping them. Deduplicate by stable call identity and content hash. Partition the corpus before execution when a partition could exceed 15 minutes of own work; each partition must have disjoint call IDs and an observable manifest receipt. Do not replay calls or infer outputs.

### Inputs and dependencies

Parent: [CA-P-2401](../05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good.md).

No prior audit Task dependency; publication of this planning record precedes execution.

The historical window is [2026-10-15 14:13:44 +0400, 2026-10-20 14:13:44 +0400), exactly 120 hours anchored at this audit's first observation. Filter by event timestamps and project association, not session filenames or model. Missing/truncated/nonpairable calls stay explicit coverage gaps.

### Execution budget and safety

Estimated own work: at most 15 minutes. Before further work that would exceed this limit, split into separately recorded bounded subtasks with disjoint responsibility and acceptance checks. Use Luna workers for every delegated audit lane, dispatch all useful independent ready lanes within capacity, and create no filler lanes. After completion, review/update each dependent next Task before it starts. Historical review is read-only and needs no test server. All current MCP reproductions/tests require a verified isolated nonproduction instance, distinct port, project/golden fixture and state namespace; never test, stop, reload, restart or redeploy production. No historical mutation is replayed. A local fix/test does not establish deployed resolution. Concern creation/status changes remain governed operations and are not covered by the manual planning-only exception. Record blockers as Problems and unresolved choices as Questions without fabricating completion.

### Definition of Done

One exact manifest (or explicit bounded partition manifests) covers every eligible call in the window, with no guessed timestamps, duplicated call, unowned partition, or unrecorded output.

Planning checkpoint: not started; this Task record is not audit evidence or a passing result.
