---
atom_id: CA-P-2526@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 83
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 4
updated_at: 2026-10-24 06:04:46 +0400
tier: 3
---
# Summary

Align post-green Local release image retention

## Objective

Align post-green Local release image retention.

## Details

Record the new Operator policy before implementation: after a green full suite, normal Local release names its image and retains only the last rebuild of the current version. Bind that image to the exact admitted candidate SHA and package version, not a moving tag or host clock. Use the Operator-selected Project-only cleanup scope. Preserve all container references, exact non-force removal and truthful pending results. Align applicable R1878, O164/O169/O178, M332/E573/D564 at their current tiers, preserving exact predecessors. O179 is not an additional registered release Step. At most 15 minutes own work; split before extending. No actual release or cleanup is authorized by this implementation task.

### Accepted source checkpoint

The Operator selected Project-only retention. Aligned R1878@6, M332@9, E573@3, D564@5 and O164@19/O169@10/O178@6/O179@3 at their existing tiers, preserving exact predecessors. Candidate-only means immutable identity, including same-fingerprint rebuilds; image ownership needs complete Project/root/control labels, not container linkage. All references and other Projects remain protected. C563 is Resolved. Source alignment is complete; implementation and isolated acceptance remain P2527/P2529, not runtime activation.
