---
identity:
  atom_id: CA-M-422
  ref_id: CA-M-422@12
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage/Temporary
      State
    dependencies:
    - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage/Directory
      Layout
  tier: 3
relations:
  method_for:
  - CA-R-1473
state:
  status: Archived
  version: 12
  updated_at: 2026-11-09 07:45:15 +0400
current_scope_unit: PROGRAMMATIC
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a0263a-7510-7672-bce4-58830bc4d184
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
destination:
  file:
    name: CA-M-422@12-PROGRAMMATIC-DIRECT_POLICY--route-all-temporary-carriers-through-project-temp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/archive
---

## Summary

Route all temporary Carriers through project temp

## Claim

### Prose Claim

resolve the configured Project Temporary State root **before** a PROGRAMMATIC
component creates a temporary Carrier **or** invokes a dependency that can create
one. allocate a component-owned **and**, **when** concurrency is possible, run-specific
descendant below `.caprmedio_tmp/`. pass that descendant explicitly **to**
temporary-file APIs **and** configure dependency cache, temporary, staging, build,
**and** Evaluation paths **before** invocation. materialize shared development-tool
cache paths through the root `pyproject.toml`; provide explicit run-specific
paths through launch Carriers for dependencies that do **not** read that file.
do **not** rely on an ambient host
temporary directory **or** the process working directory.

route Python bytecode cache output **to** `.caprmedio_tmp/cache/python/` **before**
importing Project modules, **or** disable bytecode writes for an isolated process.
do **not** create `__pycache__/` **or** `.pyc` Carriers below `.caprmedio_runtime/`.

for an atomic replacement, create its staging Carrier below the Project
Temporary State root **and** verify that the staging **and** destination Carriers satisfy the
required same-filesystem atomicity boundary **before** the first mutation. stop
**without** falling back **to** a destination sibling **or** host temporary location **when**
that precondition is false.

attempt bounded cleanup **when** the owning operation ends. treat interrupted **or**
denied cleanup as retained non-authoritative temporary state, report its owned
path, **and** leave it confined below `.caprmedio_tmp/`. never weaken placement
because cleanup is best-effort.

keep executable releases, shared implementation libraries, registries, stable
launchers, Hook Carriers, runtime logs, sessions, databases, service state,
resumable state, **and** governed Artifacts outside the Temporary State root **in**
their applicable authority **or** runtime places.

## Details

Candidate source: [CA-M-289@9](archive/CA-M-289-PROGRAMMATIC-CORE-METHOD--route-all-temporary-carriers-through-project-temp@9.md)
