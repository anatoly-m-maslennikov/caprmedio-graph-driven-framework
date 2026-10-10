---
atom_id: CA-E-602
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-10 10:17:20 +0400"
subjects:
  governs: "Framework Installation contribution/Package acceptance"
  depends_on: [Tool, Framework Package, Manifest, Methodology, Skill, Projection]
relations:
  evaluation_for: [CA-R-1902, CA-M-359, CA-D-596, CA-D-561, CA-D-562]
---
# Summary

Verify complete reusable package by exact manifest

## Scope

the package inventory, catalog, binding-projection and version-carrier acceptance fixture.

## Claim

the QA case **must** accept a package **only** when its exact manifest verifies Engine, dependencies, version, defaults, `ca`, Methodology catalog and support, and the complete sealed `binding-projection` role required by its frozen frontier, and **must not** accept partial or checkout-derived content.

## Details

The golden verifies paths, bytes, modes, `framework_version`, `version_toml_sha256`, catalog rows and no automatic optional/private selection. It injects missing/extra Engine rows, changed `pyproject.toml`, `uv.lock` or `version.toml`, unknown catalog revision, symlink and secret-shaped carriers; every case refuses before package selection or target state.

Binding fixtures use a generic nonempty `binding_atoms` frontier with more than one distinct Atom/Tool identity and an explicit empty-frontier package. The nonempty case proves exact one-to-one projection coverage, canonical projection metadata, inverse equality to the pinned raw bytes, original Atom ID/Version/path/SHA lineage, catalog/admission/manifest coverage and observed mode. Missing, extra, duplicated, reordered-to-select, copied-authority, metadata-altered, raw-source-stale, relation-digest-stale and unreferenced projections all refuse before image or package effect. The empty case is accepted only when the same sealed source selection contains no package-owned Tool binding; removing a required binding and claiming an empty frontier refuses.

A fresh differently named non-Git Project fixture proves that the selected verified package can supply discovery metadata for every retained binding projection without producer control sources or checkout fallback. Discovery alone does not start an Action, create a Run, write a Journal event or satisfy Operator authorization, and `binding-projection` members never enter Methodology, Extension or Configuration selection.
