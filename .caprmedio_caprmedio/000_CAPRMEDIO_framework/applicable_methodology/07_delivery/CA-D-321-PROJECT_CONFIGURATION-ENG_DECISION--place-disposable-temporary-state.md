---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/Directory
version: 22
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
atom_id: CA-D-321
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-321-PROJECT_CONFIGURATION-ENG_DECISION--place-disposable-temporary-state.md
  source_atom_id: CA-D-321
  source_atom_revision: 22
  source_sha256: 3dd08897bb2910aff7b9cc258d918f50545b51a04e8047bffdfa12633880ddc5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Place Disposable Temporary State

## Claim

### Prose Claim


disposable temporary state in a CAPRMEDIO Project.


the CAPRMEDIO Project **must** place disposable scratch, staging, test cache, atomic-write intermediate, build intermediate, **and** interrupted-cleanup Carriers under `.caprmedio_tmp/`.

## Details

deleting `.caprmedio_tmp/` **must not** delete governed authority, Project Journal history, installed Framework Engine releases, runtime logs, sessions, databases, service state, **or** resumable state.
