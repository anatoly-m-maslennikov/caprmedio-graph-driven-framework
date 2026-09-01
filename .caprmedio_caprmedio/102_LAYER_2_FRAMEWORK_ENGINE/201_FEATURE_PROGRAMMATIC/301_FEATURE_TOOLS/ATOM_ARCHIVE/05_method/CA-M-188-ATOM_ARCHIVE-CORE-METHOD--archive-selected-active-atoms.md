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
    - CA-R-868
  derived_from:
    - CA-A-058
---
# Archive selected active Atoms

## Applicable when

Use this Method when a sealed Initiative withdraws current authority from selected active Atoms while preserving their historical carriers.

## Procedure

1. Resolve every target and prove that it is an active Atom in its owning Content role.
2. Derive the role-local archive destination while preserving filename, bytes, ID, revision history, and historical dependents.
3. Reject drafts, already archived carriers, non-Atoms, invalid archive locations, and destination collisions.
4. Freeze and present the archive map as a dry-run.
5. On explicit authorized apply, move the entire set atomically and remove it from current-authority discovery.
6. Verify archived presence, active absence, byte identity, and retained historical resolvability; roll back on any discrepancy.

## Outcome

Every selected Atom is preserved in its role-local archive and no longer contributes current authority.

## Failure or stop

Stop or roll back the full set when lifecycle, destination, collision, or postcondition checks fail.
