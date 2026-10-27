---
atom_id: CA-P-2531@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Release Version/Runtime Package Carrier
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2527
version: 5
updated_at: 2026-10-24 10:35:14 +0400
tier: 3
---
# Summary

Retire eligible stopped noncandidate Project containers

## Objective

Implement the accepted Project-only candidate-retention contract.

## Details

Own release_cleanup.py and test_release_cleanup.py only, including its shared DockerFixture. Remove only positively identified stopped selected-Project MCP containers using noncandidate images, even with matching fingerprint; exact candidate and other running containers remain protected. Inspect positive runtime classification before removal; no force/retry. Give fixture-created owned images explicit ownership metadata, not arbitrary inserted orphans. Synthetic tests only, at most15 minutes own work; split before extending.

### Accepted implementation evidence

Worker focused9/9 and related24/24 checks passed. Root integrated10-module gate102/102 passed16.084s. Stopped selected-Project noncandidate containers lose the fingerprint-only exemption, with positive image inspection before removal; exact candidate, running/foreign/unknown-state resources remain protected. Shared synthetic fixture assigns ownership only to deliberately created Project images, not raw orphans. Owned files pass pinned Ruff/diff checks. No Docker/release execution. Import/call removal completed before root removed unused identity helpers.

### Container placement reconciliation

Parent P2527 is now Done; this already-Done child moves with its matching container hierarchy. Carrier-only relocation advances Version/time and retains exact predecessor; status and accepted implementation are unchanged.
