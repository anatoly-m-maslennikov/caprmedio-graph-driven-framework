---
atom_id: CA-P-2486
content_role: Plan
type: Plan
label: Task
work_sequence_number: 62
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
updated_at: "2026-10-20T19:57:02.964Z"
---
# Summary

Align Plan archive validation and predictions

## Objective

Make Plan archive validation and Subject-history predictions match the shared flat archive destination.

## Details

At most 15 minutes own work; split before extending. Depends on accepted P2484 resolver contract; review after P2485. Own check_structure_extended.py, atom_subject_patch.py and subject_batch_frontier.py plus their focused frozen fixture checks only. Validate Archived Plan Markdown directly under owning 03_plan/archived with matching Version suffix. Preserve legacy trees byte-for-byte; no migration, incoming-link repair or non-Archived hierarchy changes. Do not duplicate the publication owner placement rule or infer new policy.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
