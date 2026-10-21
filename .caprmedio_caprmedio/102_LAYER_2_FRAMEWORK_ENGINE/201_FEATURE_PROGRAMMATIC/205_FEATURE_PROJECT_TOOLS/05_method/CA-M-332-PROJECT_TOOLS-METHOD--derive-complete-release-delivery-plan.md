---
atom_id: CA-M-332
content_role: Method
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 10
updated_at: "2026-10-21T16:26:28Z"
subjects:
  governs: "Tool/RELEASE_VERSION/Direct delivery"
  depends_on: [Tool, Methodology, Runtime, Skill, Image]
relations:
  method_for: [CA-R-1877, CA-R-1878]
---
# Summary

Deliver one selected release directly

## Scope

The direct Local release path from active Methodology source through compilation, package installation, runtime/Skill verification, and Docker/MCP smoke.

## Claim

The Tool copies the selected active source, compiles it, prepares the package, installs the selected project runtime and `ca` Skill, and runs the intended Docker/MCP smoke checks. It stops and reports a failed step; it does not seal a candidate, aggregate a gate, or recover a prior attempt.

## Details

As the first Local release step, commit all tracked changes and untracked nonignored files allowed by existing file-safety exclusions, then verify a clean worktree and index. Preserve ignored files and environment-file exclusions; excluded nonignored dirty files stop release rather than being committed or waived. A clean repository is a no-op; commit failure or residual tracked/nonignored untracked changes stop before tests, image preparation/build or Docker work. Before each later Local release step and at completion, inspect Git state and verify cleanliness after its checkpoint. Preserve the project's runtime configuration and do not modify authoritative sources during delivery. Enumerate accumulated Project-owned release containers and images, proving exact ownership and noncandidate immutable identity rather than inferring them from tags or version age. Remove eligible stopped obsolete containers before MCP startup; after successful installation and smoke, repeat and remove obsolete images unused by any container or protected reference. Preserve the exact admitted candidate, running containers outside the existing exact-prior MCP replacement path, unrelated resources and targets with unknown ownership/code identity. Retain and report unproven orphans and cleanup failures; never force-delete or prune globally.

For fresh local-release image builds, attach and inspect exact Project ownership, canonical Project name and full owning-repository build-time Git HEAD commit labels under CA-D-562; refuse fresh preparation when name or HEAD is unavailable or invalid. Keep existing cache reuse without a metadata-only rebuild or a new ownership claim for reused images. Use matching inspected exact ownership labels to identify eligible labelled orphans; preserve legacy unlabelled or unproven images. Name and HEAD are provenance only, not cleanup ownership gates: use inspected complete Project ownership and exact immutable identity for retirement. Fingerprints validate runtime classification and source correspondence, not an extra retention slot for another rebuild.

Prepare canonical version/build-date/digest naming after the complete discovered suite passes on the default route or the explicitly selected focused scope passes on the focused route, reusing ImageManager. Bind retention to that release's exact candidate, not host-clock ordering. Before startup, the existing exact-prior MCP replacement path may replace a positively identified selected-Project container whose image differs from the candidate even when fingerprints match; accumulated cleanup never stops other running containers. After exact candidate launch and smoke verification, inspect selected-Project runtime images and all container references, removing eligible noncandidate digests individually without force. Preserve other Projects' images and unknown ownership even when a selected-Project container formerly referenced them. Retained references or failed inspection/removal remain visible as pending cleanup.

When the Operator explicitly supplies one or more repeatable `--test-module` paths to the Local host command, select only those discovered repository-relative source test modules, including Docker modules when selected; the existing shared image and launcher handling remains in force. Reject an empty selection, duplicates, malformed or foreign paths, and symlink modules before test execution. A selected-module failure or required skip stops downstream Local delivery before installation, image cleanup or MCP startup. Omitting `--test-module` retains the complete discovered suite as the Local default. This focused route is an explicit validation scope, not a full-suite claim and never satisfies the separate Public Full Gate; public release remains bound to its current public Full Gate.
