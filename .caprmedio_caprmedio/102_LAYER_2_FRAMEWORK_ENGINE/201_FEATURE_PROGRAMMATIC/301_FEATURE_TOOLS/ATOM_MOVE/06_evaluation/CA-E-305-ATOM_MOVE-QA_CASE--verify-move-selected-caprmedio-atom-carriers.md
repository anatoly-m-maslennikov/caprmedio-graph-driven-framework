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
    - CA-M-187
---
# Verify move selected caprmedio atom carriers

## Claim checked

CA-M-187 relocates the complete sealed target set while preserving every carrier byte, filename, and Atom ID.

## Applicable when

Apply to any ATOM_MOVE realization that can move individual carriers or recursive subtrees.

## Test case

Select a two-level subtree with three Atom carriers and one non-Atom file. Preview a shape-preserving move into a valid Scope Unit, introduce a destination collision, observe apply, then remove the collision and apply the unchanged move map.

## Acceptance criteria

The collision attempt moves nothing; the valid attempt moves all three Atoms to the mapped subtree, excludes the non-Atom, removes all source carriers, and preserves each filename, ID, and digest.

## Failure disposition

Reject the realization and preserve source and destination maps, collision evidence, before-and-after digests, and any incomplete move state.
