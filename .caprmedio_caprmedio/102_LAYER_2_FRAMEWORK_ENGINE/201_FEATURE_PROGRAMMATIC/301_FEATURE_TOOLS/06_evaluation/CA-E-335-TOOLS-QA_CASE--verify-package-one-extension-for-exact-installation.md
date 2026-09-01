---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  evaluation_for:
    - CA-M-217
---
# Verify package one extension for exact installation

## Claim checked

CA-M-217 produces a reproducible exactly versioned Extension package whose clean installed state is fully inventoried.

## Applicable when

Apply whenever Extension packaging, manifest, versioning, or installation instructions change.

## Test case

Package the same sealed Extension candidate twice, compare manifests and package digests, then install one package into a clean compatible Project fixture and compare installed files and state to the manifest.

## Acceptance criteria

Both builds have identical identity, exact version, manifest, and package digest; clean installation succeeds without hidden external state; installed inventory matches the manifest exactly and reports compatibility and verification status.

## Failure disposition

Reject the package and preserve candidate frontier, both builds, manifests, digests, installation trace, and installed-state comparison.
