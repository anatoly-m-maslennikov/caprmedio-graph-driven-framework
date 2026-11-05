---
atom_id: CA-E-335
ref_id: CA-E-335
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Carrier
tier: 2
relations:
  evaluation_for:
  - CA-R-1150
  - CA-O-044
status: Active
version: 27
updated_at: 2026-10-27 19:59:33 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Verify package one extension for exact installation

## Claim checked

CA-O-044 produces a reproducible exactly versioned Extension package whose manifest exactly accounts for its package contents.

## Applicable when

apply whenever Extension packaging, manifest, versioning, **or** package-content derivation changes.

## Test case

package the same sealed Extension candidate twice, compare manifests **and** package digests, **then** compare **every** package inventory with its manifest **without** performing an installed-state operation.

## Acceptance criteria

both builds have identical identity, exact version, manifest, **and** package digest; **every** package inventory matches its manifest exactly. installation, uninstallation, update, downgrade, **and** installed-state verification are delegated **to** CA-O-042.

## Failure disposition

reject the package **and** preserve candidate frontier, both builds, manifests, digests, package inventories, manifest comparisons, **and** delegation boundary.
