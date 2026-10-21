---
atom_id: CA-P-2496
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
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2484]
version: 2
updated_at: "2026-10-20T21:12:44.538Z"
---
# Summary

Unify Status predecessor destinations

## Objective

Use one Status-publication history calculation for publisher, Draft-promotion prediction and recovery.

## Details

At most 15 minutes own work; split before extending. Independent P2493 code review found existing-marker prediction uses preserved_revision_destination, which intentionally differs from Status-publication history for non-Plan roles. Non-Plan promotion may expect archive/ while publisher wrote archived/; nested Plan non-Archive paths can likewise diverge. Own only atom_operations.py, preserve generic model-driven admission and all exact pins. Extract/reuse the actual shared Status-predecessor path calculation and use it for prediction, writes, postconditions and recovery; all Plan predecessors follow existing flat owning-scope preservation, while non-Plan established Status spelling remains unchanged. Add non-Plan marker-to-Active and nested Plan-to-Done functional regressions plus injected cleanup rollback proving no extra history remains. Independent test owner edits only test_flat_plan_archive.py. Review frozen next P2493 dependency before rerun. No new API, modes, scope migration, release or production tests.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Verified completion

One private _status_predecessor_destination now drives existing-marker prediction and publisher writes/recovery. All Plan predecessors use the owning flat archive; non-Plan Status spelling remains unchanged. Independent code review APPROVE and final native71 passed, including non-Plan markerActive, nested Plan markerDone and injected cleanup-failure full-frontier restoration. Production/test hashes 537863a8261c38cf560098949d44a057b0fa7b95cf203c6b6b0a123ca5245284 and d31a8c68673f8a71cad59e41060d91d7739fb3fcbdd6b7b2c372daac6c04c29e were identical before/after. C901 count12 remains baseline; publisher complexity improved29 to28. No new API, mode, deployment or replay.
