---
atom_id: CA-M-359
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Package assembly"
  depends_on: [Tool, Framework Package, Manifest, Methodology, Extension]
relations:
  method_for: [CA-R-1902, CA-R-1908]
---
# Summary

Assemble and seal a reusable Framework package

## Scope

the deterministic package-construction procedure before candidate verification.

## Claim

the INSTALL_TOOLS facade **must** inventory, copy and reopen **=1** complete package from admitted rows **before** it may be sealed, and **must not** read undeclared checkout or host state.

## Details

1. Reopen the active Methodology source frontier, Core, declared support, defaults, `ca`, `102_FRAMEWORK_ENGINE/`, `pyproject.toml`, `uv.lock` and `version.toml`.
2. Require each selected catalog identity to have a revision, digest and admission receipt; retain optional/private entries as available only.
3. Copy ordered regular-file rows and modes into candidate `package/`, compute manifest, framework version and catalog digest, then reopen every row.
4. Refuse drift, symlink, secret-shaped or unlisted carriers; retain the failed candidate without publishing a package or target effect.
