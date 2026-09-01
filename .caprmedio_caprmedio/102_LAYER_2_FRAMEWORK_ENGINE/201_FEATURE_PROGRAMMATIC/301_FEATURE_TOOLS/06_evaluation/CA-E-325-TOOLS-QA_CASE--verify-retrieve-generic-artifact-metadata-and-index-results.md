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
    - CA-M-207
---
# Verify retrieve generic artifact metadata and index results

## Claim checked

CA-M-207 returns complete deterministic metadata-filtered Artifact results without reading bodies or hiding absent and malformed fields.

## Applicable when

Apply whenever generic metadata extraction or Artifact index filtering changes.

## Test case

Create Artifacts spanning two Scope Units, roles, Tiers, lifecycle states, subjects, and relations; include one absent requested field and one malformed frontmatter carrier. Run one combined filter and record whether body-only sentinel text is accessed or returned.

## Acceptance criteria

Every and only matching stable IDs and paths appear in deterministic order; requested metadata and derived identity are correct; absent and malformed fields are explicit; no body text is read or returned.

## Failure disposition

Reject the realization and preserve fixture metadata, filters, expected membership, observed order, parse diagnostics, and body-access evidence.
