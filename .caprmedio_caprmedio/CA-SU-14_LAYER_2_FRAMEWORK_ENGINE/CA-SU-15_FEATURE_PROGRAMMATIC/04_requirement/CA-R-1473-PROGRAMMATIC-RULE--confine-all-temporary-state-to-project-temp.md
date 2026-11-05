---
atom_id: CA-R-1473
ref_id: CA-R-1473
container:
  scope_unit: CA-SU-15
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings.Temporary State
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
tier: 1
status: Active
version: 20
updated_at: 2026-10-27 19:59:55 +0400
carrier_destination:
  file:
    name: CA-R-1473-PROGRAMMATIC-RULE--confine-all-temporary-state-to-project-temp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Confine all temporary state to project temp

## Scope

## Claim

**every** temporary File **or** Directory Carrier created by a CAPRMEDIO-controlled
PROGRAMMATIC execution **must** be located below the configured Project
Temporary State root `.caprmedio_tmp/`. This obligation applies **to** Tools, App backend
services, MCP components, their tests **and** Evaluations, their launchers, **and**
dependencies whose execution they configure. It includes temporary, scratch,
staging, cache, intermediate build **or** Evaluation, **and** interrupted-cleanup
Carriers.
Python bytecode caches, including **every** `__pycache__/` Directory Carrier **and**
`.pyc` File Carrier, are temporary cache state under this obligation.

A PROGRAMMATIC component **must not** use the repository root, the process
working directory, a source **or** Delivery Carrier, the Project control root,
`.caprmedio_runtime/`, **or** a host temporary root as a fallback. If the Project
Temporary State root is unavailable, an invoked dependency cannot be redirected,
**or** a required same-filesystem atomicity precondition cannot be satisfied, the
component **must** stop **before** the affected effect **and** report the boundary
failure with one stable diagnostic identifying its creating owner **and**
violating path.

retained temporary paths **must** preserve their owner **and** run identity.
temporary confinement **must** remain correct **when** bounded cleanup is interrupted
**or** denied; cleanup completion is **not** a prerequisite for confinement.

Temporary state **must not** become authority **or** installed implementation.
Deleting `.caprmedio_tmp/` **may** discard caches, diagnostics, disposable
workspaces, **or** interrupted-cleanup remnants, but **must not** discard a governed
Artifact, Project Journal history, an installed release, **or** resumable runtime
progress.

## Details
