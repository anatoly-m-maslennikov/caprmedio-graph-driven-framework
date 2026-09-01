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
    - CA-M-188
---
# Verify archive selected active atoms

## Claim checked

CA-M-188 removes selected Atoms from current authority while preserving byte-identical historical carriers and resolvability.

## Applicable when

Apply to any ATOM_ARCHIVE realization before it can perform active-to-archive lifecycle transitions.

## Test case

Select two related active Atoms and one draft. Preview one bulk archive request containing all three, observe rejection, then archive only the two active Atoms and inspect active discovery, archive discovery, bytes, and historical references.

## Acceptance criteria

The mixed-lifecycle request changes nothing; the valid request places both active Atoms in role-local archives with identical filenames, IDs, versions, and bytes; current discovery excludes them; historical resolution still finds them.

## Failure disposition

Reject the realization and preserve lifecycle classifications, archive map, current-authority result, digest comparison, and reference-resolution evidence.
