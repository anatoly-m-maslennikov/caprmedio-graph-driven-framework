---
atom_id: CA-M-360
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 16:57:27 +0400"
subjects:
  governs: "Framework Installation contribution/Package gating and promotion"
  depends_on: [Tool, Framework Package, Test Suite, Docker Image, Manifest]
relations:
  method_for: [CA-R-1909, CA-R-1910]
---
# Summary

Gate and promote the exact sealed package

## Scope

the candidate Full Gate, image proof and no-substitution promotion procedure.

## Claim

the INSTALL_TOOLS facade **must** run and reopen the existing Full Gate and immutable image proof on the same sealed package bytes **before** promotion, and **must not** promote a reconstructed or Boolean-approved package.

## Details

1. Require the closed Unit Gate evidence for the compiled candidate, then freeze candidate package manifest, catalog and version rows under the candidate root.
2. Build, immutable-ID inspect and canary the exact sealed tree; reopen immutable image, package, catalog and version bindings.
3. Run the exact three host-capable Candidate E2E harnesses against that immutable image, then aggregate Unit Gate, build, canary and E2E evidence into the existing Full Gate.
4. Copy or atomically move the unchanged gated tree to its digest release root; only then atomically publish `.caprmedio_install/current.toml` under the installation lock. No package or image is rebuilt after gate aggregation.

Any changed row, receipt, image or promotion destination blocks and preserves evidence.
