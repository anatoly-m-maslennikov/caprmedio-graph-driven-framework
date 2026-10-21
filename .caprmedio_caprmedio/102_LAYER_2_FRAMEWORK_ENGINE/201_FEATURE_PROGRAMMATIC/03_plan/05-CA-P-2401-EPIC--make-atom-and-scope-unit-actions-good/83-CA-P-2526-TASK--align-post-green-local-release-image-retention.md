---
atom_id: CA-P-2526
content_role: Plan
type: Plan
label: Task
work_sequence_number: 83
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 2
updated_at: "2026-10-21T10:13:48Z"
---
# Summary

Align post-green Local release image retention

## Objective

Align post-green Local release image retention.

## Details

Record the new Operator policy before implementation: after a green full suite, normal Local release names its image and retains only the last rebuild of the current version. Bind that image to the exact admitted candidate SHA and package version, not a moving tag or host clock. Resolve host-wide versus selected-Project cleanup scope before deletion behavior. Preserve all container references, exact non-force removal and truthful pending results. Align applicable R1878, O164/O169/O178, M332/E573/D564 at their current tiers, preserving exact predecessors. O179 is not an additional registered release Step. At most 15 minutes own work; split before extending. No actual release or cleanup is authorized by this implementation task.

### Current reviewed checkpoint

Confirmed policy: keep only the current release's last rebuild, bound to the exact admitted immutable candidate and package version. Host-wide unused CAPRMEDIO versus selected-Project cleanup remains unanswered in C563; active R/M/E/D/O policy changes and scope-sensitive deletion code are held. Existing naming is already after green tests. No release execution is inferred.
