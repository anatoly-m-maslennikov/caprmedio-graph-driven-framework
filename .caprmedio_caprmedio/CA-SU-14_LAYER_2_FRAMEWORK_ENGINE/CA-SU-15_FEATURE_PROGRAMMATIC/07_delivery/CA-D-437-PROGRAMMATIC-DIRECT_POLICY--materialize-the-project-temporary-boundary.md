---
identity:
  atom_id: CA-D-437
  ref_id: CA-D-437
context:
  container:
    scope_unit: CA-SU-15
  role: delivery
  form: direct_policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Storage <+ Directory Layout
    dependencies:
    - MODEL//CAPRMEDIO <+ Carrier
    - MODEL//CAPRMEDIO <+ Project.Settings
  tier: 4
relations:
  delivery_for:
  - CA-M-422
state:
  status: Active
  version: 24
  updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a0263a-7510-7672-bce4-58830bc4d184
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
destination:
  file:
    name: CA-D-437-PROGRAMMATIC-DIRECT_POLICY--materialize-the-project-temporary-boundary.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/07_delivery
---
## Summary

Materialize the Project temporary boundary

## Claim

### Prose Claim

the shared Project Temporary State path boundary **must** be carried **in**
canonical source under `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/` **and** the selected
`.caprmedio_runtime/tools/` release.

the root `pyproject.toml` carries the admitted development **and** Evaluation-tool
cache-path configuration. dependency launch Carriers carry explicit temporary,
staging, build, **and** cache-path parameters **when** that dependency does **not**
read `pyproject.toml`. those configured temporary Carriers occupy descendants
of `.caprmedio_tmp/`.

Python bytecode caches use `.caprmedio_tmp/cache/python/`; the corresponding
entrypoint, test-runner, **or** service-launcher Carrier stores that path **or** the
disabled-bytecode-write setting. the delivered Runtime State root **must not**
contain `__pycache__/` Directory Carriers **or** `.pyc` File Carriers.

temporary-path representations carry owner **and** run identity. the boundary
diagnostic representation carries the violating owner **and** path.

CA-M-422 owns temporary-path confinement, identity, cleanup, construction and configuration conventions.
