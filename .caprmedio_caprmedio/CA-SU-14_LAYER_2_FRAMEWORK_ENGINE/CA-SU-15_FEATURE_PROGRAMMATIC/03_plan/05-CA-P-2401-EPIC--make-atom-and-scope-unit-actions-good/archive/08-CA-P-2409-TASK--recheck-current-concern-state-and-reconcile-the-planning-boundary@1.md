---
atom_id: CA-P-2409
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
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

Recheck current concern state and reconcile the planning boundary

## Objective

Check whether each concrete concern is still active, resolved, or unverified, then reconcile the result with CA-P-2401 without editing the Epic.

## Details

Consume the t06 concern ledger and its evidence links. Use only the allowed current-state validation/find operations needed to verify the affected project, Scope Unit, Atom carrier, or C/Problem; do not replay mutations. Any current reproduction or test call must use the verified t08 nonproduction instance, distinct port, project fixture, state namespace, and golden fixtures; never fall back to production. For each concern, record current evidence, status active/resolved/unverified, resolution receipt when resolved, and whether the Epic's existing planning boundary covers it, needs a future bounded child, or remains a C/Question hold. Never mark a historical symptom resolved from absence of evidence, a plan, a refusal, or an unverified harness. Preserve the existing Epic scope and report proposed reconciliation separately for root to review.

### Inputs and dependencies

Parent: [CA-P-2401](../05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good.md).

- [CA-P-2407 — Register and deduplicate concrete C/Problems](06-CA-P-2407-TASK--register-and-deduplicate-concrete-c-problems.md)
- [CA-P-2408 — Establish and verify the isolated nonproduction MCP harness](07-CA-P-2408-TASK--establish-and-verify-the-isolated-nonproduction-mcp-harness.md)

The historical window is [2026-10-15 14:13:44 +0400, 2026-10-20 14:13:44 +0400), exactly 120 hours anchored at this audit's first observation. Filter by event timestamps and project association, not session filenames or model. Missing/truncated/nonpairable calls stay explicit coverage gaps.

### Execution budget and safety

Estimated own work: at most 15 minutes. Before further work that would exceed this limit, split into separately recorded bounded subtasks with disjoint responsibility and acceptance checks. Use Luna workers for every delegated audit lane, dispatch all useful independent ready lanes within capacity, and create no filler lanes. After completion, review/update each dependent next Task before it starts. Historical review is read-only and needs no test server. All current MCP reproductions/tests require a verified isolated nonproduction instance, distinct port, project/golden fixture and state namespace; never test, stop, reload, restart or redeploy production. No historical mutation is replayed. A local fix/test does not establish deployed resolution. Concern creation/status changes remain governed operations and are not covered by the manual planning-only exception. Record blockers as Problems and unresolved choices as Questions without fabricating completion.

### Definition of Done

A current-state matrix covers every deduplicated concern, separates historical and current evidence, and yields an explicit plan disposition or unresolved hold without an Epic edit or deployment claim.

Planning checkpoint: not started; this Task record is not audit evidence or a passing result.
