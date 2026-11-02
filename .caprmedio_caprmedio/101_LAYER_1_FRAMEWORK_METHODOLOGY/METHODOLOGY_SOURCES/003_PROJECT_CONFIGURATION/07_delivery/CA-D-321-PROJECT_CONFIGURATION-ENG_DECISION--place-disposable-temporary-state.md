---
subjects:
  active: Carrier/Directory
  passive: []
version: 21
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-321
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Place Disposable Temporary State

## Claim scope

disposable temporary state in a CAPRMEDIO Project.

## Claim

the CAPRMEDIO Project **must** place disposable scratch, staging, test cache, atomic-write intermediate, build intermediate, **and** interrupted-cleanup Carriers under `.caprmedio_tmp/`.

## Details

deleting `.caprmedio_tmp/` **must not** delete governed authority, Project Journal history, installed Framework Engine releases, runtime logs, sessions, databases, service state, **or** resumable state.
