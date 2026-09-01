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
    - CA-M-185
---
# Verify create sealed caprmedio atom carriers

## Claim checked

CA-M-185 creates a sealed Atom set atomically only after complete validation and explicit apply authority.

## Applicable when

Apply to any ATOM_CREATE realization that can create one or more governed Atom carriers.

## Test case

Prepare a frozen two-Atom request with valid role placement and unique IDs, then introduce a collision into the second target. Observe dry-run and apply behavior for the invalid set; remove the collision and apply the unchanged valid set under a sealed Initiative.

## Acceptance criteria

Dry-run creates nothing; the colliding set creates neither Atom; the valid apply creates both first revisions exactly once with canonical filenames and complete metadata; no temporary or partial carrier remains.

## Failure disposition

Reject the realization and preserve the sealed request, collision evidence, dry-run, resulting directory state, and any partial-write residue.
