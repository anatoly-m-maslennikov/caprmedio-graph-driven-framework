---
atom_id: CA-R-1902
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Reusable package completeness"
  depends_on: [Tool, Framework Package, Manifest, Methodology, Skill, Extension]
relations:
  relates_to: [CA-D-596, CA-D-602]
---
# Summary

Require a complete reusable Framework package

## Scope

the package content reusable by isolated target-Project installations.

## Claim

the INSTALL_TOOLS facade **must** admit **=1** package containing the complete Engine, exact dependency and version carriers, admitted defaults, `ca`, active Methodology source catalog and declared support **before** installation.

## Details

The complete Engine is the whole `102_FRAMEWORK_ENGINE/` package row set, not a selected runtime subset. `pyproject.toml`, `uv.lock` and `version.toml` are sealed rows; the manifest binds both `framework_version` and `version_toml_sha256`. Core is required; optional available extensions and configuration are catalogued with immutable admission but are **not** autoloaded, including private entries. Missing, extra, checkout-derived, secret-shaped, mutable or mode-mismatched members refuse admission.
