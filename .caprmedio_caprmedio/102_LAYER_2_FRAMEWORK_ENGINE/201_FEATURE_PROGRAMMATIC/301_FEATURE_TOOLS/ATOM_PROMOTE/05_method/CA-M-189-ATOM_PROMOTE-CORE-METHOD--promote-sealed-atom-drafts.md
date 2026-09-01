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
    - CA-R-869
  derived_from:
    - CA-A-058
---
# Promote sealed Atom drafts

## Applicable when

Use this Method when a sealed Initiative accepts selected draft Atoms as current authority and assigns their stable role-matching IDs.

## Procedure

1. Resolve every selected draft and bind it to the operator-supplied stable Atom ID.
2. Validate that the ID matches the Content role, is unused, and produces one canonical active filename and location.
3. Remove only the draft lifecycle carrier segment; preserve the accepted body and other governed bytes except required identity and revision metadata.
4. Freeze the promotion map and expose the complete result as a dry-run.
5. On explicit authorized apply, publish all active carriers and retire their draft carriers in one rollbackable transaction.
6. Verify unique active identity, absence from the draft surface, valid references, and complete set membership.

## Outcome

Each accepted draft becomes exactly one valid active Atom with its operator-assigned stable identity.

## Failure or stop

Stop or roll back on invalid or mismatched IDs, collisions, non-draft inputs, stale carriers, or incomplete promotion.
