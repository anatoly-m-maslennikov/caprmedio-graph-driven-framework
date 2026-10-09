---
atom_id: CA-E-602
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Package acceptance"
  depends_on: [Tool, Framework Package, Manifest, Methodology, Skill]
relations:
  evaluation_for: [CA-R-1902, CA-M-359, CA-D-596]
---
# Summary

Verify complete reusable package by exact manifest

## Scope

the package inventory, catalog and version-carrier acceptance fixture.

## Claim

the QA case **must** accept a package **only** when its exact manifest verifies Engine, dependencies, version, defaults, `ca`, Methodology catalog and support, and **must not** accept partial or checkout-derived content.

## Details

The golden verifies paths, bytes, modes, `framework_version`, `version_toml_sha256`, catalog rows and no automatic optional/private selection. It injects missing/extra Engine rows, changed `pyproject.toml`, `uv.lock` or `version.toml`, unknown catalog revision, symlink and secret-shaped carriers; every case refuses before package selection or target state.
