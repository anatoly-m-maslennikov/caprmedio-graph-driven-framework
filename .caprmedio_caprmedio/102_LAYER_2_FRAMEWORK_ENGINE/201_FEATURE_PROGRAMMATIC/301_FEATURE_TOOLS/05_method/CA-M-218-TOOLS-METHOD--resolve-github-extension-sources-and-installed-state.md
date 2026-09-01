---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1151
    - CA-R-1152
  derived_from:
    - CA-A-058
---
# Resolve GitHub Extension sources and installed state

## Applicable when

Use this Method when resolving or changing an Extension whose declared distribution source is a GitHub repository or repository subdirectory.

## Procedure

1. Normalize the declared GitHub repository, optional subdirectory, immutable source revision, Extension identity, and exact package version.
2. Retrieve and verify the selected source manifest and digest without treating a moving branch name as an installed version.
3. Compare the verified source with the current installed-state inventory.
4. Plan the requested install, uninstall, update, or downgrade as an exact version transition with a complete file map and rollback state.
5. On authorization, apply the transition atomically and report the resulting Extension identity, source revision, version, files, and verification status.

## Outcome

The Project has an exact, attributable installed Extension state derived from a verified GitHub source boundary.

## Failure or stop

Stop or roll back on an ambiguous source, mutable unresolved revision, identity mismatch, missing manifest, digest failure, collision, or unverifiable resulting state.
