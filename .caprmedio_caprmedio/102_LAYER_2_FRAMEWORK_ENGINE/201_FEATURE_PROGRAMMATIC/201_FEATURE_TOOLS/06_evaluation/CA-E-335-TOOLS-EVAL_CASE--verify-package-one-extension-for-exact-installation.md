---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Carrier
version: 27
updated_at: 2026-10-27 19:59:33 +0400
relations:
  evaluation_for:
  - CA-R-1150
  - CA-O-044
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-335
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
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
