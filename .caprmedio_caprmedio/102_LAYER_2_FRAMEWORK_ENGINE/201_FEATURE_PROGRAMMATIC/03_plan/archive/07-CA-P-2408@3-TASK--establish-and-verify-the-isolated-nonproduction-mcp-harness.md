---
atom_id: CA-P-2408@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 7
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
version: 3
updated_at: 2026-10-24 06:04:41 +0400
tier: 3
---
# Summary

Establish and verify the isolated nonproduction MCP harness

## Objective

Prove a safe nonproduction endpoint, port, project fixture, and state namespace before any current reproduction or test call.

## Details

After publication and before t07 current reproductions, establish or verify an isolated nonproduction MCP instance using a distinct port, project/root/control-root fixture, state/lock/cache/run/receipt namespace, and golden fixtures. Verify endpoint and port identity so a production endpoint cannot be selected. Record the preflight evidence and any owner-controlled lifecycle requirement; do not start or restart servers during planning preparation, and do not stop, reload, restart, redeploy, or test production. If any isolation check is unavailable, mark the harness unverified and block current reproductions rather than falling back to production.

### Inputs and dependencies

Parent: [CA-P-2401](../05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good.md).

No prior audit Task dependency; publication of this planning record precedes execution.

The historical window is [2026-10-15 14:13:44 +0400, 2026-10-20 14:13:44 +0400), exactly 120 hours anchored at this audit's first observation. Filter by event timestamps and project association, not session filenames or model. Missing/truncated/nonpairable calls stay explicit coverage gaps.

### Execution budget and safety

Estimated own work: at most 15 minutes. Before further work that would exceed this limit, split into separately recorded bounded subtasks with disjoint responsibility and acceptance checks. Use Luna workers for every delegated audit lane, dispatch all useful independent ready lanes within capacity, and create no filler lanes. After completion, review/update each dependent next Task before it starts. Historical review is read-only and needs no test server. All current MCP reproductions/tests require a verified isolated nonproduction instance, distinct port, project/golden fixture and state namespace; never test, stop, reload, restart or redeploy production. No historical mutation is replayed. A local fix/test does not establish deployed resolution. Concern creation/status changes remain governed operations and are not covered by the manual planning-only exception. Record blockers as Problems and unresolved choices as Questions without fabricating completion.

### Bounded image and harness preparation

The read-only safety preflight identified and protected production at port56317 and its exact Project instance; it performed no test/server lifecycle action. Preparation is split into [CA-P-2410 — Prepare a fresh isolated MCP audit image and harness](07-CA-P-2408@3-TASK--establish-and-verify-the-isolated-nonproduction-mcp-harness/01-CA-P-2410-TASK--prepare-a-fresh-isolated-mcp-audit-image-and-harness.md), with its own at-most15-minute budget. The parent remains Active until the complete fixture isolation and non-interference evidence is verified. No production endpoint is admitted as a fallback.

### Definition of Done

A preflight receipt proves nonproduction instance, distinct port, project fixture, state namespace, golden fixtures, and port identity; otherwise the harness is explicitly blocked/unverified and t07 cannot reproduce anything.

Planning checkpoint: not started; this Task record is not audit evidence or a passing result.
