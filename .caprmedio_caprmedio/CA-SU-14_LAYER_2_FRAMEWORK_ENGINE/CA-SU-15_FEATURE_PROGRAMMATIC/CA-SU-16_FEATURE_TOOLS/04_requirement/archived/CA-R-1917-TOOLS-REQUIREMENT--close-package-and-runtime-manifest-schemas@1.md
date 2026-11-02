---
atom_id: CA-R-1917
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Closed schemas"
  depends_on: [Tool, Manifest, Framework Package, Runtime, Project]
relations:
  relates_to: [CA-D-596, CA-D-598, CA-D-599, CA-D-600]
---
# Summary

Close package and runtime manifest schemas

## Scope

the fixed schemas for package, catalog, current selection and target activation.

## Claim

the INSTALL_TOOLS facade **must** reject every absent, additional or inconsistent manifest and selector field, and **must not** use an arbitrary JSON pass flag or implicit default as admission.

## Details

CA-D-596 through CA-D-604 declare each TOML schema, digest relation and filesystem location. Cross-carrier equality includes package manifest, source catalog, version bytes, Full Gate receipt, image digest, target context and state generation where applicable. A parser may report diagnostics, but no unsealed field gains authority.
