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
    - CA-R-865
  derived_from:
    - CA-A-058
---
# Create sealed CAPRMEDIO Atom carriers

## Applicable when

Use this Method when a sealed Initiative authorizes creation of one Atom or one frozen bulk set of Atoms.

## Procedure

1. Normalize each request into a target directory, canonical filename, complete frontmatter, and Markdown body.
2. Validate Content role placement, filename grammar, required metadata, relations, and the initial revision before touching the filesystem.
3. Reject any path, filename, or Atom-ID collision across both existing authority and the requested set.
4. Freeze the target set and produce a complete dry-run showing every carrier and validation result.
5. On explicit authorized apply, write all carriers through temporary files and publish them as one atomic transaction.
6. If any publish step fails, remove unpublished temporary files and restore the pre-action state.

## Outcome

The requested Atom set is either fully absent or fully present as valid first revisions with no partial creation.

## Failure or stop

Remain in dry-run mode unless apply authority is explicit. Stop on an unsealed Initiative, invalid carrier, collision, changed target set, or failed atomic publish.
