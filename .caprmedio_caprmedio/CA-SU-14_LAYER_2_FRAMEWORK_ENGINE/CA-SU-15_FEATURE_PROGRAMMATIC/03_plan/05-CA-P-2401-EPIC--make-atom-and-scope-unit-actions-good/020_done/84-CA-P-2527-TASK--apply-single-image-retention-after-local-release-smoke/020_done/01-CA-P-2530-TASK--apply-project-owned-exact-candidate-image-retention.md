---
atom_id: CA-P-2530
ref_id: CA-P-2530
container:
  atom: CA-P-2527
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Release Version/Runtime Package Carrier
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2527
status: Done
version: 6
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 1-CA-P-2530-TASK--apply-project-owned-exact-candidate-image-retention.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/84-CA-P-2527-TASK--apply-single-image-retention-after-local-release-smoke/done
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
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
