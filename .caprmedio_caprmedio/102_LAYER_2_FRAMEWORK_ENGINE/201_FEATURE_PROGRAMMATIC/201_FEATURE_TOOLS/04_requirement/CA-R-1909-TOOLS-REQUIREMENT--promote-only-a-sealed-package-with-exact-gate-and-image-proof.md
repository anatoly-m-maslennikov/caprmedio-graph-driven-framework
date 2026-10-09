---
atom_id: CA-R-1909
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Candidate promotion"
  depends_on: [Tool, Framework Package, Test Suite, Docker Image, Manifest]
relations:
  relates_to: [CA-D-597, CA-D-598, CA-M-360]
---
# Summary

Promote only a sealed package with exact gate and image proof

## Scope

the private candidate-to-reusable-package promotion boundary.

## Claim

the INSTALL_TOOLS facade **must** promote **only** a candidate sealed beneath `.caprmedio_tmp/release_candidates/<run_id>/` after the existing Full Gate and image proof reopen against its identical package bytes.

## Details

The candidate seal, Full Gate receipt, immutable image inspection and canary all carry the same package manifest SHA-256, source catalog digest and sealed version carrier. Promotion verifies unchanged ordered rows and modes at the destination and then may update the sole `.caprmedio_install/current.toml`. Failed or uncertain proof retains candidate evidence and leaves current selection unchanged.
