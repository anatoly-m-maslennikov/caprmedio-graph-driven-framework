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
    - CA-M-183
---
# Verify search caprmedio atom carriers

## Claim checked

CA-M-183 returns the complete deterministic set of matching Atom carriers without changing any project file.

## Applicable when

Apply to any ATOM_SEARCH realization before it is accepted for read-only discovery.

## Test case

Use a fixture containing active, draft, archived, malformed, and non-Atom files across two Scope Units. Select one subtree with combined lifecycle, Content-role, Tier, exact-field, and body-text filters, request metadata and content, then repeat the same search after recording every file digest.

## Acceptance criteria

The result contains every and only matching Atoms in stable path order; malformed candidates have separate diagnostics; excluded files never appear; both runs are identical; and every recorded digest remains unchanged.

## Failure disposition

Reject the realization and preserve the fixture, query, unexpected membership or ordering, diagnostics, and any detected mutation.
