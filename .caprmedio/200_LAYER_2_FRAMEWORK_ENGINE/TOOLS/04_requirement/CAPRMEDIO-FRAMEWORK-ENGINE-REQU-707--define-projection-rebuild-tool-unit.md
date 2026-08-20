---
subject_scopes:
  - feature-boundary
version: 1
updated_at: 2026-08-20 05:18:05
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-702--define-tools-feature-scope
  relates_to:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-542--rebuild-one-programmatic-projection
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-543--validate-projection-currentness
---
# Define the PROJECTION_REBUILD Tool unit

`PROJECTION_REBUILD` must be one Doer Tool owned immediately by `TOOLS` as an `unordered_unit` at Structural level `3`, addressed by `FRAMEWORK_ENGINE/TOOLS/PROJECTION_REBUILD`, and realized under `02_FR_ENGN/TOOLS/PROJECTION_REBUILD/`; it derives the complete affected Projection set from changed source frontiers, orders rebuilds by declared dependencies, previews every output effect, materializes only explicitly approved outputs, and verifies currentness and idempotence after publication.
