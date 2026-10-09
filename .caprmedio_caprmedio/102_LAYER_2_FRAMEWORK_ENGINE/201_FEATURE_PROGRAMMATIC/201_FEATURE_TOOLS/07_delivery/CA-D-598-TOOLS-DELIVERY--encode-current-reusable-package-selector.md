---
atom_id: CA-D-598
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Current package selector"
  depends_on: [Tool, Framework Package, Manifest, Docker Image, Test Suite]
relations:
  delivery_for: [CA-R-1903, CA-R-1909, CA-M-360]
---
# Summary

Encode the current reusable package selector

## Scope

The single installation-owned pointer to an admitted reusable package.

## Claim

the INSTALL_TOOLS facade **must** publish `.caprmedio_install/current.toml` **only after** reopening an admitted package, Full Gate and immutable-image proof, and **must** make the file the sole current-package selector.

## Details

The closed TOML keys are `schema_version = 1`, `package_manifest_sha256`, `release_relpath`, `framework_version`, `version_toml_sha256`, `source_catalog_sha256`, `full_gate_receipt_sha256` and `image_digest`. `release_relpath` is exactly `releases/<package_manifest_sha256>` relative to `.caprmedio_install`; all digest values are lowercase 64-hex and `image_digest` is immutable. Extra, missing or inconsistent keys reject rather than falling back to a checkout, tag or ambient package.

The selector is written atomically under CA-D-603's per-Project installation lock after the package tree, manifest rows, full-gate receipt and image proof are re-read. A target runtime selector may reference this package digest, but no target selector can make an unselected package current.
