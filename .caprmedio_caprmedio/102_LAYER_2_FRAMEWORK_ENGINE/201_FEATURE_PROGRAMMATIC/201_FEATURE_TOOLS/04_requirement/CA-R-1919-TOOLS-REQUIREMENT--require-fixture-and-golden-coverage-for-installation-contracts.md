---
atom_id: CA-R-1919
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Contract acceptance"
  depends_on: [Tool, Framework Package, Runtime, Test Suite, Manifest]
relations:
  relates_to: [CA-D-608, CA-E-602, CA-E-609]
---
# Summary

Require fixture and golden coverage for installation contracts

## Scope

the regression evidence required before implementing the portable package and installation contribution.

## Claim

the INSTALL_TOOLS facade **must** have exact fixture and golden coverage for package, target, concurrency, migration and refusal contracts, and **must not** treat unit-only or synthetic evidence as complete acceptance.

## Details

Coverage includes exact manifests and selectors, non-git, two Projects in one repository, relocation, unknown catalog revision, unchanged package execution, existing Full Gate/image identity, concurrent publication, legacy copy/verify/switch, unsafe quiescence and separately approved cleanup. Goldens assert carrier bytes and refusal preservation.
