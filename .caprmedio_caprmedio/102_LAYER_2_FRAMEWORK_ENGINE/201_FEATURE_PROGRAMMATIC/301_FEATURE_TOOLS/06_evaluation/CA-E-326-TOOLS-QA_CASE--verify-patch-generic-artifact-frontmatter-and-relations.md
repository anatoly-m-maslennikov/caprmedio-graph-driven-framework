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
    - CA-M-208
---
# Verify patch generic artifact frontmatter and relations

## Claim checked

CA-M-208 applies only schema-valid metadata and direct-relation patches while preserving body, identity, and atomicity.

## Applicable when

Apply whenever generic frontmatter or relation patch mechanics or schemas change.

## Test case

Seal one Artifact with known body bytes. Request one valid field change and relation addition together with an invalid endpoint that violates relation direction; observe apply, then remove the invalid operation and apply the sealed valid patch.

## Acceptance criteria

The invalid patch changes nothing; the valid patch changes only declared frontmatter, stores the canonical direct relation, advances revision once, and preserves body bytes, path, filename, and identity.

## Failure disposition

Reject the realization and preserve schema, relation policy, patch operations, endpoint evidence, exact diff, revision, and body digest.
