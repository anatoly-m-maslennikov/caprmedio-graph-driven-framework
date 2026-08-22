---
subject_scopes:
  - scope-topology
version: 4
updated_at: 2026-08-20 02:25:18
relations:
  child_of:
    - CAPRMEDIO-P-020-CHANGE_PLAN--orchestrate-bootstrap-seed-migration
---
# Relocate approved folder structure

1. [x] Verify approved M002 snapshot SHA-256 `571b36de08cf03ac2f0a31f04f3a6fee97e3254033ece7dc062bb053d8c15b47` and source-frontier SHA-256 `3fc8547c30e1f094309f9a0fb74cc6ef3aabe95aea7fb938b23b2ec99592a9de`, and register only the P-020 Action-9 and P-016 transfer control delta.
2. [x] Create the exact pre-migration byte/path tar backup and rollback manifest under `.caprmedio_runtime/migrations/p020_action_10/`.
3. [x] Produce the deterministic source-to-destination folder map: 1,388 sources, 1,072 relocated or lifecycle-overlaid (including four Plan lifecycle overlays), 315 retained at their original addresses, and one retired empty EXTNS unit; preserve every carrier byte and legacy basename; reject collisions; and exclude `.f4f`.
4. [x] Apply the folder map transactionally, remove only the retired empty EXTNS Structural unit, and write durable result Map M003.
5. [x] Reconcile all 1,387 destination bytes and paths against the pre-migration digest, verify the one retired source absent, verify backup/manifest SHA-256 equality, verify no old Structural payload files, and verify `--apply` idempotency without running tests or broad validators.
6. [x] Have P-016 terminalize the transferred legacy Plans unchanged in `archive/`, record this Plan as `done`, and do not begin P020 Action 11 or later.
