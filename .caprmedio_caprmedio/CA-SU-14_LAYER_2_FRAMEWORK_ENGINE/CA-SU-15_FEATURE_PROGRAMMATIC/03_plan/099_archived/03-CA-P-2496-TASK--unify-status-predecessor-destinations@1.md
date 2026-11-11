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
status: Active
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2484]
version: 1
updated_at: "2026-10-20T21:02:38.428Z"
---
# Summary

Unify Status predecessor destinations

## Objective

Use one Status-publication history calculation for publisher, Draft-promotion prediction and recovery.

## Details

At most 15 minutes own work; split before extending. Independent P2493 code review found existing-marker prediction uses preserved_revision_destination, which intentionally differs from Status-publication history for non-Plan roles. Non-Plan promotion may expect archive/ while publisher wrote archived/; nested Plan non-Archive paths can likewise diverge. Own only atom_operations.py, preserve generic model-driven admission and all exact pins. Extract/reuse the actual shared Status-predecessor path calculation and use it for prediction, writes, postconditions and recovery; all Plan predecessors follow existing flat owning-scope preservation, while non-Plan established Status spelling remains unchanged. Add non-Plan marker-to-Active and nested Plan-to-Done functional regressions plus injected cleanup rollback proving no extra history remains. Independent test owner edits only test_flat_plan_archive.py. Review frozen next P2493 dependency before rerun. No new API, modes, scope migration, release or production tests.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
