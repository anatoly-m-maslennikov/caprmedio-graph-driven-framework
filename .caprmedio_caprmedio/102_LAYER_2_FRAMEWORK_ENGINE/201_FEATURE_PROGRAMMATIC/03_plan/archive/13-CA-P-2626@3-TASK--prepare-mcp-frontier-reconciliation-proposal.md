---
atom_id: CA-P-2626@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 13
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
version: 3
updated_at: 2026-10-24 06:04:43 +0400
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2613
  depends_on:
  - CA-P-2625
  - CA-C-584
  relates_to:
  - CA-O-016
  - CA-O-127
  - CA-R-1847
  - CA-E-567
  - CA-C-576
tier: 3
---
# Summary

Prepare the MCP frontier reconciliation proposal

## Objective

Prepare a bounded read-only proposal for reconciling the public MCP's exact 15-operation contract with the Project/code optional move_atom extension after CA-P-2625's fresh inventory. Keep source authority and the visible binding unchanged.

## Details

This is one Task with at most 15 minutes of own work. Review the inventory against R1847@16, E567@7 and O127, preserving the distinction between a source contract, a Project configuration and an implementation frontier. State whether the next action is a source decision, a compatible adapter change or a candidate-only update; do not choose silently. Do not edit RMED, manifests, selected bindings, A1142, projections or runtime code. No live MCP, publication, runtime admission, release, deployment, replay or full-suite run.

## Definition of Done

Return a compact proposal with explicit accepted, rejected and unresolved operation differences and the exact owner of any next change. Do not resolve CA-C-584, rename the 15-operation source contract, add move_atom to the source, or unblock CA-P-2620/CA-P-2621 from proposal evidence alone.

### C584 candidate-direction checkpoint — 23 October 2026

The corrective direction is explicit for the detached candidate: omit optional
move_atom, preserve the optional implementation capability, and keep O127's
internal Move distinct from public MCP admission. The live Project manifest's
16-operation surface remains untouched until a later validated publication
decision. CA-C-584 stays Active until that correction is validated; this
proposal does not retire Move, repair the live manifest or claim publication
or runtime admission.
