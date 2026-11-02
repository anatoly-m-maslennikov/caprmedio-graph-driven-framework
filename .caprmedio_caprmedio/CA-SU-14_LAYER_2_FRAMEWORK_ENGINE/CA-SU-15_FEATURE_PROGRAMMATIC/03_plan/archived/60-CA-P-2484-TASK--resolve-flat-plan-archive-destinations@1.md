---
atom_id: CA-P-2484
content_role: Plan
type: Plan
label: Task
work_sequence_number: 60
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-20T19:57:02.954Z"
---
# Summary

Resolve flat Plan archive destinations

## Objective

Use the existing Atom publication owner to resolve owning Scope Unit 03_plan/archived for newly archived Plan Markdown carriers and required new exact predecessor records.

## Details

At most 15 minutes own work; split before extending. CA-D-461@15, CA-E-502@13 and C539 govern. Review P2481 findings and wait for P2478 accepted frozen source. Own atom_operations.py and lifecycle_intents.py only. Reuse one existing-owner resolver, retain @Version suffixes and raw predecessor bytes, refuse destination collisions. Preserve non-Plan and non-Archived placement. No physical migration or rewriting old archive/ trees. Review the dependent bundle-safety Task before execution.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
