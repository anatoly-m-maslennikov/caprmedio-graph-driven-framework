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
status: Active
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 2
updated_at: "2026-10-20T20:33:21.511Z"
---
# Summary

Align Plan archive validation and predictions

## Objective

Make Plan archive validation and Subject-history predictions match the shared flat archive destination.

## Details

At most 15 minutes own work; split before extending. Depends on accepted P2484 resolver contract; review after P2485. Own check_structure_extended.py, atom_subject_patch.py and subject_batch_frontier.py plus their focused frozen fixture checks only. Validate Archived Plan Markdown directly under owning 03_plan/archived with matching Version suffix. Preserve legacy trees byte-for-byte; no migration, incoming-link repair or non-Archived hierarchy changes. Do not duplicate the publication owner placement rule or infer new policy.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Independent validator lane admission

P2485 history-bearing bundle execution is postponed for C549, not a reason to block the independently settled Archived Plan validator predicate. Activate only the source-bound validator/frozen-fixture lane now; Subject edits wait for P2490 canonical preservation API. Review D461@15, D289@13 and E502@13 as exact authority. The validator owns independent Evaluation enforcement under M316 and does not import effectful publication logic or redefine placement policy; this separate read-only source-bound check is the justified module boundary under M393. Special-case Archived Plans past the decomposition early return, enforce flat scope placement and Version suffix, and retain non-Archived/non-Plan behavior. Refresh exact D461/D289 pins/fixtures only after adapter reconciliation. No parser/address rule fork, live fixture load, legacy carrier migration, Scope Unit operation, runtime change or new policy. Final integrated acceptance remains P2487.
