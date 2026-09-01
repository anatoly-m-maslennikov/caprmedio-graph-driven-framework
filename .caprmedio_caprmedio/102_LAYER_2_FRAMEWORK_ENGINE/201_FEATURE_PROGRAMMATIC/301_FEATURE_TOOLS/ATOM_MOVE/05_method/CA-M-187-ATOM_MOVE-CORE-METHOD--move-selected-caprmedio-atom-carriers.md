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
    - CA-R-867
  derived_from:
    - CA-A-058
---
# Move selected CAPRMEDIO Atom carriers

## Applicable when

Use this Method when a sealed Initiative authorizes relocation of selected Atom carriers without changing their governed content or identity.

## Procedure

1. Resolve exact targets or a recursive subtree and capture every source path, digest, and destination mapping.
2. Preserve the subtree shape by default; flatten only when the Initiative explicitly requests it.
3. Validate destination Scope Unit and Content role placement, path uniqueness, and collision freedom without editing carrier bytes.
4. Freeze the move map and expose it as a dry-run.
5. On explicit authorized apply, recheck the source digests and move the complete set as one rollbackable transaction.
6. Verify that each source is absent, each destination is present, and every moved carrier retains its original bytes, filename, and Atom ID.

## Outcome

The selected carriers occupy exactly their approved destinations and remain byte-identical governed Atoms.

## Failure or stop

Stop or roll back the full move on an invalid destination, collision, stale source, incomplete mapping, or failed post-move verification.
