---
atom_id: CA-P-2530
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
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
  is_decomposition_of: [CA-P-2527]
version: 1
updated_at: "2026-10-21T10:42:00Z"
---
# Summary

Apply Project-owned exact-candidate image retention

## Objective

Implement the accepted Project-only candidate-retention contract.

## Details

Own release_cleanup_images.py and test_release_image_ownership.py only. After verified candidate smoke, preserve exact candidate and all references; require complete matching Project/root/control image ownership and positive runtime classification. Remove eligible other digests even with matching fingerprint. Unknown/foreign resources remain protected with truthful reporting. Synthetic Docker tests only; no Docker, release, Atom or Git writes. At most15 minutes own work; split before extending.
