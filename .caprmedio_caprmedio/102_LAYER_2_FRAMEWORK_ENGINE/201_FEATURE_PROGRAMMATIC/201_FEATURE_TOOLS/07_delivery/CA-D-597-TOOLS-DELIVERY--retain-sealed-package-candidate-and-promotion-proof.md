---
atom_id: CA-D-597
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Sealed candidate and promotion proof"
  depends_on: [Tool, Framework Package, Manifest, Test Suite, Docker Image, Journal]
relations:
  delivery_for: [CA-R-1909, CA-R-1910, CA-M-360]
---
# Summary

Retain sealed package candidate and promotion proof

## Scope

One private candidate package and its exact suite, image and promotion evidence.

## Claim

the INSTALL_TOOLS facade **must** stage and seal every candidate beneath `.caprmedio_tmp/release_candidates/<run_id>/` **before** it may be promoted, and the promoted package **must** have the same manifest bytes as the tested image input.

## Details

The candidate root contains `package/`, `seal.toml`, `full-gate.toml`, `image-proof.toml` and `promotion.toml`. `seal.toml` binds run ID, package manifest SHA-256, source-catalog digest and ordered package rows. `full-gate.toml` names the existing closed Full Gate receipt and its exact package manifest digest; `image-proof.toml` names the immutable inspected image digest, complete-package/MCP canary receipt and the same manifest digest. Neither a Boolean JSON field, mutable tag, cached report nor a second package copy is gate evidence.

Promotion copies or atomically moves only the sealed package tree to the digest-named release directory, then reopens its exact `manifest.toml` and records source and destination tree digests in `promotion.toml`. A changed byte, mode, source catalog, image input or gate receipt refuses promotion and retains the candidate evidence.
