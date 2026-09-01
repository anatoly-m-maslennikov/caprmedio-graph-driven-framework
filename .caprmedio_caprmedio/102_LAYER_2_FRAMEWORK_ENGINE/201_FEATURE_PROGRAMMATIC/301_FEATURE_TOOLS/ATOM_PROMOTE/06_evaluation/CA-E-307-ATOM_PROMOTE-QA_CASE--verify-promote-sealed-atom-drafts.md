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
    - CA-M-189
---
# Verify promote sealed atom drafts

## Claim checked

CA-M-189 promotes each accepted draft to exactly one valid active Atom with the assigned stable role-matching ID.

## Applicable when

Apply to any ATOM_PROMOTE realization before it can admit draft authority into the active graph.

## Test case

Prepare two valid drafts and assign one valid ID plus one ID whose role token conflicts with its draft. Observe the mixed-set apply, then correct the ID and apply the same frozen pair.

## Acceptance criteria

The mismatched set promotes neither draft; the corrected set creates exactly two canonical active carriers, removes both draft carriers, preserves accepted bodies, assigns unique stable IDs, and leaves all references valid.

## Failure disposition

Reject the realization and preserve draft identities, assigned IDs, promotion map, final lifecycle locations, and any duplicate or partial active identity.
