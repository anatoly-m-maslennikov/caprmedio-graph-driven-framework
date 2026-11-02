---
atom_id: CA-D-564
content_role: Delivery
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-11 17:34:07 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Image carrier"
  depends_on: [Tool, Image, Container, Manifest, Journal, Runtime]
relations:
  delivery_for: [CA-R-1879, CA-R-1880, CA-M-333, CA-R-1890, CA-M-346]
---
# Summary

Bind candidate-image and safe-retirement evidence

## Scope

The actual Docker candidate-image proof between the closed Unit Gate and Candidate E2E Gate, and the post-success cleanup boundary for all verified superseded release-owned images of the current Project.

## Claim

After the closed Unit Gate passes for a retained N+1 candidate, Release Version **must** bind the candidate build to `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile`, record `candidate_image_digest`, `prior_image_digest`, and exact retaining container/rollback references in the candidateSnapshotManifest result, retain immutable candidate and prior image identities with actual execution evidence, and permit post-success removal of all verified superseded CAPRMEDIO release-owned image identities for the current Project only after the complete gate, verified N+1 installation/promotion and successful Project-MCP startup/smoke, with proof of no retaining container or required protected reference for each removal.

## Details

The Dockerfile path does not establish a built, runnable, or accepted image. A passing Unit Gate is the image-build prerequisite, not promotion authority. The current Docker surface retains a mutable local tag, so implementation must produce and return the bound immutable digest fields rather than treating the tag as promotion or retirement proof. The exact inspected `candidate_image_digest` must bind the later fixed candidate canary and all three CA-R-1890 Candidate E2E harnesses; their passing receipts plus the passing Unit receipt are the sole Full Gate promotion prerequisite. Cleanup evidence retains each exact immutable image identity, actual current-Project ownership proof reference, Docker inspection, retaining-container and protection references, and the actual removed, protected, in-use or unproven disposition. Ownership may be proven by existing actual Project release, build, launcher or start manifests with exact image ID and Project-root identity; observed Docker metadata must agree with that proof. Preserve the promoted candidate, unrelated and other-Project protected images; a tag prefix alone never proves ownership. A cleanup blocker does not authorize forced container deletion, automatic rollback or effect replay, and cannot be reported as all images removed. This Delivery forbids tag-only equivalence, broad prune, deletion before complete gating and successful installation/MCP smoke, and any claim that a build log or Unit-only result substitutes for actual candidate-image execution.
