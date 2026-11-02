---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Project.Settings.Temporary State
  depends_on:
  - Subject/Graph Node/Engineering/Temporary State
  - Subject/Graph Node/Domain/Continuant/Project.Settings
version: 18
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-R-1473@18
content_role: Requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
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
