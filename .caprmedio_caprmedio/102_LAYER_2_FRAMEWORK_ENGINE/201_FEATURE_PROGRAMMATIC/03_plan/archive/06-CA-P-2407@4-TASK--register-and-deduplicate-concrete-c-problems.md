---
atom_id: CA-P-2407@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
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
version: 4
updated_at: 2026-10-24 06:04:43 +0400
tier: 3
---
# Summary

Register and deduplicate concrete C/Problems

## Objective

Turn lane findings into a deduplicated concern ledger while preserving historical evidence and avoiding duplicate or speculative Problems.

## Details

Consume t02 through t05 outputs. Normalize each concrete concern by affected project/Scope Unit, operation or validation family, invariant, and evidence references. Find matching current C/Problem records before proposing a new one; reuse an exact match, link a distinct concern, or record a non-problem/refusal/manual outcome. Keep fields for historical_observed_symptom, evidence_call_ids, current_verification_status, and plan_disposition separate. New governed C/Problem creation, if still warranted, uses the normal MCP path where available, or the Operator-authorized manual fallback when it cannot perform the operation.

### Inputs and dependencies

Parent: [CA-P-2401](../05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good.md).

- [CA-P-2403 — Audit Scope Unit and project_structure validation calls](02-CA-P-2403-TASK--audit-scope-unit-and-project-structure-validation-calls.md)
- [CA-P-2404 — Audit Atom YAML, body, filename and placement validity calls](03-CA-P-2404-TASK--audit-atom-yaml-body-filename-and-placement-validity-calls.md)
- [CA-P-2405 — Audit Atom lifecycle and container action calls](04-CA-P-2405-TASK--audit-atom-lifecycle-and-container-action-calls.md)
- [CA-P-2406 — Audit Scope Unit create, move, rename and update calls](05-CA-P-2406-TASK--audit-scope-unit-create-move-rename-and-update-calls.md)

The historical window is [2026-10-15 14:13:44 +0400, 2026-10-20 14:13:44 +0400), exactly 120 hours anchored at this audit's first observation. Filter by event timestamps and project association, not session filenames or model. Missing/truncated/nonpairable calls stay explicit coverage gaps.

### Execution budget and safety

Estimated own work: at most 15 minutes. Before further work that would exceed this limit, split into separately recorded bounded subtasks with disjoint responsibility and acceptance checks. Use Luna workers for every delegated audit lane, dispatch all useful independent ready lanes within capacity, and create no filler lanes. After completion, review/update each dependent next Task before it starts. Historical review is read-only and needs no test server. All current MCP reproductions/tests require a verified isolated nonproduction instance, distinct port, project/golden fixture and state namespace; never test, stop, reload, restart or redeploy production. No historical mutation is replayed. A local fix/test does not establish deployed resolution. Concern creation/status changes remain governed operations and are now covered by the Operator-authorized manual fallback when MCP cannot perform them. Record blockers as Problems and unresolved choices as Questions without fabricating completion.

### Definition of Done

One ledger has a stable dedup key, one disposition per finding, source links to lane evidence, and an explicit no-duplicate decision for every proposed concern.

Planning checkpoint: completed registration only; not implementation or runtime acceptance.

### Current checkpoint

Independent semantic review reconciled 384 disjoint lifecycle call IDs and the auxiliary facets. The smallest reviewed Problem set is three candidates: current stale CA-D-305 graph-authority pin; historical uncertain CA-P-1959 update; historical interrupted CA-P-1911 status Run. Their causes/current states must not be merged by guess. Scope/validator missing coverage and truncated evidence are not invented product defects. Consolidated report: .caprmedio_tmp/mcp-audit-20261020/report.md. The Operator expanded manual fallback permission. CA-C-525 through CA-C-527 now carry the three reviewed Problems; CA-C-528 records the separate current Concern-status authority gap found by unchanged authoring preflight. All four are Active investigations, not four proven current reproductions. Normal creation context and outer preview recovered; full-carrier validation still refused before effects. Manual source records, exact predecessor archives and actual provenance are retained; no MCP create execute was sent.
