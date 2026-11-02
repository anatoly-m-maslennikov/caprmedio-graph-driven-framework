---
atom_id: CA-R-1903
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Package and runtime selection"
  depends_on: [Tool, Framework Package, Runtime, Project, Manifest]
relations:
  relates_to: [CA-D-596, CA-D-598, CA-D-599]
---
# Summary

Separate package selection from target runtime selection

## Scope

the relationship between reusable package storage and one target runtime activation.

## Claim

the INSTALL_TOOLS facade **must** select a verified package at `.caprmedio_install/current.toml` and a target runtime at `.caprmedio_runtime/installation/current.toml` as distinct carriers, and **must not** create a second package selector.

## Details

The release directory is `.caprmedio_install/releases/<package_manifest_sha256>/`; the package selector is installation-owned and does not activate any target. The target selector binds its selected package digest, target context and state generation. Both reject checkout fallbacks, digest drift and extra fields. An existing admitted package selector may precede a first runtime installation.
