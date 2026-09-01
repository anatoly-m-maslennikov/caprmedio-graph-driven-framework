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
    - CA-M-218
---
# Verify resolve github extension sources and installed state

## Claim checked

CA-M-218 resolves immutable GitHub Extension sources and applies exact rollbackable installed-version transitions with complete resulting-state reports.

## Applicable when

Apply whenever GitHub source resolution or Extension install, update, downgrade, or uninstall mechanics change.

## Test case

Resolve one Extension from a declared repository subdirectory first through an unresolved moving branch and then through an immutable revision with a verified manifest. Update an installed older version and compare resulting inventory to the exact source package.

## Acceptance criteria

The moving unresolved source is not installed; the immutable source resolves to the declared Extension and exact version; the update completes atomically; resulting source revision, version, files, digests, and verification match the package.

## Failure disposition

Reject the realization and preserve source declarations, revision resolution, manifests, transition plan, rollback state, and resulting installed inventory.
