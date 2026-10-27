---
atom_id: CA-P-2530@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2527
version: 4
updated_at: 2026-10-24 06:04:46 +0400
tier: 3
---
# Summary

Apply Project-owned exact-candidate image retention

## Objective

Implement the accepted Project-only candidate-retention contract.

## Details

Own release_cleanup_images.py and test_release_image_ownership.py only. After verified candidate smoke, preserve exact candidate and all references; require complete matching Project/root/control image ownership and positive runtime classification. Remove eligible other digests even with matching fingerprint. Unknown/foreign resources remain protected with truthful reporting. Synthetic Docker tests only; no Docker, release, Atom or Git writes. At most15 minutes own work; split before extending.

### Accepted implementation evidence

Worker ownership7/7, sharedcleanup9/9 and localcleanup8/8 checks passed. Root integrated10-module gate102/102 passed16.084s, including strict launcher and canonical metadata. Exact candidate protection, complete ownership, same-fingerprint noncandidate eligibility, all-container references and unknown/foreign ownership are covered. Pinned Ruff and diff check pass in owned files. No Docker/release execution. Parent P2527 integration is frozen for independent P2529 acceptance.

### Container placement reconciliation

Parent P2527 is now Done; this already-Done child moves with its matching container hierarchy. Carrier-only relocation advances Version/time and retains exact predecessor; status and accepted implementation are unchanged.
